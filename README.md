# Minpro-2-DDP-AlbumPopInternasional
Muhammad Ihsan_A_009

# Nada Internasional — Manajemen Album Pop Internasional

1. Deskripsi Singkat Program

**Nada Internasional** adalah program berbahasa Python untuk mengelola daftar album pop internasional beserta rating-nya. Data disimpan dalam list `Album_Pop` (judul album, nama artis, rating) dan ditampilkan dalam bentuk tabel menggunakan library **PrettyTable**.

Program memiliki sistem **login berbasis peran (role)** dengan batas 3 kali percobaan. Password disamarkan memakai **pwinput**.

| Role | Username | Password | Menu yang tersedia |
|------|----------|----------|--------------------|
| Admin|  `admin` |`admin123`| Lihat daftar album, tambah album, ubah rating, hapus album, logout. 
| User |  `user`  |`user123` | Lihat daftar album, merchandise gratis (acak), logout.

Fitur pendukung: validasi input kosong (`input_teks`), validasi rating angka dengan rentang lebih dari 0 sampai 5 (`input_rating`), pembersihan layar otomatis, dan hitung mundur 5 detik pada fitur merchandise.

2. Gambar flowchart serta penjelasan alurnya

