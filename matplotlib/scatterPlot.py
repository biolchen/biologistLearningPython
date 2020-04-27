## Import dataset
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sqlite3
conn=sqlite3.connect('//Volumes/x5/db/titanic.db')
midwest=pd.read_sql_query("SELECT * FROM matplotlib_midwest;",conn)

# http://liyangbit.com/pythonvisualization/matplotlib-top-50-visualizations/
# https://ggplot2.tidyverse.org/reference/midwest.html
#c=conn.cursor()
#renameTable = "ALTER TABLE test RENAME TO titanic_test;"
#renameTable = "ALTER TABLE train RENAME TO titanic_train;"
#c.execute(renameTable)
#pd.read_sql_query("SELECT * FROM test;",conn)
#midwest.to_sql("matplotlib_midwest", conn, if_exists = "replace", index = False)

# Create as many colors as there are unique midwest['category']
pd.options.display.max_rows=10
pd.options.display.max_columns=100
pd.options.display.width=1000
midwest

categories = np.unique(midwest['category'])
colors = [plt.cm.tab10(i/float(len(categories)-1)) for i in range(len(categories))]

# Draw Plot for Each Category
plt.figure(figsize=(16, 10), dpi= 80, facecolor='w', edgecolor='k')

for i, category in enumerate(categories):
    plt.scatter('area', 'poptotal',
                data=midwest.loc[midwest.category==category, :],
                s=60, cmap=colors[i], label=str(category))
    # "c=" 修改为 "cmap="，Python数据之道 备注
# Decorations
plt.gca().set(xlim=(0.0, 0.1), ylim=(0, 90000),
              xlabel='Area', ylabel='Population')

plt.xticks(fontsize=12); plt.yticks(fontsize=12)
plt.title("Scatterplot of Midwest Area vs Population", fontsize=22)
plt.legend(fontsize=12)
plt.savefig("/Users/liangchen/Downloads/test2.png")

##


