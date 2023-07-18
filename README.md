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
Data yang digunakan adalah data yang berasal dari kaggle, data ini berisikan dataset berisi transaksi yang dilakukan oleh HR Department to predict employees Behaviour pada tahun 2021

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
