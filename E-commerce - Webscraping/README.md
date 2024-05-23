[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/xOhv878p)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=14503064&assignment_repo_type=AssignmentRepo)
# Graded Challenge 3

_Graded Challenge ini dibuat guna mengevaluasi pembelajaran pada Hacktiv8 Data Science Fulltime Program khususnya pada konsep Web Scraping, Business Knowledge dan Practical Statistics._

---

## Assignment Instructions

*Graded Challenge 3* dikerjakan dalam format ***Notebook (.ipynb)**  di bawah ini:

1. *Project* dinyatakan selesai dan diterima untuk dinilai jika notebook dapat dirun seluruhnya tanpa ada error (code block web scraping tidak perlu dirun ulang).

2. Pada tugas Graded Challenge 3, akan diminta untuk membuat:
  -  **Notebook (.ipynb)** yang berisikan pengambilan, pengolahan, dan analisis data. Kerjakan dengan Visual Studio Code!

3. Notebook **wajib** diberikan keterangan atau pengenalan dengan menggunakan `comment` atau `docstring` yang berisikan Judul tugas, Nama, Batch, dan penjelasan singkat tentang program yang dibuat, fitur-fitur. Contoh:
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
5. Tiap cell diberikan penjelasan mengenai apa yang dilakukan/dijalankan dengan markdown.

6. **WARNING**: Plagiarisme sekecil apapun dapat terdeteksi. Tugas ini akan diuji tingkat plagiarismenya dengan software khusus.

---

## Assignment Submission

- Simpan assignment pada Graded Challenge 3 ini dengan nama `P0G3_<nama-student>.ipynb` (notebook). Misal `P0G3_fahmi-iman.ipynb`(**Maksimal nama dua suku kata**).
- Push file Assigment yang telah dibuat ke repository Github Classroom masing-masing student.

---

## Assignment Objectives

*Graded Challenge 3* ini dibuat guna mengevaluasi konsep Web Scraping, Business Knowledge dan Practical Statistics sebagai berikut:

- Mampu mengambil data dari sumber internet dengan Web Scraping
- Mampu melakukan data preparation sebelum analisis selanjutnya
- Mampu membangun problem statement dengan framework SMART sebagai salah satu langkah business understanding
- Mampu melakukan perhitungan statistik deskriptif
- Mampu melakukan pengujian statistik dan merumuskan hipotesis
- Mampu mengambil insight/informasi dari hasil perhitungan
- Mampu mengambil kesimpulan yang menjawab problem statement

---

## Assignment Instructions and Cases

#### Case
Kamu ingin menambah pendapatanmu dengan berjualan. Namun, kamu tidak punya cukup modal untuk produksi barang dan hanya cukup untuk promosi, sehingga kamu memutuskan untuk menjalanan skema dropship di platform Tokopedia.

Kamu masih bingung akan berjualan apa dan teringat bahwa saat ini sedang viral seblak. Namun, kamu tidak yakin apakah benar bahwa masyarakat memiliki animo yang besar terhadap seblak.

Karena kamu lulusan bootcamp Data Science Hacktiv8, dengan kemampuan dan pengetahuan kamu, kamu ingin menganalisis bagaimana penjualan produk seblak di Tokopedia. Apakah orang suka, apakah banyak yang beli, dsb.

Tantangannya, kamu tidak punya data sama sekali selain yang terpampang pada website e-commerce Tokopedia. Oleh karena itu, perjalanan kamu dimulai dari pengambilan data menggunakan Web Scraping!

