import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('datasets/full_data.csv')

# Plot 1: Jointplot with hex bins
with sns.axes_style('white'):
    sns.jointplot(x="age", y="bmi", data=data, kind='hex')
    plt.show()

# Plot 2: Histogram of age
sns.set_theme(style='darkgrid')
sns.histplot(data.age)
plt.show()

# Plot 3: Countplot of a categorical variable (assuming the 6th column is categorical)
plt.figure(figsize=(8, 6))
sns.countplot(x=data.iloc[:, 5])
plt.show()
