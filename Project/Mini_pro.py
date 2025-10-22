from Functions.functions import * 
import os

#file directory:
base_dir = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(base_dir,"Functions","ips.log")
print(file_path)

operations = ["Email Verification","Phone number extractor","Valid IP extractor","Extract valid and invalid IPs","Email Hider"]
print("Select the operation you want perform:")
for index , op in enumerate(operations):
    print(f"{index}: {op}")


try:
    operation = int(input("Enter Opertation: "))
    if operation == 0:
        email = input("Enter email to verify:")
        print(validate_email(email))
        
    elif operation == 1:
        text = input("Enter the text from you want to extract the phone numbers: ")
        print(phone_number_matcher(text))
        
    elif operation == 2:
        logs = "127.0.0.1 - success"
        print(valid_ip_extractor(logs))
        
    elif operation == 3:
        file_path = "/home/sanaullah/Desktop/MS-Cyber-Security/Second-semester/Python-and-Shell-Programming/Bash-Scripting/CyberLab/Scripts/Regular expressions/Project/Functions/ips.log"
        print(extract_ips_from_log(file_path))
        
    elif operation == 4:
        report_text = input("Please write your report:")
        print(email_hider(report_text))
    else:
        print("Invalid option. Please select a valid number.")
except ValueError:
    print("Please enter correct value")