#### A. Web Scraping
1. Lakukan pengambilan data dari halaman pencarian kata kunci produk "seblak". Kamu bisa langsung akses link ini:
  https://www.tokopedia.com/search?navsource=&page=1&q=seblak&srp_component_id=02.01.00.00&srp_page_id=&srp_page_title=&st=
  
  Berikut tampilan halaman link di atas:
  ![img](https://github.com/FTDS-learning-materials/phase-0/blob/main/img/p0gc3_1.png?raw=true)

2. Ambil data `Nama Produk`, `Harga Produk`, `Penjual`, `Kota Toko`, `Banyaknya Terjual`, dan `Rating Produk`.

3. Tokopedia memiliki skema promosi sehingga pada panel teratas merupakan info produk suatu merchant yang membayar iklan. Kita akan ambil produk di dalam box yang reguler dengan elemen `<div class="css-974ipl">`.

  **Tambahan:** untuk produk baru, belum ada informasi berapa produk yang terjual dan rating sehingga hasil akhir akan berbeda jumlah data yang diperoleh untuk kolom `Banyaknya Terjual` dan `Rating Produk` seperti contoh gambar di bawah:

  ![img](https://github.com/FTDS-learning-materials/phase-0/blob/main/img/p0gc3_2.png?raw=true)

  Sehingga kamu perlu mengatasi hal ini dengan cara, jika menemukan bahwa tidak ada informasi `Banyaknya Terjual` dan `Rating Produk`, kamu hanya perlu mengisi data dengan `None` (tanpa string) dan pandas akan langsung mendeteksi sebagai missing value.

4. Untuk memudahkan kamu, sudah disediakan list elemen salah satu produk:
  ```html
  <div class="prd_link-product-name css-3um8ox" data-testid="spnSRPProdName">SEBLAK JUARA INSTAN MASAK BASAH ASLI BANDUNG ENAK MANTAP</div>
<div class="prd_link-product-price css-1ksb19c" data-testid="spnSRPProdPrice">Rp22.000</div>
<div class="css-1rn0irl"><span class="prd_link-shop-loc css-1kdc32b flip" data-testid="spnSRPProdTabShopLoc">Bandung</span><span class="prd_link-shop-name css-1kdc32b flip" data-testid="">Rasa Juara Indonesia</span></div>
<span class="prd_label-integrity css-1duhs3e" data-testid="">Terjual 750+</span>
<span class="prd_rating-average-text css-t70v7i" data-testid="">4.9</span>
  ```
  **WARNING:** Kamu harus mengecek lagi kebenaran dari elemen tersebut karena Tokopedia merupakan website dinamis yang bisa saja berubah lagi attribute dan attribute value nya. Perlu diingat juga, Tokopedia senantiasa ingin melakukan improvisasi khususnya UI website sehingga bisa jadi sedang dilakukan A/B Testing dan kamu mendapatkan tampilan web yang berbeda. Tampilan web berbeda, maka elemennya juga berbeda.

  Pastikan seluruh attribute dan values digunakan dalam positioning di Beautifulsoup nya.

5. Ambil informasi produk minimal dari 10 halaman pencarian (perhatikan format url linknya dan eksplorasi terlebih dahulu halaman web nya).

6. Perlu diingat bahwa setiap orang dan setiap waktu akan menghasilkan hasil data yang berbeda, hal ini tidak masalah, yang paling penting jumlah data yang diperoleh minimal 50 data dari minimal 10 halaman yang diakses.

7. Simpan hasil scrape ke pandas data frame dan kemudian diolah. Kamu dibebaskan memberikan nama kolom yang memudahkan kamu.

#### B. Data Preparation

1. Lakukan eksplorasi data sederhana:
  - Tampilkan beberapa baris data - tuliskan insight
  - Tampilkan informasi rangkuman data - tuliskan insight dan berikan penjelasan langkah apa yang akan kamu lakukan
  - Cek missing value - tuliskan insight dari temuan yang kamu dapatkan
2. Lakukan data cleaning:
  Kamu bisa handle missing value bila ada, mengubah bentuk data menjadi konsisten dan menyesuaikan tipe data. Perlu diingat bahwa data ini akan digunakan untuk perhitungan statisik dan membutuhkan angka.
3. Catatan:
  Pada kolom "Banyaknya Terjual", jumlah produk yang terjual dituliskan sebagai `Terjual 750+`, `Terjual 1 rb`. Ambil angkanya saja. Misal `Terjual 750+` -> `750` dan `Terjual 1 rb` -> `1000`.

#### C. Business Understanding/Problem Statement
Buat problem statement menggunakan SMART framework berikut dengan penjabaran Specific, Measurable, Achievable, Relevant, dan Time-bound. Jangan lupa merangkup dalam satu kalimat problem statement serta gunakan metrik yang tepat dari kasus ini.

#### D. Analysis
  Dalam melakukan analisa data untuk mencapai tujuan yang diinginkan, kamu perlu mengikuti soal/pertanyaan/instruksi berikut ini:
1. Hitung rata-rata, median, standar deviasi, skewness, dan kurtosis dari kolom harga, banyak produk terjual, dan rating. Dari hasil perhitungan, insight apa saja yang bisa kamu dapatkan khususnya terkait dengan produk seblak dan datanya (distribusi dan kecenderungan ada/tidaknya outlier)?

  **Note:** Jika menemukan adanya indikasi outlier dari perhitungan ini, tidak perlu dihandle karena sifatnya alami. Dibiarkan saja.

2. Kamu memikirkan berapa potensi minimum dan maksimum pendapatan jika kamu menjual produk seblak?(Gunakan confidence interval untuk mendapatkan lower value dan upper value dari distribusi populasi pendapatan).

  Anggap data terdistribusi normal dan informasi produk terjual merupakan penjualan produk per bulan. Ambil confidence level 95%.

3. Apakah harga barang di Jabodetabek dan di luar Jabodetabek berbeda? mengingat biaya bahan baku di kedua lokasi berbeda. (Gunakan uji hipotesis yang diawali dengan menuliskan hipotesis null dan alternatifnya serta tentukan jenis hipotesis yang digunakan).

4. Apakah orang lebih cenderung suka dengan produk yang harganya murah?

  Kamu dapat jawab pertanyaan ini dengan uji korelasi. Gunakan library scipy jangan pandas. Analisis nilai korelasi dan p-value nya. Gunakan teknik yang sesuai dengan kondisi data!

Kamu dilarang untuk copy-paste pertanyaan soal. Buat lah cerita yang runut dari persoalan dan jawaban nomor 1 sampai 4 sebagai ganti kalimat soal.

#### E. Conclusion
  Tuliskan di markdown kesimpulan dari hasil analisis dari nomor 1-4. Kesimpulan yang baik menjawab tujuan yang ingin dicapai. Kamu dibebaskan menuliskan dalam format paragraf atau poin.

## Assignment Rubrics

![img](https://github.com/FTDS-learning-materials/phase-0/blob/main/img/P0GC3_Rubric.png?raw=true)

---
## Score Reduction

Jika Student terlambat mengumpulkan dengan waktu yang ditentukan, maka Graded Challenge akan diberi poin nol.

---
