from tkinter import *
from pytube import YouTube
from tkinter import messagebox as msg
def df ():
    def do():
        try:
            video=YouTube(dd.get())
            a=video.streams.get_audio_only()
            a.download()
            msg.showinfo("Download","Your youtube video is sucessfully downloaded")

        except:
            print("Error in dependencies loading!!")
    r=Tk()
    r.title("Musicplayer downloader")
    Label(r,text="Download the youtube video",font="lucida 10 bold").pack()
    dd=StringVar()
    e=Entry(r,textvariable=dd).pack()
    c=Button(r,text="Download",bg="green",fg="white",command=do).pack()
    r.mainloop()
if __name__=='__main__':
    df()
