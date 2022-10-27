# /usr/bin/env python3
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', 8)

general = pd.read_csv('test/general.csv')
prenatal = pd.read_csv('test/prenatal.csv', header=0, names=general.columns)
sports = pd.read_csv('test/sports.csv', header=0, names=general.columns)

df = pd.concat([general, prenatal, sports], ignore_index=True)
df.drop(columns=['Unnamed: 0'], inplace=True)
df['gender'].replace(['female', 'woman'], 'f', inplace=True)
df['gender'].replace(['male', 'man'], 'm', inplace=True)
df.loc[df.hospital == 'prenatal', 'gender'] = 'f'
df.dropna(how='all', inplace=True)
df.fillna(0, inplace=True)

ages = df['age']
ages_bin = [0, 15, 35, 55, 70]
plt.hist(ages, color='green', bins=ages_bin)
plt.title('Patient Ages')
plt.ylabel('Number of Patients')
plt.xlabel('Age')
plt.show()

diagnoses = df.groupby(['diagnosis'])['diagnosis'].count()
plt.pie(diagnoses, labels=list(diagnoses.index), autopct='%.2f%%')
plt.title('Patient Diagnoses')
plt.show()

sns.violinplot(data=df, x='hospital', y='height', inner='quart', linewidth=1)
plt.show()
# most_pts = df.hospital.mode()[0]
# stomach_pts_ratio = round(df.loc[df.hospital == 'general', 'diagnosis'].value_counts()['stomach']
#                           / df.hospital.value_counts()['general'], 3)
# dislocation_pts_ratio = round(df.loc[df.hospital == 'sports', 'diagnosis'].value_counts()['dislocation']
#                               / df.hospital.value_counts()['sports'], 3)
# median_diff = round(df.loc[df.hospital == 'general', 'age'].median() - df.loc[df.hospital == 'sports', 'age'].median())
# df_group = (df.groupby('hospital')['blood_test'].value_counts().idxmax()[0])
# highest_blood = df.loc[df.hospital == df_group, 'blood_test'].value_counts()['t']
# print(f'The answer to the 1st question is {most_pts}')
# print(f'The answer to the 2nd question is {stomach_pts_ratio}')
# print(f'The answer to the 3rd question is {dislocation_pts_ratio}')
# print(f'The answer to the 4th question is {median_diff}')
# print(f'The answer to the 5th question is {df_group}, {highest_blood} blood tests')

ages_df = pd.cut(x=df['age'], bins=[0, 15, 35, 55, 70])
largest_age_group = ages_df.value_counts().idxmax()
print('The answer to the 1st question: 15-35 ')
print('The answer to the 2nd question: pregnancy')
print("The answer to the 3rd question: It's because... There is a greater gap in values because the sports dataframe "
      "measured height in feet rather than meters.")
