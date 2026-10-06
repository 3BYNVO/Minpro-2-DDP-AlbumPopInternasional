# Minpro-2-DDP-AlbumPopInternasional
Muhammad Ihsan_A_009

# Nada Internasional — Manajemen Album Pop Internasional

A. Deskripsi Singkat Program

**Nada Internasional** adalah program berbahasa Python untuk mengelola daftar album pop internasional beserta rating-nya. Data disimpan dalam list `Album_Pop` (judul album, nama artis, rating).

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
<img width="1107" height="1192" alt="pop2-1  Alur Utama   Login drawio" src="https://github.com/user-attachments/assets/e96925b3-b5c0-44de-983d-027d68db77b6" />

1. Program dimulai dengan membersihkan layar dan menampilkan **Menu Awal** (1. Login, 2. Keluar), lalu meminta input pilihan. Input kosong ditolak dan diulang oleh `input_teks`.
2. Jika pilihan `"1"`, program memanggil `login()` dengan `percobaan = 1`.
3. Di dalam `login()`, selama percobaan belum melewati 3, program meminta **username** dan **password** (password tampil sebagai `*`).
4. Jika username ada dan password cocok, program mencetak "Login berhasil!", menunggu 1 detik, lalu mengembalikan `(username, role)` dan masuk ke **`menu_utama`**
5. Jika salah, program menghitung `sisa = 3 - percobaan`. Bila `sisa > 0`, pesan "Sisa percobaan" dicetak lalu input diulang. Bila `sisa = 0` (percobaan ke-3 gagal), perulangan berakhir.
6. Setelah perulangan berakhir tanpa login berhasil, program mencetak "Login gagal 3 kali. Program ditutup." dan mengembalikan `None`.
7. Jika pilihan menu awal `"2"`, program langsung menuju penutup. Jika pilihan selain `"1"` atau `"2"`, program mencetak "Pilihan tidak valid." lalu fungsi berakhir sehingga program juga menuju penutup.
8. Semua jalur berakhir di pesan **"Terima kasih telah mendengarkan Nada Internasional!"**, lalu program selesai.

<img width="800" height="953" alt="pop2-2  Menu Utama (Admin   User) drawio" src="https://github.com/user-attachments/assets/2dd38aed-c26a-42dc-a287-50f35252fd19" />

1. `menu_utama(username, role)` memilih kamus menu: `MENU_ADMIN` bila `role == "admin"`, selain itu `MENU_USER`.
2. Layar dibersihkan, lalu header "Login sebagai: ..." dan daftar nomor menu dicetak.
3. Pengguna memasukkan pilihan. Jika nomor tidak ada di menu, pesan "Pilihan tidak valid." muncul dan input diulang.
4. Jika pilihan valid dan fungsinya `None` (menu **Logout**), program mencetak "Sampai jumpa, ..." lalu kembali ke `main()`.
5. Jika bukan Logout, layar dibersihkan, fungsi menu dijalankan (lihat Gambar 3 dan 4), kemudian `jeda()` meminta Enter. Setelah itu alur kembali menampilkan menu.

<img width="1159" height="822" alt="pop2-3  Fungsi Admin (Tambah, Ubah, Hapus) drawio" src="https://github.com/user-attachments/assets/7feb1f4f-8c0e-4ad1-80b1-b024182bd4b9" />

1. **`tambah_album()`** menampilkan daftar dan petunjuk, lalu masuk perulangan: meminta nama album. Jika `"selesai"`, perulangan berhenti. Jika bukan, program meminta artis dan rating (rating divalidasi: angka, lebih dari 0, maksimal 5), menambahkan data ke `Album_Pop`, mencetak konfirmasi, menampilkan daftar terbaru, dan kembali meminta album berikutnya.
2. **`ubah_rating()`** menampilkan daftar, meminta judul album, lalu mencari album dengan judul sama tanpa membedakan huruf besar/kecil. Jika ketemu, program meminta rating baru, memperbarui nilainya, dan menampilkan daftar terbaru. Jika tidak ketemu, program mencetak pesan "tidak ditemukan".
3. **`hapus_album()`** menampilkan daftar, meminta judul album, membentuk ulang `Album_Pop` tanpa album yang judulnya sama persis (membedakan huruf besar/kecil), mencetak pesan "telah dihapus", lalu menampilkan daftar terbaru.

<img width="792" height="662" alt="pop2-4  Fungsi Lihat Album   Merchandise Gratis drawio" src="https://github.com/user-attachments/assets/fa10bf8f-9c77-4d73-932c-e1fc512d9bcc" />

1. **`lihat_album()`** hanya memanggil `tampilkan_daftar()`, yang membuat tabel PrettyTable dari isi `Album_Pop` dan mencetaknya.
2. **`merchandise_gratis()`** mencetak pesan pembuka, menjalankan hitung mundur dari 5 sampai 1 (cetak angka, jeda 1 detik), memilih satu merchandise secara acak dari `["T-shirt", "Poster", "Stiker", "Topi"]`, lalu mencetak hasil dan petunjuk klaim.

