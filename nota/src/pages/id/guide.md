---
layout: ../../layouts/Doc.astro
title: Cara menggunakan Nota
description: Cara memulai, cara mengirim dokumen, arti setiap kolom spreadsheet, dan apa yang perlu dilakukan dengan catatan.
updated: '25 November 2026'
lang: id
slug: guide
---

Nota membantu Anda mengendalikan pengeluaran bisnis. Anda mengirim struk, invoice, dan screenshot pembayaran di Telegram, lalu Nota membacanya, memeriksa duplikat dan kesalahan, dan mencatatnya ke spreadsheet Google Sheets Anda. Tidak ada yang perlu diisi manual.

Nota tidak melakukan pembukuan dan tidak menggantikan akuntan. Nota memberi kontrol: apa yang sudah dibayar, kepada siapa, untuk apa, dan apakah ada yang dibayar dua kali.

## 1. Cara memulai

1. Buka [@NotaGetBot](https://t.me/NotaGetBot) di Telegram dan tekan "Mulai".
2. Tekan "Hubungkan Google" dan masuk ke akun Anda. Nota akan membuat spreadsheet dan folder dokumen di Google Drive Anda. Membuka spreadsheet: /table, akun Google dan folder: /google.
3. Kirim dokumen pertama atau tambahkan Nota ke grup kerja.

30 dokumen pertama gratis, tanpa kartu pembayaran. Paket dan sisa dokumen: /subscription.

Tanpa Google, Anda hanya menerima laporan atas arsip. Spreadsheet, pemberitahuan, dan laporan terjadwal berfungsi setelah Google terhubung. Yang dikirim tanpa Google disimpan selama 7 hari: hubungkan Google dalam waktu tersebut, dan semuanya akan dicatat ke spreadsheet.

## 2. Cara mengirim dokumen

### Langsung ke bot

Foto struk atau invoice dan kirim ke bot. Anda juga bisa mengirim PDF atau meneruskan pesan berisi dokumen dari chat lain, email, atau aplikasi pesan lain. Ukuran file hingga 50 MB. Semenit kemudian dokumen sudah masuk spreadsheet.

### Di grup kerja

Tambahkan Nota ke chat tempat karyawan sudah biasa mengirim struk. Perintah /group akan menjelaskan caranya. Bagi karyawan tidak ada yang berubah: mereka tidak perlu login atau mendaftar di mana pun.

- Hanya pemilik akun yang bisa menghubungkan Nota ke grup: data pengeluaran bersifat rahasia.
- Saat dihubungkan, Nota menyapa anggota grup satu kali. Setelah itu Nota tidak menulis di grup, hanya menandai setiap dokumen yang sudah dicatat dengan ✍, sehingga semua orang tahu struk itu sudah tercatat.
- Nota hanya mengambil dokumen pembayaran. Foto biasa, skema, dan percakapan dilewati.
- Soal duplikat dan kesalahan, Nota hanya memberi tahu pemilik, lewat chat pribadi. Pesan lain dikirim ke grup hanya dengan izin Anda.
- Setiap grup mendapat Business Unit sendiri, misalnya proyek, vila, atau gerai, sehingga pengeluaran tidak tercampur.
- Jumlah grup yang bisa dihubungkan tergantung paket: Start — hingga 5, Growth — hingga 10, Scale — tanpa batas.

Untuk mitra, Anda bisa membuka akses ke spreadsheet, menambahkan Nota ke grup tempat mereka sudah bergabung, atau meneruskan laporan mingguan dan bulanan kepada mereka.

### Sebagai arsip bulan-bulan sebelumnya

Gunakan perintah /import. Kirim arsip ZIP berisi dokumen atau ekspor chat kerja, hingga 50 MB. Ekspor chat dibuat di Telegram Desktop di komputer. Nota akan membaca semuanya dan menunjukkan apakah sebelumnya ada duplikat.

### Dokumen apa saja yang dipahami Nota

Dokumen pembayaran apa pun yang memuat jumlah, tanggal, dan keterangan pembayaran:

- faktur dan invoice dari pemasok;
- struk dari toko, kafe, SPBU;
- nota dan struk tulisan tangan, termasuk dalam bahasa lokal;
- screenshot transfer bank dan slip transfer;
- screenshot pesanan dari toko online;
- daftar pembayaran gaji.

Foto, PDF, dan arsip ZIP hingga 50 MB bisa dikirim, dalam bahasa apa pun. Nota juga membaca yang sulit dibaca manusia: struk thermal yang pudar, nota yang kusut, tulisan tangan yang tidak jelas.

### Cara memotret

- Foto seluruh dokumen, dengan cahaya yang cukup dan tanpa pantulan.
- Satu foto untuk satu dokumen.
- Kirim dokumen berhalaman banyak sebagai satu PDF.

### Hanya dokumen

Nota hanya mencatat yang dibuktikan dengan dokumen. Input suara dan input manual tidak tersedia: pesan "habis 500 untuk taksi" tanpa struk tidak akan dicatat. Pengeluaran tanpa dokumen tidak bisa diperiksa, jadi juga tidak bisa dikendalikan.

## 3. Yang dilakukan Nota pada setiap dokumen

1. Mengenali jenis, tanggal, jumlah, kepada siapa dibayar, dan untuk apa.
2. Membuat sidik digital file dan membandingkannya dengan dokumen yang sudah dicatat.
3. Menghitung ulang jumlah di dalam dokumen.
4. Mencatat dokumen sebagai baris tersendiri di spreadsheet dan menulis hasil pemeriksaan di kolom Check.
5. Memberi file nama yang jelas, menyimpannya ke folder di Google Drive Anda, dan menaruh tautannya di baris tersebut.

Jika screenshot membuktikan pembayaran invoice yang sudah dicatat, Nota akan bertanya apakah screenshot itu dicatat sebagai baris terpisah atau dilewati. Pilihan ini bisa disimpan, dan bot tidak akan bertanya lagi. Untuk mengubahnya: /proofs.

## 4. Kolom spreadsheet

Spreadsheet memiliki 14 kolom dengan nama dalam bahasa Inggris. Semua kolom bisa Anda ubah. Kolom yang biasanya Anda isi ditandai pensil ✎ di judulnya. Pilihan di daftar dropdown diambil dari lembar References.

### Diisi oleh Nota

**ID · File** — nomor catatan dan nomor dokumen, misalnya "14 · 5867486165572". Ini adalah tautan ke dokumen asli di folder Google Drive Anda. Penomorannya satu urutan untuk chat pribadi dan semua grup. Jika dokumen tidak bernomor, tertulis "no-num".

**Type** — jenis dokumen:

- **Invoice** — invoice dari pemasok;
- **Receipt** — struk;
- **Hand** — dokumen tulisan tangan, misalnya nota;
- **Proof** — bukti pembayaran: slip transfer atau screenshot transfer;
- **Statement** — mutasi rekening atau daftar pembayaran;
- **Document** — dokumen pembayaran lainnya.

**Reported By** — siapa yang mengirim dokumen.

**Date** — tanggal yang tertera di dokumen, bukan tanggal dokumen dikirim.

**Amount** — jumlah dalam mata uang spreadsheet; mata uangnya tertulis di judul kolom, misalnya "Amount, IDR". Dokumen dalam mata uang lain dikonversi Nota sesuai kurs.

**Purpose** — untuk apa dibayar: item dari dokumen, singkat dan berurutan.

**Payee** — kepada siapa dibayar: toko, pemasok, kontraktor, karyawan.

**Check** — hasil pemeriksaan:

- **OK** — dokumen baru dan semuanya cocok. Jumlahnya masuk ke total.
- **Review** — dokumen diterima dan masuk ke total, tetapi sebaiknya diperiksa: misalnya, perhitungannya tidak cocok atau ada koreksi di dokumen.
- **DBL** — duplikat: dokumen ini sudah pernah dicatat. Tidak masuk ke total.

**Match** — penjelasan hasil pemeriksaan. Untuk OK kosong, untuk Review berisi tautan "Comment→" ke penjelasan di kolom Comments, untuk DBL berisi nomor catatan pertama.

### Kolom Anda

Kolom ini tidak wajib diisi, Nota tetap berjalan tanpanya. Sebagian nilainya diisi Nota secara otomatis.

**Status** — status pembayaran:

- **Paid** — sudah dibayar. Nota mengisinya otomatis jika dokumen itu sendiri membuktikan pembayaran: struk toko atau slip transfer. Dalam kasus lain kolom ini kosong.
- **To pay** — invoice perlu dibayar.
- **Rejected** — baris tidak diperlukan, misalnya duplikat atau dokumen yang terkirim karena salah. Baris tetap ada di spreadsheet, tetapi tidak dihitung di semua total, dashboard, dan laporan.

**Category** — kategori pengeluaran, misalnya Materials, Staff, Transport, Rent. Nota mengisi kategori berdasarkan daftar baku, dan set kategorinya tergantung bidang usaha Anda (selengkapnya di bagian 8). Jika kategori lain lebih cocok, pilih dari daftar dropdown langsung di baris tersebut. Daftar kategori: /category. Lembar Monthly spend dan laporan disusun dari kolom ini.

**Business Unit** — pengeluaran ini terkait dengan apa. Nota mengisi nama grup asal dokumen, atau Personal jika dokumen dikirim lewat chat pribadi. Nilainya bisa diubah, dan proyek, vila, atau gerai Anda sendiri bisa ditambahkan di lembar References. Lembar Monthly spend difilter berdasarkan kolom ini.

**Account** — dari mana dibayar: rekening bank, kartu, atau tunai. Daftarnya diatur di lembar References.

**Comments** — untuk catatan bertanda Review, di sini tertulis apa yang perlu diperiksa. Anda juga bisa menambahkan keterangan sendiri di sini.

## 5. Yang perlu dilakukan dengan catatan

- **Review.** Buka dokumen asli lewat tautan di ID · File, baca penjelasan di Comments, dan perbaiki baris jika perlu.
- **DBL.** Cocokkan baris dengan catatan pertama, nomornya ada di Match. Jangan membayar dua kali, dan beri duplikat status Rejected.
- **Invoice perlu dibayar.** Tandai To pay, lalu Paid setelah dibayar.
- **Kategori salah.** Pilih yang benar dari daftar dropdown di kolom Category.
- **Pengeluaran terkait proyek tertentu.** Tulis proyek itu di Business Unit. Nama grup bisa diganti dengan nama Anda sendiri di lembar References.
- **Nota keliru.** Perbaiki barisnya: jumlah, deskripsi, rekanan, kategori, status, atau hasil pemeriksaan. Nota tidak menimpa perubahan Anda, dan total serta dashboard langsung memperhitungkannya.
- **Baris tidak diperlukan.** Beri status Rejected: baris tetap ada di riwayat, tetapi tidak masuk ke total. Anda juga bisa menghapus seluruh baris.

## 6. Dashboard dan lembar

**Dashboard di atas spreadsheet.** Empat indikator yang langsung menunjukkan situasinya: berapa pembayaran yang tidak bermasalah, berapa duplikat, berapa yang menunggu diperiksa, dan berapa yang tanpa kategori. Masing-masing menampilkan jumlah item dan nilai totalnya.

**Monthly spend** — pengeluaran per bulan dalam bentuk arus kas: kategori di baris, bulan di kolom. Di bagian atas ada tiga indikator: pengeluaran bulan ini dan perubahannya dibanding bulan lalu, total kumulatif pengeluaran selama seluruh periode, dan porsi pengeluaran tanpa kategori. Dengan filter, Anda bisa memilih status pembayaran, hasil pemeriksaan, dan Business Unit. Duplikat dikecualikan secara default, dan pos pengeluaran terbesar disorot.

**Insights** — yang perlu diperhatikan: pembayaran yang berkali lipat lebih besar dari biasanya, invoice yang harus dibayar menurut jatuh tempo, duplikat yang masih berstatus "harus dibayar", pengeluaran per karyawan dan per rekanan.

**References** — daftar untuk menu dropdown: kategori, Business Unit, dan akun pembayaran.

## 7. Pemberitahuan dan laporan

- **Pemberitahuan:** /notifications. Pilih apakah bot mengirim kartu untuk setiap catatan atau hanya yang perlu diperhatikan: duplikat dan dokumen yang perlu diperiksa.
- **Terjadwal:** setiap Senin pagi — laporan minggu lalu, tanggal 1 — laporan bulan lalu.
- **Atas permintaan:** /report. Kapan saja Anda bisa meminta laporan untuk minggu atau bulan berjalan, meskipun belum selesai, serta untuk bulan lalu.

Isi laporan: pengeluaran selama periode dan perbandingannya dengan periode sebelumnya, rata-rata pengeluaran per hari dan puncaknya, pengeluaran per hari dan per kategori, berapa duplikat yang tidak dihitung sebagai pengeluaran, dan berapa dokumen yang menunggu diperiksa. Laporan mudah diteruskan ke mitra atau investor.

## 8. Fitur tambahan

**Mata uang apa pun.** Pilih mata uang yang Anda pakai untuk kontrol: /currency. Pembayaran dalam mata uang lain dikonversi Nota sesuai kurs. Mata uang bisa diganti kapan saja, dan semua catatan, termasuk yang lama, akan dihitung ulang.

**Pemeriksaan bulan-bulan sebelumnya.** Kirim arsip dokumen atau ekspor chat kerja lewat /import. Nota akan menunjukkan apakah sebelumnya ada duplikat dan kesalahan.

**Kategori sesuai bisnis Anda.** Daftar baku 15 kategori disusun berdasarkan IFRS dan disesuaikan untuk 10 bidang usaha, serta untuk pengeluaran pribadi dan keluarga. Biasanya pada dokumen ke-15 hingga ke-30, Nota menanyakan bidang usaha Anda dan memakai set kategori yang sesuai:

- konstruksi;
- vila dan hotel;
- kuliner;
- perdagangan;
- pariwisata;
- kecantikan dan olahraga;
- jasa;
- produksi;
- transportasi dan otomotif;
- acara;
- keuangan pribadi dan keluarga;
- bisnis lain yang pengeluarannya dibuktikan dengan struk dan invoice.

**Bahasa.** Dokumen bisa dikirim dalam bahasa apa pun. Bot berbahasa Rusia, Inggris, dan Indonesia; bahasanya dipilih sesuai pengaturan Telegram. Untuk mengganti: /language. Spreadsheet dibuat dalam bahasa Inggris.

**Analitik.** Spreadsheet dirinci per kategori, rekanan, jenis dokumen, dan Business Unit, sehingga mudah dianalisis. Misalnya, Gemini yang ada di Google Sheets bisa menyarankan dan menyusun laporan sendiri: kepada siapa Anda paling banyak membayar dan bagaimana harga berubah, karyawan mana yang mengeluarkan uang dan untuk apa, proyek mana yang biayanya lebih besar, dan apa yang naik paling cepat.

**Kerja bersama.** Spreadsheet bisa dibagikan kepada mitra, pengelola, atau investor, seperti file Google lainnya.

## 9. Situasi umum

- **Perlu memutus koneksi grup:** keluarkan Nota dari grup tersebut.
- **Ada pertanyaan atau ada masalah:** /support atau bot dukungan [@NotaSuppBot](https://t.me/NotaSuppBot). Kami membalas dalam 24 jam.
- **Ingin menghapus data Anda:** /delete_all. Nota akan menghapus catatan dokumen Anda dan sidik digitalnya, memutus koneksi dari Google, dan keluar dari semua grup. Spreadsheet dan folder dokumen di Google Drive Anda tetap ada pada Anda.
- **Ingin mulai dari awal:** /start.

## 10. Perintah bot

Semua perintah ada di menu bot.

**Utama**

- /report — laporan minggu atau bulan
- /table — buka spreadsheet
- /google — akun Google dan folder
- /group — hubungkan grup kerja
- /import — unggah arsip dokumen
- /subscription — paket dan sisa dokumen

**Pengaturan**

- /settings — semua pengaturan
- /currency — mata uang spreadsheet
- /language — bahasa bot
- /notifications — pemberitahuan yang dikirim
- /category — daftar kategori
- /proofs — cara mencatat bukti pembayaran
- /delete_all — hapus data saya

**Bantuan**

- /start — mulai dari awal
- /support — hubungi tim Nota

## 11. Pertanyaan umum

**Apakah ini pembukuan?** Bukan. Nota tidak menghitung pajak dan tidak menyampaikan laporan resmi. Nota membantu pemilik bisnis mengendalikan uang, dan spreadsheet siap pakai dengan dokumen asli akan menghemat waktu akuntan.

**Di mana data saya disimpan?** Spreadsheet dan file ada di Google Drive Anda, dan Anda yang menentukan siapa yang punya akses. Nota hanya melihat spreadsheet dan folder yang dibuatnya. Dokumen hanya ada pada kami selama diproses, dan yang kami simpan hanya sidik digital file untuk menemukan duplikat.

**Apa yang dilihat karyawan di grup?** Satu sapaan saat Nota dihubungkan dan ✍ pada struk yang sudah dicatat. Jumlah, duplikat, dan temuan tidak ditulis Nota di grup.

**Bagaimana jika Nota keliru?** Perbaiki baris di spreadsheet. Perubahan Anda tetap ada, dan total dihitung ulang.

## Siapa yang membuat Nota

Nota dikembangkan oleh tim ahli keuangan Axiom Consulting: lebih dari 15 tahun pengalaman dalam pengendalian pengeluaran dan pemodelan keuangan untuk proyek pengembangan properti, konstruksi, dan IT. Dasar Nota adalah sistem pengendalian pembayaran milik sendiri yang sudah dipakai oleh klien perusahaan. Lebih dari 100.000 dokumen telah diproses melalui sistem ini.

---

Dengan menggunakan Nota, Anda menerima [Ketentuan Layanan](/id/terms) dan [Kebijakan Privasi](/id/privacy). Selengkapnya tentang Nota ada di [halaman utama](/id/).
