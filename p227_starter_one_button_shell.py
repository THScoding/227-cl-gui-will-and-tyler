# p227_starter_one_button_shell.py
# Note this will not run in the code editor and must be downloaded

import subprocess
import tkinter as tk
import tkinter.scrolledtext as tksc
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename

def do_command():
    subprocess.call("ping localhost")
<<<<<<< HEAD
=======
    

>>>>>>> 1b16942 (new code)

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

# set up button to run the do_command function
<<<<<<< HEAD
ping_btn = tk.Button(frame, text="ping", command=do_command)
=======
# Makes the command button pass it's name to a function using lambda
# CODE TO ADD
# Makes the command button pass it's name to a function using lambda
ping_btn = tk.Button(frame, text="Check to see if a URL is up and active", command=lambda:do_command("ping"))
ping_btn.pack()

def do_command():#makes nslookup button 
    subprocess.call("nslookup")

nslookup_btn = tk.Button(frame, text="Find IP adresses or domain names", command=lambda:do_command("nslookup"))

nslookup_btn.pack()


def do_command():#makes tracert button
    subprocess.call("tracert")

tracert_btn = tk.Button(frame, text="map path of data packets", command=lambda:do_command("tracert"))

tracert_btn.pack()


>>>>>>> 1b16942 (new code)
# creates the frame with label for the text box
frame_URL = tk.Frame(root, pady=10,  bg="black") # change frame color
frame_URL.pack()

# decorative label
url_label = tk.Label(frame_URL, text="Enter a URL of interest: ", 
    compound="center",
    font=("comic sans", 14),
    bd=0, 
    relief=tk.FLAT, 
    cursor="heart",
    fg="mediumpurple3",
    bg="black")
url_label.pack(side=tk.LEFT)
url_entry= tk.Entry(frame_URL,  font=("comic sans", 14)) # change font
url_entry.pack(side=tk.LEFT)

frame = tk.Frame(root,  bg="black") # change frame color
frame.pack()
ping_btn.pack()

root.mainloop()
# Adds an output box to GUI.
command_textbox = tksc.ScrolledText(frame, height=10, width=100)
<<<<<<< HEAD
command_textbox.pack()
=======
command_textbox.pack()

>>>>>>> 1b16942 (new code)
