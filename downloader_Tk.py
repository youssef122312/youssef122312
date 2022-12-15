from pytube import YouTube
from tkinter import filedialog
import tkinter, customtkinter
from tkinter import *
'''

customtkinter==4.6.3

'''
from customtkinter import *
from pytube import *
from urllib.request import urlopen
from PIL import Image, ImageTk, ImageFile
import requests, os, threading, pathlib, pyautogui, time

PATH1 = os.path.dirname(os.path.realpath(__file__))
PATH = PATH1.replace("\\", "//")



class App():
   
    WIDTH = 780 # 430
    HEIGHT = 520 # 270
    
    def mypopup(self, e):
        self.menu.tk_popup(e.x_root, e.y_root)
    
    def copy(self):
        self.ent.focus()
        pyautogui.hotkey("ctrl", "c")
    
    def paste(self):
        self.ent.focus()
        pyautogui.hotkey("ctrl", "v")
    
    def cut(self):
        self.ent.focus()
        pyautogui.hotkey("ctrl", "x")
        
    def select_all(self):
        self.ent.focus()
        pyautogui.keyDown("shift")
        pyautogui.hotkey("home")
        pyautogui.keyUp("shift")
    
    def about(self):
        try:
            
            pyautogui.hotkey("win", "r")
            time.sleep(0.05)
            pyautogui.write("chrome https://youssefw.netlify.app/")
            time.sleep(0.05)
            pyautogui.hotkey("enter")
            
        except:
            pass

    def __init__(self):
        
        self.root = root = customtkinter.CTk()
        
        customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
        customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
        root.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        root.resizable(False, False)
        root.title('Youtube Downloader By YM')
        #########################################################################################################################################################

        self.frame_left = customtkinter.CTkFrame(master=self.root, width=350, height=250, corner_radius=7)
        self.frame_left.place(relx=0.016, rely=0.02)
        
        self.frame_left_botton = customtkinter.CTkFrame(master=self.root, width=350, height=240, corner_radius=7)
        self.frame_left_botton.place(relx=0.016, rely=0.52)
        
        self.frame_right = customtkinter.CTkFrame(master=self.root, width=400, height=500, corner_radius=7)
        self.frame_right.place(relx=0.48, rely=0.02)
        
        ##########################################################################################################################################################
        
        self.entput = StringVar()
        self.ent=CTkEntry(master=self.frame_left, width=340, textvariable=self.entput, placeholder_text='Enter a url', corner_radius=10) 
        self.ent.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)
         
        self.lab=customtkinter.CTkLabel(master=self.frame_left, text='Enter Your Vedio url', text_font=("arial Bold", 14))  
        self.lab.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)
        
        self.btn2=customtkinter.CTkButton(master=self.frame_left, text='ok', text_font=("arial Bold", 10), command=self.ok) 
        self.btn2.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

        
        self.clabal = customtkinter.CTkLabel(master=self.frame_left_botton, text="Choose Your Vedio Quality",  text_font=("arial Bold", 14))
        self.clabal.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)
        
        self.ocbox = ["highest"]
        self.cpbox = StringVar()
        self.cbox = customtkinter.CTkOptionMenu(master=self.frame_left_botton,variable=self.cpbox, values=self.ocbox, command=self.ok)
        self.cbox.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)
        self.cbox.set('highest')
        
        self.cflabal = customtkinter.CTkLabel(master=self.frame_left_botton, text=" Choose Your Vedio Saving path",  text_font=("arial Bold", 14))
        self.cflabal.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    
        self.cfbox = customtkinter.CTkButton(master=self.frame_left_botton, text='Select From PC', text_font=("arial", 10), command=self.filepath)
        self.cfbox.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)
        
        
        self.lab1 = CTkLabel(master=self.frame_right, text="Title:  ", text_font=("arial Bold", 11))
        self.lab1.place(relx= 0.06, rely=0.4)
        
        self.lab4 = CTkLabel(master=self.frame_right, text="Lenth:  ", text_font=("arial Bold", 11))
        self.lab4.place(relx= 0.06, rely=0.5)     
        
        self.lab4 = CTkLabel(master=self.frame_right, text="size:  ", text_font=("arial Bold", 11))
        self.lab4.place(relx= 0.06, rely=0.6)
        
        self.lab3 = CTkLabel(master=self.frame_right, text="date uploaded:  ", text_font=("arial Bold", 11))
        self.lab3.place(relx= 0.05, rely=0.7)
        
        self.btn1 = CTkButton(master=self.frame_right, text="Download", text_font=("arial Bold", 10), command=self.download)
        self.btn1.place(relx= 0.63, rely=0.92)
        
        self.menu = Menu(master=root, tearoff=False, activebackground="#1840af", background="#3a6cf4", fg="white")
        self.menu.add_command(label="Copy", command=self.copy)
        self.menu.add_command(label="Paste", command=self.paste)
        self.menu.add_command(label="Cut", command=self.cut)
        self.menu.add_separator()
        self.menu.add_command(label="Select all", command=self.select_all)
        self.menu.add_separator()
        self.menu.add_command(label="About", command=self.about)
        root.bind("<Button - 3>", self.mypopup)
        
        root.mainloop()
        
    
    
    
    def filepath(self):
        
        self.folder = filedialog.askdirectory()
        
        
    def image_down(self):
        
        img_sourse = requests.get(self.ims)
        suf = pathlib.Path(self.ims).suffix
        if suf not in ['.png', '.jpg', '.jpeg', '.gif']:
            self.out = 'img.png'
        else:
            self.out = 'img'+suf
            
        with open(f"{PATH}//{self.out}", "wb") as f:
            f.write(img_sourse.content)
            f.close()
            
        ImageFile.LOAD_TRUNCATED_IMAGES = True

    def haeh(self):
        self.imafe2 = Image.open(f"{PATH}//{self.out}")
        resized = self.imafe2.resize((self.imafe2.width//3, self.imafe2.height//3), Image.Resampling.LANCZOS)
        self.home_image = ImageTk.PhotoImage(resized)
        self.label11 = CTkLabel(master=self.frame_right,corner_radius=5, width=self.imafe2.width//3, image=self.home_image)
        self.label11.place(relx= 0.23, rely=0.04)
        #my_image = customtkinter.CTkImage(light_image=Image.open(f"{PATH}//{self.out}"),dark_image=Image.open(f"{PATH}//{self.out}"),size=(self.imafe2.width//3, self.imafe2.height//3))

    
    def ok(self, choise='highest'):
        self.lab1.place(relx= 5, rely=6)
        
        self.url = self.entput.get()
        self.quality = choise
        self.v_info = YouTube(self.url)
        self.strems = YouTube(self.url).streams
        self.ims = YouTube(self.url).thumbnail_url
        
        q1 = threading.Thread(target=self.image_down)
        q2 = threading.Thread(target=self.haeh)
        q1.start()
        q1.join()
        q2.start()
        
        self.dete = YouTube(self.url).publish_date
        self.title = YouTube(self.url).title
        self.lenth = YouTube(self.url).length
        if choise == "highest" :
            self.size = YouTube(self.url).streams.get_highest_resolution().filesize
        else:
            self.size = YouTube(self.url).streams.get_by_resolution(choise).filesize
             
        ltitle = len(self.title)
        
        


        if ltitle <= 40:
            self.lab1 = CTkLabel(master=self.frame_right, text=f"Title:  {self.title}", text_font=("arial Bold", 11))
        if ltitle > 40:
            self.lab1 = CTkLabel(master=self.frame_right, text=f"Title:  {self.title[:40]}\n{self.title[40:]}", text_font=("arial Bold", 11))
        if ltitle >= 80:
            self.lab1 = CTkLabel(master=self.frame_right, text=f"Title:  {self.title[:40]}\n{self.title[40:80]}\n{self.title[80:]}", text_font=("arial Bold", 11))
        for i in range(ltitle):
            if i < 30:
                self.lab1.place(relx= -0.04+(int(i)/500), rely=0.4) 
            else:
                pass
            
        self.lab4 = CTkLabel(master=self.frame_right, text=f"Lenth:  {self.lenth}s", text_font=("arial Bold", 11))
        self.lab4.place(relx= 0.06, rely=0.5)     

        self.lab4 = CTkLabel(master=self.frame_right, text=f"size:  {self.size/(1024*1024):.2f} MB", text_font=("arial Bold", 11))
        self.lab4.place(relx= 0.06, rely=0.6) 
        
        self.lab3 = CTkLabel(master=self.frame_right, text=f"date uploaded: {self.dete}", text_font=("arial Bold", 11))
        self.lab3.place(relx= 0.05, rely=0.7)
        
        
        for stream in self.strems.filter(file_extension='mp4', progressive=True):
            
            if stream.resolution in self.ocbox:
                pass
            else:
                self.ocbox.append(f"{stream.resolution}")
            
        
        self.cbox = customtkinter.CTkOptionMenu(master=self.frame_left_botton, variable=self.cpbox, values=self.ocbox, command=self.ok)
        self.cbox.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)
        self.folder = None
        
        
        
    def download(self):
        
        if self.quality == 'highest':
            t = self.strems.get_highest_resolution()
            t.download(self.folder)
        else:
            for stream in self.strems.filter(file_extension='mp4', progressive=True):
                if stream.resolution == self.quality:
                    stream.download(self.folder)
                else:
                    self.d = False
                    pass
                    
        
if __name__ == "__main__":
    App()
