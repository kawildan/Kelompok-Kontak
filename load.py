import tkinter as tk
from tkinter import messagebox

class ContactApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Aplikasi Kontak")
        
        # Dictionary untuk menyimpan kontak
        self.contacts = {}

        # Label dan Listbox untuk menampilkan kontak
        self.label = tk.Label(master, text="Daftar Kontak")
        self.label.pack()

        self.listbox = tk.Listbox(master)
        self.listbox.pack(padx=10, pady=5)

        # Button untuk menambahkan dan menghapus kontak
        self.add_button = tk.Button(master, text="Tambah Kontak", command=self.add_contact)
        self.add_button.pack(pady=5)

        self.remove_button = tk.Button(master, text="Hapus Kontak", command=self.remove_contact)
        self.remove_button.pack(pady=5)

    def add_contact(self):
        # Menggunakan simpledialog untuk mendapatkan input nama kontak
        contact_name = tk.simpledialog.askstring("Tambah Kontak", "Masukkan Nama Kontak:")
        if contact_name:
            # Menambahkan kontak ke dictionary
            self.contacts[contact_name] = True
            # Menampilkan kontak di Listbox
            self.listbox.insert(tk.END, contact_name)

    def remove_contact(self):
        # Mendapatkan indeks item yang dipilih dari Listbox
        selected_index = self.listbox.curselection()

        # Memastikan bahwa ada item yang dipilih
        if selected_index:
            # Mendapatkan nama kontak dari Listbox
            contact_name = self.listbox.get(selected_index)
            
            # Menampilkan konfirmasi penghapusan
            confirmation = messagebox.askquestion("Hapus Kontak", f"Apakah Anda yakin ingin menghapus kontak {contact_name}?")

            # Jika pengguna mengkonfirmasi penghapusan, lakukan penghapusan
            if confirmation == 'yes':
                # Menghapus kontak dari dictionary
                del self.contacts[contact_name]
                # Menghapus kontak dari Listbox
                self.listbox.delete(selected_index)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactApp(root)
    root.mainloop()
