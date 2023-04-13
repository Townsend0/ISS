from data import *
import time

a = Iss()

while True:
    time.sleep(50)
    a.my_location()
    a.iss_location()

    if a.iss_near() and a.is_night():
        a.mail_me()
        break