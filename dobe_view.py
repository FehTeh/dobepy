import sys
import tkinter as tk
import cv2
from datetime import date, datetime
from PIL import ImageTk, Image
from dobe_config import *
from dobe_api import *

LARGE_FONT = ("ChicagoFLF", 90)
MED_FONT = ("ChicagoFLF", 20) 

DIVIDER_HEIGHT = 3

class Dobe_View():
    def __init__(self):
        root = tk.Tk()
        config = Dobe_Config()
        main = Dobe_MainView(root, background=config.background_color)
        main.pack(side="top", fill="both", expand=True)
        
        width_value = root.winfo_screenwidth()
        height_value = root.winfo_screenheight()
        
        root.geometry(f"{width_value}x{height_value}+0+0")
        root.resizable(False, True)
        root.attributes("-fullscreen", True)
        root.bind("<Escape>", self.close)
        root.mainloop()
    
    def close(self, event=None):
        sys.exit()


class Dobe_MainView(tk.Frame):
    def __init__(self, api, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        config = Dobe_Config()

        #Header (clock and internet)
        self.header_container = tk.Canvas(self, bg=config.background_color, highlightthickness=0, relief='ridge')
        self.header_container.grid(sticky='we')

        self.clock_indicator = tk.Label(self.header_container, font=MED_FONT, background=config.background_color, foreground=config.primary_color)
        self.clock_indicator.grid(sticky='w', column=0, row=0, padx=(10, 10), pady=(10, 0))    
        self.clock_refresh(self.clock_indicator)

        self.network_indicator = tk.Label(self.header_container, text="Wifi On", font = MED_FONT, background=config.background_color, foreground=config.primary_color)
        self.network_indicator.grid(sticky='w', column=3, row=0, padx=(10, 10), pady=(10, 0))
        self.network_refresh(self.network_indicator)

        self.header_container.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        #Divider between header and content
        self.divider = tk.Canvas(self)
        self.divider.configure(bg=config.primary_color, height=DIVIDER_HEIGHT, bd=0, highlightthickness=0, relief='ridge')
        self.divider.grid(row = 1, column = 0, sticky ="we", pady=10, padx=(10, 10))
        
        #Body
        p1 = Dobe_IntercomView(self, bg=config.background_color, highlightthickness=0, relief='ridge')
        p1.grid(row = 2, column = 0, sticky ="nswe")

        #Last Divider
        self.divider2 = tk.Canvas(self)
        self.divider2.configure(bg=config.primary_color, height=DIVIDER_HEIGHT, bd=0, highlightthickness=0, relief='ridge')
        self.divider2.grid(row = 3, column = 0, sticky ="we", pady=10, padx=(10, 30))
        
        #self.settingsButton = tk.Button(self, text="Remove", command= lambda: self.remove(p1))
        #self.settingsButton.grid(row = 4,column = 0)
        #self.settings2Button = tk.Button(self, text="Add", command=lambda: self.add(p1))
        #self.settings2Button.grid(row = 4, column = 1)

    def clock_refresh(self, clockLabel):
        clockLabel.configure(text=datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        clockLabel.after(1, lambda: self.clock_refresh(clockLabel))

    def network_refresh(self, networkLabel):
        networkLabel.configure(text="Wifi on")
        #networkLabel.after(1, lambda: self.clock_refresh(clockLabel))
    
    #def remove(self, p1):
        #p1.grid_forget()

    #def add(self, p1):
        #p1.grid(row = 2, column = 0, sticky ="nswe")

class Dobe_IntercomView(tk.Canvas):
    def __init__(self, *args, **kwargs):
        tk.Canvas.__init__(self, *args, **kwargs)
        config = Dobe_Config()

        #self.frame.grid_rowconfigure(2, weight=1)
        self.videoFrame = tk.Canvas(self)
        self.videoFrame.configure(bg=config.background_color, bd=0, highlightthickness=0)
        self.videoFrame.grid(row=0, column=0, sticky="nsew")
        self.videoLabel = tk.Label(self.videoFrame, bg=config.background_color)
        self.videoLabel.pack(fill='both')

        # Capture from camera
        self.cap = cv2.VideoCapture(config.video_source)
        self.video_stream(self.cap, self.videoLabel)

        # Right buttons
        self.buttonsFrame = tk.Canvas(self)
        self.buttonsFrame.configure(bg=config.background_color, bd=0, highlightthickness=0)
        self.buttonsFrame.grid(row=0, column=1, sticky="nsew")
        self.callImg = tk.PhotoImage(file="assets/call.png")
        self.callButton = tk.Button(self.buttonsFrame, image=self.callImg, bg=config.background_color, height=150, width=150, highlightthickness = 0, bd = 0)
        self.callButton.pack()
        self.unlockImg = tk.PhotoImage(file="assets/call.png")
        self.unlockButton = tk.Button(self.buttonsFrame, image=self.unlockImg, bg=config.background_color, height=150, width=150, highlightthickness = 0, bd = 0)
        self.unlockButton.pack()

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def video_stream(self, cap, videoLabel):
        _, frame = cap.read()
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        img = Image.fromarray(cv2image)
        #newimg = img.resize((100, 100), Image.ANTIALIAS)
        imgtk = ImageTk.PhotoImage(image=img)
        videoLabel.imgtk = imgtk
        videoLabel.configure(image=imgtk)
        videoLabel.after(1, lambda: self.video_stream(cap, videoLabel)) 