
#import the operating system library
import os;

#Press 1 : To shutdown your computer.
print("1. Shutdown Computer");

#Press 2 : To reboot your system.
print("2. Restart Computer");
print("3. Exit");

#Enter the choice.
choice = int(raw_input("\nEnter your choice: "));

if(choice>=1 and choice<=2):
    if choice == 1:

        os.system('shutdown /s /t 1');
	
    else:
        os.system('restart /r /t 1');
else:
    exit();
