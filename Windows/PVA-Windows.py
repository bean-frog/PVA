import time
import win10toast

toaster = win10toast.ToastNotifier()

option = input("Choose harshness level: (low, mid, or high): ")

if option == 'high':
  while True:
    toaster.show_toast("BITCH YOU HAD BETTER BE STUDYING OR SO HELP ME GOD I WILL BEAT THE EVERLOVING SHIT OUT OF YOU. THERE IS NO WAY ON EARTH YOU GOT FUCKING DISTRACTED AGAIN YOU USELESS PIECE OF HUMAN GARBAGE","GET THE FUCK BACK ON TASK",
                       duration=10)
    time.sleep(600)
    
elif option == 'mid':
    
    
elif option == 'low':
  

else:
  print("Invalid option, try again")


