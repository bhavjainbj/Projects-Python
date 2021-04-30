import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import getpass
from prompt_toolkit import prompt
import time



email_user =  input("Enter your email : ")
email_password = prompt("Password: ", is_password=True)
email_send = input("Enter the receptant email : ")

subject = input("Subject : ")

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject



Tk().withdraw()
what = input("What type of file you want to send press (1 for text/ 2 for attachment) : ")
if what=="2":
    filename=askopenfilename()
    attachment =open(filename,'rb')
    part = MIMEBase('application','octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition',"attachment; filename= "+filename)
    msg.attach(part)
elif what=="1":
    filename='text'
    attachment=input("Type your text : ")
    msg.attach(MIMEText(attachment, 'plain'))
else:
    print('Such type of file I can not send')
    time.sleep(5)
    quit()
    




text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(email_user,email_password)


server.sendmail(email_user,email_send,text)
print(" Email sent!! ")
time.sleep(5)
server.quit()
