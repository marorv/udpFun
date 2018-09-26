import tkinter as tk
from tkinter import ttk

import random
import time
import socket

#UDP_IP = "10.42.0.2"
UDP_IP = "192.168.43.250"
UDP_PORT = 4444
MESSAGE = "Hello, World!\n"
MESSAGE = "aaaa"

LARGE_FONT= ("Verdana", 12)            

class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "Sea of BTC client")
        

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        frame = GraphPage(container, self)

        self.frames[GraphPage] = frame

        frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(GraphPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

    
class GraphPage(tk.Frame):

    def sendUDP():
        sock =  socket.socket(socket.AF_INET, # Internet
                socket.SOCK_DGRAM) # UDP
        sock.sendto(MESSAGE.encode(), (UDP_IP, UDP_PORT))
        
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="UDP Page!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Send a UDP message to " + str(UDP_IP) + ":" + str(UDP_PORT),
                            command=lambda: GraphPage.sendUDP() )
        button1.pack()        

app = SeaofBTCapp()
app.mainloop()