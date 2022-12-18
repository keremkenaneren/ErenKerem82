
from tkinter import *

# Pencere oluşturma
pencere = Tk()
canvas = Canvas(pencere, width=570, height=600)
canvas.pack()

# Bir metin giriş yeri oluşturma
entry = Entry(pencere, font="Verdana 20 bold",
              justify="right",  bg="Lightblue")
entry.place(relx=0.2, rely=0.1, relheight=0.1,
            relwidth=0.6)  # işlemi buraya yazıcaz


# İşimize yarıycak olan fonksiyonlar..

def sıfırla():
    entry.delete(0, 'end')


def tıklanan_buton(sayi):
    entry.insert(END, sayi)


def toplama():
    global sayi1
    global islem
    islem = "Toplama"
    sayi1 = int(entry.get())
    entry.delete(0, END)


def cikarma():
    global sayi1
    global islem
    islem = "Cikarma"
    sayi1 = int(entry.get())
    entry.delete(0, END)


def carpma():
    global sayi1
    global islem
    islem = "Carpma"
    sayi1 = int(entry.get())
    entry.delete(0, END)


def bol():
    global sayi1
    global islem
    islem = "Bol"
    sayi1 = int(entry.get())
    entry.delete(0, END)


def esittir():
    sayi2 = int(entry.get())
    entry.delete(0, END)
    if islem == "Toplama":
        entry.insert(0, sayi1+sayi2)
    if islem == "Cikarma":
        entry.insert(0, sayi1-sayi2)
    if islem == "Carpma":
        entry.insert(0, sayi1*sayi2)
    if islem == "Bol":
        entry.insert(0, sayi1/sayi2)


def temizle():
    entry.delete(0, END)


"""""
Hesap Makinesi için lazım olucak fonksiyonları oluşturduk .
Bu fonksiyonları , oluşturacağımız butonlarda kullanıcaz..

Sıra Butonlarımızda :
örnek(1,2,..,0,+,-,*,/,<-) 

"""
# buton oluşturma
buton1 = Button(pencere)
buton1.config(text="1", bg="black", fg="white", command=lambda: tıklanan_buton(
    1), borderwidth=10, font="verdana 12 bold")  # buton özellikleri
buton1.place(relx=0.1, rely=0.3, relheight=0.1,
             relwidth=0.10)  # butona ait koordinatlar

buton2 = Button(pencere)
buton2.config(text="2", bg="black", fg="white",
              command=lambda: tıklanan_buton(2), borderwidth=10, font="verdana 12 bold")
buton2.place(relx=0.2, rely=0.3, relheight=0.1, relwidth=0.10)

buton3 = Button(pencere)
buton3.config(text="3", bg="black", fg="white",
              command=lambda: tıklanan_buton(3), borderwidth=10, font="verdana 12 bold")
buton3.place(relx=0.3, rely=0.3, relheight=0.1, relwidth=0.10)

buton4 = Button(pencere)
buton4.config(text="4", bg="black", fg="white",
              command=lambda: tıklanan_buton(4), borderwidth=10, font="verdana 12 bold")
buton4.place(relx=0.1, rely=0.4, relheight=0.1, relwidth=0.10)

buton5 = Button(pencere)
buton5.config(text="5", bg="black", fg="white",
              command=lambda: tıklanan_buton(5), borderwidth=10, font="verdana 12 bold")
buton5.place(relx=0.2, rely=0.4, relheight=0.1, relwidth=0.10)

buton6 = Button(pencere)
buton6.config(text="6", bg="black", fg="white",
              command=lambda: tıklanan_buton(6), borderwidth=10, font="verdana 12 bold")
buton6.place(relx=0.3, rely=0.4, relheight=0.1, relwidth=0.10)

buton7 = Button(pencere)
buton7.config(text="7", bg="black", fg="white",
              command=lambda: tıklanan_buton(7), borderwidth=10, font="verdana 12 bold")
buton7.place(relx=0.1, rely=0.5, relheight=0.1, relwidth=0.10)

buton8 = Button(pencere)
buton8.config(text="8", bg="black", fg="white",
              command=lambda: tıklanan_buton(8), borderwidth=10, font="verdana 12 bold")
buton8.place(relx=0.2, rely=0.5, relheight=0.1, relwidth=0.10)

buton9 = Button(pencere)
buton9.config(text="9", bg="black", fg="white",
              command=lambda: tıklanan_buton(9), borderwidth=10, font="verdana 12 bold")
buton9.place(relx=0.3, rely=0.5, relheight=0.1, relwidth=0.10)

butonparantez1 = Button(pencere)
butonparantez1.config(text="(", bg="black", fg="white",
                      command=lambda: tıklanan_buton("("), borderwidth=10, font="verdana 12 bold")
butonparantez1.place(relx=0.1, rely=0.6, relheight=0.1, relwidth=0.10)


buton0 = Button(pencere)
buton0.config(text="0", bg="red", fg="black",
              command=lambda: tıklanan_buton(0), borderwidth=10, font="verdana 12 bold")
buton0.place(relx=0.2, rely=0.6, relheight=0.1, relwidth=0.10)


butonparantez2 = Button(pencere)
butonparantez2.config(text=")", bg="black", fg="white",
                      command=lambda: tıklanan_buton(")"), borderwidth=10, font="verdana 12 bold")
butonparantez2.place(relx=0.3, rely=0.6, relheight=0.1, relwidth=0.10)

# şimdi sıra operatör butonlarda
buton_arti = Button(pencere)
buton_arti.config(text="+", bg="Red", fg="Black",
                  command=toplama, borderwidth=10, font="verdana 14 bold")
buton_arti.place(relx=0.5, rely=0.3, relheight=0.1, relwidth=0.10)

buton_eksi = Button(pencere)
buton_eksi.config(text="-", bg="Red", fg="Black",
                  command=cikarma, borderwidth=10, font="verdana 14 bold")
buton_eksi.place(relx=0.5, rely=0.4, relheight=0.1, relwidth=0.10)


buton_carp = Button(pencere)
buton_carp.config(text="*", bg="Red", fg="Black",
                  command=carpma, borderwidth=10, font="verdana 14 bold")
buton_carp.place(relx=0.5, rely=0.5, relheight=0.1, relwidth=0.10)

buton_bol = Button(pencere)
buton_bol.config(text="/", bg="Red", fg="Black",
                 command=bol, borderwidth=10, font="verdana 14 bold")
buton_bol.place(relx=0.5, rely=0.6, relheight=0.1, relwidth=0.10)

# silme işlemi için buton
buton_sil = Button(pencere)
buton_sil.config(text="<-", bg="Green", fg="Black",
                 command=lambda x="<-": sıfırla(), borderwidth=10, font="verdana 23 bold")
buton_sil.place(relx=0.6, rely=0.3, relheight=0.2, relwidth=0.20)

# işlemi çözmek için butonumuz
buton_coz = Button(pencere)
buton_coz.config(text="=", bg="Green", fg="Black",
                 command=esittir, borderwidth=10, font="verdana 23 bold")
buton_coz.place(relx=0.6, rely=0.5, relheight=0.2, relwidth=0.20)

mainloop()
