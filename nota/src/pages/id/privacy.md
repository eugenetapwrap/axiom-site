---
layout: ../../layouts/Doc.astro
title: Kebijakan Privasi
description: Kebijakan Privasi Nota.
updated: ''
lang: id
slug: privacy
plan:
  - data apa yang diterima Nota dari Telegram, Google dan dokumen Anda;
  - untuk apa data digunakan dan berapa lama disimpan;
  - akses hanya ke spreadsheet dan folder Nota di Google Drive;
  - kepada siapa data dibagikan;
  - cara menghapus data dan menghubungi kami.
---
<!--
DRAF 22.11, terjemahan dari versi Rusia (src/pages/privacy.md). Bukan nasihat hukum: periksa dengan pengacara sebelum dipublikasikan.
Teks perlu diperiksa penutur asli bahasa Indonesia.
"[perlu dikonfirmasi: …]" — pertanyaan terbuka, juga ada di founder/legal-docs-questions.md.
-->

Kebijakan ini menjelaskan data apa yang diterima Nota, untuk apa, di mana disimpan dan cara menghapusnya.

## 1. Pengendali data

Pengendali data adalah Individual Entrepreneur Evgenii Popov (pengusaha perorangan), Georgia, nomor identifikasi 346999215, alamat resmi: Rustaveli Street 140-v, Entrance 1, Floor 6, Kobuleti, Georgia.

