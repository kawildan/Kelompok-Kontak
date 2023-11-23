import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

class KontakQu:
    def __init__(self, root):
        self.root = root
        self.root.title("KontakQu")

        # Variabel untuk menyimpan data kontak
        self.nama_var = tk.StringVar()
        self.telepon_var = tk.StringVar()

        # Label dan Entry untuk input nama
        lbl_nama = tk.Label(root, text="Nama:")
        lbl_nama.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        entry_nama = tk.Entry(root, textvariable=self.nama_var)
        entry_nama.grid(row=0, column=1, padx=10, pady=5)

        # Label dan Entry untuk input nomor telepon
        lbl_telepon = tk.Label(root, text="Nomor Telepon:")
        lbl_telepon.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        entry_telepon = tk.Entry(root, textvariable=self.telepon_var)
        entry_telepon.grid(row=1, column=1, padx=10, pady=5)

        # Tombol untuk menyimpan kontak
        btn_simpan = tk.Button(root, text="Simpan", command=self.simpan_kontak)
        btn_simpan.grid(row=2, column=0, pady=10)

        # Tombol untuk menampilkan kontak
        btn_tampilkan = tk.Button(root, text="Tampilkan_Kontak", command=self.tampilkan_kontak)
        btn_tampilkan.grid(row=2, column=1, pady=10)
    
        # Menu Bar
        menubar = tk.Menu(root)
        root.config(menu=menubar)

        # Menu File
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Simpan", command=self.simpan_ke_file)
        file_menu.add_command(label="Buka", command=self.buka_file)

    def simpan_kontak(self):
        nama = self.nama_var.get()
        telepon = self.telepon_var.get()

        # Validasi input
        if not nama or not telepon:
            messagebox.showwarning("Peringatan", "Nama dan nomor telepon harus diisi.")
        else:
            # Menyimpan kontak ke dalam file
            with open("kontak.txt", "a") as file:
                file.write(f"{nama}: {telepon}\n")

            # Menampilkan pesan bahwa kontak telah disimpan
            messagebox.showinfo("Informasi", f"Kontak {nama} dengan nomor {telepon} telah disimpan.")

    def tampilkan_kontak(self):
        try:
            with open("kontak.txt", "r") as file:
                isi_file = file.read()
                if isi_file:
                    # Menampilkan daftar kontak dalam messagebox
                    messagebox.showinfo("Daftar Kontak", isi_file)
                else:
                    messagebox.showinfo("Daftar Kontak", "Tidak ada kontak yang disimpan.")
        except FileNotFoundError:
            messagebox.showinfo("Daftar Kontak", "Tidak ada kontak yang disimpan.")

    def simpan_ke_file(self):
        nama_file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])

        if nama_file:
            with open(nama_file, "w") as file:
                file.write(f"Nama: {self.nama_var.get()}\n")
                file.write(f"Nomor Telepon: {self.telepon_var.get()}\n")

    def buka_file(self):
        nama_file = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])

        if nama_file:
            with open(nama_file, "r") as file:
                # Membaca kontak dari file dan menampilkan dalam messagebox
                isi_file = file.read()
                messagebox.showinfo("Kontak dari File", isi_file)

    def delete_contact(self):
        selected_index = self.listbox.curselection()

        if selected_index:
            self.listbox.delete(selected_index)
            self.contacts.pop(selected_index[0])
            self.clear_entries()
        else:
            messagebox.showwarning("Peringatan", "Pilih kontak yang ingin dihapus!")

    def load_contact(self, event):
        selected_index = self.listbox.curselection()

        if selected_index:
            contact = self.contacts[selected_index[0]]
            name, phone = contact.split(" - ")
            self.entry_name.delete(0, tk.END)
            self.entry_phone.delete(0, tk.END)
            self.entry_name.insert(0, name)
            self.entry_phone.insert(0, phone)

    def clear_entries(self):
        self.entry_name.delete(0, tk.END)
        self.entry_phone.delete(0,tk.END)

import tkinter as tk

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Program dengan Latar Belakang")

        # Mengatur ukuran window
        self.root.geometry("400x300")

        # Menambahkan latar belakang
        self.background_image = tk.PhotoImage(file="background.png")  # Ganti "background.png" dengan nama file gambar latar belakang Anda
        self.background_label = tk.Label(root, image=self.background_image)
        self.background_label.place(relwidth=1, relheight=1)

        # Menambahkan elemen-elemen lainnya
        self.label = tk.Label(root, text="Selamat datang di program!", font=("Helvetica", 16), bg="white")
        self.label.pack(pady=20)

        self.button = tk.Button(root, text="Keluar", command=root.quit)
        self.button.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()



if __name__ == "__main__":
    root = tk.Tk()
    app =KontakQu(root)
    root.mainloop()
