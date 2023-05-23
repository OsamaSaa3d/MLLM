import os
import tkinter
import time
import threading

from PIL import Image, ImageTk
import customtkinter as ctk
from tkinter import END, Text, filedialog, ttk
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import *
from customtkinter import FontManager, CTkFont
from tkinter.font import Font
from LLM_api import reply

"""
root = ctk.CTk()
root.title("mesiGPT")
app_width = 1000
app_height = 740

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width / 1.84) - (app_width / 2)
y = (screen_height / 2.1) - (app_height / 2)

root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
root.resizable(False, False)

frame = ctk.CTkFrame(root)
frame.grid(row=0, column=0, sticky="nsew")

chatScreen = ctk.CTkTextbox(frame, font=('Arial', 16))
chatScreen.pack(fill="both", expand=True, padx=20, pady=20)

insertField = ctk.CTkEntry(root)
insertField.grid(row=1, column=0, sticky="ew", padx=20, pady=(5, 5))

sendImageButton = ctk.CTkButton(root, text="Insert Image", font=('Arial', 16))
sendImageButton.grid(row=1, column=1, sticky="w", padx=10, pady=10)

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
"""

global path
path = None
global bot_response
bot_response = None
global isWaiting
isWaiting = True

def waitForReply(text):
    global isWaiting
    global bot_response
    if path:
        bot_response = reply(text, 1, path)
    else:
        bot_response = reply(text, 0 , '')
    isWaiting = False


def scrollToBottom():
    chatBox.yview(END)
    chatBox.yview(END)

def startText():
    for char in welcomeText:
        welcomeLabel.insert("end-1c", char, "center")
        welcomeLabel.update()
        time.sleep(0.09)
    welcomeLabel.configure(state='disabled')
    time.sleep(0.05)
    startButton.pack(side='top', pady=10, padx=(10, 0))

def startSession():
    welcomeScreen.pack_forget()
    chatBox.pack(fill='both', expand=True, padx=20, pady=(10, 10))
    frame.pack(side='bottom', fill='x', padx=20, pady=(0, 10))
    insertField.pack(side='left', fill='x', expand=True)
    attachImageButton.pack(side='left', padx=(10, 0))


def receiveImage():
    global path

    """
    confirmFrame = ctk.CTkFrame(root, fg_color="transparent")
    imageFrame = tkinter.Frame(confirmFrame, width=200,
                               height=200,
                               bg="#000000",
                               bd=2)
    imageLabel = tkinter.Label(imageFrame)
    imageLabel.configure(image='')
    imageLabel.photo = None"""

    file_path = filedialog.askopenfilename(
        initialdir=os.getcwd(),
        title="Select an image",
        filetypes=[("Image Files", "*.png *.jpg *.jpeg *.ico *.bmp")]
    )
    path = file_path
    if path:
        # attachImageButton.configure(text='Image Attached!')
        # confirmFrame = ctk.CTkFrame(root, fg_color="transparent")
        confirmFrame.pack(side='bottom', fill='x', padx=20, pady=(0, 10))
        img = Image.open(path)
        img = img.resize((200, 200))
        photo = ImageTk.PhotoImage(img)
        """
        imageFrame = tkinter.Frame(confirmFrame, width=img.width,
                                   height=img.height,
                                   bg="#000000",
                                   bd=2)
                                   """
        # imageFrame.pack_propagate(False)
        imageFrame.pack(side='left', fill='both', expand=False)

        # imageLabel = tkinter.Label(imageFrame, image=photo)
        imageLabel.configure(image=photo)
        imageLabel.place(relx=0, rely=0)
        imageLabel.photo = photo

        deselectX.pack(side='left')

        imageLabel.pack(side='left', fill='both', expand=False)

        # deselectX = ctk.CTkButton(imageFrame, text='X', bg_color='red', fg_color='white')
        deselectX.place(x=img.width - deselectX.winfo_reqwidth() - 35, y=2)
        scrollToBottom()
        # deselectX.pack(side='left')