Untuk pertanyaan tentang data, tulis ke [perlu dikonfirmasi: email dukungan] atau ke bot [@NotaGetBot](https://t.me/NotaGetBot).

## 2. Data yang kami terima

**Dari Telegram:**

- Telegram ID, nama, username dan bahasa antarmuka Anda;
- ID dan nama grup kerja tempat Anda menambahkan bot;
- nama dan Telegram ID anggota grup yang mengirim dokumen;
- pesan yang Anda kirim langsung ke bot.

Di grup kerja, bot hanya mengambil dokumen pembayaran. Nota tidak menyimpan pesan grup lainnya. [perlu dikonfirmasi dengan developer]

**Dokumen yang Anda kirim:** file struk, invoice, nota pengiriman, bukti transfer dan arsip chat, serta data yang dibaca Nota darinya: tanggal, jumlah, pemasok, detail pembayaran, rincian barang, kategori, proyek. Dokumen bisa berisi data orang lain: nama, nomor telepon, nomor rekening.

**Dari Google**, jika Anda menghubungkan Google:

- alamat email Akun Google Anda;
- token akses agar Nota dapat menulis ke spreadsheet dan folder;
- akses ke spreadsheet dan folder yang dibuat Nota di Google Drive Anda. Nota tidak dapat melihat file lain di Google Drive Anda.

**Data pembayaran:** paket, jumlah, tanggal dan status pembayaran, nomor transaksi di bank atau layanan kripto. Data kartu dimasukkan di halaman Bank of Georgia; kami tidak menerima atau menyimpannya.

**Data teknis:** log server dan kesalahan; alamat IP dan browser saat Anda membuka situs atau halaman pembayaran. [perlu dikonfirmasi: apakah situs memakai analitik atau cookie]

## 3. Untuk apa kami menggunakan data

- Membaca dokumen, mencatat baris di spreadsheet Anda dan menyimpan file asli ke folder.
- Mencari duplikat dan kesalahan jumlah, mengirim laporan dan pemberitahuan.
- Menerima pembayaran, mengelola paket dan menerbitkan invoice.
- Menjawab permintaan dukungan.
- Memperbaiki kesalahan dan melindungi layanan dari penyalahgunaan.

Dasar pemrosesan: pelaksanaan perjanjian dengan Anda ([Ketentuan Layanan](/id/terms)), persetujuan Anda (menghubungkan Google), kepentingan sah kami (keamanan layanan) dan kewajiban hukum (catatan pembayaran).

Kami tidak menjual data Anda, tidak menampilkan iklan dan tidak menggunakan dokumen Anda untuk melatih model AI. [perlu dikonfirmasi: penyedia pengenalan dokumen juga tidak melatih model dengan data ini]

## 4. Data dari Google

Penggunaan dan pengalihan informasi yang diterima Nota dari Google API mematuhi [Google API Services User Data Policy](https://developers.google.com/terms/api-services-user-data-policy), termasuk persyaratan Limited Use. Artinya:

- data dari Google hanya digunakan untuk mengelola spreadsheet dan folder Anda;
- kami tidak mengalihkannya kepada pihak ketiga, kecuali jika diperlukan untuk menjalankan layanan, diwajibkan hukum, atau atas permintaan Anda;
- kami tidak menggunakannya untuk iklan dan tidak menjualnya;
- tidak ada yang membacanya, kecuali jika Anda meminta bantuan, diperlukan untuk keamanan, atau diwajibkan hukum;
- kami tidak menggunakannya untuk mengembangkan, meningkatkan atau melatih model AI atau machine learning umum.

Anda dapat mencabut akses Nota kapan saja: Akun Google → Keamanan → Aplikasi & layanan pihak ketiga. Spreadsheet dan folder tetap menjadi milik Anda.

## 5. Kepada siapa data dibagikan

Hanya kepada penyedia yang diperlukan agar layanan berjalan:

| Siapa | Untuk apa | Di mana |
|---|---|---|
| Telegram | menerima dan mengirim pesan | [perlu dikonfirmasi] |
| Google | spreadsheet dan folder Anda di Google Drive | sesuai pengaturan akun Anda |
| [perlu dikonfirmasi: penyedia pengenalan dokumen] | membaca teks pada dokumen | [perlu dikonfirmasi] |
| [perlu dikonfirmasi: hosting, mis. DigitalOcean] | server dan basis data | [perlu dikonfirmasi: Singapura?] |
| Bank of Georgia | pembayaran kartu | Georgia |
| [perlu dikonfirmasi: layanan kripto] | pembayaran kripto | [perlu dikonfirmasi] |

Kami juga dapat mengungkapkan data kepada otoritas negara jika diwajibkan hukum.

## 6. Transfer data ke luar negeri

Server dan penyedia kami dapat berada di luar negara Anda, termasuk di luar Indonesia. Kami hanya mentransfer data kepada penyedia di atas dan mewajibkan mereka melindunginya setidaknya sesuai standar hukum, termasuk Undang-Undang Nomor 27 Tahun 2022 tentang Pelindungan Data Pribadi (UU PDP). [perlu dikonfirmasi dengan pengacara: persyaratan transfer data ke luar Indonesia]

## 7. Berapa lama data disimpan

- **Tanpa Google terhubung**, file yang Anda kirim dan data yang dibaca darinya disimpan selama 7 hari. Jika Anda menghubungkan Google dalam waktu itu, semuanya dicatat ke spreadsheet. Jika tidak, data dihapus dan Anda tetap memiliki laporan di chat.
- **Dengan Google terhubung**, file asli dan baris disimpan di spreadsheet dan folder di Google Drive Anda hingga Anda menghapusnya. Di servernya sendiri, Nota menyimpan [perlu dikonfirmasi dengan developer: apa saja] selama paket Anda aktif.
- **Setelah paket berakhir**, kami menyimpan data Anda selama 30 hari agar Anda bisa kembali tanpa kehilangan data, lalu menghapusnya.
- **Catatan pembayaran** disimpan selama yang diwajibkan hukum pajak Georgia. [perlu dikonfirmasi: jangka waktu]
- **Cadangan (backup)** dihapus sesuai siklusnya dalam [perlu dikonfirmasi] hari.

## 8. Cara menghapus data

Kirim perintah [perlu dikonfirmasi: nama perintah, mis. /delete] ke bot atau email ke [perlu dikonfirmasi: email dukungan]. Kami akan menghapus data Anda dari server kami dalam 30 hari dan mengonfirmasinya di bot atau melalui email.

Kami tidak menghapus spreadsheet dan folder di Google Drive Anda: itu milik Anda, dan hanya Anda yang dapat menghapusnya.

## 9. Hak Anda

Anda berhak:

- mengetahui data apa yang kami miliki tentang Anda dan mendapatkan salinannya;
- memperbaiki data yang tidak akurat;
- menghapus data;
- menarik persetujuan, misalnya mencabut akses Google;
- menolak atau membatasi pemrosesan;
- mengajukan keluhan kepada otoritas pelindungan data di negara Anda.

Untuk menggunakan hak tersebut, tulis ke [perlu dikonfirmasi: email dukungan]. Kami akan membalas dalam [perlu dikonfirmasi dengan pengacara: tenggat menurut UU PDP dan hukum Georgia].

## 10. Cara kami melindungi data

Data dikirim melalui koneksi terenkripsi. Data setiap pelanggan disimpan terpisah. Hanya orang yang memerlukan akses server untuk pekerjaannya yang memilikinya. [perlu dikonfirmasi dengan developer]

Jika terjadi kebocoran yang menyangkut data Anda, kami akan memberi tahu Anda dan, jika diwajibkan hukum, regulator dalam batas waktu yang ditentukan.

## 11. Anak-anak

Nota adalah layanan untuk bisnis. Kami tidak dengan sengaja memproses data orang berusia di bawah 18 tahun.

## 12. Perubahan kebijakan

Kami akan memberi tahu perubahan penting di bot terlebih dahulu. Tanggal versi saat ini tercantum di bagian atas halaman.
