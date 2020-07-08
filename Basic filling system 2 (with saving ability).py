#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 16:50:48 2020

Author: @aktorevan47

Desc: 
    
    This code is to create the filling system and able to save the user data
    into your storage. This is intended to understand to use functions inside 
    another function. Besides, to understand the definition of global 
    and local variable.

"""
import os

quest = []


def wrte():
    
    name = input("What's your name?")
    quest.append(name)

    age = input("How old are you?")
    quest.append(age)
    
    sex = input("Are you male/female?")
    quest.append(sex)
    
    job = input("What desired job you are going to apply?")
    quest.append(job)
    
    disp2()
    stor()

def rewrte():
    
    name = input("What's your name?")
    quest[0] = name

    age = input("How old are you?")
    quest[1] = age
    
    sex = input("Are you male/female?")
    quest[2] = sex
    
    job = input("What desired job you are going to apply?")
    quest[3] = job
    
    disp2()
    stor()

def disp():

    return "Name :"+quest[0]+" Age :"+quest[1]+" Sex :"+quest[2]+" Desired position :"+quest[3]

def disp2():
    
    os.system('clear')
    
    print("Please check your information below:")
    print("Name : ", quest[0])
    print("Age : ", quest[1])
    print("Sex : ", quest[2])
    print("Desired poaition : ", quest[3])
    
def stor():
    
    
    conf = input("Is the information correct? (Y/N)")
    
    if conf == "N":
        os.system('clear')
        return rewrte()
    
    elif conf == "Y":
       
        file = open('user.txt', "w")
        file.write(disp())
        file.close()
        print("Thank your for using our filling system")
    
    else:
        print("Can only return Y or N")
        print(stor())
    
wrte()
