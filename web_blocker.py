import time
from datetime import datetime as dt


hosts_temp="hosts"
hosts_path="C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
website_list=[]


start=int(input("enter starting time: "))
end=int(input("enter end time: "))
choice1= input("do you want to enter website (yes/no): ")
choice1=choice1.lower()
if choice1=='yes':
    
    choice='yes'
    while choice!='no':
        temp=input("enter website you want to block: ")
        website_list.append(temp)
        website_list.append("www."+temp)
        choice=input("do you want to block more websites (yes/no): ")
        
        
    
while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,start) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,end):
        print("Working hours...")
        with open(path,'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+ website+"\n")
    else:
        with open(hosts_path,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Fun hours...")
    time.sleep(5)
