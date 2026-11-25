---
layout: ../../layouts/Doc.astro
title: Cara menggunakan Nota
description: Cara memulai, cara mengirim dokumen, dan apa yang perlu dilakukan dengan spreadsheet yang diisi oleh Nota.
updated: '25 November 2026'
lang: id
slug: guide
---

Nota mencatat struk, invoice, dan nota ke spreadsheet Google Sheets Anda, memeriksa jumlah, menemukan duplikat, dan mengirim laporan. Di bawah ini ada semua yang Anda perlukan untuk memulai dan memahami spreadsheet.

## 1. Memulai

1. Buka [@NotaGetBot](https://t.me/NotaGetBot) di Telegram dan tekan "Mulai".
2. Tekan "Hubungkan Google" dan masuk ke akun Google Anda.

Nota akan membuat spreadsheet dan folder untuk dokumen di Google Drive Anda. Tautan ke spreadsheet selalu tersedia lewat perintah /table.

- 30 dokumen pertama gratis. Paket dan pembayaran: /subscription.
- Nota memilih bahasa sesuai pengaturan Telegram: bahasa Rusia, Inggris, atau Indonesia. Untuk menggantinya: /language.

## 2. Cara mengirim dokumen

**Langsung ke bot.** Ambil foto struk atau invoice, lalu kirim ke bot. Anda juga bisa mengirim PDF atau meneruskan pesan berisi dokumen dari chat lain.

**Di grup kerja.** Tambahkan Nota ke chat tempat karyawan sudah biasa mengirim struk. Hanya pemilik akun yang bisa melakukannya.

- Nota akan menyapa satu kali di grup, lalu hanya memberi tanda ✍ pada setiap dokumen yang sudah dicatat.
- Karyawan tidak perlu melakukan apa pun.
- Soal duplikat dan kesalahan, Nota hanya memberi tahu Anda, lewat chat pribadi.
- Jumlah grup yang bisa dihubungkan tergantung paket: Start — hingga 5, Growth — hingga 10, Scale — tanpa batas.

**Sebagai arsip bulan-bulan sebelumnya.** Gunakan perintah /history. Kirim arsip ZIP berisi dokumen atau ekspor chat kerja. Ekspor chat dibuat di Telegram Desktop di komputer.

Agar Nota membaca dokumen dengan akurat:

- foto seluruh dokumen, dengan cahaya yang baik dan tanpa pantulan;
- satu foto untuk satu dokumen;
- kirim dokumen yang terdiri dari beberapa halaman sebagai satu PDF.

Nota hanya mencatat dokumen: struk, invoice, nota, dan screenshot pembayaran. Pesan "habis 500 untuk taksi" tanpa dokumen tidak akan dicatat.

## 3. Apa yang muncul di spreadsheet

Setiap dokumen menjadi baris tersendiri. Dokumen asli terbuka lewat tautan di kolom **ID · File**.

Di kolom **Check**, Nota menuliskan hasil pemeriksaan:

- **OK** — semuanya cocok, tidak ada yang perlu dilakukan.
- **Review** — dokumen sudah dicatat dan masuk ke total, tetapi sebaiknya diperiksa. Nota menuliskan apa yang perlu diperiksa di kolom Comments; di kolom Match ada tautan "Comment→" ke penjelasan tersebut. Buka dokumen asli dan, jika perlu, perbaiki barisnya.
- **DBL** — duplikat: dokumen ini sudah pernah dicatat, nomor catatan pertamanya ada di kolom Match. Bandingkan kedua catatan, jangan membayar dua kali, dan beri duplikat itu status Rejected.

Semua data di spreadsheet bisa Anda perbaiki, dan baris bisa dihapus seluruhnya. Nota tidak menimpa perubahan Anda, dan total langsung dihitung ulang. Jika sebuah baris memang tidak diperlukan, lebih mudah memberinya status Rejected: baris itu tetap ada di riwayat, tetapi tidak ikut dijumlahkan.

Total ada di dasbor di bagian atas spreadsheet. Pengeluaran per bulan dan per kategori ada di lembar Monthly spend, sedangkan hal yang perlu diperhatikan ada di lembar Insights.

## 4. Kolom yang bisa Anda isi sendiri

Kolom ini ditandai dengan pensil ✎ di judulnya. Anda tidak wajib mengisinya: Nota tetap bekerja tanpa kolom ini. Tetapi dengan kolom ini, Anda lebih mudah memantau pembayaran dan melihat pengeluaran per proyek.

**Status** — status pembayaran:

- **Paid** — sudah dibayar. Jika dokumen itu sendiri membuktikan pembayaran, misalnya struk toko, Nota mengisi Paid sendiri.
- **To pay** — invoice perlu dibayar.
- **Rejected** — baris tidak diperlukan: duplikat atau dokumen yang terkirim tidak sengaja. Baris tetap ada di spreadsheet, tetapi tidak ikut dijumlahkan.

**Category** — kategori pengeluaran. Di antara dokumen ke-15 dan ke-30, Nota akan menanyakan bidang usaha Anda, lalu selanjutnya mengisi kategori sendiri. Jika kategori lain lebih sesuai, pilih dari daftar dropdown langsung di baris tersebut.

**Business Unit** — pengeluaran ini terkait dengan apa. Nota mengisi nama grup asal dokumen, atau Personal jika dokumen dikirim langsung ke bot. Di lembar References, nama ini bisa diganti dengan nama proyek, vila, atau outlet Anda.

**Account** — sumber pembayaran: rekening, kartu, atau tunai. Pilihan Anda sendiri bisa dimasukkan lebih dulu di lembar References, dan pilihan itu akan muncul di daftar dropdown.

**Comments** — di sini Nota menuliskan apa yang perlu diperiksa pada baris bertanda Review. Anda juga bisa menambahkan catatan sendiri di sini.

## 5. Pemberitahuan dan laporan

- **Pemberitahuan:** /notifications. Pilih apakah Nota mengirim kartu untuk setiap catatan, atau hanya yang penting: duplikat dan dokumen yang perlu diperiksa.
- **Terjadwal:** setiap Senin pagi — laporan minggu lalu, tanggal 1 — laporan bulan lalu. Laporan ini mudah diteruskan ke mitra.
- **Atas permintaan:** kapan saja, lewat menu, Anda bisa meminta laporan untuk minggu atau bulan berjalan, meskipun belum berakhir, serta untuk bulan lalu.

## 6. Situasi yang sering terjadi

- **Perlu mata uang lain:** /currency. Semua catatan, termasuk yang lama, akan dihitung ulang.
- **Perlu menonaktifkan grup:** keluarkan Nota dari grup tersebut.
- **Ada pertanyaan atau ada yang tidak beres:** /support atau bot dukungan [@NotaSuppBot](https://t.me/NotaSuppBot). Kami membalas dalam 24 jam.
- **Ingin menghapus data Anda:** /delete. Nota akan menghapus catatan tentang dokumen Anda, memutus koneksi dari Google, dan keluar dari semua grup. Spreadsheet dan folder dokumen di Google Drive Anda tetap di tangan Anda.

Informasi lebih lanjut tentang Nota ada di [halaman utama](/id/).
