[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/TW2mF7lO)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=14298354&assignment_repo_type=AssignmentRepo)
# Graded Challenge 1

_Graded Challenge ini dibuat guna mengevaluasi pembelajaran pada Hacktiv8 Data Science Fulltime Program khususnya pada konsep Conditionals, Loops, Functions, Object-Oriented Programming, Python Unit Test, dan Computational Thinking._

---

## Assignment Instructions

*Graded Challenge 1* dikerjakan dalam format ***Python script (.py)*** dengen beberapa **kriteria wajib** di bawah ini:

1. *Project* dinyatakan selesai dan diterima untuk dinilai jika script dapat dijalankan dengan baik di prompt maupun terminal.

2. Pada tugas Graded Challenge 1, akan diminta untuk membuat:
  -  **dua file .py** yang berisikan masing-masing full program sesuai dengan instruksi soal dan unit test
  - satu file gambar yang berisikan flowchart program.
  - dua file gambar screenshot running program dan hasil running

3. **Tidak diperkenankan** membuat program dalam format notebook.

4. Masing-masing file **wajib** memberikan keterangan atau pengenalan dengan menggunakan `comment` atau `docstring` yang berisikan Judul tugas, Nama, Batch, dan penjelasan singkat tentang program yang dibuat, fitur-fitur. Contoh:
    ```py
    '''
    =================================================
    Graded Challenge 1

    Nama  : Fahmi Iman Alfarizki
    Batch : BSD-50

    Program ini dibuat untuk melakukan automatisasi pengolahan (cleaning) data text yang berguna untuk pemodelan model analisa sentimen.
    =================================================
    '''
    ```
5. Tiap class dan method/function diberikan penjelasan mengenai untuk apa class/method ini dan bagaimana alur algoritmanya dengan `docstring`

  ```py
  #Contoh:

  def f(x):
    '''
    Fungsi ini ditujukan untuk menghitung kuadrat angka yang dimasukkan pengguna dengan rumus x^2.

    Argument x merupakan inputan angka berupa bilangan real.

    Contoh penggunaan:
      y = f(2)
      print(y)
      --------
      Output: 4
    '''
    return x**2

  ```

6. **WARNING**: Plagiarisme sekecil apapun dapat terdeteksi. Tugas ini akan diuji tingkat plagiarismenya dengan software khusus.

---

## Assignment Submission

- Simpan assignment pada Graded Challenge 1 ini dengan nama `<nama-student>_app.py` (file app), `<nama-student>_test.py` (file unit test), dan  `<nama-student>_flowchart.jpg` (gambar flowchart - extension bebas). Misal `fahmi-iman_app.py`, `fahmi-iman_test.py` dan `fahmi-iman_flowchart.jpg` (**Maksimal nama dua suku kata**).
- Push file Assigment yang telah dibuat ke repository Github Classroom masing-masing student.

---

## Assignment Objectives

*Graded Challenge 1* ini dibuat guna mengevaluasi konsep konsep Conditionals, Loops, Functions, Object-Oriented Programming, Python Unit Test, dan Computational Thinking sebagai berikut:

- Mampu menerapkan conditional if pada sebuah kasus
- Mampu menerapkan _while_ loop
- Mampu membuat object menggunakan class
- Mampu membuat method pada object dengan function
- Mampu melakukan pengujian code yang sudah dibuat dengan `unittest`
- Mampu menggambarkan flowchart

---

## Assignment Instructions and Cases

**Case**

Kamu adalah seorang Python developer di perusahaan retail. Kamu diminta untuk membuat program `shopping cart` sederhana yang memungkinkan user untuk menambah, menghapus, dan melihat barang di keranjang belanja (cart) mereka. Tiap barang memiliki informasi nama barang dan harganya. User juga bisa melihat total harga belanjanya.

**Requirements**

1. Buat flowchart yang menggambarkan alur algoritma dari program yang akan dibuat pada `<nama-student>_app.py` berupa file gambar. Flowchart berdasarkan kasus dan requirement yang diminta. Ini berguna untuk memudahkan dalam membuat code. **Buat flowchart dengan Miro**.

2. Buat kelas bernama `CartItem` sebagai `class` untuk sebuah objek barang dengan atribut nama dan harga.

