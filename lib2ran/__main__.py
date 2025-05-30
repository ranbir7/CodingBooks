import os
import requests
from libgen_api import LibgenSearch
import inquirer
import argparse
def download_book(book, searcher):
    """
    Download a book using the resolved download link.
    """
    try:
        # Resolve the direct download links
        download_links = searcher.resolve_download_links(book)
        if not download_links:
            print("No download links found for this book.")
            return False

        # Attempt to download from the available links
        for source_name, url in download_links.items():
            try:
                response = requests.get(url, stream=True, timeout=10)
                response.raise_for_status()

                # Construct filename and clean it
                filename = f"{book['Title']} - {book['Author']}.{book['Extension']}"
                filename = "".join(c for c in filename if c.isalnum() or c in (".", "_", "-")).rstrip()
                filepath = os.path.join(os.getcwd(), filename)

                # Download file in chunks
                with open(filepath, "wb") as f:
                    for chunk in response.iter_content(chunk_size=1024):
                        if chunk:
                            f.write(chunk)
                print(f"Downloaded: {filepath}")
                return True
            except requests.RequestException:
                print(f"Failed to download from {source_name}. Trying next link...")
                continue

        print("All download attempts failed.")
        return False

    except Exception as e:
        print(f"Error downloading file: {e}")
        return False

def display_results(results):
    """
    Display search results and prompt user to select a book.
    """
    if not results:
        print("No results found.")
        return None
    limited_results = results[:min(len(results), 100000)]
    # Prepare choices for inquirer
    choices = [
        f"{i+1}. {book['Title']} by {book['Author']} ({book['Year']}, {book['Size']}, {book['Extension']})"
        for i, book in enumerate(limited_results)
    ]

    questions = [
        inquirer.List(
            "book",
            message="Select a book to download",
            choices=choices
        )
    ]

    answers = inquirer.prompt(questions)
    if not answers:
        return None

    selected_index = int(answers["book"].split(".")[0]) - 1
    if 0 <= selected_index < len(limited_results):
        return limited_results[selected_index]
    else:
        print("Invalid selection.")
        return None

def main():
    """
    Main function to run the LibGen book downloader.
    Supports both interactive and command-line modes.
    """
    parser = argparse.ArgumentParser(description="LibGen Book Downloader by Ran7")
    parser.add_argument(
        "-b", "--book", metavar="BOOK_TITLE", type=str, nargs='?', help="Download a book by title directly"
    )
    args = parser.parse_args()

    s = LibgenSearch()
    print("Library Genesis Book Downloader By Ran7")

    if args.book:
        query = args.book.strip()
        print(f"Searching for '{query}'...")
        try:
            results = s.search_title(query)
            selected_book = display_results(results)  # Reuse display_results
            if not selected_book:
                print("No book selected or no results found.")
                return
            print(f"Downloading '{selected_book['Title']}'...")
            download_book(selected_book, s)
        except Exception as e:
            print(f"Error: {e}")
        return

    # Fallback to interactive mode
    while True:
        query = input("\nEnter the book name (or type 'quit' to exit): ").strip()
        if query.lower() == 'quit':
            print("Exiting program. Goodbye!")
            break
        if not query:
            print("Book name cannot be empty.")
            continue

        print(f"Searching for '{query}'...")
        try:
            results = s.search_title(query)
        except Exception as e:
            print(f"Error searching LibGen: {e}")
            continue

        selected_book = display_results(results)
        if not selected_book:
            print("No book selected.")
            continue

        print(f"Downloading '{selected_book['Title']}'...")
        download_book(selected_book, s)

        questions = [
            inquirer.List(
                "continue",
                message="Do you want to download another book?",
                choices=["Yes", "No"]
            )
        ]
        answer = inquirer.prompt(questions)
        if not answer or answer["continue"] == "No":
            print("Exiting program. Goodbye!")
            break 
if __name__ == "__main__":
    main()