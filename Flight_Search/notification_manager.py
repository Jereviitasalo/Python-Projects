import smtplib
import os
from dotenv import load_dotenv
load_dotenv()

MY_EMAIL = os.environ.get("my_email")
EMAIL_PASS = os.environ.get("email_password")

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def send_email(self, price, city, date, link, stop_overs):
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=EMAIL_PASS)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=MY_EMAIL,
                                msg=f"Subject: LENTO LOYTYI!\n\nLoysin lennon hintaan {price} euroa.\n"
                                f"Lennon kohteena on {city}.\nLento lahtee Helsingista:"
                                 f" {date}.\nPysahdyksia: {stop_overs}.\n\n{link}".encode('utf-8'))