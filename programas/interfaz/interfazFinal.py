from tkinter import * 
import subprocess
import prueba as pb

window = Tk()
window.title("Detector de Emociones")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

#Label  #cambio texto como diccionario

my_label1 = Label(font=("Times", 24)) #create component
my_label1["text"] = "Bienvenido a nuestro detector de emociones"
my_label1.grid(column=1, row=0)

#otra forma de cambiar texto #cambio atributo del objeot
my_label2 = Label(font=("Times", 24))
my_label2.config(text="Seleccione una opcion: ")
my_label2.grid(column=1, row=1)

#Botones

def button1_clicked():
    command1 = ("ssh", "root@192.168.0.100", "-X", "python3 DETECTOR.py 0.1")
    sshProcess =subprocess.run(command1)
    

def button2_clicked():
    pb.holaMundo("Walter")
    # print("Button 2 clicked")

def button3_clicked():
    print("Button 3 clicked")
    

button1 = Button(text="INICIAR PROGRAMA", command=button1_clicked)
button1.grid(column=0, row=2)

button2 = Button(text="FINALIZAR PROGRAMA", command=button2_clicked)
button2.grid(column=1, row=2)

button3 = Button(text="MOSTRAR DATOS", command=button3_clicked)
button3.grid(column=2, row=2)



window.mainloop()