# Name: Dinesha Priyadarshanee Kanatte Kankanamalage 
# Student Number: 10570495

# Imports for the implementations.
import tkinter
import tkinter.messagebox
import json
from os import path

class ProgramGUI:     
    
    def __init__(self):        
        self.main = tkinter.Tk()
        self.main.title("Word Find Log Viewer")
        self.main.geometry('550x150') #Size of the application.                  
               
        # Read the log file at first the program is created and relevant data will be stored accordingly.
        readFile()      

        # Creating 4 different frames to add the labels and buttons.
        self.f1 = tkinter.Frame(self.main)
        self.f2 = tkinter.Frame(self.main)
        self.f3 = tkinter.Frame(self.main)
        self.f4 = tkinter.Frame(self.main)
 
        # Frame 1 - label "Letters" and the label for 9 letter sample to be shown.
        self.labelLetters = tkinter.Label(self.f1, text='Letters:  ', font=2)
        self.labelLetters.pack(side = 'left')
        self.labelLetterValues = tkinter.Label(self.f1)
        self.labelLetterValues.pack(side = 'right')
        
        # Frame 2 - label "Words" and the label for the user given words to be shown.
        self.labelWords = tkinter.Label(self.f2, text='Words:  ', font=2)
        self.labelWords.pack(side = 'left')
        self.labelWordValues = tkinter.Label(self.f2)
        self.labelWordValues.pack(side = 'right')

        # Frame 3 - label "Score" and the label for the score to be shown.
        self.labelScore = tkinter.Label(self.f3, text='Score:  ', font=2)
        self.labelScore.pack(side = 'left')
        self.labelScoreValue = tkinter.Label(self.f3)
        self.labelScoreValue.pack(side = 'right')

        # Filling up data from the log file to the labels created to show the letters, words and score.
        show_log(self)

        # Frame 4 - Button to show the previous record, if available.
        self.prevButton = tkinter.Button(self.f4, text='Previous', font=2, command=self.previous_log)
        self.prevButton.pack(side = 'left')        
        
        # Button to show the next record, if available 
        self.nextButton = tkinter.Button(self.f4, text='Next', font=2, command=self.next_log)
        self.nextButton.pack(side = 'right')

        # Create a label to show the current record number and number of records. Ex. Log 1/3
        self.labelLogRecord = tkinter.Label(self.f4, font=1)
        self.labelLogRecord.pack()
        # Update the current record number according to the list index.
        updateLogRecord(self)

        self.f1.pack()
        self.f2.pack()
        self.f3.pack()
        self.f4.pack(fill=None, expand=True)
        
        tkinter.mainloop()

    # This method is invoked when the button 'Previous' is clicked.
    def previous_log(self):
        global current_log

        # If the current log was accessing the first record, there are no previous record to show and warning is given.
        if current_log-1 < 0:
            tkinter.messagebox.showwarning('End of File', 'No previous log.')
        else:
            increaseIndex(False)#Increase or decrease the index of the log accessing.
            show_log(self)#Letters, words and score are updated accordingly.     
            updateLogRecord(self)#Log record number is updated.

    # This method is invoked when the button 'Next' is clicked.
    def next_log(self):
        global current_log

        # If the current log was accessing the last record, there are no next records to show and warning is given.
        if current_log+1 > len(logs)-1:
            tkinter.messagebox.showwarning('End of File', 'No next log.')
        else:
            increaseIndex(True)#Increase or decrease the index of the log accessing.
            show_log(self)#Letters, words and score are updated accordingly.
            updateLogRecord(self)#Log record number is updated.

global current_log
current_log = 0
logs = [] 

# Read the txt file and load the content to a list 'logs'.
def readFile():
    if path.isfile('log.txt') is True:
        with open('log.txt', 'r') as fp:
            listObj = json.load(fp)
            for obj in listObj:
                logs.append(obj)
            fp.close()

# Update and show the log data by setting the values to the relevant labels.
def show_log(self):
    dic = logs[current_log]
    l = str(' , '.join(dic["letters"]))#remove square brackets
    w = str(' , '.join(dic["words"]))
    self.labelLetterValues.config(text=l, font=2)
    self.labelWordValues.config(text=w, font=2)
    self.labelScoreValue.config(text=dic["score"], font=2)

# Increase or decrease the index of the log list according to the current place accessing.
def increaseIndex(isIncrease):
    global current_log
    if isIncrease:
        current_log += 1
    else:
        current_log -= 1

# Update the current log index to be shown in the label.
def updateLogRecord(self):
    text_val = 'log '+ str(current_log+1) + '/' + str(len(logs))
    self.labelLogRecord.config(text=text_val)
        
gui = ProgramGUI()
