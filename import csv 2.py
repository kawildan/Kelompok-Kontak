import csv
import tkinter as tk
from tkinter import ttk, messagebox

class KontakkuApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Kontakku")

        # Frame utama
        self.frame_utama = ttk.Frame(root, padding="10")
        self.frame_utama.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Judul aplikasi
        self.label_judul = ttk.Label(self.frame_utama, text="Kontakku", font=('Helvetica', 16, 'bold'))
        self.label_judul.grid(row=0, column=0, columnspan=3, pady=(0, 10), sticky=tk.W)

        # Baris pencarian
        self.label_search = ttk.Label(self.frame_utama, text="Search:")
        self.label_search.grid(row=1, column=0, padx=(0, 5), pady=5, sticky=tk.W)
        self.entry_search = ttk.Entry(self.frame_utama, width=100)
        self.entry_search.grid(row=1, column=1, padx=(0, 10), pady=5, sticky=tk.W)
        self.button_search = ttk.Button(self.frame_utama, text="Cari", command=self.cari_kontak)
        self.button_search.grid(row=1, column=2, pady=5, sticky=tk.W)

        # Listbox untuk menampilkan data kontak
        self.listbox_kontak = tk.Listbox(self.frame_utama, height=15, width=100)
        self.listbox_kontak.grid(row=2, column=0, columnspan=3, pady=(0, 10), sticky=(tk.W, tk.E))

        # Tombol-tombol aksi
        self.button_edit = ttk.Button(self.frame_utama, text="Edit Kontak", command=self.edit_kontak)
        self.button_edit.grid(row=3, column=0, pady=10, padx=5, sticky=tk.W)
        
        self.button_hapus = ttk.Button(self.frame_utama, text="Hapus Kontak", command=self.hapus_kontak)
        self.button_hapus.grid(row=3, column=1, pady=10, padx=5, sticky=tk.W)

        self.button_tambah = ttk.Button(self.frame_utama, text="Tambah Kontak Baru", command=self.tambah_kontak)
        self.button_tambah.grid(row=3, column=2, pady=10, padx=5, sticky=tk.W)


        # Membaca data dari file CSV dan menampilkan dalam listbox
        self.baca_data_dan_tampilkan()
    def baca_data_dan_tampilkan(self):
        try:
            with open("data_kontak.csv", "r") as file_csv:
                pembaca_csv = csv.reader(file_csv)
                next(pembaca_csv)  # Lewati header
                for row in pembaca_csv:
                    self.listbox_kontak.insert(tk.END, f"{row[0]} - {row[1]} - {row[2]} - Favorit: {row[3]}")
        except FileNotFoundError:
            messagebox.showwarning("File Tidak Ditemukan", "File data_kontak.csv tidak ditemukan.")

    def cari_kontak(self):
        # Membersihkan listbox sebelum menampilkan hasil pencarian
        self.listbox_kontak.delete(0, tk.END)

        keyword = self.entry_search.get().lower()
        try:
            with open("data_kontak.csv", "r") as file_csv:
                pembaca_csv = csv.reader(file_csv)
                next(pembaca_csv)  # Lewati header
                for row in pembaca_csv:
                    # Menambahkan ke listbox jika keyword cocok dengan salah satu kolom
                    if keyword in row[0].lower() or keyword in row[1].lower() or keyword in row[2].lower():
                        self.listbox_kontak.insert(tk.END, f"{row[0]} - {row[1]} - {row[2]} - Favorit: {row[3]}")
        except FileNotFoundError:
            messagebox.showwarning("File Tidak Ditemukan", "File data_kontak.csv tidak ditemukan.")

    def tambah_kontak(self):
        # Fungsi ini akan membuat jendela baru untuk memasukkan informasi kontak baru

        # Jendela Toplevel untuk tambah kontak
        jendela_tambah_kontak = tk.Toplevel(self.root)
        jendela_tambah_kontak.title("Tambah Kontak Baru")

        # Frame untuk elemen-elemen dalam jendela
        frame_tambah_kontak = ttk.Frame(jendela_tambah_kontak, padding="10")
        frame_tambah_kontak.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Label dan Entry untuk nama
        label_nama = ttk.Label(frame_tambah_kontak, text="Nama:")
        label_nama.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        entry_nama = ttk.Entry(frame_tambah_kontak, width=30)
        entry_nama.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

        # Label dan Entry untuk nomor HP
        label_nomor_hp = ttk.Label(frame_tambah_kontak, text="Nomor HP:")
        label_nomor_hp.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        entry_nomor_hp = ttk.Entry(frame_tambah_kontak, width=30)
        entry_nomor_hp.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

        # Label dan Entry untuk email
        label_email = ttk.Label(frame_tambah_kontak, text="Email:")
        label_email.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        entry_email = ttk.Entry(frame_tambah_kontak, width=30)
        entry_email.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)

        # Checkbutton untuk favorit
        favorit_var = tk.BooleanVar()
        checkbutton_favorit = ttk.Checkbutton(frame_tambah_kontak, text="Favorit", variable=favorit_var)
        checkbutton_favorit.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W)

        # Tombol untuk menyimpan kontak baru
        button_simpan = ttk.Button(frame_tambah_kontak, text="Simpan", command=lambda: self.simpan_kontak(
            entry_nama.get(), entry_nomor_hp.get(), entry_email.get(), favorit_var.get(), jendela_tambah_kontak))
        button_simpan.grid(row=4, column=1, pady=10, sticky=tk.W)

    def simpan_kontak(self, nama, nomor_hp, email, favorit, jendela_tambah_kontak):
        try:
            # Menulis kontak baru ke dalam file CSV
            with open("data_kontak.csv", mode='a', newline='') as file_csv:
                penulis_csv = csv.writer(file_csv)
                penulis_csv.writerow([nama, nomor_hp, email, favorit])

            # Menampilkan pesan berhasil dan menutup jendela tambah kontak
            messagebox.showinfo("Sukses", "Kontak berhasil ditambahkan.")
            jendela_tambah_kontak.destroy()

            # Membersihkan listbox sebelum menampilkan hasil pencarian
            # self.listbox_kontak.delete(0, tk.END)

            # Membaca data dari file CSV dan menampilkan dalam listbox
            self.baca_data_dan_tampilkan()
        except Exception as e:
            messagebox.showerror("Error", f"Terjadi kesalahan: {str(e)}")
            
    def hapus_kontak(self):
        # Fungsi ini akan menghapus kontak yang dipilih dari listbox dan dari file CSV

        # Mendapatkan indeks terpilih dari listbox
        indeks_terpilih = self.listbox_kontak.curselection()

        if not indeks_terpilih:
            messagebox.showwarning("Pilih Kontak", "Pilih kontak yang ingin dihapus.")
            return

        # Mendapatkan teks kontak yang dipilih dari listbox
        kontak_terpilih = self.listbox_kontak.get(indeks_terpilih[0])

        # Menampilkan konfirmasi pengguna
        konfirmasi = messagebox.askyesno("Konfirmasi Hapus", f"Apakah Anda yakin ingin menghapus kontak:\n{kontak_terpilih}?",
                                         icon='warning')

        if konfirmasi:
            try:
                # Membaca seluruh data dari file CSV
                with open("data_kontak.csv", mode='r') as file_csv:
                    pembaca_csv = csv.reader(file_csv)
                    data_kontak = [row for row in pembaca_csv]

                # Membuka file CSV untuk ditulis
                with open("data_kontak.csv", mode='w', newline='') as file_csv:
                    penulis_csv = csv.writer(file_csv)

                    # Menulis header
                    penulis_csv.writerow(['Nama', 'Nomor HP', 'Email', 'Favorit'])

                    # Menulis kembali data ke file CSV, kecuali yang ingin dihapus
                    for row in data_kontak:
                        if f"{row[0]} - {row[1]} - {row[2]} - Favorit: {row[3]}" != kontak_terpilih:
                            penulis_csv.writerow(row)

                # Membersihkan listbox sebelum menampilkan hasil pencarian
                self.listbox_kontak.delete(0, tk.END)

                # Membaca data dari file CSV dan menampilkan dalam listbox
                self.baca_data_dan_tampilkan()

                messagebox.showinfo("Sukses", "Kontak berhasil dihapus.")
            except Exception as e:
                messagebox.showerror("Error", f"Terjadi kesalahan: {str(e)}")
     
    def edit_kontak(self):
            # Fungsi ini akan membuat jendela baru untuk mengedit informasi kontak yang dipilih

        # Mendapatkan indeks terpilih dari listbox
        indeks_terpilih = self.listbox_kontak.curselection()

        if not indeks_terpilih:
            messagebox.showwarning("Pilih Kontak", "Pilih kontak yang ingin diedit.")
            return

        # Mendapatkan teks kontak yang dipilih dari listbox
        kontak_terpilih = self.listbox_kontak.get(indeks_terpilih[0])

        # Membuka jendela baru untuk mengedit kontak
        jendela_edit_kontak = tk.Toplevel(self.root)
        jendela_edit_kontak.title("Edit Kontak")

        # Frame untuk elemen-elemen dalam jendela
        frame_edit_kontak = ttk.Frame(jendela_edit_kontak, padding="10")
        frame_edit_kontak.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Label dan Entry untuk nama
        label_nama = ttk.Label(frame_edit_kontak, text="Nama:")
        label_nama.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        entry_nama = ttk.Entry(frame_edit_kontak, width=30)
        entry_nama.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

        # Label dan Entry untuk nomor HP
        label_nomor_hp = ttk.Label(frame_edit_kontak, text="Nomor HP:")
        label_nomor_hp.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        entry_nomor_hp = ttk.Entry(frame_edit_kontak, width=30)
        entry_nomor_hp.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

        # Label dan Entry untuk email
        label_email = ttk.Label(frame_edit_kontak, text="Email:")
        label_email.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        entry_email = ttk.Entry(frame_edit_kontak, width=30)
        entry_email.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)

        # Checkbutton untuk favorit
        favorit_var = tk.BooleanVar()
        checkbutton_favorit = ttk.Checkbutton(frame_edit_kontak, text="Favorit", variable=favorit_var)
        checkbutton_favorit.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W)

        # Mendapatkan informasi kontak terpilih dari teks kontak yang dipilih sebelumnya
        info_kontak_terpilih = kontak_terpilih.split(" - ")
        entry_nama.insert(0, info_kontak_terpilih[0])
        entry_nomor_hp.insert(0, info_kontak_terpilih[1])
        entry_email.insert(0, info_kontak_terpilih[2])
        favorit_var.set("Favorit" in info_kontak_terpilih[3])

        # Tombol untuk menyimpan perubahan
        button_simpan = ttk.Button(frame_edit_kontak, text="Simpan", command=lambda: self.simpan_perubahan(
            indeks_terpilih, entry_nama.get(), entry_nomor_hp.get(), entry_email.get(), favorit_var.get(), jendela_edit_kontak))
        button_simpan.grid(row=4, column=1, pady=10, sticky=tk.W)

    def simpan_perubahan(self, indeks_terpilih, nama, nomor_hp, email, favorit, jendela_edit_kontak):
        try:
            # Membaca seluruh data dari file CSV
            with open("data_kontak.csv", mode='r') as file_csv:
                pembaca_csv = csv.reader(file_csv)
                data_kontak = [row for row in pembaca_csv]

            # Mengupdate data kontak yang dipilih
            data_kontak[indeks_terpilih[0]] = [nama, nomor_hp, email, favorit]

            # Menulis kembali data ke file CSV
            with open("data_kontak.csv", mode='w', newline='') as file_csv:
                penulis_csv = csv.writer(file_csv)

                # Menulis header
                penulis_csv.writerow(['Nama', 'Nomor HP', 'Email', 'Favorit'])

                # Menulis kembali data ke file CSV setelah perubahan
                penulis_csv.writerows(data_kontak)

            # Membersihkan listbox sebelum menampilkan hasil pencarian
            self.listbox_kontak.delete(0, tk.END)

            # Membaca data dari file CSV dan menampilkan dalam listbox
            self.baca_data_dan_tampilkan()

            # Menutup jendela edit kontak
            jendela_edit_kontak.destroy()

            messagebox.showinfo("Sukses", "Perubahan berhasil disimpan.")
        except Exception as e:
            messagebox.showerror("Error", f"Terjadi kesalahan: {str(e)}")
                
if __name__ == "__main__":
    root = tk.Tk()
    aplikasi = KontakkuApp(root)
    root.mainloop()
