from tkinter import *
import tkinter.font

root = Tk()
root.geometry("300x400")

# membuat file pada komputer kita 
f_data = open("data.txt","a")
notice = Label(root,text="file is created").place(x = 100,y = 370)

# mengganti ukuran font
changefont = tkinter.font.Font(size=20)

# ini judulnya
judl = Label(root,text = "KontakQu",font =changefont)
judl.place(x =80,y = 10)

# ini label frame untuk menampilkan pada aplikasi 
labelfr = LabelFrame(root,text = "result",padx=20,pady=20)
labelfr.place(x = 60,y = 380)

# membuat nama nama pada setiap baris kotak
nama = Label(root,text = "Nama")
Nomer_Telepon = Label(root,text = "Telepon")
email = Label(root,text = "Email")

# membuat kotaknya
e1 = Entry(root,width=40)
e2 = Entry(root,width=40)
e3 = Entry(root,width=40)

# meletakkan  setiap kotak pada aplikasi
nama.place(x = 20, y =50)
Nomer_Telepon.place(x = 20, y =90)
email.place(x = 20, y =130)
e1.place(x = 20, y = 70)
e2.place(x = 20, y = 110)
e3.place(x = 20, y = 150)

# membuat object untuk semua nilai dan menampung semua nilainya
def cetak():
    class orang:
        def _init_(self,nama,nomer_telepon,email):
            self.nama = nama
            self.nomer_telepon = nomer_telepon 
            self.email = email
        def hasil(self):
            # ini adalah nilai yang dapat ditampilkan pada aplikasi
            # lbl = Label(labelfr,text="first name ="+self.nama+"\nlast name ="+self.).grid()

            # ini hanya nilai nya saja
            lbl = ("first name ="+self.nama+"\nlast name ="+self.nama2+"\nage ="+self.age+"\nusername = "+self.username+"\nemail ="+self.email+"\npassword ="+self.password+"\ngender ="+self.gender+"\n\n")
            # mengirim data ke notepad atau txt file
            f_data.write(lbl)
            
    # memanggil fungsi pada object
    ditampilkan = orang(e1.get(), e2.get(), e3.get(), "r".get())
    ditampilkan.hasil()
    # menghapus tulisan ketika tombol submit ditekan
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
   


btn = Button(root,text = "Simpan",command=cetak).place(x = 100,y = 350)


root.mainloop()