C.Dokumentasi Program & Output

### 1 Data Awal dan Konstanta

```python
Album_Pop = [
    ["Petal", "Ariana Grande", 4.7],
    ["YSPSFAGSIL", "Olivia Rodrigo", 4.9],
    ["brat", "Charli XCX", 3.9],
    ["WOR$T GIRL IN AMERICA", "Slayyyter", 4.0],
    ["LUX", "Rosalia", 4.3],
]

RATING_MIN = 0.0
RATING_MAX = 5.0
MAKS_PERCOBAAN_LOGIN = 3

Akun = {
    "admin": {"password": "admin123", "role": "admin"},
    "user": {"password": "user123", "role": "user"},
}
```

**Penjelasan**

- `Album_Pop` adalah *list of list*. Setiap album disimpan dengan format `[nama_album, artis, rating]`.
- `RATING_MIN`, `RATING_MAX`, dan `MAKS_PERCOBAAN_LOGIN` adalah konstanta agar batas nilai mudah diubah di satu tempat.
- `Akun` adalah *dictionary* yang menyimpan data login. Key-nya adalah username, dan value-nya berisi password serta role.

| Username | Password | Role |
|---|---|---|
| `admin` | `admin123` | admin |
| `user` | `user123` | user |

---

### 2 Fungsi Tampilan dan Validasi Input

#### `tampilkan_daftar()`

```python
def tampilkan_daftar():
    tabel = PrettyTable()
    tabel.field_names = ["No", "Album", "Artis", "Rating"]
    for i, (album, artis, rating) in enumerate(Album_Pop, start=1):
        tabel.add_row([i, album, artis, rating])
    print(tabel)
```

**Output**

```
+----+-----------------------+----------------+----------+
| No |         Album         |     Artis      |  Rating  |
+----+-----------------------+----------------+----------+
| 1  |         Petal         | Ariana Grande  |   4.7    |
| 2  |       YSPSFAGSIL      | Olivia Rodrigo |   4.9    |
| 3  |         brat          |   Charli XCX   |   3.9    |
| 4  | WOR$T GIRL IN AMERICA |   Slayyyter    |   4.0    |
| 5  |          LUX          |    Rosalia     |   4.3    |
+----+-----------------------+----------------+----------+
```

**Penjelasan:** Fungsi membuat objek `PrettyTable`, menentukan nama kolom, lalu mengisi baris dengan `enumerate(..., start=1)` supaya penomoran dimulai dari 1. Fungsi ini dipanggil di banyak fitur agar pengguna selalu melihat data terbaru.

#### `input_teks(pesan)`

```python
def input_teks(pesan):
    while True:
        teks = input(pesan).strip()
        if teks == "":
            print("Input tidak boleh kosong, silakan ulangi.")
        else:
            return teks
```

**Output (jika dikosongkan)**

```
Username :
Input tidak boleh kosong, silakan ulangi.
Username :
```

**Penjelasan:** Mengulang input terus-menerus sampai pengguna mengisi teks yang tidak kosong. `strip()` menghapus spasi di awal dan akhir sehingga input yang hanya berisi spasi juga ditolak.

#### `input_rating(pesan)`

```python
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
```

**Output**

```
Rating Album: abc
Rating harus berupa angka (contoh: 4.5), silakan ulangi.
Rating Album: 7
Rating harus lebih dari 0.0 dan maksimal 5.0, silakan ulangi.
Rating Album: 4.5
```

**Penjelasan:** Memakai `try-except` untuk menangkap input non-angka (`ValueError`). Setelah itu rating dicek agar berada pada rentang lebih dari 0 sampai 5. Input hanya diterima jika valid.

#### `bersihkan_layar()` dan `jeda()`

```python
def bersihkan_layar():
    os.system("cls" if os.name == "nt" else "clear")

def jeda():
    input("\nTekan Enter untuk kembali ke menu album...")
```

**Penjelasan:** `bersihkan_layar()` memilih perintah sesuai sistem operasi (`cls` untuk Windows, `clear` untuk Linux/macOS). `jeda()` menahan tampilan supaya hasil fitur sempat dibaca sebelum layar dibersihkan.

---

### 3 Sistem Login

```python
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
```

**Output – login gagal lalu berhasil**

```
=== AKUN NADA INTERNASIONAL ===
Username : admin
Password : ********
Username atau password salah. Sisa percobaan: 2

Username : admin
Password : *********

Login berhasil! Selamat datang, admin (role: admin).
```

**Output – gagal 3 kali**

```
Username atau password salah. Sisa percobaan: 2

Username atau password salah. Sisa percobaan: 1

Login gagal 3 kali. Program ditutup.
```

