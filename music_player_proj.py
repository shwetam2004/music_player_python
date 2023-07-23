from tkinter import *
from tkinter import filedialog
from pygame import mixer
import os

root = Tk()
root.title('Music player project')
root.geometry("920x670+290+85")
root.configure(bg="#0f1a2b")
root.resizable(False, False)

mixer.init()

def Add_Music():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir(path)

        for song in songs:
            if song.endswith(".mp3"):
                Playlist.insert(END, song)

def Play_Music():
    Music_Name = Playlist.get(ACTIVE)
    print(Music_Name[0:-4])
    mixer.music.load(Playlist.get(ACTIVE))
    mixer.music.play()

def Next_Song():
    next_index = (Playlist.curselection()[0] + 1) % Playlist.size()
    Playlist.selection_clear(0, END)
    Playlist.activate(next_index)
    Playlist.selection_set(next_index)
    Play_Music()

def Previous_Song():
    prev_index = (Playlist.curselection()[0] - 1) % Playlist.size()
    Playlist.selection_clear(0, END)
    Playlist.activate(prev_index)
    Playlist.selection_set(prev_index)
    Play_Music()


#Play Button
Button_Play = PhotoImage(file="play.png")
Button(root, image=Button_Play, bg="#0f1a2b", bd=0, command=Play_Music).place(x=100, y=450)

#Stop button
Button_Stop = PhotoImage(file="stop.png")
Button(root, image=Button_Stop, bg="#0f1a2b", bd=0, command=mixer.music.stop).place(x=200, y=450)

#Pause Button
Button_Pause = PhotoImage(file="pause.png")
Button(root, image=Button_Pause, bg="#0f1a2b", bd=0, command=mixer.music.pause).place(x=300, y=450)

#Resume Button
Button_Resume = PhotoImage(file="resume.png")
Button(root, image=Button_Resume, bg="#0f1a2b", bd=0, command=mixer.music.unpause).place(x=400, y=450)

# Previous Song Button
Button_Previous = PhotoImage(file="previous.png")
Button(root, image=Button_Previous, bg="#0f1a2b", bd=0, command=Previous_Song).place(x=500, y=450)

# Next Song Button
Button_Next = PhotoImage(file="next.png")
Button(root, image=Button_Next, bg="#0f1a2b", bd=0, command=Next_Song).place(x=600, y=450)

#music
Frame_Music = Frame(root, bd=2, relief = RIDGE)
Frame_Music.place(x=30, y=120, width=560, height=250)

Button(root, text="Add Music", width=15, height=2, font=("Hello valentica",20,"bold"),fg="Black", bg="#21b3de", command= Add_Music).place(x=30, y=30)

Scroll = Scrollbar(Frame_Music)
Playlist = Listbox(Frame_Music, width=100, font=("Comic sans",16), bg="#333333", fg="grey", selectbackground="lightblue", cursor="hand2", bd=0, yscrollcommand=Scroll.set)
Scroll.config(command=Playlist.yview)
Scroll.pack(side=RIGHT, fill=Y)
Playlist.pack(side=LEFT, fill=BOTH)

root.mainloop()
