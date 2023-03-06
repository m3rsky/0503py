import tkinter as tk

# Tworzenie głównego okna aplikacji
root = tk.Tk()
# Ustawienie tytułu okna
root.title("Moja aplikacja")
# Ustawienie rozmiaru okna aplikacji
root.geometry("1024x768")


# Definicja funkcji do obsługi naciśnięcia przycisku
def button1_click():
    print("Naciśnięto przycisk 1!")
    create_new_window1()

def button2_click():
    print("Naciśnięto przycisk 2!")
    create_new_window2()

def button3_click():
    print("Naciśnięto przycisk 3!")
    create_new_window3()

def button4_click():
    print("Naciśnięto przycisk 4!")
    create_new_window4()

def button5_click():
    print("Naciśnięto przycisk 5!")
    create_new_window5()

def button6_click():
    print("Naciśnięto przycisk 6!")
    create_new_window6()

def button7_click():
    print("Naciśnięto przycisk 7!")
    create_new_window7()

def button8_click():
    print("Naciśnięto przycisk 8!")
    create_new_window8()



def create_new_window1():
    new_window = tk.Toplevel(root)
    new_window.geometry("1024x320")
    new_window.title("Nowe okno aplikacji okno1")

    label = tk.Label(new_window, text="Entry 1", pady=30)
    label.grid(row=1, column=1)
    input_field = tk.Entry(new_window)
    input_field.grid(row=1, column=2)

    label2 = tk.Label(new_window, text="Entry 2")
    label2.grid(row=2, column=2)
    input_field2 = tk.Entry(new_window)
    input_field2.grid(row=3, column=2)

    label3 = tk.Label(new_window, text="Entry 3")
    label3.grid(row=2, column=3)
    input_field3 = tk.Entry(new_window)
    input_field3.grid(row=3, column=3)

    label4 = tk.Label(new_window, text="Entry 4")
    label4.grid(row=2, column=4)
    input_field4 = tk.Entry(new_window)
    input_field4.grid(row=3, column=4)

    label5 = tk.Label(new_window, text="Wynik ent2/ent3:_")
    label5.grid(row=3, column=5)

    label6 = tk.Label(new_window, text="Entry 5")
    label6.grid(row=4, column=2)
    input_field_label6 = tk.Entry(new_window)
    input_field_label6.grid(row=5, column=2)

    label7= tk.Label(new_window, text="Entry 6")
    label7.grid(row=4, column=3)
    input_field_label7 = tk.Entry(new_window)
    input_field_label7.grid(row=5, column=3)

    label7= tk.Label(new_window, text="Entry 6")
    label7.grid(row=4, column=4)
    input_field_label7 = tk.Entry(new_window)
    input_field_label7.grid(row=5, column=4)

    label8= tk.Label(new_window, text="Entry 7")
    label8.grid(row=4, column=5)
    input_field_label8 = tk.Entry(new_window)
    input_field_label8.grid(row=5, column=5)

    label9= tk.Label(new_window, text="Entry 7")
    label9.grid(row=4, column=6)
    input_field_label9 = tk.Entry(new_window)
    input_field_label9.grid(row=5, column=6)

    label10= tk.Label(new_window, text="Entry 8")
    label10.grid(row=4, column=7)
    input_field_label10 = tk.Entry(new_window, width=50)
    input_field_label10.grid(row=5, column=7, padx=15)

def create_new_window2():
    new_window = tk.Toplevel(root)
    new_window.geometry("1024x512")
    new_window.title("Nowe okno aplikacji okno2")

def create_new_window3():
    new_window = tk.Toplevel(root)
    new_window.geometry("1024x512")
    new_window.title("Nowe okno aplikacji okno3")

def create_new_window4():
    new_window = tk.Toplevel(root)
    new_window.geometry("1024x512")
    new_window.title("Nowe okno aplikacji okno4")

def create_new_window5():
    new_window = tk.Toplevel(root)
    new_window.geometry("1024x512")
    new_window.title("Nowe okno aplikacji okno5")

def create_new_window6():
    new_window = tk.Toplevel(root)
    new_window.geometry("1024x512")
    new_window.title("Nowe okno aplikacji okno6")

def create_new_window7():
    new_window = tk.Toplevel(root)
    new_window.geometry("1024x512")
    new_window.title("Nowe okno aplikacji okno7")

def create_new_window8():
    new_window = tk.Toplevel(root)
    new_window.geometry("1024x512")
    new_window.title("Nowe okno aplikacji okno8")

# Tworzenie przycisków
button1 = tk.Button(root, text="Przycisk 1", width=25, height=5, command=button1_click)
button2 = tk.Button(root, text="Przycisk 2", width=25, height=5, command=button2_click)
button3 = tk.Button(root, text="Przycisk 3", width=25, height=5, command=button3_click)
button4 = tk.Button(root, text="Przycisk 4", width=25, height=5, command=button4_click)
button5 = tk.Button(root, text="Przycisk 5", width=25, height=5, command=button5_click)
button6 = tk.Button(root, text="Przycisk 6", width=25, height=5, command=button6_click)
button7 = tk.Button(root, text="Przycisk 7", width=25, height=5, command=button7_click)
button8 = tk.Button(root, text="Przycisk 8", width=25, height=5, command=button8_click)

# Ustawienie pozycji przycisków w siatce
button1.grid(row=1, column=0, padx=35, pady=20)
button2.grid(row=1, column=1, padx=35, pady=20)
button3.grid(row=1, column=2, padx=35, pady=20)
button4.grid(row=1, column=3, padx=35, pady=20)
button5.grid(row=2, column=0, padx=35, pady=20)
button6.grid(row=2, column=1, padx=35, pady=20)
button7.grid(row=2, column=2, padx=35, pady=20)
button8.grid(row=2, column=3, padx=35, pady=20)










# Uruchomienie głównej pętli programu
root.mainloop()