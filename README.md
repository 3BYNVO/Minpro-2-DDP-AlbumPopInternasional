# Minpro-2-DDP-AlbumPopInternasional
Nama: Muhammad Ihsan

Kelas: A

NIM:2609116009

## A. Deskripsi Singkat Program

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

## B. Flowchart

Flowchart dibagi menjadi tiga warna: abu-biru (awal & login), merah/salmon (role admin), dan hijau (role user).

<img width="1982" height="1722" alt="Flowchart Nada  drawio" src="https://github.com/user-attachments/assets/9069c990-cffd-4865-a48c-a00819b8a538" />

**1. Awal & Login (abu-biru)**

**START → Menu Awal.** `main()` memanggil `menu_awal()`, yang membersihkan layar lalu menampilkan:
```
Selamat datang di Nada Internasional Anda!
1. Login
2. Keluar
```

**Percabangan "1. Login"**
- **Ya (pilih 1)** → `login()`.
- **Tidak** → "2. Keluar" → **END**, dengan pesan "Terima kasih telah mendengarkan Nada Internasional!".
- Pilihan selain 1 dan 2 menampilkan "Pilihan tidak valid", lalu `menu_awal()` dipanggil lagi. Bagian ini tidak digambar.

**Input Username → Input Password.** Username diubah ke huruf kecil (`.lower()`), dan password disembunyikan dengan `*` (`pwinput`). Datanya dicocokkan dengan dictionary `Akun`:
- `admin` / `admin123` → role admin
- `user` / `user123` → role user

**Login Gagal 1X → 2X → 3X.** Setiap salah, program menampilkan sisa percobaan (2, lalu 1). Setelah 3 kali gagal (`MAKS_PERCOBAAN_LOGIN = 3`), muncul "Login gagal 3 kali. Program ditutup." lalu menuju **END**. Itu garis panjang dari "Login Gagal 3X" ke END.

**Jika berhasil**, program mencetak "Login berhasil! Selamat datang..." dan `login()` mengembalikan `(username, role)`.

**2. Percabangan Role**

```python
menu = MENU_ADMIN if role == "admin" else MENU_USER
```
- **Role: Admin = ya** → alur admin (merah).
- **Tidak** → Role: User (hijau).

**3. Alur Admin (merah)**

Menu admin (1-5) tampil, lalu flowchart mengecek pilihan berurutan dari 1 sampai 5. "Tidak" berarti lanjut ke pilihan berikutnya. Di kode, ini dilakukan lewat dictionary `MENU_ADMIN`.

**1. Lihat Daftar Album**
- `lihat_album()` menampilkan tabel PrettyTable (No, Album, Artis, Rating).
- Lalu **"(Tekan Enter) sebelum kembali ke menu"** (`jeda()`), dan kembali ke Daftar Menu Admin.

**2. Tambah Album** → `tambah_album()`
1. Input nama album
2. Input nama artis
3. Input rating, dicek dengan syarat **0 < rating ≤ 5**
4. **Valid ("ya")** → data masuk ke `Album_Pop` ("Menyimpan Data Baru Album") → "(Tekan Enter)" → kembali ke menu admin
5. **Tidak valid ("tidak")** → "Pemanggilan fungsi ulang", yaitu rating diminta lagi lewat loop `while True` di `input_rating()`

Di kode, mengetik `selesai` menghentikan penambahan, dan beberapa album bisa ditambahkan berturut-turut. Ini tidak digambar.

**3. Ubah Rating Album** → `ubah_rating()`
1. Tabel tampil, lalu input nama album
2. Input rating baru, dicek dengan syarat **0 < rating ≤ 5**
3. **Valid ("ya")** → rating diperbarui → "(Tekan Enter)" → kembali ke menu admin
4. **Tidak valid ("tidak")** → "Pemanggilan fungsi ulang"

Jika nama album tidak ditemukan, kode memanggil `ubah_rating()` lagi (rekursi).

**4. Hapus Album** → `hapus_album()`
1. Input nama album
2. **Ditemukan ("ya")** → "Album berhasil dihapus" → "(Tekan Enter)" → kembali ke menu admin
3. **Tidak ditemukan** → "Pemanggilan fungsi ulang", yaitu `hapus_album()` dipanggil lagi

**5. Log Out** → "Sampai jumpa, [username]! Anda telah logout." → **END**.

**4. Alur User (hijau)**

Menu user (1-3) memakai `MENU_USER`:

**1. Lihat Daftar Album** → tabel tampil → "(Tekan Enter)" → kembali ke Daftar Menu User. User tidak bisa menambah, mengubah, atau menghapus album.

**2. Free Merchandise** → `merchandise_gratis()`
1. Hitung mundur 5 detik (5, 4, 3, 2, 1) dengan `time.sleep(1)`
2. `random.choice()` memilih satu dari T-shirt, Poster, Stiker, Topi, Mug
3. Menampilkan merchandise yang didapat dan info klaim di website resmi
4. "(Tekan Enter)" → kembali ke menu user

**3. Log Out** → **END**.

**5. Ringkasan**

