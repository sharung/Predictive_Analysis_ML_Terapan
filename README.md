# Laporan Proyek Mahine Leraning - Adam Pamungkas
## Domain Proyek

seorang karyawan merupakan salah satu faktor yang menentukan maju atau tidaknya suatu perusahaan, banyaknya pelamar pekerjaan membuat Human Resource (HR) menjadi salah satu pekerjaan yang harus pandai dalam memilih seseorang yang tepat.  

Budaya kerja merupakan suatu pembeda atau ciri khas antara perusahaan satu dengan yang lainnya, bahkan banyak orang yang mencari pekerjaan dilihat dari budaya kerja yang diterapkan. semakin baik budaya kerja suatu perusahaan, maka sekamin produktif karyawannya. ada beberapa karyawan yang juga tidak dapat mengikuti budaya bekerja yang berada di beberapa perusahaan.

tujuan dalam menganalisis karyawan adalah untuk mengembangkan model prediksi yang dapat mengidentifikasi kebiasaan karyawan yang dapat membuat seorang karyawan memutuskan untuk keluar dari perusahaan.

maka pembuatan model prediksi analysis karyawan diharapkan dapat meminimalisir karyawan yang keluar dari prilaku dan kebiasaan seorang karyawan

# Busness Understanding

## Problem Statement
- menyiapkan data sehingga data siap untuk di latih oleh model machine learning?
- Bagaimana cara menentukan alogritma Machine Learning yang baik untuk mengklafisikasi permasalahan karyawan?
- Bagaimana penggunaan metode K-Nearest Neighbors, Random Forest, dan Boosting Algorithm?

## Goals
- Mengetahui algoritma machine learning yang baik dalam mengklasifikasi permasalahan karyawan
- Menganalisis evaluasi metode K-Nearest Neighbors, Random Forest, dan Boosting Algorithm.

# Data Understanding
Data yang digunakan adalah data yang berasal dari kaggle [<em> Hr Analytics Job Prediction</em>](https://www.kaggle.com/datasets/mfaisalqureshi/hr-analytics-and-job-prediction)
, data ini berisikan dataset berisi transaksi yang dilakukan oleh HR Department to predict employees Behaviour pada tahun 2021.
## Variable analysis karyawan
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

Overview Data :
    
    - Datasets Name : Hr Department to Predict Employees Behaviour 2021
    - Overall Columns:
        - Valid : 14999 
        - MissMatched : 0
        - Missing : 0
    - Source : U.S. Energy Information Administration (Jan 2021)
    - Link : https://www.kaggle.com/datasets/mfaisalqureshi/hr-analytics-and-job-prediction
    - License : CC0: Public Domain

# Predictiv analysis
|Parameters|satisfaction_level | last_evaluation| number_project | average_montly_hours | time_spend_company| work_accident| left|promotion_last_5years|
|----------|-------------------|----------------|----------------|----------------------|-------------------|--------------|---------------------------|
|count     |1361.000000        |1361.000000     |1361.000000     |1361.000000           |1361.000000        |1361.000000   |1361.000000                |
|mean      |2.285680           |2.234511        |2.396873        |2.225170   |2.178511   |2.329126   |2.382822   |
|std       |0.859028           |0.843815        |0.883311        |0.850143   |0.835549   |0.876739   |0.882107   |
|min       |0.949000           |0.926000        |1.039000        |0.907000   |0.885000   |0.974000   |1.008000   |
|25%       |1.461000           |1.433000        |1.550000        |1.421000   |1.393000   |1.489000   |1.517000   |
|50%       |2.326000           |2.251000        |2.458000        |2.237000   |2.175000   |2.367000   |2.481000   |
|75%       |2.903000           |2.825000        |3.060000        |2.828000   |2.765000   |2.976000   |3.033000   |
|max       |4.165000           |4.102000        |4.301000        |4.114000   |4.054000   |4.247000   |4.229000   |
