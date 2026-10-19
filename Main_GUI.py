# import tkinter module 
import tkinter
import os  # accessing the os functions
import check_camera
import Capture_Image
import Train_Image
import Recognize

# creating main tkinter window/toplevel 
master = tkinter.Tk() 
master.configure(bg='#0059b3')
master.title("Face Attendence")
def checkCamera():
    check_camera.camer()
    
    master.mainloop() 

def CaptureFaces():
    Capture_Image.takeImages()
    
    master.mainloop() 

def Trainimages():
    Train_Image.TrainImages()
    
    master.mainloop() 

def RecognizeFaces():
    Recognize.recognize_attendence()
    
    master.mainloop() 

def mail():
    os.system("py automail.py")
    
def quit():
    master.destroy()
   

# setting geometry of tk window 
master.geometry("260x300+200+30") 

# button widget 
b1 = tkinter.Button(master, text = "Check Camera", command = checkCamera,bg='green',fg='White') 
b1.place(x = 70, y = 30 + 1*30, width=140, height=25)


# button widget 
b2 = tkinter.Button(master, text = "Capture Faces", command = CaptureFaces,bg='orange',fg='black') 
b2.place(x = 70, y = 30 + 2*30, width=140, height=25)


b3 = tkinter.Button(master, text = "Train Images", command = Trainimages,bg='gray',fg='white') 
b3.place(x = 70, y = 30 + 3*30, width=140, height=25)


b4 = tkinter.Button(master, text = "Recognize & Attendance", command = RecognizeFaces,bg='yellow',fg='black') 
b4.place(x = 70, y = 30 + 4*30, width=140, height=25)


b5 = tkinter.Button(master, text = "Auto Mail", command = mail,bg='red',fg='White') 
b5.place(x = 70, y = 30 + 5*30, width=140, height=25)


b6 = tkinter.Button(master, text = "Quit", command = quit,bg='blue',fg='white') 
b6.place(x = 70, y = 30 + 6*30, width=140, height=25)

master.mainloop() 
