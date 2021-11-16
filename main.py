from blur import BBlur
from tkinter import * 
from tkinter import ttk
import os
import sys
import tkinter as tk
import tkinter.font as tkFont
import easygui
import re
from PIL import UnidentifiedImageError
from PIL import Image, ImageTk


        
class App():
    
    #commands for file_button
    def file_button(self):
            self.aaa = easygui.fileopenbox(title="BBlur choose files", multiple=True)
            
            if self.aaa == None:
                self.aaa == ""
                    
    #commands for do_it_button    
    def do_it_button(self):
        v1 = f"{self.var1.get()}"
        v2 = f"{self.var2.get()}"
        v3 = f"{self.var3.get()}"
        
        d1 = int(f"{self.dig1.get()}")
        d2 = int(f"{self.dig2.get()}")
        
        try:
            if v1 == "True":
                for o in self.aaa:
                    BBlur().imgBlur(o)
            if v2 == "True":
                for o in self.aaa:
                    BBlur().imgBoxBlur(o, d1)
            if v3 == "True":
                for o in self.aaa:
                    BBlur().imgGausBlur(o, d2)
                    
        except ValueError:
            self.mess.set("Format error, please choose another.")
        
        except AttributeError:
            self.mess.set("Format error or you didn't select a file.")
        
        except TypeError:
            self.mess.set("Format error or you didn't select a file.")
        
        except UnidentifiedImageError:
            self.mess.set("Format error, select png or jpg.")
            
    
    def __init__(self, root):
        
        root.title("BBlur - Blur Tool")
        root.iconphoto(True, tk.PhotoImage(file='yell_box.png'))
        
        width=350
        height=600
        
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)

        
        mainframe = Frame(root, bg="#ffffff")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        
        root.resizable(width=False, height=False)
        
        
        #Image on the top
        
        self.imgg = Image.open("text.png")
        self.phimgg = ImageTk.PhotoImage(self.imgg)
        tk.Label(mainframe, image=self.phimgg).place(x=10,y=10,width=330,height=180)
        
        #Checkbuttons variable
        self.var1 = BooleanVar()
        self.var1.set(0)
        self.var2 = BooleanVar()
        self.var2.set(0)
        self.var3 = BooleanVar()
        self.var3.set(1)
        
        #Checkbuttons
        self.ch_bt_bl = tk.Checkbutton(mainframe, 
                                       variable=self.var2, 
                                       bg="#ffffff", 
                                       text="Pixel", 
                                       onvalue=1, 
                                       offvalue=0, 
                                       relief=FLAT).place(x=10,y=220,width=100,height=50)
        
        self.ch_bt_px = tk.Checkbutton(mainframe, 
                                       bg="#ffffff", 
                                       variable=self.var1, 
                                       text="Blur", 
                                       relief=FLAT).place(x=125,y=220,width=100,height=50)
        
        self.ch_bt_gs = tk.Checkbutton(mainframe, 
                                       bg="#ffffff", 
                                       variable=self.var3, 
                                       text="Gauss", 
                                       relief=FLAT,).place(x=240,y=220,width=100,height=50)
        
        #Scale
        self.dig1 = IntVar()
        self.dig1.set(5)
        self.dig2 = IntVar()
        self.dig2.set(7)
        
        tk.Scale(mainframe, 
                 bg="#ffffff", 
                 orient=VERTICAL, 
                 length=100, 
                 width=50, 
                 variable=self.dig2, 
                 to=25, 
                 from_=1).place(x=240,y=290,width=100,height=100)
        
        tk.Scale(mainframe, 
                 bg="#ffffff", 
                 orient=VERTICAL, 
                 length=100, 
                 width=50, 
                 variable=self.dig1, 
                 to=25, 
                 from_=1).place(x=10,y=290,width=100,height=100)
        
        #File search
        tk.Button(mainframe, 
                  bg="#ffffff", 
                  text="Get files", 
                  command=self.file_button).place(x=80,y=430,width=75,height=45)
        
        #Do it! button
        tk.Button(mainframe, 
                  bg="#ffffff", 
                  text="Do it!", 
                  command=self.do_it_button).place(x=205,y=430,width=75,height=45)
        
        self.mess = StringVar()
        
        #License and rights texts
        tk.Message(mainframe, bg="#ffffff", textvariable=self.mess, anchor=NW, relief=RAISED, width=300).place(x=25,y=500,width=300,height=35)
        

root = Tk()
App(root)
root.mainloop()
