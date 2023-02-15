import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(styles"ticks",color_codes=true)
titanic=sns.load_dataset("titanic")
sns.catplot(x="sex",y="syrvived",kind="bar",data=titanic)
plt.show()