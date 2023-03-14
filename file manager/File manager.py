import sys
import os
import tkinter as tk
from tkinter import *
import pyrebase
from PIL import ImageTk, Image
from AESencryptfunc import *
import math 
import getpass 
from tkinter.filedialog import askopenfile
from AESdecryptfunc import *  
import io
import getpass
    

window=Tk()

window.title("File repository manager")
window.geometry('800x700')
#window.configure(bg="#856ff8")
bg = ImageTk.PhotoImage(Image.open("icon.png"), master=window )
canvas1 = tk.Canvas( window, width = 800, height = 800)
  
canvas1.pack(fill = "both", expand = True)
canvas1.create_image( 150, 200, image = bg, anchor = "nw")

l = Label(window, text = "File Repository Manager", width=25)
l.config(font =("Arial bold", 20))
l1 = Label(window, text = "Encrypt and Upload files", width=25)
l1.config(font =("Courier", 14))
l2 = Label(window, text = "Restore and Decrypt files", width=25)
l2.config(font =("Courier", 14))
l.place(x=200,y=50)
l1.place(x=30,y=150)
l2.place(x=500,y=150)

def encryption():
    #file=open("files\plaintext1.txt", "r")
    file= askopenfile(mode ='r')
    message=(file.read())
    #print("Inside your plaintext message is:\n%s\n" % message)
    file.close()
    print("File selected...\n")
    PassPhrase=""
    while(len(PassPhrase)!=16):
        print("Enter the master key to encrypt your file")
        PassPhrase=getpass.getpass()
        if(len(PassPhrase)<16):
            while(len(PassPhrase)!=16):
                PassPhrase=PassPhrase+"\00"
        if(len(PassPhrase)>16):
            print("Your passphrase was larger than 16, truncating passphrase.")
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

def decryption():
    PassPhrase=""

    while(len(PassPhrase)!=16):
        print("Enter the master key to decrypt ")
        PassPhrase=getpass.getpass()
        if(len(PassPhrase)<16):
            while(len(PassPhrase)!=16):
                PassPhrase=PassPhrase+"\00"
        if(len(PassPhrase)>16):
            print("Your passphrase was larger than 16, truncating passphrase.")
            PassPhrase=PassPhrase[0:16]


    file=open("files\ciphertext.txt", "r")
    message=(file.read())
    #print("Inside your ciphertext message is:\n%s\n" % message)
    file.close()


    start=0
    end=32
    length=len(message)
    loopmsg=0.00
    loopmsg=math.ceil(length/32)+1
    outputhex=""
    asciioutput=""


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

    FILEOUT = io.open("files\plaintext2.txt", 'w', encoding='utf-8')


    for y in range(1, loopmsg): 
        plaintextseg = message[start:end]

    
        bv1 = BitVector(hexstring=plaintextseg)
        bv2 = BitVector(hexstring=roundkeys[9])
        resultbv = bv1 ^ bv2
        myhexstring = resultbv.get_bitvector_in_hex()

    
        myhexstring=invshiftrow(myhexstring)

  
        myhexstring=invsubbyte(myhexstring)

        for x in range(8, -1, -1):
       
            bv1 = BitVector(hexstring=myhexstring)
            bv2 = BitVector(hexstring=roundkeys[x])
            resultbv = bv1 ^ bv2
            myhexstring = resultbv.get_bitvector_in_hex()

       
            bv3 = BitVector(hexstring=myhexstring)
            myhexstring=invmixcolumn(bv3)


            myhexstring = invshiftrow(myhexstring)

        
            myhexstring = invsubbyte(myhexstring)

    
        bv1 = BitVector(hexstring=myhexstring)
        bv2 = PassPhrase
        resultbv = bv1 ^ bv2
        myhexstring = resultbv.get_bitvector_in_hex()

        start = start + 32 
        end = end + 32 

        replacementptr = 0
        while (replacementptr < len(myhexstring)):
            if (myhexstring[replacementptr:replacementptr + 2] == '0d'):
                myhexstring = myhexstring[0:replacementptr] + myhexstring[replacementptr+2:len(myhexstring)]
            else:
                replacementptr = replacementptr + 2

        outputhex = BitVector(hexstring=myhexstring)
        asciioutput = outputhex.get_bitvector_in_ascii()
        asciioutput=asciioutput.replace('\x00','')
        FILEOUT.write(asciioutput)

    FILEOUT.close()

    print("The file was decrypted sucessfully")

    file2=io.open("files\plaintext2.txt", "r", encoding='utf-8')
    print("\nThe decrypted message is:\n%s\n\n " % file2.read())
    file2.close()
    os.remove("files\plaintext2.txt")
    #os.remove("files\ciphertext.txt")
    
def upload():
    
    firebaseConfig = {
   'apiKey': "AIzaSyC8vywFlC_W6dhOAoGPp9zT76_LVcs67qo",
   'authDomain': "password-repository-4fb04.firebaseapp.com",
    'databaseURL':"https://password-repository-4fb04.firebaseio.com",
   'projectId': "password-repository-4fb04",
   'storageBucket': "password-repository-4fb04.appspot.com",
   'messagingSenderId': "394258851576",
   'appId': "1:394258851576:web:5d0ba76c7559bf11f8bd0d",
   'measurementId': "G-Q4ZC04QTLK"
     }


    firebase = pyrebase.initialize_app(firebaseConfig)

    storage = firebase.storage()

    file = "files\ciphertext.txt"

    cloudname=input("Enter name of file in repository")

    storage.child(cloudname).put(file)

    print("file uploaded sucessfully...")

    #os.remove(file)
def restore():
    firebaseConfig = {
  'apiKey': "AIzaSyC8vywFlC_W6dhOAoGPp9zT76_LVcs67qo",
  'authDomain': "password-repository-4fb04.firebaseapp.com",
    'databaseURL':"https://password-repository-4fb04.firebaseio.com",
  'projectId': "password-repository-4fb04",
  'storageBucket': "password-repository-4fb04.appspot.com",
  'messagingSenderId': "394258851576",
  'appId': "1:394258851576:web:5d0ba76c7559bf11f8bd0d",
  'measurementId': "G-Q4ZC04QTLK"
    }

    firebase = pyrebase.initialize_app(firebaseConfig)

    storage = firebase.storage()

    cloudname=input("Enter name of file in repository :")

    file="files\ciphertext.txt"
    storage.child(cloudname).download(file)

    print("\n File sucessfully restored at",file)
    

btn2 = Button(window, text="Encryption", bg="black", width=8,height=3,fg="white",command=encryption)

btn3 = Button(window, text="Decryption", bg="black",width=8,height=3, fg="white",command=decryption)

btn = Button(window, text="Upload", bg="black",width=8,height=3, fg="white",command=upload)

btn1 = Button(window, text="Restore", bg="black",width=8,height=3, fg="white",command=restore)


btn2.place(x=70,y=300)
btn3.place(x=700,y=400)
btn.place(x=70,y=400)
btn1.place(x=700,y=300)
window.mainloop()