# 📂 Python File Organizer

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

## 🚀 What this project does

A simple Python automation tool that organizes messy folders by sorting files into folders based on their file extensions.

This project was built as part of my Python automation learning journey and demonstrates working with files, folders, and automation using Python.

---
### 🔍 Before Execution & Runtime Overview
<p align="center">
  <img src="images/messy%20Downloads%20folder.png" width="350"/>
  <img src="images/Terminal%20Output%202.png" width="350"/>
</p>

### ✨ Post-Execution Result
<p align="center">
  <img src="images/After%20running.png" width="500"/>
</p>



## ✨ Features

*  Automatically creates folders if they don't exist.
*  Organizes image files.
*  Organizes video files.
*  Organizes PDF files.
*  Organizes document files.
*  Places unknown file types into an **Others** folder.
*  Skips already organized folders.
*  Displays how many files were moved.
*  Prints each file as it is organized.
*  Lists unknown file extensions encountered during execution.

---

## 🧠 What I Learned

* Working with `pathlib`
* Creating folders automatically
* Traversing directories with `os.walk()`
* Moving files using `shutil`
* Handling different file types
* Basic file automation
* Writing cleaner and more readable Python code

---

## 🛠️ Technologies Used

* Python 3
* pathlib
* os
* shutil

---

## 📊 Example Output


```
================
 FILE ORGANIZER
================

moving image: cat.jpg
✓ Moved:
cat.jpg -> Images

moving pdf: report.pdf
✓ Moved:
report.pdf -> PDFs

Finished!

Images moved: 4
Videos moved: 2
PDFs moved: 3
Documents moved: 5
Other files moved: 1
Unknown file types found: ['.psd']
Total: 15
```

## Project Structure

```
Downloads/
│
├── Images/
├── Videos/
├── PDFs/
├── Documents/
└── Others/
```

## What I Learned

* Working with `pathlib`
* Creating folders automatically
* Traversing directories with `os.walk()`
* Moving files using `shutil`
* Handling different file types
* Basic file automation
* Writing cleaner and more readable Python code

## Future Improvements

* Handle duplicate filenames more elegantly.
* Add logging instead of print statements.
* Allow users to choose the folder to organize.
* Replace repeated code with a cleaner dictionary-based solution.
* Build a graphical user interface (GUI).

---

Created by **DevBlueprint Lab**
