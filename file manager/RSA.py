import sys

def isPrime(number): # prime control
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                return -1
                break
        else:
            return 1
    else:
        return -1


def findGCD(x, y): # Greatest common divisor
    while y != 0:
        c = x % y
        x = y
        y = c
    return x

def modinv(a, m): # mod inverse
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def coprimes(number): # return coprime array
    l = []
    for x in range(2, number):
        if findGCD(number, x) == 1 and modinv(x,phi) != None:
            l.append(x)
    for x in l:
        if x == modinv(x,phi):
            l.remove(x)
    return l

def mod(x,y): # get modulus for 2 number
    if(x<y):
        return y
    else:
        c=x%y
        return c

def encryptString(plainText):
    cipher=""
    for x in list(plainText):
        c = mod(ord(x)**e, n)
        cipher+=(chr(c))
    return cipher
def decryptString(plainText):
    plain=""
    for x in list(plainText):
        c = mod(ord(x)**d, n)
        plain+=(chr(c))
    return plain

def encryptHexadecimal(plainText):
    hexaList = plainText.split(" ")
    cipherHexa=[]
    for i in hexaList:
        decimalElement=int(i, 16)
        cipherElement=mod(decimalElement**e,n)
        cipherHexa.append(hex(cipherElement))
    return cipherHexa
def decryptHexadecimal(plainText):
    plainHexa=[]
    for i in plainText:
        decimalElement=int(i, 16)
        cipherElement=mod(decimalElement**d,n)
        plainHexa.append(hex(cipherElement))
    return plainHexa
def encryptDecimal(plainText):
    decimalList = plainText.split(" ")
    cipherDecimal=[]
    for i in decimalList:
        cipherElement=mod(int(i)**e,n)
        cipherDecimal.append(cipherElement)
    return cipherDecimal

def decryptDecimal(plainText):
    plainDecimal=[]
    for i in plainText:
        cipherElement=mod(int(i)**d,n)
        plainDecimal.append(cipherElement)
    return plainDecimal



print("\nBe careful for prime numbers. The bigger the better ")
print("Example: (61,53) ")

p=int(input('Enter a prime p: '))
if isPrime(p)==-1:
     print("Please select a PRIME NUMBER !!!")
     sys.exit()
     
q=int(input('Enter a prime q: '))
if isPrime(q)==-1:
     print("Please select a PRIME NUMBER !!!!")
     sys.exit()
     
print("\nYour choices are : p=" + str(p) + ", q=" + str(q) + "\n")

n=p*q
print("n = p * q = " + str(n) + "\n")

phi=(p-1)*(q-1)
print("Euler's function : " + str(phi) + "\n")

print("Choose an coprime from array:\n")
print(str(coprimes(phi)) + "\n")

e=int(input("Enter a coprime : "))
d=modinv(e,phi)

print("\nYour public key is (e=" + str(e) + ", n=" + str(n) + ").\n")
print("Your private key is (d=" + str(d) + ", n=" + str(n) + ").\n")

choice=int(input("Will you encrypt text/decimal or hexadecimal? (for text:1/decimal:2/else enter:3) : "))

if choice==1:
    
    s = input("Enter a text to encrypt: ")
    print("\nPlain message: " + s + "\n")
    
    enc = encryptString(s)
    print("Encrypted message: " + str(enc) + "\n")
    
    dec = decryptString(enc)
    print("Decrypted message: " + dec + "\n")

elif choice==2:
    
    s = input("Enter a hexadecimal numbers to encrypt: ex:(12 36 43 54) : ")
    print("\nPlain message: " + s + "\n")
   
    enc = encryptDecimal(s)
    print("Encrypted message: " + str(enc) + "\n")
    
    dec = decryptDecimal(enc)
    print("Decrypted message: " + str(dec) + "\n")
    
elif choice==3:
    
    s = input("Enter a hexadecimal numbers to encrypt: ex:(65 AB EC 1E) : ")
    print("\nPlain message: " + s + "\n")
   
    enc = encryptHexadecimal(s)
    print("Encrypted message: " + str(enc) + "\n")
    
    dec = decryptHexadecimal(enc)
    print("Decrypted message: " + str(dec) + "\n")
     
else:
    print("Invalid choice")
    
    
    
    
    
    
    
    
    
    
    
    