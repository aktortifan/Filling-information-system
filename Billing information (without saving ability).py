'''
Author: @aktortifan47
Email: aktorevan@nuist.edu.cn
Desc: 
    This is the billing information simulator. The script is intended to 
    understand the concept of "recursion" as funtions calling themselves.
'''


def resubmit():
    print("Please only choose Y/N")
    
    confirm = input("Is the submitted information correct ? (Y/N)")
    
    if confirm == "N":
        form()
    elif confirm == "Y":
        print("Thank you for using our system!")

#Here is the idea of "recursion" is getting cool. You can can still reuse
#the function inside your active function.

    else:
        resubmit()


def form():
    
    '''
    Hello, welcome to our billing system. Please insert your information!
    '''

#Write your personal information first
    
    name = input("Full Name : ")
    age = input("Age : ")
    sex = input("Sex : ")
    job = input("The desired position : ")
    
#It will show your submitted information
    
    print("Your Full Name :", name)
    print("Your Age :", age)
    print("Sex : ", sex)
    print("The position you are going to apply : ", job)
    
#If the user says "N", then it would return to the form function
#If the user says other characters (except Y or N), then it would lead to 
#the function resubmit()
    
    confirm = input("Is the information correct ? (Y/N)")
    
    if confirm == "N":
        form()
    elif confirm == "Y":
        print("Thank you for using our system!")
    else:
        resubmit()
        
#The program will start here
help(form)        
print(form())
  
    
