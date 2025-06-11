import pandas as pd

def read_CSV(file):
    try:
        read_csv = pd.read_csv(file)
        data_transaction = read_csv.to_dict(orient="records")
    except FileNotFoundError:
        data_transaction = []
    return data_transaction

def read_EXCEL(file):
    try:
        read_xls = pd.read_excel(file)
        data_transaction = read_xls.to_dict(orient="records")
    except FileNotFoundError:
        data_transaction = []
    return data_transaction

