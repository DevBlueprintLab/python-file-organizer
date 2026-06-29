# 📂 Python File Organizer

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![Type](https://img.shields.io/badge/Type-Automation%20Tool-purple)

---

##  Overview

Automatically organizes messy folders into a clean structure in seconds.



## ⭐ Why this project matters

Manually organizing files is repetitive and time-consuming, especially in cluttered Downloads folders. 

This tool automates the process, saving time and keeping files structured and easy to access.

---


## 🧠 Key Features

- 📁 Automatically creates folders when needed
- 🖼️ Organizes images, videos, PDFs, and documents
- 📦 Moves unknown file types into an **Others** folder
- 🚫 Skips already organized directories
- 📊 Displays real-time file movement tracking
- 🔍 Detects and reports unknown file extensions

---

## 🖥️ Demo

### 🔍 Before Execution & Runtime Overview

<p align="center">
  <img src="images/messy%20Downloads%20folder.png" width="350"/>
  <img src="images/Terminal%20Output%202.png" width="350"/>
</p>

### ✨ Post-Execution Result

<p align="center">
  <img src="images/After%20running.png" width="500"/>
</p>

---

## 🛠️ Tech Stack

- Python 3
- pathlib
- os
- shutil

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
