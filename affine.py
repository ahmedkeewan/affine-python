#Affine encryption/decryption algorithm
#Author: Ahmed Keewan
#ST_ID: 0166851
#ST_Section: 8-9:30

#to stop the execution of the program if the modular inverse doesn't exist
import sys as system

#mode refers to either encryption or decryption
#use the words encrypt or decrypt when you're asked to enter the mode
#the string will not be case sensitive....lower()function
mode =input("Enter Mode: ").lower()


while mode!="encrypt" and mode!="decrypt":
        print("Check your spelling!....Hint(encrypt/decrypt)")
        mode=input("Enter Mode: ").lower()
        if mode=="encrypt" or mode=="decrypt":
            break
        z=eval(input("Do you want to exit(Yes=1,No=0): "))
        print(system.exit(0) if z==1 else "Enter Model: ",end="")
        mode=input().lower()

if mode=="encrypt":
    string = input("Enter PlainText: ").lower()
elif mode=="decrypt":
    string = input("Enter CipherText: ").lower()        
a,b=eval(input("Enter A,B: "))


def encrypt(string, a, b):
    cyphertext = ""
    for char in string:
        if not char.isalpha():
            cypher = char
        elif char.isalpha():
            num = ord(char) -97
            cypher = (a * num + b) % 26
            cypher = chr(cypher + 97)
        cyphertext += cypher
    return cyphertext


# Extended Euclidean algorithm...
def egcd(a, b):
	if a == 0:
		return (b, 0, 1)
	else:
		g,y,x = egcd(b % a, a)
		return (g, x - (b // a) * y, y)
    
    
    
#used to calculate the inverse of a in the case of decrypting a cipher text    
def findinverse(a):
	
	g, x, y = egcd(a, 26)
	if g != 1:
		print("Modular inverse of a does not exist")
		system.exit(0)
	else:
		return x % 26
    
    
   
def decrypt(string, a, b):
    
    plaintext = ""
    inv = findinverse(a)
    print("\nThe inverse of A is: ",inv)
    for char in string:
        if not char.isalpha():
            plain = char
        elif char.isalpha():
            num = ord(char) -97
            plain = (inv * (num - b)) % 26
            plain = chr(plain + 97)
        plaintext += plain
    return plaintext	




if mode == "encrypt":
    print('\nCipher text: ',encrypt(string, a, b))
elif mode == "decrypt":
	print('Plain text: ',decrypt(string, a, b))
