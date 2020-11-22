import pandas as pd
from fuzzywuzzy import fuzz
import pickle
from solve import create_dataframe


def get_string():
    pickle_in = open("check.pickle","rb")
    ref_string = pickle.load(pickle_in)
    df = pd.read_csv('result.csv', index_col=0)
    actual_string = ""
    for index, row in df.iterrows():
        actual_string += str(row[0])+str(row[1])+str(row[2])
    return ref_string,actual_string

def test_answer():
    ref, real = get_string()
    ratio = fuzz.ratio(real, ref)
    assert ratio > 95

def test_column_name1():
    df = create_dataframe()
    names = list(df.columns.values)
    assert names == ['even','odd','sum'] 


