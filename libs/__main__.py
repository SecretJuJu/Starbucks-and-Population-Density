import pandas as pd
import numpy as np

def read_csv(file_path):
    return pd.read_csv(file_path,encoding='euc-kr')

def drop_column(df,column):
    df = df.drop(column)
    return df



def main():
    population_density_csv = "../data/population.csv"
    population_density = read_csv(population_density_csv)
    print(population_density)

if __name__ == "__main__":
    main()