```
START → Menu Awal → 1. Login? ─tidak→ Keluar → END
                        │ ya
              Username & Password
                        │
        Gagal 3x → END     Berhasil → cek role
                                        │
                  Admin (1-5) ←─────────┴─────────→ User (1-3)
                       │                                │
        tiap aksi → Tekan Enter → menu     tiap aksi → Tekan Enter → menu
        Log Out → END                      Log Out → END
```

## C. Penjelasan Program dan Output

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

<img width="457" height="326" alt="validasi tambah album" src="https://github.com/user-attachments/assets/e6d98f7d-51e9-46ee-adf5-ed3c2d99b517" />

### 3. Menu Awal & Login
```python
def menu_awal(): ...
def login(): ...
```
**Penjelasan:** `menu_awal` menampilkan pilihan Login/Keluar. `login` meminta username dan password (disamarkan dengan `pwinput`), mencocokkannya dengan dictionary `Akun`, memberi maksimal 3 percobaan, dan mengembalikan `(username, role)` jika berhasil atau `None` jika gagal.

**Output menu awal:**

<img width="356" height="117" alt="1menu awal" src="https://github.com/user-attachments/assets/0932d596-fa1e-4b10-a7ef-2026d3e10a7b" />

**Output login berhasil:**

<img width="422" height="153" alt="7login admin" src="https://github.com/user-attachments/assets/4a3a0885-cede-47c2-99d4-18953136d573" />

**Output login gagal (3 kali):**

<img width="531" height="296" alt="validasi login" src="https://github.com/user-attachments/assets/ae0f4896-aaa6-4a0f-a94a-e69e21066382" />

### 4. Menu Utama
```python
MENU_ADMIN = {"1": ("Lihat Daftar Album Pop", lihat_album), ... "5": ("Logout", None)}
MENU_USER  = {"1": ("Lihat Daftar Album Pop", lihat_album), "2": ("Merchandise Gratis", merchandise_gratis), "3": ("Logout", None)}
def menu_utama(username, role): ...
```
**Penjelasan:** Menu disimpan sebagai dictionary berisi label dan fungsi. `menu_utama` memilih menu sesuai role, menampilkan pilihan, memvalidasi input, lalu memanggil fungsi terkait. Pilihan dengan fungsi `None` berarti logout.

**Output menu admin:**

<img width="376" height="173" alt="8menu admin" src="https://github.com/user-attachments/assets/14d28d67-fadb-4333-ad78-7003c80c242c" />

**Output menu user:**

<img width="362" height="132" alt="3menu user" src="https://github.com/user-attachments/assets/665e320f-47b5-44f2-8e79-4d21d2bc0d59" />

### 5. Lihat Daftar Album (Admin & User)
```python
def lihat_album():
    tampilkan_daftar()
```
**Penjelasan:** Menampilkan seluruh album dalam bentuk tabel.

**Output:**

<img width="441" height="246" alt="4daftar album" src="https://github.com/user-attachments/assets/01e22e3b-8c15-4854-935a-e64d245e6795" />

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

<img width="436" height="328" alt="10tambah album admin" src="https://github.com/user-attachments/assets/e4b49204-0aaa-4788-afff-2f15f617bee6" />

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

<img width="433" height="328" alt="11rating admin" src="https://github.com/user-attachments/assets/d1d0802e-ced7-4962-a6f7-28925a3d26cb" />

**Output album tidak ditemukan:**

<img width="441" height="322" alt="validasi rating" src="https://github.com/user-attachments/assets/83e68839-20c9-4a94-94d6-43642a0b6f9a" />

### 8. Hapus Album (Admin)
```python
def hapus_album():
    global Album_Pop
    ...
    Album_Pop = [album for album in Album_Pop if album["nama"].lower() != hapus.lower()]
```
**Penjelasan:** Program memeriksa apakah nama album ada. Jika ada, list dibuat ulang tanpa album tersebut (list comprehension). Jika tidak, pengguna diminta mengulang input.

**Output berhasil:**

<img width="442" height="327" alt="12hapus admin" src="https://github.com/user-attachments/assets/597e6a83-1117-4f8e-9498-87dcde4ba8ec" />

**Output album tidak ditemukan:**

<img width="436" height="323" alt="validasi hapus album" src="https://github.com/user-attachments/assets/d2bd3bf8-f471-4406-b0a2-d96cc23d27ad" />

### 9. Merchandise Gratis (User)
```python
def merchandise_gratis():
    for i in range(5, 0, -1):
        print(i)
        time.sleep(1)
    ... random.choice(merchandise_list) ...
```
**Penjelasan:** Menampilkan hitung mundur 5 detik, lalu memilih satu merchandise secara acak (T-shirt, Poster, Stiker, Topi, atau Mug) dengan `random.choice`.

**Output:**

<img width="742" height="222" alt="5doorprize user" src="https://github.com/user-attachments/assets/c52bc83e-9d4e-4365-8b6f-f9f86f607407" />

### 10. Logout & Keluar
**Output logout Admin:**

<img width="536" height="235" alt="13logout admin" src="https://github.com/user-attachments/assets/a6bfa081-93e2-4736-8b52-569de754aacc" />

**Output logout User:**

<img width="547" height="187" alt="6logout user" src="https://github.com/user-attachments/assets/cfd8d1f6-975a-440e-9f2f-0f4d4ac8e306" />

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
