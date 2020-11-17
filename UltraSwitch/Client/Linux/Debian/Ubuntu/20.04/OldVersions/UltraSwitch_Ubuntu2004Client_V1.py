print ("UltraSwitch Ubuntu 20.04 LTS (Focal Fossa) client")
confirm1 = str(input("Do you want to back up your Ubuntu data to another device? (y/N)"))
confirm1 == answer1
answer1 == answer1.upper()
if (answer1 == "Y"):
  print ("Make sure UltraSwitch is open on the other device you are connecting to")
  print ("Device types")
  print ("Fedora Linux machine 1")
  print ("Arch Linux machine 1")
  print ("Mint Linux machine 1")
  print ("Ubuntu 20.04 machine 2")
  print ("More demos unavailable")
  inputT = input("Press the [ENTER] key to confirm")
  device = str("Ubuntu 20.04 machine 2")
  if (device == "Ubuntu 20.04 machine 2"):
  scopeOfBackup = ["Home/Downloads", "Home/Desktop", "Home/Documents", "snap/", "Home/Videos", "Home/Music", "Home/Starred", "Home/Pictures", "Home/.mozilla"]
    print ("You are about to transfer the following data: ")
    print (scopeOfBackup())
    print ("Add or remove entries [unavailable]")
    backupEstimate = int(600)
    backupGiB = int(36000)
    backupTi = backupEstimate / backupGiB
    # This is not yet functional
    print ("Backup is estimated to take [unknown] make sure your Internet connection stays stable and that the devices are close.")
   else:
    print ("Unable to find the right device, quitting")
print("Backup canceled, the app will now close")
noMore = input("Press [ENTER] key to close")
print ("This program should now be closed. If it isn't, try pressing the close button. If that doesn't work, end the process with a process manager or task manager")
#
 elif (answer1 == "N" or not answer1 = "Y" or "N"):
  print("Backup canceled, the app will now close")
  noMore = input("Press [ENTER] key to close")
  print ("This program should now be closed. If it isn't, try pressing the close button. If that doesn't work, end the process with a process manager or task manager")
 
# This script is currently terribly bad, it currently only serves as a demo. It is going to take a lot more work