**Penjelasan**

- Pengguna diberi maksimal 3 kali percobaan (`MAKS_PERCOBAAN_LOGIN`).
- Username diubah ke huruf kecil dengan `.lower()` sehingga `Admin` dan `admin` dianggap sama. Password tetap *case-sensitive*.
- `pwinput` menampilkan `*` sebagai pengganti karakter password.
- `Akun.get(username)` mengembalikan `None` jika username tidak ada, sehingga tidak terjadi error.
- Jika berhasil, fungsi mengembalikan `(username, role)`. Jika gagal 3 kali, fungsi mengembalikan `None` dan program berakhir.

---

### 4 Menu Awal

```python
def menu_awal():
        bersihkan_layar()
        print("Selamat datang di Nada Internasional Anda!")
        print("1. Login")
        print("2. Keluar")
        pilihan = input_teks("Pilih menu anda (1-2): ")
        ...
```

**Output**

```
Selamat datang di Nada Internasional Anda!
1. Login
2. Keluar
Pilih menu anda (1-2): 1
```

**Penjelasan:** Pilihan `1` memanggil `login()`, sedangkan pilihan `2` mengembalikan `None` sehingga program keluar. Jika pilihan tidak valid, program menampilkan "Pilihan tidak valid." lalu fungsi selesai tanpa mengembalikan sesi.

**Output – keluar**

```
Pilih menu anda (1-2): 2
Terima kasih telah mendengarkan Nada Internasional!
```

---

### 5 Menu Utama Berdasarkan Role

```python
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
```

**Output – menu admin**

```
Nada Internasional | Login sebagai: admin (admin)
1. Lihat Daftar Album Pop
2. Tambahkan Album Favorit
3. Ubah Rating Album
4. Hapus Album
5. Logout
Pilih menu anda: (1-5):
```

**Output – menu user**

```
Nada Internasional | Login sebagai: user (user)
1. Lihat Daftar Album Pop
2. Merchandise Gratis
3. Logout
Pilih menu anda: (1-3):
```

**Penjelasan**

- Menu disimpan dalam *dictionary* dengan format `nomor: (label, fungsi)`. Dengan pola ini, menambah fitur cukup menambah satu entri tanpa perlu `if-elif` panjang.
- `menu_utama()` memilih `MENU_ADMIN` atau `MENU_USER` sesuai role, menampilkan menu secara dinamis, lalu memvalidasi pilihan dengan `while pilihan not in menu`.
- Jika fungsi bernilai `None` (menu Logout), program menampilkan pesan perpisahan dan kembali ke `main()`.

**Output – pilihan tidak valid**

```
Pilih menu anda: (1-5): 9
Pilihan tidak valid. Silakan pilih menu yang tersedia.
Pilih menu anda: (1-5):
```

**Output – logout**

```
Sampai jumpa, admin! Anda telah logout.
Terima kasih telah mendengarkan Nada Internasional!
```

---

### 6 Fitur Admin

#### a. Lihat Daftar Album (`lihat_album`)

Memanggil `tampilkan_daftar()`. Outputnya sama seperti tabel pada bagian 3.2. Fitur ini tersedia untuk admin dan user.

#### b. Tambah Album (`tambah_album`)

```python
def tambah_album():
    tampilkan_daftar()
    print("Ketik 'selesai' jika anda merasa cukup dengan albumnya.")
    while True:
        album = input_teks("Tambahkan Album Anda : ")
        if album.lower() == "selesai":
            break
        artis = input_teks("Tambahkan Artis : ")
        rating = input_rating("Rating Album: ")
        Album_Pop.append([album, artis, rating])
        print(f"Album '{album}' telah ditambahkan ke daftar.")
        tampilkan_daftar()
```

**Output**

```
Ketik 'selesai' jika anda merasa cukup dengan albumnya.
Tambahkan Album Anda : GUTS
Tambahkan Artis : Olivia Rodrigo
Rating Album: 4.6
Album 'GUTS' telah ditambahkan ke daftar.
+----+-----------------------+----------------+----------+
| No |         Album         |     Artis      |  Rating  |
+----+-----------------------+----------------+----------+
| 1  |         Petal         | Ariana Grande  |   4.7    |
| 2  |       YSPSFAGSIL      | Olivia Rodrigo |   4.9    |
| 3  |         brat          |   Charli XCX   |   3.9    |
| 4  | WOR$T GIRL IN AMERICA |   Slayyyter    |   4.0    |
| 5  |          LUX          |    Rosalia     |   4.3    |
| 6  |          GUTS         | Olivia Rodrigo |   4.6    |
+----+-----------------------+----------------+----------+
Tambahkan Album Anda : selesai
```

