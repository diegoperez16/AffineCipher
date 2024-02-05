import math
import string

#Require: Integers a and m with m>0
#Ensure: The inverse of a modulo m or the message that gcd(a,n) > 1

#a = int(input("What would be the input for a"))
#m = int(input("What would be modulus"))
m = 26 # There are 26 letters in the alphabet

def getInverse(a,m):
    d0 = a
    d1 = m
    x0 = 1
    x1 = 0

    while d1 != 0:
        q = (d0//d1)
        d2 = d0 - (q*d1)
        x2 = x0 - (q*x1)
        x0 = x1
        x1 = x2
        d0 = d1
        d1 = d2

    if d0 == 1:
        return x0 % m #Return the congruent 
    else:
        return math.gcd(a,m) > 1

def afEncrypt(text,a,b):
    rE = "" #Encryption Result
    for i in text:
        x = string.ascii_lowercase.index(i) # calculate position of letter in alphabet

        e = ((a*x) + b) % m #encryption equation

        el = chr(97+e)  # encrypted letter #find letter in alphabet
        rE += el #append it to Encryption Result
    return rE

def afDecrypt(text,a,b):
    inverse = getInverse(a,m)
    rD = ""
    for i in text:
        y = string.ascii_lowercase.index(i) # calculate position of letter in alphabet

        d = (inverse * (y - b)) % m

        dl = chr(97+d)

        rD += dl
    return rD

#-------------------------------------------------------------------------------------------------------#
while True:
    r = ''
    a = int(input("What is a?: "))
    b = int(input("What is b?: "))
    
    text = input("What is the text?: ")
    op = input("What is the operation? (Enter d for decryption or e for encryption): ")

    if op.lower() == 'e':
        r = afEncrypt(text,a,b)
        print(r)
        loop = input("Continue?: ")

        if loop.lower() == 'yes':
            continue
        else:
            break
    if op.lower() == 'd':
        r = afDecrypt(text,a,b)
        print(r)
        loop = input("Continue?: ")

        if loop.lower() == 'yes':
            continue
        else:
            break
    





#print(getInverse(a,m))

