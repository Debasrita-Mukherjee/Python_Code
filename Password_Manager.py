import random
import string


passwords= {}

#Load existing password file
try:
    with open("passwords.txt","r") as file:
        for line in file:
            website, pwd = line.strip().split(":")
            passwords[website]=pwd