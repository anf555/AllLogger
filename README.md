<p align="center"><img alt="project-logo" width="100" src="https://github.com/anf555/AllLogger/blob/2c41bafd45d27e5bf710f3c10b36237de289d496/images/Logo.png"></p>

# AllLogger

AllLogger is a security tools that allows you to do :
- Get target computer hostname
- Get the target computer private IP Address
- Get list of installed application on desktop folder
- Get list of installed program using wmic product get name
- Insert all of that data to sqlite3 database and upload it to the cloud

# Disclaimer : This Project Is For Educational Purposes Only
I AM NOT RESPONSIBLE FOR ANY ILLEGAL USE OF THIS PROJECT

# Description :
When you run this project its started getting target computer ip address, hostname and list of installed program on desktop folder and inserting it to sqlite3 database and uploading the database to ftp server.

If you think you can improve this project you can submit it in issue tab.

# Guide to make executable :
- Create ftp server (if you dont have one).
- Change ftp server address, username, password in main.py to your ftp server login credential.
- Compile python script to executables(.exe) using pyinstaller or auto-py-to-exe.
- Run the file on target computer

# Data output :
