# Laporan Proyek Mahine Leraning - Adam Pamungkas
## Domain Proyek

seorang karyawan merupakan salah satu faktor yang menentukan maju atau tidaknya suatu perusahaan, banyaknya pelamar pekerjaan membuat Human Resource (HR) menjadi salah satu pekerjaan yang harus pandai dalam memilih seseorang yang tepat.  

Budaya kerja merupakan suatu pembeda atau ciri khas antara perusahaan satu dengan yang lainnya, bahkan banyak orang yang mencari pekerjaan dilihat dari budaya kerja yang diterapkan. semakin baik budaya kerja suatu perusahaan, maka sekamin produktif karyawannya. ada beberapa karyawan yang juga tidak dapat mengikuti budaya bekerja yang berada di beberapa perusahaan.

tujuan dalam menganalisis karyawan adalah untuk mengembangkan model prediksi yang dapat mengidentifikasi kebiasaan karyawan yang dapat membuat seorang karyawan memutuskan untuk keluar dari perusahaan.

maka pembuatan model prediksi analysis karyawan diharapkan dapat meminimalisir karyawan yang keluar dari prilaku dan kebiasaan seorang karyawan

# Busness Understanding

## Problem Statement
- Bagaimana cara menentukan alogritma Machine Learning yang baik untuk mengklafisikasi permasalahan karyawan?
- Bagaimana penggunaan metode K-Nearest Neighbors, Random Forest, dan Logistic Regression?

## Goals
- Mengetahui algoritma machine learning yang baik dalam mengklasifikasi permasalahan karyawan
- Menganalisis evaluasi metode K-Nearest Neighbors, Random Forest, dan Logistic Regression.

