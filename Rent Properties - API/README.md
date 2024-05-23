[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/x0PpyWY_)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=14538148&assignment_repo_type=AssignmentRepo)
# **Live Code 3**
---
## **Instruction**

1. Live Code ini dikerjakan dalam format ***notebook*** isi *notebook* harus mengikuti *outline* di bawah ini:
  * Perkenalan\
   Bab pengenalan harus diisi dengan identitas (Nama dan Batch) serta objective yang ingin dicapai dengan singkat 
  * *Answer*\
   Bagian ini berisi proses dalam menjawab soal, tiap nomor soal dikerjakan dalam satu cell masing-masing dan berikan judul soal dengan markdown sebelum cell code.

2. Pada graded challenge ini, data diakses dari BigQuery dengan ketentuan:

  - **Project_id**: `bigquery-public-data`
  - **Dataset**   : `properati_properties_ar`
  - **Tabel**     : `properties_rent_201501`

  Untuk melihat langsung datanya, buka [Google Cloud Platform](https://console.cloud.google.com/), masuk ke BigQuery, lalu buka tab `bigquery-public-data` atau klik link [berikut](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=samples&page=dataset&_ga=2.245085957.1471931019.1642739417-486643658.1638156099) atau link [berikut](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=iowa_liquor_sales&t=sales&page=table) untuk langsung menuju ke tabel.

  

3. Koneksikan data diatas dari `BigQuery` ke Google Colab tempat pengerjaan P0-LC3 dengan code berikut:

```
from google.colab import auth
from google.cloud import bigquery
auth.authenticate_user()
print('Authenticated')

  project_id = "rock-wonder-317907" #GUNAKAN GCP PROJECT-ID KALIAN MASING-MASING
client = bigquery.Client(project=project_id)
```

4. Untuk melakukan Query menggunakan cara ini, kamu dapat menggunakan method client.query('Masukkan Querynya').to_dataframe(). Outputnya akan berupa Pandas dataframe, sehingga harus import Pandas. Contoh:

```
df = client.query('''
SELECT *
FROM `bigquery-public-data.thelook_ecommerce.orders`
WHERE created_at < "2022-07-01"
ORDER BY year,month ASC
''').to_dataframe()
```
---
## **Assignment Submission**

- Simpan assignment pada sesi ini dengan nama `h8dsft_P0LC3_<nama-student>.ipynb`, misal `h8dsft_P0LC3_raka_ardhi.ipynb`.
- Push juga file data `.csv` dan file API `<nama-student>_app.py`
- Push Assigment yang telah kalian buat ke repository Github Classroom masing-masing student.
---
## **Assignment Objectives**

*Live Code 3* ini dibuat guna mengevaluasi SQL, Statistics, dan API sebagai berikut:

- Mampu mengambil data dari SQL database.
- Mampu menerapkan konsep central tendency.
- Mampu menerapkan konsep distribusi data.
- Mampu menerapkan konsep extreme value analysis.
- Memahami konsep statistik.
- Mampu membuat API sederhana dengan FastAPI
---

## **Assignment Instructions and Cases**

```
Perhatikan petunjuk penggunaan dataset!
```

Buatlah query dengan kriteria sebagai berikut:
   - Pilih **HANYA** kolom `price`
   - Pilih data dengan value `operation` 'rent' dan `property_type` 'Apartement`
   - Batasi jumlah data yang diambil sebanyak 5000 (atau lebih rendah)

**A. Analisis Anomali**

Kamu diminta untuk menganalisis data penyewaan rumah. Namun, kamu sadar bahwa sepertinya ada data anomali yang harus dikeluarkan.

Untuk mengetahui adanya anomali, kamu bisa menggunakan metode extreme value analysis. Untuk melakukan pengecekan anomali/outlier, lakukan langkah-langkah di bawah ini:
1. Lakukan perhitungan central tendency (mean, median, modus) terhadap data sebelum dideteksi adanya anomali.
2. Cek skewness data untuk mengetahui apakah data terdistribusi normal atau tidak.
3. Lakukan pengolahan data dengan menggunakan extreme value analysis.
4. Buat variabel baru yang menyimpan data yang sudah dibuang data anomalinya.
5. Simpan data yang sudah dibuang anomalinya ke file csv dengan nama file `<nama-student>.csv`.

**B. API**

1. Buat API sederhana menggunakan FastAPI untuk menampilkan data yang sudah dibuang data anomalinya.
2. Clue: Load data csv yang sudah diolah dengan pandas, kemudian konversi data ke dictionary (`df.to_dict()` atau json (`df.to_json()`) untuk dapat ditampilkan dengan API menggunakan FastAPI.
3. Simpan file script dengan nama `<nama-student>_app.py`

**B. PERTANYAAN**

**Silahkan jawab pertanyaan-pertanyaan di bawah ini berdasarkan hasil yang kamu peroleh dan tulis dengan markdown:**
1. Berapa rata-rata, median, dan modus dari data tersebut sebelum dihilangkan outliernya? Bagaimana kecerendungan pemusatan datanya? jelaskan jawabanmu!
2. Sebelum melakukan extreme value analysis, kamu harus melakukan pengecekan skewness dari distribusi datanya. Apakah datanya skew atau normal? jelaskan jawabanmu!
3. Ada dua teknik untuk melakukan extreme value analysis, teknik yang mana yang kamu pakai? berikan alasanmu berdasarkan data!

---
## **Assignment Rubrics**

![img](https://github.com/FTDS-learning-materials/phase-0/blob/main/img/P0LC3_Rubric.png?raw=true)

---

```
Total Points : 25
```
