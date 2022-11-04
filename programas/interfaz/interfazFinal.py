from tkinter import * 
import subprocess
import prueba as pb
import os

pathResultado = "/home/wsser09/Desktop/TEC/Taller Embebidos/proyecto_2git/Proyecto2_Grupo_2/programas/resultado"


#Interfaz
window = Tk()
window.title("Detector de Emociones")
window.minsize(width=200, height=200)
window.config(padx=100, pady=100)

#Label  #cambio texto como diccionario

my_label1 = Label(font=("Times", 24)) #create component
my_label1["text"] = "Bienvenido a nuestro detector de emociones"
my_label1.grid(column=1, row=0)

#otra forma de cambiar texto #cambio atributo del objeot
my_label2 = Label(font=("Times", 24))
my_label2.config(text="Seleccione una opcion: ")
my_label2.grid(column=1, row=1)

#Botones

def button1_clicked():  #crea conexion e inicia programa
    command1 = ("ssh", "root@192.168.0.100", "-X", "python3 DETECTOR.py 0.1")
    sshProcess =subprocess.run(command1)
    
archivoTexto = ""
def button2_clicked():  #copia archivos mediante scp
    p = subprocess.Popen("scp -r root@192.168.0.100:/home/root/resultado /home/wsser09/Desktop/TEC/'Taller Embebidos'/proyecto_2git/Proyecto2_Grupo_2/programas", shell=True)
    sts= p.wait()
    def listbox_used(event):
        print(listbox.get(listbox.curselection()))
        global archivoTexto
        archivoTexto = listbox.get(listbox.curselection())
        print(type(archivoTexto))

#crea una listbox con los nuevos datos 

    listbox = Listbox(width=30)
    contenido = os.listdir(pathResultado)
    for item in contenido:
        listbox.insert(contenido.index(item), item)
    listbox.bind("<<ListboxSelect>>",
    listbox_used)
    listbox.grid(column=1, row=3)
    
def button3_clicked():  #procesa los datos y los muestra

    print("Button 3 clicked")



# listbox = Listbox(width=30)
# contenido = os.listdir(pathResultado)
# for item in contenido:
#     listbox.insert(contenido.index(item), item)
# listbox.grid(column=2, row=3)

print(archivoTexto)     #compruebo que obtengo el texto

button1 = Button(text="INICIAR PROGRAMA", command=button1_clicked)
button1.grid(column=0, row=2)

button2 = Button(text="OBTENER DATOS", command=button2_clicked)
button2.grid(column=1, row=2)

button3 = Button(text="MOSTRAR DATOS", command=button3_clicked)
button3.grid(column=2, row=2)



window.mainloop()