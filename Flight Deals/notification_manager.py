import smtplib
import os

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.MY_EMAIL = "davidbengtsson321@gmail.com"
        self.PASSWORD = "fdhveyrdpsqzghif"



    def SendEmail(self,recepient, subject, message):
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(self.MY_EMAIL, self.PASSWORD)
            email_message = f"Subject: {subject}\n\n{message}"
            connection.sendmail(self.MY_EMAIL, recepient, email_message.encode('utf-8'))