3. Buat kelas bernama `ShoopingCart` sebagai `class` untuk sebuah objek keranjang belanja tiap orang. Kelas ini harus berisikan method untuk menambah barang, menghapus barang, menghitung total belanja, dan menjalankan user-interface aplikasi. Serta terdapat atribut items yang berupa list yang berisikan objek barang-barang dalam keranjang belanja.

  
  > _Khusus untuk method untuk menghitung total harga belanja, jangan menerapkan `print` di dalam code function untuk mengeluarkan total belanja. Berikan `return` berupa nilai total belanja yang nantinya akan ditampilkan ke interface dengan `print` yang dipanggil pada menu utama, bukan di dalam function untuk memudahkan unit test._
  

4. Program harus berupa menu-based interface dimana user akan berinteraksi dengan shopping cart nya.

  Pilihan menu harus terdapat:
  1. Menambah Barang
  2. Hapus Barang
  3. Tampilkan Barang di Keranjang
  4. Lihat Total Belanja
  5. Exit

  Jika terdapat kesalahan input menu ataupun input nilai yang diminta maka akan muncul pesan error.

5. Gunakan `While Loop` dan `Conditional If` supaya user dapat terus berinteraksi dengan program sampai user pilih menu exit.

6. Lakukan unit test untuk kelas `ShoppingCart` menggunakan `unittest`. Pengujian dilakukan dengan skenario yang bervariasi antara lain:
  - Penambahan barang ke cart
  - Penghapusan barang dari cart
  - Perhitungan total belanja

  Pengujian dengan unit test ini bertujuan untuk menguji apakah program berjalan sesuai dengan yang diharapkan.

7. Tahapan nomor 2 - 5 dikerjakan pada file `<nama-student>_app.py`, sedangkan nomor 6 pada file `<nama-student>_test.py`.

8. Running program `<nama-student>_app.py` dan `<nama-student>_test.py` satu per satu di `Anaconda Prompt` atau `Terminal MacOS/Linux` serta screenshot running program dan hasilnya untuk masing-masing file. Satu file gambar untuk satu running file `.py`.



**Contoh program interface:**

```
Selamat Datang di Keranjang Belanja Toko Makmur!

Menu:
1. Menambah Barang
2. Hapus Barang
3. Tampilkan Barang di Keranjang
4. Lihat Total Belanja
5. Exit

Pilihan: 1
Masukan nama barang: Apel
Masukan harga: 3400
Barang "Apel" berhasil dimasukkan ke keranjang.

Menu:
1. Menambah Barang
2. Hapus Barang
3. Tampilkan Barang di Keranjang
4. Lihat Total Belanja
5. Exit

Pilihan: 1
Masukan nama barang: Jeruk
Masukan harga: 2100
Barang "Jeruk" berhasil dimasukkan ke keranjang.

Menu:
1. Menambah Barang
2. Hapus Barang
3. Tampilkan Barang di Keranjang
4. Lihat Total Belanja
5. Exit

Pilihan: 3
Barang di Keranjang:
0. Apel - Rp 3400.00
1. Jeruk - Rp 2100.00

Menu:
1. Menambah Barang
2. Hapus Barang
3. Tampilkan Barang di Keranjang
4. Lihat Total Belanja
5. Exit

Pilihan: tiga
Pilihannya salah. Coba lagi ya.

Menu:
1. Menambah Barang
2. Hapus Barang
3. Tampilkan Barang di Keranjang
4. Lihat Total Belanja
5. Exit

Pilihan: 4
Total belanja: Rp 5500.00

Menu:
1. Menambah Barang
2. Hapus Barang
3. Tampilkan Barang di Keranjang
4. Lihat Total Belanja
5. Exit

Pilihan: 2
Masukan nama barang yang ingin dihapus: Apel
Barang "Apel" berhasil dihapus di keranjang belanja.

Menu:
1. Menambah Barang
2. Hapus Barang
3. Tampilkan Barang di Keranjang
4. Lihat Total Belanja
5. Exit

Sampai Jumpa! Terima kasih sudah belanja di Toko Makmur.

```


---

## Assignment Rubrics

<img src="https://raw.githubusercontent.com/FTDS-learning-materials/phase-0/main/img/P0G1_Rubric.png"></img>

---
## Score Reduction

Jika Student terlambat mengumpulkan dengan waktu yang ditentukan, maka live code akan diberi poin nol.

---
