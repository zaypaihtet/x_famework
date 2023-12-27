import ftplib

host = input("Host Domain : ")
try:
	ftp = ftplib.FTP(host)
	ftp.login('anonymous',"")
	print('FTP Anonymous Login Succedded')
	ftp.quit()
except Exception as e:
	print(host,+'FTP Anonymous Login Failed')