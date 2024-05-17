#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re

def check_password_strength(password):
    # Check length of the password
    if len(password) < 8:
        return "Weak: Password should be at least 8 characters long."
    
    # Check for presence of uppercase and lowercase letters in password
    if not any(c.isupper() for c in password) or not any(c.islower() for c in password):
        return "Weak: Password should contain both uppercase and lowercase letters."
    
    #check for blanck space in password
    if  re. search(" ",password):
        return " Weak: blank spaces are not allowed."

    # Check for presence of special characters in the password
    if not re.search("[!@#$%^&*()_+=\-{}[\]:\"|;',./<>?]", password):
        return "Weak: Password should contain at least one special character"
    
    return "Thank you for entering a Strong password"


Password=input("enter a password:")
strength=check_password_strength(Password)
print(strength)


