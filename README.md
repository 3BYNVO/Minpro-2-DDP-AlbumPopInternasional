# Minpro-2-DDP-AlbumPopInternasional
Muhammad Ihsan_A_009

A. Deskripsi Singkat Program

**Nada Internasional** adalah program berbahasa Python untuk mengelola daftar album pop internasional beserta rating-nya. Data disimpan dalam list `Album_Pop` (nama album, nama artis, rating).

**Library yang digunakan**

| Library | Fungsi |
|---|---|
| `os` | Membersihkan layar terminal (`cls` / `clear`) |
| `time` | Memberi jeda (`sleep`) pada pesan |
| `random` | Memilih merchandise secara acak |
| `pwinput` | Menyembunyikan password dengan tanda `*` saat diinput oleh user |
| `prettytable` | Menampilkan daftar album dalam bentuk tabel |

---
Program memiliki sistem **login berbasis peran (role)** dengan batas 3 kali percobaan. Password disamarkan memakai **pwinput**.

| Role | Username | Password | Menu yang tersedia |
|------|----------|----------|--------------------|
| Admin|  `admin` |`admin123`| Lihat daftar album, tambah album, ubah rating, hapus album, logout. 
| User |  `user`  |`user123` | Lihat daftar album, merchandise gratis (acak), logout.

Fitur pendukung: validasi input kosong (`input_teks`), validasi rating angka dengan rentang lebih dari 0 sampai 5 (`input_rating`), pembersihan layar otomatis, dan hitung mundur 5 detik pada fitur merchandise teracak.

B. Flowchart

C. Penjelasan Program dan Output

Setiap Bagian Kode Program Album Pop (struktur data, validasi, login, menu, lihat, tambah, ubah rating, hapus, merchandise, logout, main) memiliki penjelasan dan output sebagai berikut.

### 1. Struktur Data & Konfigurasi
```python
Album_Pop = [
    {"nama": "Petal", "artis": "Ariana Grande", "rating": 4.7},
    ...
]
RATING_MIN = 0.0
RATING_MAX = 5.0
MAKS_PERCOBAAN_LOGIN = 3
Akun = {
    "admin": {"password": "admin123", "role": "admin"},
    "user":  {"password": "user123",  "role": "user"},
}
```
**Penjelasan:** `Album_Pop` adalah list berisi dictionary (nama, artis, rating) sebagai data utama. `Akun` menyimpan username, password, dan role. Konstanta rating dan batas login dibuat terpisah agar mudah diubah.

### 2. Fungsi Bantu (Validasi & Tampilan)
```python
def tampilkan_daftar():
    tabel = PrettyTable()
    tabel.field_names = ["No", "Album", "Artis", "Rating"]
    for i, album in enumerate(Album_Pop, start=1):
        tabel.add_row([i, album["nama"], album["artis"], album["rating"]])
    print(tabel)
```
**Penjelasan:** Membuat tabel PrettyTable dari `Album_Pop` dengan nomor urut otomatis.

```python
def input_teks(pesan):   # menolak input kosong
def input_rating(pesan): # menolak non-angka dan rating di luar 0 < rating <= 5
```
**Penjelasan:** `input_teks` mengulang input jika kosong. `input_rating` memakai `try/except ValueError` untuk menangkap input non-angka, lalu mengecek rentang rating.

**Output validasi:**
```
Tambahkan Artis :
Input tidak boleh kosong, silakan ulangi.
Rating Album: abc
Rating harus berupa angka (contoh: 4.5), silakan ulangi.
Rating Album: 7
Rating harus lebih dari 0.0 dan maksimal 5.0, silakan ulangi.
```

### 3. Menu Awal & Login
```python
def menu_awal(): ...
def login(): ...
```
**Penjelasan:** `menu_awal` menampilkan pilihan Login/Keluar. `login` meminta username dan password (disamarkan dengan `pwinput`), mencocokkannya dengan dictionary `Akun`, memberi maksimal 3 percobaan, dan mengembalikan `(username, role)` jika berhasil atau `None` jika gagal.

**Output menu awal:**
```
Selamat datang di Nada Internasional Anda!
1. Login
2. Keluar
Pilih menu anda (1-2): 1
```

