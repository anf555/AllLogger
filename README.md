<p align="center"><img alt="project-logo" width="100" src="https://github.com/anf555/AllLogger/blob/64e36e9ca829f617bca03fb283be3dc883e85385/Logo.png"></p>

# AllLogger

AllLogger is a virus that allows you to do :
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
1.Create ftp server (if you dont have one).
2.Change ftp server address, username, password in main.py to your ftp server and login credential.
3.Compile python script to executables(.exe) using pyinstaller or auto-py-to-exe.
