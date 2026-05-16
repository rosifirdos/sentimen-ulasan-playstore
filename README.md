# Sentiment Analysis of Google Play Store Reviews (Indonesian)

Proyek ini bertujuan untuk melakukan analisis sentimen pada ulasan aplikasi di Google Play Store menggunakan bahasa Indonesia. Proyek ini mencakup seluruh siklus data science, mulai dari pengumpulan data (scraping), preprocessing teks yang mendalam, pelabelan otomatis menggunakan lexicon, hingga pemodelan menggunakan machine learning.

## 🚀 Fitur Utama
- **Automated Scraping**: Mengambil ulasan terbaru dari Google Play Store menggunakan `google-play-scraper`.
- **Advanced Preprocessing**:
  - Normalisasi kata slang (Kamus Alay).
  - Stopword removal & Stemming menggunakan library `Sastrawi`.
  - Penanganan emoji dan pembersihan karakter berulang.
- **Lexicon-Based Labeling**: Pelabelan otomatis menggunakan InSet Lexicon (Koto & Rahmaningtyas).
- **Machine Learning**: Implementasi model Logistic Regression dengan TF-IDF Vectorization.
- **Evaluation**: Laporan performa model yang lengkap (Accuracy, F1-Score, Confusion Matrix, & Cross-Validation).

## 💻 Tech Stack
- **Python**: Bahasa pemrograman utama untuk analisis data dan scripting.
- **Pandas**: Library untuk manipulasi data (membaca file CSV/TSV dan mengelola DataFrame).
- **Scikit-Learn**: Framework utama untuk pembuatan model machine learning (Logistic Regression), TF-IDF vectorization, dan evaluasi model.
- **Sastrawi**: Digunakan untuk pemrosesan teks bahasa Indonesia (stemming dan penghapusan stopword).
- **Google Play Scraper**: Library untuk melakukan scraping ulasan langsung dari Google Play Store.
- **Matplotlib & Seaborn**: Digunakan untuk visualisasi data (distribusi rating, confusion matrix, dsb).
- **Jupyter Notebook**: Media untuk melakukan eksperimen dan analisis data secara interaktif.

## 📁 Struktur Proyek
```text
.
├── dataset/
│   ├── playstore_reviews_raw.csv      # Data hasil scraping mentah
│   └── playstore_reviews_labeled.csv  # Data yang telah dibersihkan dan diberi label
├── resources/
│   ├── kamus_alay.csv                 # Dictionary normalisasi bahasa gaul
│   ├── inset_positive.tsv             # Lexicon sentimen positif
│   └── inset_negative.tsv             # Lexicon sentimen negatif
├── notebook_analisis_sentimen.ipynb   # Notebook utama eksperimen & analisis
├── scraping_playstore.py              # Script untuk scraping data dari Play Store
├── requirements.txt                   # Daftar dependensi library
└── README.md                          # Dokumentasi proyek
```

## 🛠️ Instalasi

1. Clone repository ini:
   ```bash
   git clone https://github.com/username/sentiment-analysis-playstore-id.git
   cd sentiment-analysis-playstore-id
   ```

2. Buat virtual environment (opsional tapi disarankan):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Untuk Windows: venv\Scripts\activate
   ```

3. Instal dependensi:
   ```bash
   pip install -r requirements.txt
   ```

## 📖 Cara Penggunaan

### 1. Pengambilan Data (Scraping)
Jalankan script `scraping_playstore.py` untuk mengambil ulasan dari aplikasi tertentu (default: Tokopedia).
```bash
python scraping_playstore.py --app-id com.tokopedia.tkpd --target 5000
```
Argumen:
- `--app-id`: ID aplikasi di Play Store (lihat di URL aplikasi).
- `--target`: Jumlah ulasan minimum yang ingin diambil.

### 2. Analisis & Pemodelan
Buka `notebook_analisis_sentimen.ipynb` menggunakan Jupyter Notebook atau VS Code. Ikuti langkah-langkah di dalamnya:
- Load data raw.
- Lakukan preprocessing (Cleaning, Normalization, Stemming).
- Labeling otomatis dengan InSet Lexicon.
- Training model Logistic Regression.
- Evaluasi hasil.

## 📊 Hasil Evaluasi (Contoh)
Model Logistic Regression yang diimplementasikan mencapai performa yang cukup solid:
- **Accuracy**: ~88% pada data pengujian.
- **Cross-Validation Accuracy**: ~90%.
- **Balanced Class Handling**: Menggunakan `class_weight='balanced'` untuk menangani ketidakseimbangan antara sentimen positif dan negatif.

## 📚 Referensi
- **InSet Lexicon**: Koto, F., & Rahmaningtyas, G. Y. (2017). InSet Lexicon: Lexicon-Based Sentiment Analysis in Indonesian.
- **Sastrawi**: Library untuk stemming dan stopword bahasa Indonesia.
- **Google Play Scraper**: Library untuk mengambil data dari Google Play Store.

---
## 👤 Penulis
**Awanda Rosi Firdaus**  
*Submission Akhir - Coding Camp by DBS Foundation & Dicoding (2026)*
