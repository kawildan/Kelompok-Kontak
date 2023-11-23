import csv

# Data kontak untuk 10 kontak
kontak1 = ["John Doe", "08123456789", "john.doe@email.com", True]
kontak2 = ["Jane Smith", "08765432100", "jane.smith@email.com", False]
kontak3 = ["Bob Johnson", "08987654321", "bob.johnson@email.com", True]
kontak4 = ["Alice Williams", "08111223344", "alice.williams@email.com", False]
kontak5 = ["Charlie Brown", "08887776666", "charlie.brown@email.com", True]
kontak6 = ["Emma Davis", "08234567890", "emma.davis@email.com", False]
kontak7 = ["David Lee", "08654321098", "david.lee@email.com", True]
kontak8 = ["Grace Miller", "08456789012", "grace.miller@email.com", False]
kontak9 = ["Samuel Wilson", "08901234567", "samuel.wilson@email.com", True]
kontak10 = ["Olivia Taylor", "08012345678", "olivia.taylor@email.com", False]

data_kontak = [kontak1, kontak2, kontak3, kontak4, kontak5, kontak6, kontak7, kontak8, kontak9, kontak10]

# Nama file CSV
nama_file_csv = "data_kontak.csv"

# Menulis data ke file CSV
with open(nama_file_csv, mode='w', newline='') as file_csv:
    penulis_csv = csv.writer(file_csv)

    # Menulis header
    penulis_csv.writerow(['Nama', 'Nomor HP', 'Email', 'Favorit'])

    # Menulis data kontak
    penulis_csv.writerows(data_kontak)

print(f"File CSV '{nama_file_csv}' berhasil dibuat.")