# Data Understanding
Data yang digunakan adalah data yang berasal dari kaggle [<em> Hr Analytics Job Prediction</em>](https://www.kaggle.com/datasets/mfaisalqureshi/hr-analytics-and-job-prediction)
, data ini berisikan dataset berisi transaksi yang dilakukan oleh HR Department to predict employees Behaviour pada tahun 2021.
### Variable analysis karyawan
* Left adalah target data yang merupakan tipe variabel Boolean dan hanya memiliki nilai yang mungkin: 0 berarti karyawan masih bekerja dengan perusahaan, 1 – karyawan keluar dari perusahaan.
* satisfaction_level - Tingkat kepuasan kerja yang dilaporkan karyawan dalam skala dari 0 hingga 1
* last_evaluation - Skor tinjauan kinerja terakhir karyawan juga diskalakan dari 0 hingga 1
* number_project - Jumlah kontribusi karyawan proyek
* average_monthly_hours - Jumlah rata-rata jam kerja karyawan per bulan
* time_spend_company - Berapa lama karyawan telah bekerja di perusahaan (tahun)
* Work_accident - Apakah karyawan mengalami kecelakaan saat bekerja atau tidak (0 – tidak, 1- ya)
* promotion_last_5years - Apakah karyawan dipromosikan atau tidak dalam 5 tahun terakhir (0 – tidak, 1- ya)
* Department - Departemen karyawan (nilai kategoris)
* Salary - Gaji karyawan (categorical values – high, medium, low)

### Overview Data :
    
    - Datasets Name : Hr Department to Predict Employees Behaviour 2021
    - Overall Columns:
        - Valid : 14999 
        - MissMatched : 0
        - Missing : 0
    - Source : U.S. Energy Information Administration (Jan 2021)
    - Link : https://www.kaggle.com/datasets/mfaisalqureshi/hr-analytics-and-job-prediction
    - License : CC0: Public Domain

### Data Preparation
Pertama muat data csv menggunakan fungsi pandas, masukan dimana lokasi file csv berada. Dari datasets yang digunakan ini terdapat jumlah data pada table sebanyak 10 kolom dan 14999 baris.

Tabel 1. _Table Data_
|Index|satisfaction_level|last_evaluation|number_project|average_montly_hours  |time_spend_company  | Work_accident  |left  |	promotion_last_5years|	Department|	salary|
|-----|------------------|---------------|--------------|----------------------|--------------------|----------------|------|------------------------|------------|-------|
0     |0.38              |	0.53         |2             |	157                |	3               |	0            |	1   |	0                    |	sales     |	low   |
1     |0.80              |	0.86         |5             |	262                |	6               |	0            |	1   |	0                    |	sales     |	medium|
2     |0.11              |	0.88         |7             |	272                |	4               |	0            |	1   |	0                    |	sales     |	medium|
3     |0.72              |	0.87         |5             |	223                |	5               |	0            |	1   |	0                    |	sales     |	low   |
4     |0.37              |	0.52         |2             |	159                |	3               |	0            |	1   |	0                    |	sales     |	low   |
....  |...               |	...          |...           |	...                |	...             |	...          |	... |	...                  |	...       | ...   |
14994 |0.40              |	0.57         |2             |	151                |	3               |	0            |	  1 |	0                    |	support   |	low   |
14995 |0.37              |	0.48         |2             |	160                |	3               |	0            |	  1 |	0                    |	support   |	low   |
14996 |0.37              |	0.53         |2             |	143                |	3               |	0            |	  1 |	0                    |	support   |	low   |
14997 |0.11              |	0.96         |6             |	280                |	4               |	0            |	  1 |	0                    |	support   |	low   |
14998 |0.37              |	0.52         |2             |	158                |	3               |	0            |	  1 |	0                    |	support   |	low   |

dataset memiliki 8 fiture numerik yang mempunyai type data _integer_ dan _float_ dan 2 fiture data kategori

### Analisis Predictive
Tabel 2. _Describe statistics_
|Parameters|satisfactio    n_level | last_evaluation| number_project | average_montly_hours | time_spend_company| work_accident| left         |promotion_last_5years |
|----------|-------------------|----------------|----------------|----------------------|-------------------|--------------|--------------|----------------------|
count      |14999.000000	   |14999.000000	|14999.000000	 |14999.000000	        |14999.000000	    |14999.000000  |14999.000000  |14999.000000          |
mean	   |0.612834	       |0.716102	    |3.803054	     |201.050337	        |3.498233        	|0.144610	   |0.238083	  |0.021268              |
std	       |0.248631	       |0.171169	    |1.232592	     |49.943099	            |1.460136	        |0.351719	   |0.425924	  |0.144281              |
min	       |0.090000	       |0.360000	    |2.000000	     |96.000000	            |2.000000	        |0.000000	   |0.000000	  |0.000000              |
25%	       |0.440000	       |0.560000	    |3.000000	     |156.000000	        |3.000000	        |0.000000	   |0.000000	  |0.000000              |
50%	       |0.640000	       |0.720000	    |4.000000	     |200.000000	        |3.000000	        |0.000000	   |0.000000	  |0.000000              |
75%	       |0.820000	       |0.870000	    |5.000000	     |245.000000	        |4.000000	        |0.000000	   |0.000000	  |0.000000              |
max	       |1.000000	       |1.000000	    |7.000000	     |310.000000	        |10.000000	        |1.000000	   |1.000000	  |1.000000              |

* hasil analisis:
  - data terdiri dari 14999 baris dan 10 colom
  - orang yang mengerajan projek paling sedikit 2 dan paling banyak 7
  - rata-rata orang yang mengerjakan projek sebanyak 4 projek
  - kecelakaan dalam bekerja hampir tidak pernah terjadi
  - jumlah waktu bekerja dari 2 sampai 10 jam
 
Untuk train test tplit kita bisa menggunakan potongan kode berikut:

```
from sklearn.model_selection import train_test_split

x = hr_dummy.drop(columns=['left'])
y = hr_dummy.left

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state= 50)
```

### Visualisasi
Gambar 1 adalah grafik distribusi antara _statisfaction level_ dan _salary_ terhadap _left_
![image](https://github.com/sharung/Predictive_Analysis_ML_Terapan/assets/76006507/f6f13265-12f3-483e-bf6d-35cb2cc18930)
gambar 1 _grafik distribusi_

    - satisfaction by salary untuk menampilkan distribusi antara satisfaction level dan salary
    - salary history membuat perbandingan antara pegawai yang bertahan dan tidak

Gambar 2 adalah _salary_ histogram dari data karyawan left
![image](https://github.com/sharung/Predictive_Analysis_ML_Terapan/assets/76006507/dc5e07a6-8f64-456c-8058-63c033664c3f)
Gambar 2 _salary histogram_

dari gambar di atas dapat dilihat bahwa "last_evaluation" tidak ada korelasi dengan left


# Modeling
Model yang akan digunakan ada 3 algoritma yaitu K-Nearest Neighbors, Random Forest dan Logistic Regression. 3 algoritma tersebut akan dievaluasi performa di tahap evaluation untuk menentukan model terbaik.
   
    
### Models
1. KNN
    Algoritma*K-Nearest Neighbor* adalah metode*klasifikasi* terhadap suatu dataset berdasarkan jarak data pembelajaran (*neighbor*) terdekat. Jauh 
maupun dekatnya data pembelajaran (*neighbor*) tersebut dihitung dengan jarak Euclidean. [2]
    * Kelebihan KNN
        * Mudah diterapkan
        * Mudah beradaptasi
        * Memiliki sedikit hyperparameter
    * Kekurangan KNN
        * Tidak berfungsi dengan baik pada dataset berukuran besar
        * Kurang cocok untuk dimensi tinggi
        * Perlu penskalaan fitur
        * Sensitif terhadap noise data, missing values dan outliers
    * Parameter
        n_neighbors = 5
        
              
2. Random Forest  adalah algoritma machine learning yang menggabungkan keluaran dari beberapa decision tree untuk mencapai satu hasil. [1]
    * Kelebihan Algoritma Random Forest
        - Kuat terhadap data outlier (pencilan data).
        - Bekerja dengan baik dengan data non-linear.
        - Risiko overfitting lebih rendah.
        - Berjalan secara efisien pada kumpulan data yang besar.
        - Akurasi yang lebih baik daripada algoritma klasifikasi lainnya.
   * Kekurangan Algoritma Random Forest
        - Random Forest cenderung bias saat berhadapan dengan variabel kategorikal.
        - Waktu komputasi pada dataset berskala besar relatif lambat
        - Tidak cocok untuk metode linier dengan banyak fitur sparse
   * Parameter
        * n_estimator = 100
        * max_depth = Infinite / None (node diperluas sampai semua semua daun kurang dari sampel)
        * n_jobs = -1
    * Algoritma Random Forest:
      ![image](https://github.com/sharung/Predictive_Analysis_ML_Terapan/assets/76006507/7f561ecb-e0bd-4a41-a91d-fcf2138508c5)

4. Logistic Regression

### Hasil Model

Table 3. Hasil Model
| Models             | Train Accuracy | Test Accuracy      |
| ------------------ | -------------- | -------------      |
| KNN                |0.9734260405752929|0.9611111111111111|
| Random Forest      |0.9994285170016192|0.9902222222222222|
| Logistic Regression|0.7882655490999143|0.7944444444444444|



# Evaluation
Model yang digunakan adalah model regressi, sesuai penjelasan diatas saya akan menggunakan beberapa metric untuk evaluasi, berikut adalah list nya:

1. Mean Squared Error (MSE)
2. Root Mean Squared Error (RMSE)
3. Confussion Matrix
    Menghitung hasil kinerja klasifikasi dari masing-masing pengujian metode dengan Confusion Matrix untuk memperoleh hasil Accuracy, Precision, dan Recall. Confusion Matrixidigunakan untuk imenganalisisiseberapa baik classifier mengenali data kelas yang berbeda[7]

## Mean Squared Error (MSE)
## Root Mean Squared Error (RMSE)
## Confussion Matrix


# Final Report

|Index|	Model_Name|	mse     |  	r2        |	rmse     |
|-----|-----------|---------|-------------|----------|
0     |	knn	      |0.0388889|	0.7855660 |	0.1972027|
1     |	RF	      |0.0097778|	0.9460852 |	0.0988826|
2     |	LR	      |0.2160000|	-0.1910276|	0.4647580|

# Daftar Refrensi
### Referensi
[1] Umri Erdiansyah, Ahmadi Irmansyah Lubis, Kamil Erwansyah. 2022. [Komparasi Metode K-Nearest Neighbor dan Random Forest Dalam Prediksi Akurasi Klasifikasi Pengobatan Penyakit Kutil](http://ejurnal.stmik-budidarma.ac.id/index.php/mib/article/download/3373/2390) . JURNAL MEDIA INFORMATIKA BUDIDARMA. 6O(1):208-214 

[2] 

[3]

[4]
