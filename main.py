from tkinter import *
import pygame
from tkinter import filedialog


def rcc():
    
    rcc = Tk()
    rcc.geometry('500x400')
    rcc.title("FRIENDSHIP CALCULATOR")

    
    list = Listbox(rcc,bg="aquamarine",width=60,selectforeground="light cyan",selectbackground="teal")
    list.pack(pady=30)
    
    rc =Frame(rcc)
    rc.pack()

    label1=Label(rc,text="ENTER YOUR NAME")
    label1.grid(row=0,column=0)
    your=Entry(rc)
    your.grid(row=0,column=1)

    
    label1=Label(rc,text="ENTER FRIEND NAME")
    label1.grid(row=1,column=0)
    frnd1=Entry(rc)
    frnd1.grid(row=1,column=1)

    
    label1=Label(rc,text="ENTER FRIEND NAME")
    label1.grid(row=2,column=0)
    frnd2=Entry(rc)
    frnd2.grid(row=2,column=1)
    
    
    label1=Label(rc,text="ENTER FRIEND NAME")
    label1.grid(row=3,column=0)
    frnd3=Entry(rc)
    frnd3.grid(row=3,column=1)
    
    
    label1=Label(rc,text="ENTER FRIEND NAME")
    label1.grid(row=4,column=0)
    frnd4=Entry(rc)
    frnd4.grid(row=4,column=1)

    

    def submit():
        l1=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        
        sum1=0
        for i in str(frnd1):
            k=0
            for j in l1:
                k=k+1
                if(i==j):
                    break
            sum1=sum1+k
        sum1=str(sum1)
        sum1=f'{str(frnd1)}{sum1}%'
        print(sum1)
        a=sum1
        list.insert(i,a)

        sum2=0
        for i in str(frnd2):
            k=0
            for j in l1:
                k=k+1
                if(i==j):
                    break
            sum2=sum2+k
        sum2=str(sum2)
        sum2=str(frnd2)+sum2+"%"
        a=sum2
        list.insert(i,a)

        sum3=0
        for i in str(frnd3):
            k=0
            for j in l1:
                k=k+1
                if(i==j):
                    break
            sum3=sum3+k
        sum3=str(sum3)
        sum3=str(frnd3)+sum3+"%"
        a=sum3
        list.insert(i,a)

        sum4=0
        for i in str(frnd4):
            k=0
            for j in l1:
                k=k+1
                if(i==j):
                    break
            sum4=sum4+k
        sum4=str(sum4)
        sum4=str(frnd4)+sum4+"%"
        a=sum4
        list.insert(i,a)

        
    
    Submit=Button(rc,width=10,bg="light steel blue",text="Submit",command=submit)
    Submit.grid(row=5,column=1)

    
    rc.mainloop()



root = Tk()
root.geometry('500x300')
root.title('Sangeet Player')
"""root.wm_iconbitmap("")"""

pygame.mixer.init()

scrollbar=Scrollbar(root)
scrollbar.pack(side=RIGHT,fill="y")

for i in range (200):
    pass

def add_song():
        song = filedialog.askopenfilename()
        
        song_box.insert(i,song)
        
def play():
        i=0
        song = song_box.get(ACTIVE)
        pygame.mixer.music.load(song)
        pygame.mixer.music.play()


def next():
    i+1
    song_box.selection_includes
    song = song_box.get(ACTIVE)
    pygame.mixer.music.load(song)
    pygame.mixer.music.play()
    pass

def previous():
    pass


def pause():
    pygame.mixer.music.pause()

def unpause():
    pygame.mixer.music.unpause()    

def playlist():
    pass

def About():
    pass

f1=Frame(root)
f1.pack()

song_box = Listbox(root,bg="aquamarine",width=60,selectforeground="light cyan",selectbackground="teal")
scrollbar.config(command=song_box.yview_scroll)
song_box.pack(pady=30,padx=32)


control =Frame(root)
control.pack()

previous=Button(control,width=10,bg="light steel blue",text="Previous",command=previous,)
previous.grid(row=1,column=1)

Next=Button(control,width=10,bg="light steel blue",text="Next",command=next)
Next.grid(row=1,column=2)

pause=Button(control,width=10,bg="light steel blue",text="Pause",command=pause)
pause.grid(row=1,column=4)

unpause=Button(control,width=10,bg="light steel blue",text="Unpause",command=unpause)
unpause.grid(row=1,column=5)

play=Button(control,width=10,bg="light steel blue",text="Play",command=play)
play.grid(row=1,column=3,)

top=Label(text="21200153",bg="powderblue")
top.pack(side=BOTTOM,fill="x")

my_menu=Menu(root)
root.config(menu=my_menu)
my_menu.add_command(label="Add Sangeet",command=add_song)
my_menu.add_command(label="Friendship Calculator",command=rcc)
my_menu.add_command(label="About",command=About)
root.mainloop()
