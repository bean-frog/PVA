import time
import win10toast

toaster = win10toast.ToastNotifier()

while True:
    toaster.show_toast("BITCH YOU HAD BETTER BE STUDYING OR SO HELP ME GOD I WILL BEAT THE EVERLOVING SHIT OUT OF YOU. THERE IS NO WAY ON EARTH YOU GOT FUCKING DISTRACTED AGAIN YOU USELESS PIECE OF HUMAN GARBAGE","GET THE FUCK BACK ON TASK",
                       duration=10)
    time.sleep(600)
