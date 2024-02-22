import numpy as np
import pandas as pd

df_loan = pd.read_csv("data\\df_initial.csv", 
                        sep = ";", 
                        index_col = 0,
                        dtype = {"Education" : bool, 
                                 "LoanAmount" : int, 
                                 "Loan_Amount_Term" : int, 
                                 "Loan_Status" : bool})

df_initial = pd.read_csv("data\\df_initial.csv", 
                         sep = ";", 
                         index_col = 0,
                        dtype = {"Education" : bool, 
                                 "LoanAmount" : int, 
                                 "Loan_Amount_Term" : int, 
                                 "Loan_Status" : bool})

print(df_initial.info())

print(df_initial.groupby(["Loan_Status"]).mean(numeric_only = True))
print(df_initial.groupby(["Loan_Status"]).min(numeric_only = True))
print(df_initial.groupby(["Loan_Status"]).value_counts().index[0])
