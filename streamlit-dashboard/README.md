# Career Path Analysis Dashboard

## Deskripsi Proyek

Project ini bertujuan untuk menganalisis permasalahan dan tujuan karier pengguna berdasarkan dataset Pretext. Analisis dilakukan untuk memahami role yang paling diminati, masalah yang paling sering dihadapi pengguna, serta hubungan antara tingkat kemampuan pengguna dengan masalah yang mereka alami.

Selain analisis data, project ini juga menyediakan dashboard interaktif menggunakan Streamlit dan implementasi A/B Testing menggunakan Python.

---

## Struktur Project

```text
pretext_project/
│
├── analysis_pretext.ipynb
├── app.py
├── ab_testing.py
├── requirements.txt
│
├── data/
│   └── dataset_pretext.csv
│
└── outputs/
    ├── top_roles.png
    ├── problem_distribution.png
    └── ab_test_result.csv
```

---

## Business Questions

### 1. Karier apa yang paling banyak diminati oleh pengguna?

Analisis dilakukan dengan:

- Menghitung frekuensi setiap target role
- Mengurutkan berdasarkan jumlah pengguna
- Menampilkan 10 role teratas menggunakan visualisasi bar chart

### 2. Apakah tingkat kemampuan pengguna memengaruhi jenis masalah yang mereka hadapi?

Analisis dilakukan dengan:

- Membuat crosstab antara current_level dan problem_category
- Menganalisis distribusi masalah pada setiap level pengguna
- Menampilkan hasil menggunakan grouped bar chart

---

## Data Processing

Tahapan pengolahan data yang dilakukan:

1. Data Loading
2. Data Understanding
3. Data Cleaning
4. Exploratory Data Analysis (EDA)
5. Data Visualization
6. Business Insight Extraction
7. Dashboard Development
8. A/B Testing Simulation

---

## Hasil Analisis

### Insight 1

Role yang paling banyak diminati oleh pengguna adalah:

- Business Intelligence Analyst
- Data Analyst
- Data Scientist

Role tersebut menunjukkan tingginya minat pengguna terhadap bidang data dan analitik.

### Insight 2

Mayoritas pengguna berada pada level:

- Intermediate

Masalah yang paling sering muncul adalah:

- Direction Confused

Hal ini menunjukkan banyak pengguna yang masih mengalami kebingungan dalam menentukan arah pengembangan karier meskipun telah memiliki pengalaman dasar.

---

## Dashboard Features

Dashboard dibuat menggunakan Streamlit dan memiliki fitur:

- Filter berdasarkan Target Role
- Filter berdasarkan Current Level
- Filter berdasarkan Problem Category
- KPI Metrics
- Top Roles Visualization
- Problem Category Distribution
- Level vs Problem Category Analysis
- Interactive Data Table

---

## A/B Testing

Pada project ini dilakukan simulasi A/B Testing menggunakan Chi-Square Test.

### Hipotesis

H0:
Tidak terdapat perbedaan signifikan antara grup A dan grup B.

H1:
Terdapat perbedaan signifikan antara grup A dan grup B.

### Metode

- Membagi data ke dalam grup A dan B
- Membuat metrik keberhasilan berdasarkan kategori masalah
- Menggunakan Chi-Square Test untuk menguji signifikansi

Library yang digunakan:

```python
scipy.stats.chi2_contingency
```

---

## Menjalankan Notebook Analisis

Buka Jupyter Notebook:

```bash
jupyter notebook
```

Kemudian jalankan:

```text
analysis_pretext.ipynb
```

---

## Menjalankan Dashboard

Install dependencies:

```bash
pip install -r requirements.txt
```

Jalankan Streamlit:

```bash
streamlit run app.py
```

Dashboard akan tersedia pada:

```text
http://localhost:8501
```

---

## Menjalankan A/B Testing

```bash
python ab_testing.py
```

Output akan menampilkan:

- Nilai Chi-Square
- P-Value
- Keputusan Hipotesis

---

## Teknologi yang Digunakan

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- Streamlit
- SciPy
- Jupyter Notebook

---

## Author

Nama: Gregorius Christian Sunaryo

Project: Career Path Analysis Dashboard