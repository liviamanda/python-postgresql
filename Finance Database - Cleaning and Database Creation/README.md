[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/amDsZh7J)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=14404622&assignment_repo_type=AssignmentRepo)
# Graded Challenge 2

_Graded Challenge ini dibuat guna mengevaluasi pembelajaran pada Hacktiv8 Data Science Fulltime Program khususnya pada konsep Relational Database dan Pandas._

---

## Assignment Instructions

*Graded Challenge 1* dikerjakan dalam format ***Notebook (.ipynb)** dan **SQL Query (.sql)** dengan beberapa **kriteria wajib** di bawah ini:

1. *Project* dinyatakan selesai dan diterima untuk dinilai jika notebook dapat dirun seluruhnya dan file .sql dapat mengeluarkan output yang diinginkan.

2. Pada tugas Graded Challenge 2, akan diminta untuk membuat:
  -  **Notebook (.ipynb)** yang berisikan pengolahan data dengan Pandas dan Python.
  - Satu file **.sql** yang berisikan query untuk membuat database dari data yang diolah dengan Pandas.
  - Dua file data (format/extension bebas tapi disarankan csv) yang berisikan data hasil query.

3. Masing-masing file (.ipynb dan .sql) **wajib** diberikan keterangan atau pengenalan dengan menggunakan `comment` atau `docstring` yang berisikan Judul tugas, Nama, Batch, dan penjelasan singkat tentang program yang dibuat, fitur-fitur. Contoh:
    ```py
    '''
    =================================================
    Graded Challenge 2

    Nama  : Fahmi Iman Alfarizki
    Batch : BSD-50

    Program ini dibuat untuk melakukan automatisasi pengolahan (cleaning) data text yang berguna untuk pemodelan model analisa sentimen.
    =================================================
    '''
    ```
5. Tiap cell diberikan penjelasan mengenai apa yang dilakukan/dijalankan dengan markdown. Untuk file .sql, berikan comment di tiap kumpulan query sesuai dengan tahapan-tahapan yang dilakukan (seperti edit data, memasukan data, dll).

6. **WARNING**: Plagiarisme sekecil apapun dapat terdeteksi. Tugas ini akan diuji tingkat plagiarismenya dengan software khusus.

---

## Assignment Submission

- Simpan assignment pada Graded Challenge 2 ini dengan nama `P0G2_<nama-student>.ipynb` (notebook) dan `P0G2_<nama-student>.sql` (file .sql query). Misal `P0G2_fahmi-iman.ipynb` dan `P0G2_fahmi-iman.sql` (**Maksimal nama dua suku kata**).
- Push file Assigment yang telah dibuat ke repository Github Classroom masing-masing student.

---

## Assignment Objectives

*Graded Challenge 2* ini dibuat guna mengevaluasi konsep Relational Database dan Pandas sebagai berikut:

- Mampu membuat database di PostgreSQL (DDL)
- Mampu membuat tabel dengan query (DDL)
- Mampu mengisi data ke tabel (DML)
- Mampu menerapkan transactional pada query (TCL)
- Mampu memberikan akses query pada database yang dibuat (DCL)
- Mampu mengolah data sebelum ditransfer ke SQL database dengan Pandas
- Mampu mengambil data dari database yang dibuat (DQL)

---

## Assignment Instructions and Cases

Kamu adalah seorang Data Engineer yang membantu divisi Finance dalam mengatur data mereka. Mereka ingin data mereka bisa dibuatkan database dengan PostgreSQL server.

Selama ini mereka mengelola dan menyimpan data dengan Microsoft Excel dan disimpan dalam format file **.csv**.

