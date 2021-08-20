import os
import yaml
import pandas as pd


cfg = yaml.load(
    open("D:\MIMIC\python_code\config.yaml", "r"),
    Loader=yaml.FullLoader
)
MIMIC3_PATH = cfg['mimic3_path']
DIC_PATH = cfg['dic_path']


def calculate_nan(df):
    return df.isnull().sum()


def df_from_csv(path, header=0, index_col=0):
    return pd.read_csv(path, header=header, index_col=index_col)


def walk_file(mimic3_path):
    for path, dir, file in os.walk(mimic3_path):
        for file_name in file:
            print(file_name)


def j_path(mimi3_file):
    return os.path.join(MIMIC3_PATH, mimi3_file)


def j_dic_path(dic_file):
    return os.path.join(DIC_PATH, dic_file)
