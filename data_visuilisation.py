#steps involve in data visuialization

#1 import liberary
import seaborn as sns
import matplotlib.pyplot as plt

#2 set a theme
sns.set_theme(style="ticks",color_codes=True)
#3 import data set ypu can also import your own data

kasti=sns.load_dataset("titanic")

#4  plot basic graph

p1=sns.countplot(x="sex",data=kasti,)
#p1.set_title("plot for counting")
plt.show()
