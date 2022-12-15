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
    while True:
    toaster.show_toast("Hey are you studying? no? get your ass back on track rn like come on do you want to be fucking homeless and addicted to meth and eventually be having conversations with a water fountain? i didnt think so.","OI WHAT ARE YOU DOING RN",
                       duration=10)
    time.sleep(600)
    
elif option == 'low':
   while True:
    toaster.show_toast("Hey bud lets make sure we're studying because you","OI WHAT ARE YOU DOING RN",
                       duration=10)
    time.sleep(600)

else:
  print("Invalid option, try again")


