import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def data_read():
    df = pd.read_csv('/Users/manojkumar/Documents/repository/python-programming-workbench/kidney_disease.csv')
    # sample data
    print(df.head())
    np.ndarray()
    print(df.duplicated().sum())
    print(df.columns)
    print(f'pcv median {df['pcv'].mode()[0]}')
    print(f'wc mode {df['wc'].mode()}')
    df.drop()
    print(df.info())
   # print_all_col_data(df)
    df['su'] = df['su'].fillna(df['su'].median())
    #check_out_liear_and_correct(df)





def check_out_liear_and_correct(df):
    plt.figure(figsize=(10,8))
    sns.boxplot(data=df)
    plt.xlabel('coloum')
    plt.ylabel('values')
    plt.show()





def print_all_col_data(df):
    # Finding the unique values in the given columns
    for i in df.columns:
        print("***************",i,"********************")
        print()
        print(set(df[i]))
        print()

def main():
    data_read()


if __name__=='__main__':
    main()