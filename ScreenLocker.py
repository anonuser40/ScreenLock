from tkinter import *
import vlc, urllib.request, time
from PIL import Image, ImageTk

password = "test" # [!] Your password goes here [!]

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)
        urllib.request.urlretrieve('https://i.ibb.co/RCG4JzQ/slamsw.jpg',"slamsw.jpg") # Custom image from internet, Image name
        load = Image.open("slamsw.jpg") # Image name
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img_w = load.size[0] # Image width
        img_h = load.size[1] # Image height
        screen_w = root.winfo_screenwidth() # Screen Size Width
        screen_h = root.winfo_screenheight() # Screen Size Height
        global x_w, y_h
        x_w = screen_w / 2 - img_w / 2
        y_h = screen_h / 2 - img_h / 2
        img.place(x=x_w,y=y_h) # Image position

def login():
    pass_guess = enter_passwd.get()
    if pass_guess == password:exit()
    else:pass

def delwin():
    root.update()
    pass

try:
    music = vlc.MediaPlayer("") # Mp3 file link
    music.play()
except:pass

root = Tk()
app = Window(root)
root.title("ScreenLock") # Title name
root.config(cursor="arrow") # Cursor type none,arrow
root.protocol("WM_DELETE_WINDOW", delwin) # Prevent to close window
app.configure(background="#000") # Background color
root.configure(background="#000") # Background color
root.attributes('-fullscreen', True) # Fullscreen
text = Label(root, text="Stop looking at my screen", fg="#fff", bg="#000", font=('Arial', 32)) # Your text goes here!
text.pack()
enter_passwd = Entry(root, show='*', width=32,fg='#fff',borderwidth=0,font=('Arial', 14)) # Input
enter_passwd.pack()
enter_passwd.focus_set()
btn = Button(root,text='Enter',borderwidth=0,fg='#fff',command=login) # Button
btn.pack(side='bottom')
enter_passwd.place(x=20,y=100)
btn.place(x=345, y=100)
text.place(x=20,y=10)

if __name__ == '__main__':
    login()
    root.mainloop()
