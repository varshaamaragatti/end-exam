# -*- coding: utf-8 -*-
"""practial

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1G391KxufDYZTsAVs10CfE-AGI4yzOgDN
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

data=load_iris()
x=data.data
y=data.target

df=pd.DataFrame(data=x,columns=data.feature_names)
df['species']=pd.Categorical.from_codes(y,data.target_names)
print(df['species'])
print(df.describe())
print(df.shape)
print(df.info())
print(df['species'].value_counts())

print(df.isnull().sum())

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=4)
print(x_train)
print(y_train)

md=DecisionTreeClassifier(random_state=42)
md.fit(x_train,y_train)

yprd=md.predict(x_test)
yprd

plt.figure(figsize=(20,10))
tree.plot_tree(md,filled=True,feature_names=data.feature_names,class_names=data.target_names)
plt.title('Decision Tree visualization')
plt.show()

ac=accuracy_score(y_test,yprd)
ac