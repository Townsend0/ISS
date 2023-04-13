import requests
import datetime
import smtplib

class Iss:

    def my_location(self):
        self.lat = 38.4237
        self.lon = 27.1428


    def iss_location(self):
        self.json = requests.get("http://api.open-notify.org/iss-now.json")
        self.json.status_code
        self.iss_lon = float(self.json.json()["iss_position"]["longitude"])
        self.iss_lat = float(self.json.json()["iss_position"]["latitude"])


    def iss_near(self):
        if self.lat + 5 <= self.iss_lat <= self.lat + 5 and self.lon + 5 <= self.iss_lon <= self.lon + 5:
            return True
        

    def is_night(self):
        self.time = datetime.datetime.now().hour
        if self.time > self.set and self.time < self.rise:
            return True


    def sun(self):
        self.sun = requests.get("https://api.sunrise-sunset.org/json?lat=38.3337&lng=27.2911&formatted=0")
        self.sun.status_code
        self.rise = self.sun.json()["results"]["sunrise"]
        self.set = self.sun.json()["results"]["sunset"]


    def mail_me(self):
        self.mail = smtplib.SMTP("smtp.gmail.com", 587)
        self.mail.starttls()
        self.mail.login("obadah2109@gmail.com", "dkyxxnazqaddzsyk")
        self.mail.sendmail("obadah2109@gmail.com", "obadah272@gmail.com", "Subject: ISS\n\nISS is in your range right now")