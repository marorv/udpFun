import tkinter as tk
from tkinter import ttk

import socket
import time


TCP_IP = '192.168.0.160'
TCP_PORT = 4445
BUFFER_SIZE = 1024
MESSAGE = 'Hello, World!\n'

LARGE_FONT= ("Verdana", 12)            

class TCPButtonapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "TCP Button App")
        
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

    def sendTCP():
        start = time.time()

        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((TCP_IP, TCP_PORT))
            s.send(MESSAGE.encode())
            rs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            rs.bind(('', 4444))
            rs.listen(1)
            conn, addr = rs.accept()
            print ('Connection address:', addr)
            while 1:
                data = conn.recv(BUFFER_SIZE)
                if not data: break
                print ("received data:", data.decode())
            conn.close()
            rs.close()
            s.close()

        except OSError:
            print('Could not connect.')

        end = time.time()
        print('Wall time elapsed in TCP function was %.3fs' % (end - start))

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="TCP Page!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Send a TCP message to " + str(TCP_IP) + ":" + str(TCP_PORT),
                            command=lambda: GraphPage.sendTCP() )
        button1.pack()   

        button2 = ttk.Button(self, text="Receive a TCP message", command=lambda: GraphPage.sendTCP() )
        button2.pack()       

app = TCPButtonapp()
app.mainloop()
