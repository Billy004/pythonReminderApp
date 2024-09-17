#imports
from win10toast import ToastNotifier
import time # for timer

toaster = ToastNotifier()

Toasttitle = input("\nTitle of Reminder: ")
msg = input("Message: ")
minutes = float(input("How Many Minutes: "))

seconds = minutes *60

print ("\nRemainder set Successfully!\n")
time.sleep(seconds)
toaster.show_toast(Toasttitle, msg, duration=10, threaded=True)

while toaster.notification_active:
    time.sleep(0.1)