**Output login berhasil:**
```
=== AKUN NADA INTERNASIONAL ===
Username : admin
Password : ********

Login berhasil! Selamat datang, admin (role: admin).
```

**Output login gagal (3 kali):**
```
=== AKUN NADA INTERNASIONAL ===
Username : admin
Password : *****
Username atau password salah. Sisa percobaan: 2

Username : admin
Password : ****
Username atau password salah. Sisa percobaan: 1

Username : user
Password : ***
Login gagal 3 kali. Program ditutup.
Terima kasih telah mendengarkan Nada Internasional!
```

### 4. Menu Utama
```python
MENU_ADMIN = {"1": ("Lihat Daftar Album Pop", lihat_album), ... "5": ("Logout", None)}
MENU_USER  = {"1": ("Lihat Daftar Album Pop", lihat_album), "2": ("Merchandise Gratis", merchandise_gratis), "3": ("Logout", None)}
def menu_utama(username, role): ...
```
**Penjelasan:** Menu disimpan sebagai dictionary berisi label dan fungsi. `menu_utama` memilih menu sesuai role, menampilkan pilihan, memvalidasi input, lalu memanggil fungsi terkait. Pilihan dengan fungsi `None` berarti logout.

**Output menu admin:**
```
Nada Internasional | Login sebagai: admin (admin)
1. Lihat Daftar Album Pop
2. Tambahkan Album Favorit
3. Ubah Rating Album
4. Hapus Album
5. Logout
Pilih menu anda: (1-5):
```

**Output menu user:**
```
Nada Internasional | Login sebagai: user (user)
1. Lihat Daftar Album Pop
2. Merchandise Gratis
3. Logout
Pilih menu anda: (1-3):
```

### 5. Lihat Daftar Album (Admin & User)
```python
def lihat_album():
    tampilkan_daftar()
```
**Penjelasan:** Menampilkan seluruh album dalam bentuk tabel.

**Output:**
```
+----+-----------------------+----------------+--------+
| No |         Album         |     Artis      | Rating |
+----+-----------------------+----------------+--------+
| 1  |         Petal         | Ariana Grande  |  4.7   |
| 2  |      YSPSFAGSIL       | Olivia Rodrigo |  4.9   |
| 3  |         brat          |   Charli XCX   |  3.9   |
| 4  | WOR$T GIRL IN AMERICA |   Slayyyter    |  4.0   |
| 5  |          LUX          |    Rosalia     |  4.3   |
+----+-----------------------+----------------+--------+

Tekan Enter untuk kembali ke menu album...
```

### 6. Tambah Album (Admin)
```python
def tambah_album():
    ...
    while True:
        album = input_teks("Tambahkan Album Anda : ")
        if album.lower() == "selesai":
            break
        artis = input_teks("Tambahkan Artis : ")
        rating = input_rating("Rating Album: ")
        Album_Pop.append({"nama": album, "artis": artis, "rating": rating})
```
**Penjelasan:** Admin dapat menambah banyak album sekaligus. Perulangan berhenti saat mengetik `selesai`. Setiap album baru dimasukkan ke `Album_Pop` dan tabel diperbarui.

**Output:**
```
Ketik 'selesai' jika anda merasa cukup dengan albumnya.
Tambahkan Album Anda : Folklore
Tambahkan Artis : Taylor Swift
Rating Album: 4.8
Album 'Folklore' telah ditambahkan ke daftar.
+----+-----------------------+----------------+--------+
| No |         Album         |     Artis      | Rating |
+----+-----------------------+----------------+--------+
| 1  |         Petal         | Ariana Grande  |  4.7   |
| 2  |      YSPSFAGSIL       | Olivia Rodrigo |  4.9   |
| 3  |         brat          |   Charli XCX   |  3.9   |
| 4  | WOR$T GIRL IN AMERICA |   Slayyyter    |  4.0   |
| 5  |          LUX          |    Rosalia     |  4.3   |
| 6  |       Folklore        |  Taylor Swift  |  4.8   |
+----+-----------------------+----------------+--------+
Tambahkan Album Anda : selesai
```

