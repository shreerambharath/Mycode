#import packages
import pandas as pd
def create_dataframe():
    odd=pd.Series(list(range(0,100,2)))
    even=pd.Series(list(range(1,101,2)))
    result=pd.DataFrame({'Odd': odd, 'Even': even,'Sum': odd+even})
    #write to result.csv
    #return the dataframe
    return result
