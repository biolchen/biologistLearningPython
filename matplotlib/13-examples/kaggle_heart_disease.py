import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import gridspec
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier #for the model
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz #plot tree
from sklearn.metrics import roc_curve, auc #for model evaluation
from sklearn.metrics import classification_report #for model evaluation
from sklearn.metrics import confusion_matrix #for model evaluation
from sklearn.model_selection import train_test_split #for data splitting
import os
os.chdir(os.path.dirname(__file__))

pd.options.mode.chained_assignment = None  #hide any pandas warnings


df = pd.read_csv("./heart.csv")
df.columns = ['age', 'sex', 'chest_pain_type', 'resting_blood_pressure', 'cholesterol', 'fasting_blood_sugar', 'rest_ecg', 'max_heart_rate_achieved',
       'exercise_induced_angina', 'st_depression', 'st_slope', 'num_major_vessels', 'thalassemia', 'target']

plt.figure()
gs = gridspec.GridSpec(3, 4)
ax1=plt.subplot(gs[0,:1])
ax2=plt.subplot(gs[0,1:2])
ax3=plt.subplot(gs[1,:])

sns.countplot(x="target", data=df, palette="bwr", ax=ax1)
pd.crosstab(df.sex,df.target).plot(kind="bar",color=['blue','#AA1111'], ax=ax2)
pd.crosstab(df.age,df.target).plot(kind="bar", color=['blue','#AA1111'], ax=ax3)
ax1.annotate("A", xy=(-0.4, 1), xycoords="axes fraction")
ax2.annotate("B", xy=(-0.4, 1), xycoords="axes fraction")
#ax2.legend(loc="upper right")
ax2.legend(loc='upper center', bbox_to_anchor=(1.45, 0.8), shadow=True, ncol=1)
ax3.annotate("C", xy=(-0.1, 1), xycoords="axes fraction")
ax3.set_xlabel('Age')
ax3.set_ylabel('Frequency')

plt.show()


