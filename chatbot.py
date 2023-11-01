from bardapi import Bard
import os 
import time
#import gradio
from tkinter import scrolledtext,Text, Entry
import tkinter as tk
from playsound import playsound
import speech_recognition as sr
from os import system
import whisper
import warnings
import sys
import pyttsx3
from PIL import Image, ImageTk, ImageFilter
from dotenv import load_dotenv

load_dotenv()

bard_api_key = os.getenv("BARD_API_KEY")
os.environ['_BARD_API_KEY']=bard_api_key

def CustomChat(input_text):
    response=Bard().get_answer(input_text)['content']
    return response

def get_response():
    input_data=textinput.get("1.0",tk.END).strip()
    if input_data.lower() in ["bye","goodbye","by","quit"]:
        textoutput.insert(tk.END,"Goodbye! Let me know if you need any help")
        return
    output=CustomChat(input_data)
    global current_response
    current_response=output
    textoutput.insert(tk.END,"\n\n"+"YOU: "+input_data)
    output="\n"+"AMENA: "+output
    textoutput.insert(tk.END,output)
    textoutput.see(tk.END)    
    
def reset():
    textinput.delete("1.0",tk.END)   
    
def speak():
    engine.say(current_response)
    engine.runAndWait()
    
#def toggle_cursor():
#    textinput.tag_remove("cursor", "1.0", "end")
#    if cursor_visible:
#        textinput.tag_add("cursor", f"insert", f"insert+1c")
#    root.after(500, toggle_cursor)

def voiceinput():
    reset()
    os.chdir(r'C:\Users\lazee\OneDrive\Documents\programs\ChatBot')
    playsound('wake_detected.mp3')
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio=r.listen(source)
    try:
        text=r.recognize_google(audio)
        print(text)
        if text.strip()==0:
            engine.say("Speak Again")
            playsound('wake_detected.mp3')
        reset()
        textinput.insert(tk.END,text)  
        get_response()
            
    except sr.UnknownValueError:
        engine.say("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")


root=tk.Tk()
t = Text(width=40, height=10)   
current_response="How may I help you?"
root.title("Amena")
r=sr.Recognizer()
engine=pyttsx3.init()
rate=engine.getProperty('rate')
engine.setProperty('rate',rate-20)
#****************text input*********************
textinput=scrolledtext.ScrolledText(root,width=80,height=5,wrap=tk.WORD,bg="black",fg="white")
textinput.grid(row=0,column=0,padx=10,pady=10,columnspan=3)
#textinput.configure("cursor")
#cursor_visible=True
#toggle_cursor()
#cursor_label = tk.Label(textinput, text="|",fg="white")
#cursor_label.place(x=textinput.winfo_x(), y=textinput.winfo_y())
#enable_blinking_cursor()


#*************output text widget**********
textoutput=scrolledtext.ScrolledText(root,bg="black",width=80,height=20,wrap=tk.WORD,fg="white")
textoutput.grid(row=2,column=0,padx=0,pady=10,columnspan=3)
textoutput.insert("1.0","AMENA: How may I help you?")
#************send button***************
sendbutton=tk.Button(root,text="Enter",command=get_response,width=10,bg="black")
sendbutton.config(font=("Helvetica", 16), fg="white")
sendbutton.grid(row=1,column=0,padx=0,pady=10)
#************speechbutton***************
speechbutton=tk.Button(root,text="Voice Input",width=10,bg="black",command=voiceinput)
speechbutton.config(font=("Helvetica", 16), fg="white")
speechbutton.grid(row=1,column=1,pady=10)
#*************resetbutton***************
resetbutton=tk.Button(root,text="Reset",command=reset,width=10,bg="black")
resetbutton.config(font=("Helvetica", 16), fg="white")
resetbutton.grid(row=1,column=2,pady=10)
#**********speak button*****************
image = Image.open('voice.png')
image = image.resize((50, 30), Image.LANCZOS)
icon = ImageTk.PhotoImage(image)
speakbutton=tk.Button(root,image=icon,command=speak,bg="white")
speakbutton.grid(row=3,column=1,padx=5,pady=10)




root.mainloop()

#demo=gradio.Interface(fn=CustomChat, inputs="text", outputs="text",title="Your Title")
#demo.launch()