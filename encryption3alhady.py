

import random 
import string 
chars = " "+ string.punctuation + string.digits + string.ascii_letters 
chars = list (chars)
key = chars.copy()
random.shuffle(key)
plaintext = input("wsg my g. Enter your message and press enter ")
print(f"Received. Your message is {plaintext}")
ciphertext = "" 
decrypted = ""
for character in plaintext: 
    index = chars.index(character)
    ciphertext += key[index]
print("------- ENCRYPTED MESSAGE -------")
print(ciphertext)
x = input("do you wanna decrypt? (Y or N)")
if x.lower() == "y":
    for character in ciphertext: 
        index = key.index(character)
        decrypted += chars[index]
print(decrypted) 
