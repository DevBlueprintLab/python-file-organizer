# Python file Organizer
A simple Python automation script that automatically organizes files in your Downloads folder into categorized folders.

## Features

  * Automatically sorts files into folders:
  
    * Images
    * Videos
    * PDFs
    * Documents
    * Others
    
* Prevents duplicate file moves

* Counts how many files were organized

* Detects unknown file types

* Works with real Downloads folder using Path.home()

##  Technologies Used

 * Python 3
 * pathlib
 * os module
 * shutil module

##  How It Works

The script scans your Downloads folder and:

 1. Detects file types based on extensions
 2. Moves files into appropriate folders
 3. Skips already organized files
 4. Prints a summary of actions

##  How to Run

    python file_organizer.py

Make sure Python is installed on your system.

##  Example Output

    Moved:
    cat.jpg -> Images
    video.mp4 -> Videos
    report.pdf -> PDFs

    Finished!

    Images moved: 5
    Videos moved: 2
    PDFs moved: 3
    Documents moved: 4
    Other files moved: 1
    Total: 15

##  What I Learned

 * File handling in Python
 * Using pathlib for cross-platform paths
 * Automating repetitive tasks
 * Working with os.walk()
 * Handling file operations safely

##  Future Improvements

  * Handle duplicate file renaming
  * Add GUI version
  * Schedule automatic runs
  * Improve file type detection
