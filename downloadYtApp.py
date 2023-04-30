from pytube import YouTube
from tkinter import *
from tkinter import messagebox as MessageBox
import random
import string, random


def accion():
    num = str(random.randint(0, 100))
    num1 = str(random.randint(1, 15))
    lett = random.choice(string.ascii_letters)
    id = lett + num + "_" + num1
    name = "Video_"+ id +".mp4"                                 
    enlace = videos.get()
    video = YouTube(enlace)
    descarga =  video.streams.get_highest_resolution()
    descarga.download(output_path='C:/Users/danie/Downloads', filename=name)
    MessageBox.showinfo("👍","Video descargado con exito")
  
      
        
def popup():
    MessageBox.showinfo("Sobre mi", "Mi nombre es Daniel Sanchez Estudiante de Ing. En Sistemas de la ULA")
        

root = Tk()
root.config(bd=15)
root.title("Script descargar videos")

imagen = PhotoImage(file="yt.png")
foto = Label(root, image=imagen, bd=0)
foto.grid(row=0, column=0)

menubar = Menu(root)
root.config(menu=menubar)
helpmenu = Menu(menubar, tearoff=0)

menubar.add_cascade(label="Para mas informacion", menu=helpmenu)
helpmenu.add_command(label="informacion del autor", command=popup)
menubar.add_command(label="Salir", command=root.destroy)

intrucciones = Label(root, text="Pega tu enlace de YouTube y descarga el video\n")
intrucciones.grid(row=0, column=1)

videos = Entry(root)
videos.grid(row=1, column=1)
boton = Button(root, text="Descargar 😎🔥", command=accion)
boton.grid(row=2, column=1)



root.mainloop()

