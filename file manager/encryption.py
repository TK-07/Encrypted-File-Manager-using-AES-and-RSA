from AESencryptfunc import *
import math 
import getpass
import os
from tkinter import * 
from tkinter.ttk import *
from tkinter.filedialog import askopenfile


file=open("files\plaintext1.txt", "r")
#file= askopenfile(mode ='r')
message=(file.read())
#print("Inside your plaintext message is:\n%s\n" % message)
file.close()
print("File selected...\n")
PassPhrase=""
while(len(PassPhrase)!=16):
    print("Enter the master key to encrypt your files")
    PassPhrase=getpass.getpass()
    if(len(PassPhrase)<16):
        while(len(PassPhrase)!=16):
            PassPhrase=PassPhrase+"\00"
    if(len(PassPhrase)>16):
        #print("Your passphrase was larger than 16, truncating passphrase.")
        PassPhrase=PassPhrase[0:16]





message=BitVector(textstring=message)
message=message.get_bitvector_in_hex()
replacementptr=0

while(replacementptr<len(message)):
    if(message[replacementptr:replacementptr+2]=='0a'):
        message=message[0:replacementptr]+'0d'+message[replacementptr:len(message)]
        replacementptr=replacementptr+4
    else:
        replacementptr=replacementptr+2

message=BitVector(hexstring=message)
message=message.get_bitvector_in_ascii()

start=0
end=0
length=len(message)
loopmsg=0.00
loopmsg=math.ceil(length/16)+1
outputhex=""


PassPhrase=BitVector(textstring=PassPhrase)
roundkey1=findroundkey(PassPhrase.get_bitvector_in_hex(),1)
roundkey2=findroundkey(roundkey1,2)
roundkey3=findroundkey(roundkey2,3)
roundkey4=findroundkey(roundkey3,4)
roundkey5=findroundkey(roundkey4,5)
roundkey6=findroundkey(roundkey5,6)
roundkey7=findroundkey(roundkey6,7)
roundkey8=findroundkey(roundkey7,8)
roundkey9=findroundkey(roundkey8,9)
roundkey10=findroundkey(roundkey9,10)
roundkeys=[roundkey1,roundkey2,roundkey3,roundkey4,roundkey5,roundkey6,roundkey7,roundkey8,roundkey9,roundkey10]


FILEOUT = open("files\ciphertext.txt", 'w')


for y in range(1, loopmsg): 
    if(end+16<length): 
        plaintextseg = message[start:end + 16]
    else: 
        plaintextseg = message[start:length]
        for z in range(0,((end+16)-length),1): 
            plaintextseg = plaintextseg+"\00"
            

  
    bv1 = BitVector(textstring=plaintextseg)
    bv2 = PassPhrase
    resultbv=bv1^bv2
    myhexstring = resultbv.get_bitvector_in_hex()

    for x in range(1, 10):  
        
        myhexstring = resultbv.get_bitvector_in_hex()
        temp1=subbyte(myhexstring)

       
        temp2=shiftrow(temp1)

        
        bv3 = BitVector(hexstring=temp2)
        newbvashex=mixcolumn(bv3)
        newbv=BitVector(hexstring=newbvashex)

        
        bv1 = BitVector(bitlist=newbv)
        bv2 = BitVector(hexstring=roundkeys[x-1])
        resultbv = bv1 ^ bv2
        myhexresult = resultbv.get_bitvector_in_hex()

    
    myhexstring = resultbv.get_bitvector_in_hex()
    temp1=subbyte(myhexstring)

    
    temp2=shiftrow(temp1)

    
    newbv = BitVector(hexstring=temp2)
    bv1 = BitVector(bitlist=newbv)
    bv2 = BitVector(hexstring=roundkeys[9])
    resultbv = bv1 ^ bv2
    myhexstring = resultbv.get_bitvector_in_hex()

    
    outputhextemp = resultbv.get_hex_string_from_bitvector()
    FILEOUT.write(outputhextemp)
    start = start + 16 
    end = end + 16 


FILEOUT.close()

file2=open("files\ciphertext.txt","r")
print("\nThe file was encrypted sucessfully using master key and stored at files\ciphertext.txt \n")
#os.remove("files\plaintext1.txt")
msg=file2.read()
print("The encrypted message inside file is\n\n[",msg,"]")
