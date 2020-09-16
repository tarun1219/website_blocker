website_list=[]
choice1= input("do you want to enter website (yes/no): ")
choice1=choice1.lower()
if choice1=='yes':
    choice='yes'
    while choice!='no':
        temp=input("enter the website: ")
        website_list.append(temp)
        website_list.append("www."+temp)
        choice=input("do you want to block more websites (yes/no): ")
        choice=choice.lower()
print(website_list)