def deselectImage():
    global path
    path = None
    confirmFrame.pack_forget()


def updateChat():
    global path
    global bot_response
    global isWaiting
    chatBox.configure(state='normal')
    # chatBox.configure(padx=10, pady=10)
    text = insertField.get()
    # confirmFrame.pack_forget()
    attachImageButton.configure(state='disabled')
    if text:
        # chatBox.configure(text_color='blue')
        # chatBox.configure(text_color='red')
        # bold_font = Font(weight="bold")
        chatBox.tag_config("User", foreground="#028889")
        chatBox.tag_config("Bot", foreground="#569BFC")
        chatBox.tag_config("Text", foreground="#CFCFCF")

        confirmFrame.pack_forget()

        chatBox.tag_config("BotBubble", background="#1C1C1C",
                           foreground="#F3F3F3",
                           justify="left",
                           spacing1=8,
                           lmargin2=89,
                           rmargin=50,
                           spacing2=2,
                           relief="raised",
                           wrap="word",
                           spacing3=10)

        chatBox.tag_config("UserBubble", background="#A9A9A9",
                           foreground="black",
                           justify="left",
                           spacing1=5,
                           lmargin1=3,
                           lmargin2=52,
                           rmargin=50,
                           spacing2=2,
                           relief="raised",
                           wrap="word",
                           spacing3=5)

        chatBox.tag_config("space",
                           spacing1=10,
                           spacing2=10,
                           spacing3=10)

        chatBox.insert("end-1c", "You: ", "UserBubble")
        chatBox.tag_config("start", background='black', foreground='red')
        chatBox.insert("end-1c", text + '\n', "UserBubble")  # insert \n here.
        chatBox.insert("end-1c", "", "space")
        """
        chatBox.insert("end-1c", text + '\n\n', "Text")
        chatBox.insert("end-1c", "mesiGPT: ", "Bot")
        chatBox.insert("end-1c", "Testing this bot\n\n", "Text")
        """
        if path:
            try:
                img = Image.open(path)
                img = img.resize((500, 500))
                photo = ImageTk.PhotoImage(img)
                imageFrame = tkinter.Frame(chatBox, width=img.width,
                                           height=img.height,
                                           bg="#000000",
                                           bd=2)
                imageFrame.pack_propagate(False)
                # chatBox.insert("end-1c", '\n')
                chatBox.insert(END, '                                                          ',
                               "UserBubble")
                imageFrame.pack(side='top', fill='both', expand=True, anchor='center')
                imageLabel = tkinter.Label(imageFrame, image=photo)
                imageLabel.place(relx=0, rely=0, anchor='center')
                imageLabel.photo = photo
                imageLabel.pack(side='top', fill='both', expand=True, anchor='center')
                chatBox.window_create("end-2c", window=imageFrame)
                chatBox.insert("end-1c", "\n", "UserBubble")
                chatBox.insert(END, '')
            except Exception as e:
                print("Error inserting image", e)
            #path = None
            attachImageButton.configure(text='Attach Image')

        insertField.delete(0, "end")
        insertField.configure(state='disabled')
        chatBox.insert("end-1c", "asuGPT: ", "BotBubble")
        scrollToBottom()
        chatBox.update()
        scrollToBottom()
        oldtext = chatBox.get('1.0','end-1c')
        """
        bot_response = reply(text, 0, '')
        if path:
            bot_response = reply(text, 1, path)
            path = None
        """
        isWaiting = True
        responseThread = threading.Thread(target=waitForReply, args=(text,))
        responseThread.start()
        x = 1
        while isWaiting:
            print("Test")
        # chatBox.insert("end-1c", "Testing this bot\n\n", "Text")
        for char in bot_response:
            chatBox.insert("end-1c", char, "BotBubble")
            chatBox.update()
            time.sleep(0.009)
            scrollToBottom()
        chatBox.insert("end-1c", '\n', "BotBubble")
        insertField.delete(0, "end")
        isWaiting = True
        path = None
        """
    if path:
        try:
            img = Image.open(path)
            img = img.resize((500, 500))
            photo = ImageTk.PhotoImage(img)
            imageFrame = tkinter.Frame(chatBox)
            imageFrame.pack(side='top', fill='both', expand=True)
            imageLabel = tkinter.Label(imageFrame, image=photo)
            imageLabel.photo = photo  # Store the photo as an attribute of the imageLabel widget
            imageLabel.pack(side='top', fill='both', expand=True)
            chatBox.window_create(END, window=imageFrame)
            chatBox.insert(END, '\n\n')
        except Exception as e:
            print("Error inserting image", e)
        path = None
        """
    chatBox.configure(state='disabled')
    insertField.configure(state='normal')
    attachImageButton.configure(state='normal')
    chatBox.update()
    chatBox.after(100, scrollToBottom())


