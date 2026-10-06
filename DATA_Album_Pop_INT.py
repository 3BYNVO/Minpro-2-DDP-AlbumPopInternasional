import os
import time
import random
from pwinput import pwinput
from prettytable import PrettyTable

Album_Pop = [
    {"nama": "Petal", "artis": "Ariana Grande", "rating": 4.7},
    {"nama": "YSPSFAGSIL", "artis": "Olivia Rodrigo", "rating": 4.9},
    {"nama": "brat", "artis": "Charli XCX", "rating": 3.9},
    {"nama": "WOR$T GIRL IN AMERICA", "artis": "Slayyyter", "rating": 4.0},
    {"nama": "LUX", "artis": "Rosalia", "rating": 4.3},
]

RATING_MIN = 0.0
RATING_MAX = 5.0
MAKS_PERCOBAAN_LOGIN = 3

def tampilkan_daftar():
    tabel = PrettyTable()
    tabel.field_names = ["No", "Album", "Artis", "Rating"]
    for i, album in enumerate(Album_Pop, start=1):
        tabel.add_row([i, album["nama"], album["artis"], album["rating"]])
    print(tabel)

def input_teks(pesan):
    while True:
        teks = input(pesan).strip()
        if teks == "":
            print("Input tidak boleh kosong, silakan ulangi.")
        else:
            return teks

def input_rating(pesan):
    while True:
        try:
            rating = float(input(pesan))
        except ValueError:
            print("Rating harus berupa angka (contoh: 4.5), silakan ulangi.")
            continue
        if rating <= RATING_MIN or rating > RATING_MAX:
            print(f"Rating harus lebih dari {RATING_MIN} dan maksimal {RATING_MAX}, silakan ulangi.")
        else:
            return rating

Akun = {
    "admin": {"password": "admin123", "role": "admin"},
    "user": {"password": "user123", "role": "user"},
}

def login():
    print("=== AKUN NADA INTERNASIONAL ===")
    for percobaan in range(1, MAKS_PERCOBAAN_LOGIN + 1):
        username = input_teks("Username : ").lower()
        password = pwinput("Password : ", mask="*")
        data = Akun.get(username)
        if data and data["password"] == password:
            print(f"\nLogin berhasil! Selamat datang, {username} (role: {data['role']}).")
            time.sleep(1)
            return username, data["role"]
        sisa = MAKS_PERCOBAAN_LOGIN - percobaan
        if sisa > 0:
            print(f"Username atau password salah. Sisa percobaan: {sisa}\n")
    print("Login gagal 3 kali. Program ditutup.")
    return None

def bersihkan_layar():
    os.system("cls" if os.name == "nt" else "clear")

def jeda():
    input("\nTekan Enter untuk kembali ke menu album...")

def menu_awal():
    bersihkan_layar()
    print("Selamat datang di Nada Internasional Anda!")
    print("1. Login")
    print("2. Keluar")
    pilihan = input_teks("Pilih menu anda (1-2): ")
    if pilihan == "1":
        bersihkan_layar()
        hasil = login()
        if hasil:
            return hasil
        return None
    elif pilihan == "2":
        return None
    else:
        print("Pilihan tidak valid.")
        time.sleep(1)
        return menu_awal()

def lihat_album():
    tampilkan_daftar()

def tambah_album():
    tampilkan_daftar()
    print("Ketik 'selesai' jika anda merasa cukup dengan albumnya.")
    while True:
        album = input_teks("Tambahkan Album Anda : ")
        if album.lower() == "selesai":
            break
        artis = input_teks("Tambahkan Artis : ")
        rating = input_rating("Rating Album: ")
        Album_Pop.append({"nama": album, "artis": artis, "rating": rating})
        print(f"Album '{album}' telah ditambahkan ke daftar.")
        tampilkan_daftar()

def ubah_rating():
    print("Daftar album yang sudah dirating:")
    tampilkan_daftar()
    ubah = input_teks("Masukkan Album yang ingin diubah ratingnya: ")
    for data in Album_Pop:
        if data["nama"].lower() == ubah.lower():
            data["rating"] = input_rating("Masukkan rating baru: ")
            print(f"Rating untuk album '{data['nama']}' telah diperbarui menjadi {data['rating']}.")
            tampilkan_daftar()
            break
    else:
        print(f"Album '{ubah}' tidak ditemukan dalam daftar, input kembali.")
        time.sleep(1)
        return ubah_rating()

def hapus_album():
    global Album_Pop
    tampilkan_daftar()
    hapus = input_teks("Album yang akan dihapus dari daftar: ")
    if hapus.lower() in [album["nama"].lower() for album in Album_Pop]:
        Album_Pop = [album for album in Album_Pop if album["nama"].lower() != hapus.lower()]
        print(f"Album '{hapus}' telah dihapus dari daftar.")
        tampilkan_daftar()
    else:
        print(f"Album '{hapus}' tidak ditemukan dalam daftar, input kembali.")
        time.sleep(1)
        return hapus_album()

def merchandise_gratis():
    print("Anda akan mendapatkan merchandise acak secara gratis dari Nada Internasional dalam hitungan...")
    for i in range(5, 0, -1):
        print(i)
        time.sleep(1)
    merchandise_list = [
        "T-shirt",
        "Poster",
        "Stiker",
        "Topi",
        "Mug",
    ]
    print(f"Selamat! Anda mendapatkan {random.choice(merchandise_list)} dari Nada Internasional!")
    print("Silakan kunjungi website resmi kami untuk klaim merchandise.")

MENU_ADMIN = {
    "1": ("Lihat Daftar Album Pop", lihat_album),
    "2": ("Tambahkan Album Favorit", tambah_album),
    "3": ("Ubah Rating Album", ubah_rating),
    "4": ("Hapus Album", hapus_album),
    "5": ("Logout", None),
}

MENU_USER = {
    "1": ("Lihat Daftar Album Pop", lihat_album),
    "2": ("Merchandise Gratis", merchandise_gratis),
    "3": ("Logout", None),
}

def menu_utama(username, role):
    menu = MENU_ADMIN if role == "admin" else MENU_USER
    while True:
        bersihkan_layar()
        print(f"Nada Internasional | Login sebagai: {username} ({role})")
        for nomor, (label, _) in menu.items():
            print(f"{nomor}. {label}")
        pilihan = input_teks(f"Pilih menu anda: (1-{len(menu)}): ")

        while pilihan not in menu:
            print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")
            pilihan = input_teks(f"Pilih menu anda: (1-{len(menu)}): ")

        label, fungsi = menu[pilihan]
        if fungsi is None:
            print(f"Sampai jumpa, {username}! Anda telah logout.")
            return
        bersihkan_layar()
        fungsi()
        jeda()

def main():
    sesi = menu_awal()
    if sesi is None:
        print("Terima kasih telah mendengarkan Nada Internasional!")
        return
    username, role = sesi
    menu_utama(username, role)
    print("Terima kasih telah mendengarkan Nada Internasional!")

main()