# Linux Commands Documentation



## 1. pwd - Print Working Directory

**Command:** pwd

**What it does:** Shows the current directory path

**Output:** /c/Users/divya/Synergy\_TP/task\_1



## 2. ls - List Files

**Command:** ls

**What it does:** Lists files and folders in current directory

**Output:** data/  linux_commands.md  requirements.txt  setup_log.md  src/  venv/



## 3. ls -la - List All Files with Details

**Command:** ls -la

**What it does:** Lists all files including hidden ones with permissions, size, and date

**Output:**

total 9

drwxr-xr-x 1 divya 197609   0 Jun 24 14:07 ./

drwxr-xr-x 1 divya 197609   0 Jun 24 14:05 ../

drwxr-xr-x 1 divya 197609   0 Jun 24 14:03 data/

-rw-r--r-- 1 divya 197609   0 Jun 24 14:07 linux\_commands.md

-rw-r--r-- 1 divya 197609  93 Jun 24 13:57 requirements.txt

-rw-r--r-- 1 divya 197609 592 Jun 24 14:06 setup\_log.md

drwxr-xr-x 1 divya 197609   0 Jun 24 14:01 src/

drwxr-xr-x 1 divya 197609   0 Jun 24 13:54 venv/



## 4. cd - Change Directory

**Command:** cd ..

**What it does:** Moves one level up to parent directory

**Output:** (moved to /c/Users/divya/Synergy_TP)



## 5. mkdir - Make Directory

**Command:** mkdir test_folder

**What it does:** Creates a new folder

**Output:** (folder created successfully)



## 6. touch - Create Empty File

**Command:** touch test_file.txt

**What it does:** Creates an empty file

**Output:** (file created successfully)



## 7. cat - Display File Contents

**Command:** cat data/sample.txt

**What it does:** Displays the contents of a file

**Output:**

This is a sample data file for Task 1.

Name: Divyanshu

Project: Synergy_TP



## 8. echo - Print Text

**Command:** echo "Hello from terminal"

**What it does:** Prints text to the terminal

**Output:** Hello from terminal



## 9. cp - Copy File

**Command:** cp data/sample.txt data/sample_copy.txt

**What it does:** Copies a file to a new location

**Output:** (file copied successfully)



## 10. mv - Move/Rename File

**Command:** mv data/sample_copy.txt data/sample_moved.txt

**What it does:** Moves or renames a file

**Output:** (file renamed successfully)



## 11. rm - Remove File

**Command:** rm data/sample_moved.txt

**What it does:** Deletes a file permanently

**Output:** (file deleted successfully)



## 12. grep - Search Text

**Command:** grep "sample" data/sample.txt

**What it does:** Searches for a pattern inside a file

**Output:** This is a sample data file for Task 1.



## 13. find - Find Files

**Command:** find . -name "\*.py"

**What it does:** Finds files matching a pattern

**Output:** ./src/hello.py



## 14. head - Show First Lines

**Command:** head data/sample.txt

**What it does:** Shows the first 10 lines of a file

**Output:**

This is a sample data file for Task 1.

Name: Divyanshu

Project: Synergy_TP



## 15. tail - Show Last Lines

**Command:** tail data/sample.txt

**What it does:** Shows the last 10 lines of a file

**Output:**

This is a sample data file for Task 1.

Name: Divyanshu

Project: Synergy_TP



## 16. wc - Word Count

**Command:** wc data/sample.txt

**What it does:** Counts lines, words, and characters in a file

**Output:** 2 13 76 data/sample.txt



## 17. chmod - Change Permissions

**Command:** chmod 755 src/hello.py

**What it does:** Changes file permissions (7=read+write+execute, 5=read+execute)

**Output:** (permissions changed successfully)

