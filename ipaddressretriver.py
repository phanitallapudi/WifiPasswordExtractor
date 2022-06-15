from cmath import exp
from email import message
import socket 
import smtplib

hostname = socket.gethostname()   
ipaddress = socket.gethostbyname(hostname)   
print("Your Computer Name is: "+hostname)   
print("Your Computer IP Address is: "+ipaddress) 


print("\n#################################################\n")

nextcase = input("Enter Y for sending the ipaddress to email and S for saving in the local host (Y/S): ").lower()

if nextcase == 'y':
    
    try:
        senderemailid = input("Enter the sender email ID (case sensitive): ")
        senderpasswd = input("Enter the sender email password (case sensitive: ")
        print("\n#################################################\n")
        receiveemail = input("Enter the receiver email ID (case sensitive): ")
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()

        s.login(senderemailid,senderpasswd)
        messageofscript = ipaddress

        s.sendmail(from_addr=senderemailid, to_addrs=receiveemail,msg = messageofscript)
        s.quit()
        print("\n#################################################\n")
        print("Email for the IP address {} sent successfully to {}".format(ipaddress,receiveemail))
    except KeyboardInterrupt:
        print("Wrong input!!!!")
    
    except smtplib.SMTPException:
        print("Error occured, try again :(")
    
    except TimeoutError:
        print("Request timed out, please try again")
elif nextcase == 's':
    try:
        with open("dfile.txt", "r") as f:
            f.read(ipaddress)

            print("\nSaved successfully!!!")
    except FileNotFoundError:
        with open("dfile.txt", "w+") as f:              #The file will be saved under C:\Users\'YourName'
            f.write("\n"+ipaddress)
            print("\nSaved successfully!!!")
            
else:
    print("\nIncorrect KeyBoard stroke!!!")