# 📚 lib2ran – Library Genesis Book Downloader

**lib2ran** is a  Python CLI tool I made from ChatGPT ( functionalities:: almost everything in the main code is copied and pasted from chatGPT ) -
and currently enhancing and adding new functions of my own through learning,
 
The website I am scrpaing books from [Library Genesis (libgen.rs)](https://libgen.rs) effortlessly.
This tool offers both **interactive** and **direct command-line** modes for maximum flexibility.
---

## ✨ Features

* 🔍 Search for books by title on LibGen
* 📥 Choose from top 25 results and download the desired book
* ⚙️ Works on Windows, Linux, and macOS
* 🎛 Supports CLI arguments for scripting/automation

---

## 🧰 Installation

Clone the repository and install it in **editable mode**:

```bash
git clone https://github.com/yourusername/lib2ran.git
cd lib2ran
pip install -e .
```

> ✅ This will install the `lib2ran` CLI globally on your system.

---

## 🚀 Usage

### 🟢 Interactive Mode

Run the tool and follow the prompts:

```bash
lib2ran
```

### 🔵 Command-Line Mode

Download a book directly using a search term:

```bash
lib2ran -b "The Art of Computer Programming"
```

---

## 🛠 Requirements

* Python 3.7+
* Dependencies (automatically installed):

  * `libgen-api`
  * `inquirer`
  * `requests`

---

## 📁 Project Structure

```
lib2ran/
├── __main__.py     # Main CLI logic
setup.py            # Installation script
README.md           # This file
```

---

## 🧠 Future Plans

* [ ] Add fuzzy matching to improve search accuracy
* [ ] Option to auto-download the top result
* [ ] Save download history and prevent duplicates
* [ ] GUI version (Tkinter or Electron)

---

## ⚠️ Legal Disclaimer

This tool is intended for **educational purposes** only. Please ensure that you comply with your country's copyright laws. The author is **not responsible** for misuse of this tool.

---

## 🧑‍💻 Author

**Ranbir**
Inspired by learning. Built to automate knowledge.

