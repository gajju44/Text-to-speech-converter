import tkinter as tk
from tkinter import *
from PIL import Image,ImageTk
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
import pyttsx3
import mysql.connector


engine = pyttsx3.init()

#function for text to speech play button

def speaknow():

 
    
    v=text.get()

    if ( v =="" ):

       
        MessageBox.showinfo(title="Error!!!",
                            message=str("You forgot to enter text please go through it first"))

    else:
        engine.setProperty("rate",130)
        engine.say(textv.get())
        engine.runAndWait()
       
        
#function of credit button

def credits():

    credit=tk.Tk()
    credit.geometry("1000x2000")
    credit.config(bg="black")
    credit.title("CREDITS")
    labelc=tk.Label(credit,text="\nMADE BY:\t"
                        "\n1)Piyush Pise\t"
                        "\n2)Harsh Dubey\t"
                        "\n\t3)Gajendra Naphade\t"
                        "\n4)Aryan Moon\t"
                        "\n5)Jatin Mahajan\t",font=("Roboto",19
                                                      ),bd=10,fg="white",bg="black")
    labelc.pack()

    labelc2=tk.Label(credit,text="\nThis project is named"
                                "\nas Text to speech converter\t"
                                "\nWhich converts text\t"
                                "\n\tto sound which is made\t"
                                "\nAt the time of Ibase\t"
                                "\n\tTechnologies Internship\t"
                                "\n\tin the guideance of Rohini mam\t"
                                "\n\tThis project is made\t"
                                "\n\tin Python Programing\t"
                                "\nLanguage it's gui \t"
                                "\n\tis made by using tkinter\t"
                                "\n\tmodule it is also having \t"
                                "\n\tdatabase for saving users\t"
                                "\n\tfiles and user can also\t"
                                "\n\tsee it's previous recording if\t"
                                "\n\t\the/she saved it while converting\t"
                                "\n\n\tTHANK YOU\t",font=("celebri",19),fg="white",bg="black")
    labelc2.pack()

   #function for inserting data in database
   
def insert():
    
    v=text.get()

    if ( v =="" ):

       
        MessageBox.showinfo(title="Error!!!",
                            message=str("You forgot to enter text please go through it first"))
        

    else:
        

        con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="text_to_speech"
        )

        cursor = con.cursor()

        cursor.execute("INSERT INTO saves  VALUES ( '" + v +"')")
        cursor.execute("commit")

        MessageBox.showinfo(" INSERT STATUS ", "INSERTED IN SAVES SUCESSFULLY")
        con.close()


  #  Previous_recordings function    

def Previous_recordings():
    save=tk.Tk()
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="text_to_speech"
        )
    cursor = con.cursor()

    cursor.execute("select * from saves")
    records=cursor.fetchall()
    
    save.geometry("1000x2000")
    save.config(bg="black")
    save.title("Previous recordings")
    
    for row in records:
       label1=tk.Label(save,
                        text=(row[0]),font=('inter',50),bg="black",fg="green2")
       label1.pack()

      
    con.close()
    

    
global textv
global e1


#tkinter window settings 
audio=tk.Tk()
textv=tk.StringVar()
#window size when it opens
audio.geometry("2000x2000")
#background color 
audio.config(bg="#071e26")
#window logo setting
oto=PhotoImage(file='logo.png')
audio.iconphoto(False,oto)
#window title
audio.title("Audio Recordings")



#TITLE 



tk.Label(audio,text="TEXT TO SPEECH",bg="pink",fg="black",font=("Roboto",12,"bold"),width=2000,height=2).pack()


#ENTER TEXT


tk.Label(audio,text="Enter the text",font=("Roboto",13,"bold"),bd=6,fg="black",bg="white",width=48,height=1).place(x=200,y=130)

text=tk.Entry(audio,textvariable=textv,fg="black",bg="white",width=42,font=("Roboto",16),bd=3)

text.place(x=750,y=128)



#SAVE BUTTON

saveimage=Image.open('save.png')
gim=saveimage.resize((50,45),Image.BICUBIC)
imge=ImageTk.PhotoImage(gim)


insert= tk.Button(audio,text="Save ",fg="black",font=("Roboto",13,"bold"),bg="#13d64f",command = insert,bd=5,image=imge,compound=LEFT,width=500,height=26).place(x=190,y=221)



#PLAY BUTTON

image=(Image.open('speak.png'))
mg=image.resize((35,33),Image.BICUBIC)
img=ImageTk.PhotoImage(mg)


play = tk.Button(audio,text='Play audio',fg="black",bg="#13d64f",font=("Roboto",13,"bold"),image=img,compound=LEFT,bd=5,width=500,height=26,command=speaknow).place(x=750,y=220)


#PREVIOUS RECORDINGS BUTTON

previousimage=Image.open('Previous.png')
pimg=previousimage.resize((30,35),Image.BICUBIC)
pimge=ImageTk.PhotoImage(pimg)


tk.Button(audio,text="Previous recordings",command=Previous_recordings,font=("Roboto",13,"bold"),fg="black",bg="#13d64f",bd=5,image=pimge,compound=LEFT,width=500,height=26).place(x=190,y=320)


#EXIT

tk.Button(audio,text="Exit",fg="black",bg="red3",command=audio.destroy,font=("Roboto",13,"bold"),bd=5,width=40,height=1).place(x=500,y=400)

#MADE BY


tk.Button(audio,text="Credits",fg="black",bg="#13d64f",command=credits,font=("Roboto",13,"bold"),bd=5,width=50,height=1).place(x=750,y=320)

tk.mainloop()


