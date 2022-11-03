from tkinter import * 

window = Tk()
window.title("Detector de Emociones")
window.minsize(width=500, height=300)

#Label  #cambio texto como diccionario

my_label1 = Label(font=("Times", 24)) #create component
my_label1.pack() #how it show
my_label1["text"] = "Bienvenido a nuestro detector de emociones"

#otra forma de cambiar texto #cambio atributo del objeot
my_label2 = Label(font=("Times", 24))
my_label2.pack()
my_label2.config(text="Seleccione una opcion: ")

#Botones

def button1_clicked():
    print("Button 1 clicked")

def button2_clicked():
    print("Button 2 clicked")

def button3_clicked():
    print("Button 3 clicked")
    

button1 = Button(text="INICIAR PROGRAMA", command=button1_clicked)
button1.pack()

button2 = Button(text="FINALIZAR PROGRAMA", command=button2_clicked)
button2.pack()

button3 = Button(text="MOSTRAR DATOS", command=button3_clicked)
button3.pack()

#Entry

# input = Entry()
# input.pack()


window.mainloop()