### 7. Ubah Rating Album (Admin)
```python
def ubah_rating():
    ...
    for data in Album_Pop:
        if data["nama"].lower() == ubah.lower():
            data["rating"] = input_rating("Masukkan rating baru: ")
            break
    else:
        print(f"Album '{ubah}' tidak ditemukan dalam daftar, input kembali.")
        return ubah_rating()
```
**Penjelasan:** Album dicari berdasarkan nama (tidak peka huruf besar/kecil). Jika ketemu, rating diganti dengan input baru yang tervalidasi. Jika tidak ditemukan (`for-else`), pengguna diminta mengulang.

**Output berhasil:**
```
Masukkan Album yang ingin diubah ratingnya: BRAT
Masukkan rating baru: 4.5
Rating untuk album 'brat' telah diperbarui menjadi 4.5.
+----+-----------------------+----------------+--------+
| No |         Album         |     Artis      | Rating |
+----+-----------------------+----------------+--------+
| 1  |         Petal         | Ariana Grande  |  4.7   |
| 2  |      YSPSFAGSIL       | Olivia Rodrigo |  4.9   |
| 3  |         brat          |   Charli XCX   |  4.5   |
| 4  | WOR$T GIRL IN AMERICA |   Slayyyter    |  4.0   |
| 5  |          LUX          |    Rosalia     |  4.3   |
+----+-----------------------+----------------+--------+
```

**Output album tidak ditemukan:**
```
Masukkan Album yang ingin diubah ratingnya: abc
Album 'abc' tidak ditemukan dalam daftar, input kembali.
```

### 8. Hapus Album (Admin)
```python
def hapus_album():
    global Album_Pop
    ...
    Album_Pop = [album for album in Album_Pop if album["nama"].lower() != hapus.lower()]
```
**Penjelasan:** Program memeriksa apakah nama album ada. Jika ada, list dibuat ulang tanpa album tersebut (list comprehension). Jika tidak, pengguna diminta mengulang input.

**Output berhasil:**
```
Album yang akan dihapus dari daftar: LUX
Album 'LUX' telah dihapus dari daftar.
+----+-----------------------+----------------+--------+
| No |         Album         |     Artis      | Rating |
+----+-----------------------+----------------+--------+
| 1  |         Petal         | Ariana Grande  |  4.7   |
| 2  |      YSPSFAGSIL       | Olivia Rodrigo |  4.9   |
| 3  |         brat          |   Charli XCX   |  3.9   |
| 4  | WOR$T GIRL IN AMERICA |   Slayyyter    |  4.0   |
+----+-----------------------+----------------+--------+
```

**Output album tidak ditemukan:**
```
Album yang akan dihapus dari daftar: xyz
Album 'xyz' tidak ditemukan dalam daftar, input kembali.
```

### 9. Merchandise Gratis (User)
```python
def merchandise_gratis():
    for i in range(5, 0, -1):
        print(i)
        time.sleep(1)
    ... random.choice(merchandise_list) ...
```
**Penjelasan:** Menampilkan hitung mundur 5 detik, lalu memilih satu merchandise secara acak (T-shirt, Poster, Stiker, Topi, atau Mug) dengan `random.choice`.

**Output (contoh):**
```
Anda akan mendapatkan merchandise acak secara gratis dari Nada Internasional dalam hitungan...
5
4
3
2
1
Selamat! Anda mendapatkan Poster dari Nada Internasional!
Silakan kunjungi website resmi kami untuk klaim merchandise.
```

### 10. Logout & Keluar
**Output logout:**
```
Sampai jumpa, admin! Anda telah logout.
Terima kasih telah mendengarkan Nada Internasional!
```
**Penjelasan:** Saat logout, `menu_utama` selesai (`return`), lalu `main()` mencetak pesan penutup dan program berakhir.

### 11. Fungsi Utama
```python
def main():
    sesi = menu_awal()
    if sesi is None:
        print("Terima kasih telah mendengarkan Nada Internasional!")
        return
    username, role = sesi
    menu_utama(username, role)
    print("Terima kasih telah mendengarkan Nada Internasional!")

main()
```
**Penjelasan:** `main()` memulai dari menu awal. Jika login gagal atau pengguna memilih keluar, program berhenti. Jika berhasil, alur dilanjutkan ke menu sesuai role.
