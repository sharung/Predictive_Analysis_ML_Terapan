# -*- coding: utf-8 -*-
"""predictiv_analysis_job_prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1unqZKS07YB8U6KBK5nzJ7aGgi3-GBGCi

IMPORT LIBRARY
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from statsmodels.stats.outliers_influence import variance_inflation_factor

"""IMPORT DATASET"""

! pip install -q kaggle
! mkdir ~/.kaggle

# Menyalin berkas kaggle.json pada direktori aktif saat ini ke folder .kaggle
! cp kaggle.json ~/.kaggle/
! chmod 600 ~/.kaggle/kaggle.json

! kaggle datasets download -d mfaisalqureshi/hr-analytics-and-job-prediction

# Mengekstrak berkas zip ke direktori aktif saat ini
!unzip /content/hr-analytics-and-job-prediction.zip

"""# EXPLORATORY DATA ANALISIS"""

df = pd.read_csv('HR_comma_sep.csv')

"""Dataset
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
"""

df

df.info()

df.columns = df.columns.str.lower()

df.describe()

# cek missing value
df.isnull().sum()

# mengecek jumlah karyawan yang keluar
left = df[df.left == 1]
left.shape

# mengecek jumlah karyawan yang belum keluar
retained = df[df.left==0]
retained.shape

corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, fmt='.1f', cmap='crest')
plt.show()

"""hanya ada 8 variable karena 2 variable lagi yaitu salary dan department adalah category

kesimpulan:
* terdapat korelasi antara number_of_projects, monthly_hours dan evaluation_secores
* tidak ada hubungan signifikan yang terjadi kepada statisfaction_level dengan time_spend_company
* kepergian pegawai memiliki hubungan yang negatif terhadap satisfaction_level dan memiliki hubungan yang baik pada tunere (semakin lama bekerja semakin kurang keinginan karyawan untuk keluar)
"""

sns.pairplot(df)

"""korelasi antara satisfaction level dan salary"""

# set figure and axes
fig, ax = plt.subplots(1, 2, figsize=(22,8))
# membuat boxplot untuk menampilkan distribusi antara satisfaction level dan salary
sns.boxplot(data=df, x='satisfaction_level', y='salary', hue='left', orient='h', ax=ax[0])
ax[0].invert_yaxis()
ax[0].set_title('Satisfaction by salary level', fontsize='14')

# membuat perbandingan antara pegawai yang bertahan dan tidak
sns.histplot(data=df, x='salary', hue='left', multiple='dodge', shrink=1, ax=ax[1])
ax[1].set_title('Salary histogram', fontsize=14)
plt.show()

"""kebanyakan karyawan yang keluar berada pada pembayaran low dan medium"""

pd.crosstab(df.department,df.left).plot(kind='bar')

"""### grafik plot chart untuk left(target)"""

plt.figure(figsize=(15, 6))
plt.plot(abs(corr['left']).sort_values()[:-1].index, abs(corr['left']).sort_values()[:-1], color='green')
plt.grid()
plt.show()

"""terlihat bahwa "last_evaluation" tidak memiliki korelasi terhadap left"""

hr_left = df.drop(columns=['last_evaluation', 'department'])
hr_left.info()

"""### mengubah data object menjadi numerik dengan menggunakan teknik one-hot-encoding"""

hr_dummy = pd.get_dummies(hr_left, columns=['salary'])
hr_dummy

"""### Train Test Split"""

from sklearn.model_selection import train_test_split

x = hr_dummy.drop(columns=['left'])
y = hr_dummy.left

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state= 210)
print(f'Total # of sample in train dataset: {len(x_train)}')
print(f'Total # of sample in test dataset: {len(x_test)}')

x_train.head()

"""# models

## Scaler
"""

from sklearn.preprocessing import StandardScaler

x = hr_dummy.drop(columns=['left'])
y = hr_dummy.left

scaler = StandardScaler()
x = scaler.fit_transform(x)
x

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state= 150)

"""## KNN"""

from sklearn.neighbors import KNeighborsClassifier


# K-Nearest Neighbors (KNN)
knn = KNeighborsClassifier(n_neighbors=7)
knn.fit(x_train, y_train)
y_pred = knn.predict(x_test)

train_accuracy_knn = knn.score(x_train, y_train)
test_accuracy_knn = accuracy_score(y_test, y_pred)

print("K-Nearest Neighbors (KNN):")
print("Train Accuracy:", train_accuracy_knn)
print("Test Accuracy:", test_accuracy_knn)
print()
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

"""## Random Forest"""

from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier(random_state=123)
rf.fit(x_train, y_train)
y_pred_rf = rf.predict(x_test)

train_accuracy_rf = rf.score(x_train, y_train)
test_accuracy_rf = accuracy_score(y_test, y_pred_rf)

print("Random Forest:")
print("Train Accuracy:", train_accuracy_rf)
print("Test Accuracy:", test_accuracy_rf)
print()
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred_rf))

"""# Evaluation"""

from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
# KNN
mse = mean_squared_error(y_test, y_pred)
rmse = mean_squared_error(y_test, y_pred, squared=False)
r2 = r2_score(y_test, y_pred)

# RandomForest
mse_rf = mean_squared_error(y_test, y_pred_rf)
rmse_rf = mean_squared_error(y_test, y_pred_rf, squared=False)
r2_rf = r2_score(y_test, y_pred_rf)

print("K-Nearest Neighbors")
print("MSE:", mse)
print("RMSE:", rmse)
print("R2 Score:", r2)
print()
print("Random Forest")
print("MSE:", mse_rf)
print("RMSE:", rmse_rf)
print("R2 Score:", r2_rf)

final_report = {'Model_Name': [], 'mse': [], 'r2': []}
pred = knn.predict(x_test)
mse = mean_squared_error(y_true=y_test, y_pred=pred)
r2 = r2_score(y_test, pred)
final_report['Model_Name'].append('knn')
final_report['mse'].append(mse)
final_report['r2'].append(r2)

pred = rf.predict(x_test)
mse = mean_squared_error(y_true=y_test, y_pred=pred)
r2 = r2_score(y_test, pred)
final_report['Model_Name'].append('RF')
final_report['mse'].append(mse)
final_report['r2'].append(r2)

pd.options.display.float_format = '{:.7f}'.format

final_report = pd.DataFrame.from_dict(final_report)
final_report