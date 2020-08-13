#   Screen recording systems
#         ::::__::::
#         ::::__::::
# CONTENTS::
#           SCREEN CAPTURER,SCREENSHOT TAKER,CONTROL PANEL
#           MAIN MODULES->TKINTER,PYAUTOGUI,NUMPY,CV2,THREADING
#
import tkinter as ui
import pyautogui
import cv2
import datetime
import numpy
import threading
# SCREEN CAPTURER #
####### variable #######
StartCapture = True
NotPaused = True
########################
def Capture(WIDTH,HEIGHT):
    global StartCapture,NotPaused,count
    screen = (WIDTH,HEIGHT)
    videoCodec = cv2.VideoWriter_fourcc(*"XVID")
    outputName = str(datetime.datetime.today())
    outputName = outputName.replace(":"," ")
    out = cv2.VideoWriter(outputName+".avi",videoCodec,20.0,(screen))
    while StartCapture:
        if NotPaused:
            image = pyautogui.screenshot()
            image = cv2.cvtColor(numpy.array(image),cv2.COLOR_BGR2RGB)
            out.write(image)
    cv2.destroyAllWindows()
    out.release()
def RecordWindow():
    def Stop():
        global StartCapture
        StartCapture = False
        window.destroy()
    def Pause():
        global NotPaused
        if NotPaused:
            NotPaused = False
            State.set("Paused..")
        else:
            NotPaused = True
            State.set("Recording.....")
    window = ui.Tk()
    State = ui.StringVar(window)
    window.title("Recording......")
    window.geometry("400x200")
    isActive = ui.Entry(window,textvariable = State)
    isActive.grid(row = "1" ,column = "1")
    ui.Button(window,text = "Stop",command = Stop).grid(row = "2" ,column = "1")
    ui.Button(window,text = "Pause/resume",command = Pause).grid(row = "2" ,column = "2")
    State.set("Recording....")
    window.mainloop()
# CONTROL PANEL #
def ControlPanel():
    def Record():
        t1 = threading.Thread(target=RecordWindow)
        t2 = threading.Thread(target=Capture,args=(int(viewPortWidth.get()),int(viewPortHeight.get())))
        t1.start()
        t2.start()
        window.destroy()
    window = ui.Tk()
    window.title("piksRecord Control Panel")
    window.geometry("500x300")
    #ui.Label(window,text = "Display Details:"+str(pyautogui.size())).grid(row = "1",column = "0",sticky = "W")
    ui.Label(window,text = "Enter:-").grid(row = "2",column = "0", sticky = "W")
    ui.Label(window,text = "Screen Size:").grid(row = "3" ,column = "0",sticky = "W")
    viewPortWidth = ui.Entry(window)
    viewPortHeight = ui.Entry(window)
    viewPortWidth.grid(row = "4", column = "1")
    ui.Label(window,text = "X").grid(row = "4",column = "2")
    viewPortHeight.grid(row = "4", column = "3")
    ui.Button(window,text = "Record!",command = Record).grid(row = "5",column = "2")
    window.mainloop()
ControlPanel()