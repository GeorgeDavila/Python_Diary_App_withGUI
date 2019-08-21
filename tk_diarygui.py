#Modified to create exe that starts up the exe of helloworld.py

from tkinter import *
import os
 
window = Tk()
window.title("Welcome to the Python Diary App!")
window.geometry('800x400') #Determines window size 

lbl = Label(window, text="Hello! Write here:", font=("Arial Bold", 25)) #Write text
lbl.grid(column=0, row=0)   #Places the text into the GUI

txt = Entry(window,width=30, bd =5)    #Creates textbox to take input from user
txt.grid(column=1, row=0)  #Places the input box into the GUI

#Make text suitable to use as input in terminal, ie remove whitespaces
#inputtxt = str( txt.get() ).replace(" ", "_")

#def thanks():    #Defines what clicking the button below does 
#    res = "Thanks for writing, now click Run!" #adds 'welcome to' to user input 
#    lbl.configure(text=res) #Sets output of button to new var res
#Can obviously cut out 'clicked' button if we want, but also a bit more fun to add the extra one 

#write to my diary:
def diarywrite():
    inputtxt = str( txt.get() ).replace(" ", "_") #translates GUI textbox writing (ie normal writing) into something we can read as an argparse input 
    syscommand = "python write2diary.py --input " + inputtxt
    os.system( syscommand ) #inputs "python write2diary.py --input " + txt.get()  into console and runs it

#Open my diary:
def diaryopen():
    os.system( "notepad my_diary.txt" ) #works in terminals that can access notepad

#Create a new diary: 
def createnewdiary():
    new_diary_name1 = str( input("Name the diary: ") ).replace(" ", "_").replace(".txt", "")
    #take out any txt extension out in last line for ease, so in case user adds .txt themselves its no problem (and we don't need an if statement) 
    new_diary_name2 = new_diary_name1 + ".txt" 
    creatediary_syscommand = "notepad" + new_diary_name2
    os.system( creatediary_syscommand ) #works in terminals that can access notepad

#def my_script1(): #template to include your own script
#    my_input = str( txt.get() ).replace(" ", "_") #translates GUI textbox writing (ie normal writing) into something we can read as an argparse input 
#    my_syscommand = "python my_script1.py"  #or "python my_script1.py --input " + my_input
#    os.system( my_syscommand ) 

#Responsive (but currently useless) button within GUI that calls the thanks() function defined above
#btn1 = Button(window, text="Record Text", bg="orange", command=clicked)  #adds orange button that says click me, defines btn variable as this button 
#btn1.grid(column=0, row=1)   #Places the button into the GUI

btn2 = Button(window, text="Write to My Diary", bg="blue", command=diarywrite)  #adds blue button that says "Write to Diary" and appends your text to my_diary.txt using the diarywrite() function defined above 
btn2.grid(column=1, row=1)   #Places the button into the GUI

btn3 = Button(window, text="Open Diary", bg="yellow", command=diaryopen)  #adds yellow button that says "Open Diary" and opens my_diary.txt using the diaryopen() function defined above 
btn3.grid(column=1, row=2)   #Places the button into the GUI

#Button to create a new diary: 
#btn4 = Button(window, text="Create New Diary", bg="green", command=diaryopen)   
#btn4.grid(column=1, row=3)   #Places the button into the GUI

#Template button for your custom script 
#my_btn = Button(window, text="My Script", bg="red", command=my_script1)  #Runs your custom script
#my_btn.grid(column=1, row=4)   #Places the button into the GUI

window.mainloop()