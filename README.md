# Pengubah Judul Video YouTube Otomatis

Script ini secara otomatis mengubah judul dari video YouTube tertentu berdasarkan jumlah hari sejak tanggal mulai yang telah ditentukan. Script ini menggunakan YouTube Data API untuk melakukan perubahan yang diperlukan.

## Fitur

- **Pembaruan Judul Otomatis**: Script ini menghitung jumlah hari sejak tanggal mulai tertentu dan mengubah judul video YouTube yang diberikan untuk mencerminkan hal tersebut.
- **Otentikasi OAuth 2.0**: Script ini mengautentikasi dengan aman menggunakan OAuth 2.0 untuk mengakses YouTube API.
- **Manajemen Token**: Script ini menyimpan dan menggunakan kembali token autentikasi, sehingga Anda tidak perlu melakukan autentikasi manual setiap kali menjalankan script.

## Prasyarat

- Python 3.x
- Proyek Google Cloud dengan YouTube Data API yang sudah diaktifkan.
- Kredensial OAuth 2.0 untuk proyek tersebut (diunduh sebagai file JSON).

## Persiapan

1. **Clone repositori** atau unduh script ini.

2. **Instal dependensi**:
   Kemudian jalankan perintah berikut untuk menginstal paket yang diperlukan:
   ```bash
   pip install -r requirements.txt
   ```

3. **Siapkan kredensial OAuth 2.0**:
   - Tempatkan file JSON kredensial OAuth 2.0 Anda di direktori yang sama dengan script ini.
   - Nama file `test.json` sesuaikan variabel `CLIENT_SECRETS_FILE` dalam script agar sesuai dengan nama file Anda.

4. **Jalankan script**:
   ```bash
   python chloe.py
   ```
   Script akan mengautentikasi akun Google Anda, menyimpan token untuk penggunaan di masa mendatang, dan kemudian mengubah judul video YouTube yang ditentukan.

## Konfigurasi

- **ID Video**: Ubah variabel `VIDEO_ID` dalam script dengan ID video yang ingin Anda ubah.
- **Tanggal Mulai**: Modifikasi variabel `START_DATE` agar sesuai dengan tanggal mulai yang diinginkan.
- **Template Judul**: Variabel `new_title` dalam script mengontrol format dari judul yang akan diperbarui.

## Contoh

Jika tanggal mulai diatur pada 14 Mei 2023, dan script dijalankan pada 9 Agustus 2024, maka judul video akan diperbarui menjadi:

```
Menunggu Chloe Stream Day 453
```

## Troubleshooting

- Jika Anda mengalami `NameError` terkait `Request`, pastikan Anda telah mengimpor `Request` dari `google.auth.transport.requests`.
- Jika script gagal melakukan autentikasi, pastikan kredensial OAuth 2.0 Anda telah dikonfigurasi dengan benar dan bahwa YouTube Data API telah diaktifkan di proyek Google Cloud Anda.

## Dedikasi

Script ini dikhususkan untuk **Chloe Pawapua**.
