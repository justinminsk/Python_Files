import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('Titanic_train.csv')
data.head()
fare_less200 = data.Fare < 200
data_m = data[fare_less200]
fare_less50 = data.Fare < 50
data_n = data[fare_less50]
fare_less15 = data.Fare < 15
data_o = data[fare_less15]

if __name__ == '__main__':
    sns.violinplot(x=data.Fare)
    plt.show()
    sns.violinplot(x=data_m.Fare)
    plt.show()
    sns.violinplot(x=data_n.Fare, color='yellow')
    plt.show()
    sns.distplot(a=data_o.Fare)
    plt.show()