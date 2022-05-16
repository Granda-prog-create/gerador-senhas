import random
import string

from numpy import number
from requests import options

def password_generator(len_pass = 8):
    ascii_options = string.ascii_letters
    number_options = string.digits
    punt_options = string.punctuation
    options = ascii_options + number_options + punt_options
    
    password_user = ""
    
    for i in range(0, len_pass):
        digit = random.choice(options)
        password_user = password_user + digit 
    
    return password_user

choice_user = input("Quantos dígitos na senha?")

if choice_user.isdigit():
    choice_user = int(choice_user)
else:
    print("Entrada inválida")
    quit() 
    
response = password_generator(choice_user)
print(f"Senha gerada:\n{response}")


    
    
       

        
    
    
    
    
    
    
    
    