import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("planets")
df = df.dropna()

print("First 5 rows:")
print(df.head)
print()
print(df.info)
print()
print("Mass:", df["mass"].unique())
print("Year:", df["year"].unique())

sns.histplot(data=df, x="orbital_period", bins=8, color="aqua")
plt.title("Orbital Period of Planets")
plt.xlabel("Orbital Period")
plt.ylabel("Planets")
plt.show()

sns.kdeplot(data=df, x="distance", fill=True)
plt.title("Shape of the Distance Data (KDE)")
plt.xlabel("distance from the Sun in million kilometres")
plt.show()

sns.histplot(data=df, x="distance", kde=True, color="coral")
plt.title("Shape of the Distance Data - Histogram with KDE Curve")
plt.xlabel("distance from the Sun in million kilometres")
plt.ylabel("Frequency")
plt.show()

sns.scatterplot(data=df, x="distance", y="orbital_period", hue="method")
plt.title("Relationship Between Distance and Orbital Period")
plt.xlabel("Distance from the Sun")
plt.ylabel("Orbital Period")
plt.show()

corr = df.corr(numeric_only=True)
print("Correlation table:")
print(corr)
print()

sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap of Planetary Features")
plt.show()

