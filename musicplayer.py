import os
os.system("pip install pygame")
os.system("pip install pytube")
from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as ms
from pygame import mixer
import pygame
from pytube import YouTube
r=Tk()
r.geometry("300x350")
r.configure(bg="cyan")
def op ():
    #all files option is nececarry tumhare kaam  file se bhi jyda important hai
    ope=fd.askopenfilename(filetypes=(("Music","*.mp3"),("all files","*.*")))
    r.title(ope)
    pygame.mixer.init()
    mixer.music.load(ope)
    
    
    
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

    

main=Menu(r,bg="orchid")
opt=Menu(main,tearoff=0,bg="orchid")
opt.add_command(label="open",command=op)
opt.add_command(label="Download",command=h)
opt.add_command(label="quit",command=quit)
r.config(menu=main)
main.add_cascade(label="Load Music",menu=opt)
g=Label(r,text="pratv3 music player",fg="black",bg="cyan",font="lucida 20 bold").pack()
x=Canvas(height=200,width=200,background="light green").pack()

g=Button(r,text="play",command=play,bg="blue").pack(fill=X,anchor=S)
g=Button(r,text="pause",command=pause,bg="red").pack(fill=X,anchor=S)
g=Button(r,text="resume",command=resume,bg="green").pack(fill=X,anchor=S)

r.mainloop()