**Penjelasan:** Admin dapat menambahkan banyak album sekaligus dalam satu sesi. Setiap album melewati validasi `input_teks` (tidak boleh kosong) dan `input_rating` (0–5). Data ditambahkan dengan `append()`, lalu tabel diperbarui. Mengetik `selesai` menghentikan perulangan.

#### c. Ubah Rating (`ubah_rating`)

```python
def ubah_rating():
    print("Daftar album yang sudah dirating:")
    tampilkan_daftar()
    ubah = input_teks("Masukkan Album yang ingin diubah ratingnya: ")
    for data in Album_Pop:
        if data[0].lower() == ubah.lower():
            data[2] = input_rating("Masukkan rating baru: ")
            print(f"Rating untuk album '{data[0]}' telah diperbarui menjadi {data[2]}.")
            tampilkan_daftar()
            break
    else:
        print(f"Album '{ubah}' tidak ditemukan dalam daftar.")
```

**Output – berhasil**

```
Masukkan Album yang ingin diubah ratingnya: brat
Masukkan rating baru: 4.2
Rating untuk album 'brat' telah diperbarui menjadi 4.2.
(tabel diperbarui, rating brat menjadi 4.2)
```

**Output – album tidak ditemukan**

```
Masukkan Album yang ingin diubah ratingnya: Folklore
Album 'Folklore' tidak ditemukan dalam daftar.
```

**Penjelasan:** Pencarian album tidak sensitif huruf besar/kecil (`.lower()`). Struktur `for ... else` dipakai agar blok `else` hanya berjalan ketika perulangan selesai tanpa `break`, yaitu saat album tidak ditemukan.

#### d. Hapus Album (`hapus_album`)

```python
def hapus_album():
            global Album_Pop
            tampilkan_daftar()
            hapus = input_teks("Album yang akan dihapus dari daftar: ")
            Album_Pop = [album for album in Album_Pop if album[0] != hapus]
            print(f"Album '{hapus}' telah dihapus dari daftar.")
            tampilkan_daftar()
```

**Output**

```
Album yang akan dihapus dari daftar: LUX
Album 'LUX' telah dihapus dari daftar.
(tabel diperbarui tanpa album LUX)
```

**Penjelasan:** Menggunakan *list comprehension* untuk membuat daftar baru yang hanya berisi album yang namanya berbeda dari input. Kata kunci `global` diperlukan karena `Album_Pop` ditimpa dengan list baru.

---

### 7 Fitur User: Merchandise Gratis

```python
def merchandise_gratis():
    print("Anda akan mendapatkan merchandise acak secara gratis dari Nada Internasional dalam hitungan detik...")
    for i in range(5, 0, -1):
        print(i)
        time.sleep(1)
    merchandise_list = ["T-shirt", "Poster", "Stiker", "Topi"]
    print(f"Selamat! Anda mendapatkan {random.choice(merchandise_list)} dari Nada Internasional!")
    print("Silakan kunjungi website resmi kami untuk klaim merchandise.")
```

**Output**

```
Anda akan mendapatkan merchandise acak secara gratis dari Nada Internasional dalam hitungan detik...
5
4
3
2
1
Selamat! Anda mendapatkan Poster dari Nada Internasional!
Silakan kunjungi website resmi kami untuk klaim merchandise.
```

**Penjelasan:** Menampilkan hitungan mundur 5 sampai 1 dengan jeda 1 detik per angka (`time.sleep(1)`), lalu `random.choice()` memilih satu merchandise secara acak sehingga hasilnya bisa berbeda setiap kali dijalankan.

---

### 8 Alur Utama Program (`main`)

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

**Alur program**

```
Mulai
  └─ menu_awal()
       ├─ Pilih 2 (Keluar)  ──────────────► Selesai
       └─ Pilih 1 (Login)
            ├─ Gagal 3 kali ──────────────► Selesai
            └─ Berhasil → menu_utama(username, role)
                 ├─ role admin → Lihat / Tambah / Ubah Rating / Hapus / Logout
                 └─ role user  → Lihat / Merchandise Gratis / Logout
                                  (Logout) ─► Selesai
```

**Penjelasan:** `main()` memanggil `menu_awal()` terlebih dahulu. Jika hasilnya `None` (keluar, login gagal, atau pilihan tidak valid), program berakhir. Jika berhasil, `username` dan `role` diteruskan ke `menu_utama()`, yang berjalan terus sampai pengguna memilih Logout.

---

### 9 Ringkasan Fitur per Role

| Fitur | Admin | User |
|---|:---:|:---:|
| Login dengan password tersembunyi | ✅ | ✅ |
| Lihat daftar album | ✅ | ✅ |
| Tambah album | ✅ | ❌ |
| Ubah rating album | ✅ | ❌ |
| Hapus album | ✅ | ❌ |
| Merchandise gratis | ❌ | ✅ |
| Logout | ✅ | ✅ |
