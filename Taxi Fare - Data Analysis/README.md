[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/wESIpcmI)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=14448266&assignment_repo_type=AssignmentRepo)
# **Live Code 2**
---
## **Instruction**

1. Live Code ini dikerjakan dalam format ***notebook*** isi *notebook* harus mengikuti *outline* di bawah ini:
  * Perkenalan\
   Bab pengenalan harus diisi dengan identitas (Nama dan Batch)
  * *Answer*\
   Bagian ini berisi proses dalam menjawab soal, tiap nomor soal dikerjakan dalam satu cell masing-masing dan berikan judul soal dengan markdown sebelum cell code.

2. Pada graded challenge ini, data diakses dari BigQuery dengan ketentuan:

  - **Project_id_Database**: `ftds-hacktiv8-project`
  - **Dataset**   : `phase0_ftds_<nomor batch>_<kode lokasi program>`
  - **Tabel**     : `taxi_fare`

  *contoh:*

   - Stundent online: `ftds-hacktiv8-project.phase0_ftds_010_rmt.taxi_fare`
   - Student Surabaya: `ftds-hacktiv8-project.phase0_ftds_010_sby.taxi_fare`

   Sesuaikan dengan `<nomor batch>` dan `<kode lokasi program>` Anda.

<div align="center">

|Lokasi|Kode Lokasi|
|--|--|
|Remote|rmt|
|Pondok Indah|hck|
|BSD|bsd|
|Surabaya|sby|

</div>

  Berikut merupakan skema dari tabel diatas:

<div align="center">

|Nama Kolom|Deskripsi|
|--|--|
|unique_key|Unique Identifier terhadap nomor perjalanan|
|unique_taxi|Unique Identifier terhadap nomor taksi|
|trip_start_timestamp|Waktu dimulainya perjalanan, dibulatkan ke menit kelipatan 15 terdekat|
|trip_end_timestamp|Waktu dimulainya perjalanan, dibulatkan ke menit kelipatan 15 terdekat|
|trip_km|Jarak perjalanan dalama km|
|fare|Biaya perjalanan|
|tips|Uang tambahan yang diberikan pelanggan ke pengemudi, untuk cash biasanya tidak ter-record|
|payment_type|Tipe pembayaran|
|company|Nama perusahaan penyedia layanan perjalanan|
|pickup_location|Lokasi titik penjemputan perjalanan|
|dropoff_location|Lokasi titik tujuan perjalanan|


</div>

3. Koneksikan data diatas dari `BigQuery` ke Google Colab tempat pengerjaan P0-LC2 dengan code berikut:

  ```
from google.colab import auth
from google.cloud import bigquery
auth.authenticate_user()
print('Authenticated')

project_id_akun = "rock-wonder-317907" #GUNAKAN GCP PROJECT-ID KALIAN MASING-MASING
client = bigquery.Client(project=project_id_akun)
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

 5. Lakukan pengolahan SQL langsung pada Notebook Google Colaboratory.

    Jika dalam durasi 20 menit kalian kesulitan dalam mengakses data, silahkan hubungi pengawas LC.

---
## **Assignment Submission**

- Simpan assignment pada sesi ini dengan nama `h8dsft_P0LC2_<nama-student>.ipynb`, misal `h8dsft_P0LC2_raka_ardhi.ipynb`.
- Push Assigment yang telah kalian buat ke repository Github Classroom masing-masing student.
---
## **Assignment Objectives**

*Live Code 2* ini dibuat guna mengevaluasi SQL dan Pandas sebagai berikut:

- Mampu melakukan analisa data di SQL.
- Mampu melakukan pengambilan data dari SQL.
- Mampu melakukan pengolahan data di pandas.
- Mampu menerapkan looping, conditional, serta query agggregation menggunakan pandas.
---

## **Assignment Instructions and Cases**

>Kamu adalah seorang Data Analyst yang sedang melakukan analisa data perjalanan dari penyedia jasa transportasi di kotamu. Pada tahapan ini analisa yang dilakukan masih bersifat preliminary, sebagai landasan untuk analisa utama.

>**Analisa yang kamu lakukan kali ini terbagi menjadi 2 section; SQL dan Pandas.** Pada SQL akan dilakukan overview EDA analysis, sementara pada section Pandas akan dilakukan persiapan data untuk analisa lebih lanjut. Penjabaran dari apa yang akan kamu lakukan tertera di masing-masing section berikut:

### **Problem 1 - SQL**

Jawab masing-masing pertanyaan ini dengan 1 query:

1. Apa saja nama perusahaan yang terdapat dalam data?
2. Berapa nilai minimum dan maksimum dari waktu pengambilan data?
3. Bandingkan jumlah banyaknya perjalanan antara seluruh perusahaan pada tahun 2022?
4. Perusahaan mana yang memiliki tarif perjalanan per km termurah?

### **Problem 2 - Pandas**

Pengambilan data dari SQL untuk diolah di pandas **wajib** menggunakan query di bawah ini:

<div align="center">

`SELECT * FROM ftds-hacktiv8-project.phase0_ftds_<nomor batch>_<kode lokasi program>.taxi_fare`

</div>

1. buat kolom baru, dengan nama `Keterangan_Waktu`. Kolom ini berisikan label yang menunjukkan representasi keterangan waktu berdasarkan jam dengan ketentuan berikut:

<div align="center">

|Keterangan Waktu|Jam|
|--|--|
|Pagi|04:00 - 09:59|
|Siang|10:00 - 15:59|
|Sore|16:00 - 18:59|
|Malam|19:00 - 23:59|
|Dini Hari|00:00 - 03:59|

</div>

2. Berapa total jarak perjalanan yang dicapai perusahaan Federway Int. pada tahun 2022? (Gunakan pandas query untuk menjawab soal no. 2)

>**Hints:**

>- Dalam mengerjakan soal Pandas poin 1, Untuk melakukan ekstraksi waktu (jam) dapat memanfaatkan `pd.Series.dt.hour`, pastikan kolom yang akan di-ekstrak sudah memiliki format *datetime*.
>- Setelah melakukan ekstraksi waktu (jam), lakukan looping dan kondisional untuk setiap entry data sesuai ketentuan kondisi keterangan waktu diatas.
>- Simpan hasil looping dan kondisional ke dalam list dan convert menjadi kolom baru.

Narasikan asumsi dan pertimbanganmu dalam menjawab masing-masing pertanyaan pada section SQL dan Pandas, narasikan pula insightnya.

Tuliskan Kesimpulan akhir dari seluruh proses yang telah kamu kerjakan. 

---
## **Assignment Rubrics**

<img src="https://github.com/FTDS-learning-materials/phase-0/blob/main/img/P0LC2_Rubric.png?raw=true" width=75% height=75%></img>

---

```
Total Points : 42
```
