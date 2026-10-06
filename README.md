# Minpro-2-DDP-AlbumPopInternasional
Muhammad Ihsan_A_009

# Nada Internasional — Manajemen Album Pop Internasional

A. Deskripsi Singkat Program

**Nada Internasional** adalah program berbahasa Python untuk mengelola daftar album pop internasional beserta rating-nya. Data disimpan dalam list `Album_Pop` (judul album, nama artis, rating) dan ditampilkan dalam bentuk tabel menggunakan library **PrettyTable**.

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
> Layar dibersihkan (`cls`/`clear`) di setiap perpindahan menu, sehingga tiap blok menunjukkan satu layar.
<img width="1878" height="801" alt="1" src="https://github.com/user-attachments/assets/33d0acb1-7054-4d71-8d16-c818ec042383" />

`Album_Pop` adalah list berisi list `[album, artis, rating]` sebagai penyimpanan data selama program berjalan (tidak disimpan ke file). `RATING_MIN`, `RATING_MAX`, dan `MAKS_PERCOBAAN_LOGIN` adalah konstanta batas validasi. `Akun` adalah dictionary untuk autentikasi dan penentuan role.