root = ctk.CTk()

root.title("asuGPT")
app_width = 1000
app_height = 740

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width / 1.84) - (app_width / 2)
y = (screen_height / 2.1) - (app_height / 2)

root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
root.resizable(False, False)

welcomeScreen = ctk.CTkFrame(root)
welcomeScreen.pack(fill='both', expand=True)
welcomeLabel = tkinter.Text(welcomeScreen, bg='#1C1C1C', width=welcomeScreen.winfo_width(),
                            height=welcomeScreen.winfo_height() + 2,
                            background='#2B2B2B',
                            borderwidth=0,
                            highlightthickness=0) #, text="Welcome to mesiGPT", font=('Helvetica', 20, 'bold'))
welcomeLabel.tag_config('center', justify='center', foreground='#D6D6D6',
                        font=('Verdana', 30, 'bold'),
                        background='#2B2B2B')
welcomeText = 'Welcome to asuGPT'

welcomeLabel.pack(side='top', fill='x', padx=20, pady=(400, 0))
startButton = ctk.CTkButton(welcomeScreen,
                            text='Start Session',
                            font=('Arial', 12, "bold"))
startButton.configure(command=startSession)
welcomeScreen.grid_rowconfigure(0, weight=1)
welcomeScreen.grid_columnconfigure(0, weight=1)

chatBox = tkinter.Text(root, font=('Arial', 16), bg='#1C1C1C', wrap="word", spacing1=2, spacing2=2)
chatBox.configure(state='disabled')
#chatBox.pack(fill='both', expand=True, padx=20, pady=(10, 10))

frame = ctk.CTkFrame(root, fg_color="transparent")
#frame.pack(side='bottom', fill='x', padx=20, pady=(0, 10))
"""
confirmFrame = ctk.CTkFrame(root, fg_color="transparent")
confirmFrame.pack(side='bottom', fill='x', padx=20, pady=(0, 10))
"""
# separator = ttk.Separator(confirmFrame, orient='vertical')
# separator.pack(side='left', fill='y', padx=10)

insertField = ctk.CTkEntry(frame, font=('Arial', 16))
insertField.bind("<Return>", lambda event: updateChat())
#insertField.pack(side='left', fill='x', expand=True)

attachImageButton = ctk.CTkButton(frame, text='Attach Image', font=('Arial', 12, "bold"))
attachImageButton.configure(command=receiveImage)
#attachImageButton.pack(side='left', padx=(10, 0))

confirmFrame = ctk.CTkFrame(root, fg_color="transparent")
imageFrame = tkinter.Frame(confirmFrame, width=200,
                           height=200,
                           bg="#000000",
                           bd=2)
imageLabel = tkinter.Label(imageFrame, bg='#5B5B5B')
imageLabel.configure(image='')
imageLabel.photo = None

deselectX = ctk.CTkButton(imageLabel, text='X',
                          bg_color='transparent',
                          fg_color='#5B5B5B',
                          height=20,
                          width=30,
                          border_width=0,
                          border_color='grey')
deselectX.configure(command=deselectImage)

root.after(100, startText)
root.mainloop()
