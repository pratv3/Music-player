from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as ms
from pygame import mixer
import pygame
import datetime
from pytube import YouTube
import os
os.system("pip install pytube")
os.system("pip install pygame")
date=int(datetime.datetime.now().hour)
if date>=7 and date<19:
    bac="white"
    fot="black"
    print("font light")
else:
    bac="black"
    fot="white"
    print("font Dark")
r=Tk()
r.geometry("300x350")
r.configure(bg=bac)
def op ():
    #all files option is nececarry tumhare kaam  ki file se bhi jyda important hai
    ope=fd.askopenfilename(filetypes=(("Music","*.mp3"),("all files","*.*")))
    r.title(ope)
    pygame.mixer.init()
    mixer.music.load(ope)
# for chainging to night mode
def mode ():
    pass

    
    
# music playble function

def play():
    try:
        mixer.music.play()
    except:
        ms.showerror("music player","no file was loaded in the player load the file")
        op()
def pause():
    mixer.music.pause()
def resume():
    mixer.music.unpause()
def h():
    try:
        mixer.music.pause()
        d=ms.askokcancel("music player","do you want to download by youtube")
        if d==True:
            ms.showinfo("music player","paste the link of video and hit enter")
            import down
            
        else:
            mixer.music.unpause()
    except:
        ms.showinfo("music player","download canceled load a music to try it")

    

main=Menu(r,bg=bac,fg=fot)
opt=Menu(main,tearoff=0,bg=bac,fg=fot)
opt.add_command(label="open",command=op)
opt.add_command(label="Download",command=h)
the=Menu(opt,tearoff=0,bg=bac,fg=fot)
opt.add_command(label="quit",command=quit)
r.config(menu=main)
main.add_cascade(label="Load Music",menu=opt)
g=Label(r,text="pratv3 music player",fg=fot,bg=bac,font="lucida 20 bold").pack()
x=Canvas(height=200,width=200,background="grey").pack()

g=Button(r,text="play",command=play,bg="blue").pack(fill=X,anchor=S)
g=Button(r,text="pause",command=pause,bg="red").pack(fill=X,anchor=S)
g=Button(r,text="resume",command=resume,bg="green").pack(fill=X,anchor=S)

r.mainloop()
