Markdown
# Aplikasi Prediksi Penjualan E-Commerce

Aplikasi web sederhana berbasis Flask untuk memprediksi estimasi jumlah penjualan (rating count) produk e-commerce berdasarkan nilai rating produk menggunakan model Regresi Linear.

## Fitur Utama

- Input nilai rating produk (skala 1.0 - 5.0).
- Prediksi estimasi jumlah ulasan/penjualan menggunakan model Machine Learning yang telah dilatih.
- Visualisasi interaktif grafik perbandingan menggunakan Chart.js.
- Tampilan antarmuka modern dan responsif.

## Struktur Proyek

TA-02/
├── Model/
│   └── model.joblib
├── Template/
│   └── index.html
├── app.py
├── requirements.txt
└── vercel.json


## Teknologi yang Digunakan

- Python 3
- Flask
- Scikit-Learn / Joblib
- HTML5 / Tailwind CSS
- Chart.js

## Cara Menjalankan Secara Lokal

1. Clone repositori ini:
   ```bash
   git clone [https://github.com/yuuji005/TA-02.git](https://github.com/yuuji005/TA-02.git)
   cd TA-02
Buat dan aktifkan environment Python (opsional):

Bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
# atau
venv\Scripts\activate     # Windows
Install dependensi yang dibutuhkan:

Bash
pip install -r requirements.txt
Jalankan aplikasi Flask:

Bash
python app.py
Buka browser dan akses http://127.0.0.1:5000.

Deployment
Aplikasi ini dikonfigurasi untuk dapat dideploy secara langsung ke Vercel menggunakan file vercel.json.
