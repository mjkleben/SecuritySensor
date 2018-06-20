import serial
import smtplib #for emails
import sys

#Works with Gmail
send_it = False

#EDIT THE PORT "COM2"
ser = serial.Serial('COM2', 9600)
print("Starting Security System..")
while True:
    num = str(ser.readline())
    num = int(num[2:-7])



    if(num <= 200):
        print("Someone in your room!")
        send_it = True
        if send_it:
            email = smtplib.SMTP('smtp.gmail.com', 587)
            email.ehlo()
            email.starttls()
            username = "ENTER EMAIL HERE"
            password = "ENTER EMAIL PASSWORD HERE"
            email.login(username, password)
            email.sendmail(username, "RECEIVER EMAIL HERE", "Someone entered your room!")
            print("EMAIL SENT!")
            sys.exit(0)