Data yang ingin mereka simpan dalam database, dapat kamu akses di link [berikut](https://github.com/FTDS-learning-materials/phase-0/raw/main/src/Financials.csv).

Data ini berisikan informasi pendapatan dan profit per produk, segmentasi, dan negara yang didapatkan tiap harinya. Data ini pastinya belum bersih dan siap dimasukkan ke dalam database.

Ikuti langkah-langkah dan instruksi di bawah ini agar mendapatkan hasil yang diharapkan.

### 1. Data Exploration
<ol type = "a">
  <li>Load file data dengan Pandas lalu tampilkan data. Informasi apa yang bisa kamu sampaikan dari langkah ini?</li>
  <li>Tampilkan informasi summary data dan berikan penjelasan mengenai temuan yang diperoleh.</li>
  <li>Tampilkan list nama-nama kolom dan berikan penjelasan temuan apa yang kamu dapatkan, serta berikan langkah apa selanjutnya dari temuan ini.</li>
  <li>Tampilkan list nilai unik masing-masing kolom `Segment`,	`Country`,	`Product`,	`Discount Band` dan berikan informasi apa yang dapat kamu ambil dari langkah ini.</li>
</ol>

### 2. Data Cleaning

Berdasarkan langkah-langkah dan temuan-temuan dari eksplorasi data, lakukan pembersihan data!

<b>Hint: </b>Kamu dapat melakukan hal-hal berikut (List berikut tidak perlu dilakukan semua, sesuaikan dengan kondisi dan kebutuhan berdasarkan hasil eksplorasi):

<ol type = "a">
  <li>Manipulasi kolom meliputi penggantian nama kolom, penghapusan kolom, atau penambahan kolom</li>
  <li>Penggantian tipe data yang sesuai dengan seharusnya. Untuk nilai harga dengan simbol mata uang, simbol tersebut dapat dibuang supaya dapat terkonversi ke tipe data yang seharusnya. Perhatikan format penulisan angkanya apakah ada tanda yang membuat angka hanya bisa bertipe data string. (Tambahan: Di suatu kolom yang bernilai uang, terpadat beberapa data yang mengandung karakter '(' dan ')' di dalamnya sehingga harus ditake-out karakter tersebut. </li>
  <li>Cek dan handling missing value. (Hint: terdapat non-standard missing value pada kolom yang semestinya bertipe data integer, handling dapat dilakukan dengan imputasi dengan angka nol '0')</li>
</ol>

### 3. Data Normalization

<ol type = "a">
  <li>Lakukan normalisasi data yang sudah diolah sebelumnya sampai dengan 3NF.</li>
  <li>Jumlah tabel setelah dinormalisasi sebanyak 5 tabel termasuk tabel utama.</li>
  <li>Perhatikan penggunaan primary key dan foreign key antar tabel.</li>
  <li>Kemudian simpan semua tabel yang dihasilkan ke dalam file csv. Berikan nama file sesuai dengan nama tabel yang akan digunakan pada database. Jangan lupa index dataframe tidak perlu diikutsertakan dalam file karena skema tabel akan menerapkan auto incremental untuk pengisian primay key</li>
</ol>

### 4. Relational Database & SQL
Buat transaksi query yang meliputi banyak tahapan dimulai dari pembuatan tabel hingga memberikan akses beberapa query saja pada database tersebut ke seorang user. Ketentuan:
1. Buat database dengan query yang terpisah dari blok transaksional (di luar dari blok TCL). Perlu dicatat, pembuatan database di Postgres tidak bisa digabung dengan query lain meski dipisahkan dengan `;`. Sehingga, jalankan dulu query pembuatan database dan langsung diubah menjadi komentar.
2. Buat blok transaksional (transactional block) menggunakan TCL yang mengandung:
    * Pembuatan tabel\
      Pembuatan tabel-tabel dari hasil normalisasi dengan tipe data masing-masing kolom yang sesuai dengan data (atau paling tidak sama dengan Pandas) dan penentuan Primary Key dan Foreign Key yang tepat. Primary Key tabel harus bersifat auto incremental karena index DataFrame tidak diikutsertakan dalam file.
    * Input data\
      Data yang sudah diolah dan tersimpan dalam format **.csv** dapat dicopy/load ke database dengan query `COPY` seperti contoh berikut:
      ```sql
      COPY Tabel_Name(col1, col2, col3, col4, col5)
      FROM 'C:\tmp\persons.csv'
      DELIMITER ','
      CSV HEADER;
      ```
      Notes: simpan semua file csv yang akan dibaca oleh sql ke folder tmp (Windows= `C:\tmp\` dan Mac/Linux= `/tmp/` supaya mempermudah.
    * Pembuatan user\
      Buat user minimal 2 user beserta username dan passwordnya

    * Pemberian akses query\
      Berikan akses hanya command `SELECT` pada salah satu user serta block akses `INSERT`, `UPDATE`, `TRUNCATE` dan `DELETE`  khusus untuk database yang sudah dibuat. User lainnya dapat dianggap sebagai admin sehingga berikan seluruh akses command query.
3. Jalankan transactional block query ini sampai selesai dan sampai menghasilkan tabel dan isi yang sesuai dengan hasil pengolahan data dan normalisasi di notebook (sesuai dengan file csv yang dihasilkan).

4. Simpan query ke dalam file berformat **.sql**.

### 5. Pengujian Database
1. Setelah tabel sudah berhasil dibuat, uji keberhasilan database dan tabel yang kamu buat dengan kasus berikut:

    a. Berikan tabel yang berisikan informasi total profit yang didapatkan di tiap jenis segmentasi. Jangan ambil data yang tidak diskon.
  
    b. Berikan tabel yang berisikan informasi rangkuman statistik yang memuat nilai rata-rata, min, dan max (dijadikan dalam kolom yang berbeda) dari Sales masing-masing negara.
  
2. Simpan kedua tabel dalam file yang berbeda dan load ke dalam notebook pengolahan data untuk ditampilkan. **Tuliskan query SQL pada markdown!**.
---

## Assignment Rubrics

<img src="https://github.com/FTDS-learning-materials/phase-0/blob/main/img/P0G2_Rubric.png?raw=true"></img>

---
## Score Reduction

Jika Student terlambat mengumpulkan dengan waktu yang ditentukan, maka Graded Challenge akan diberi poin nol.

---
