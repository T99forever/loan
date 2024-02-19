import pandas as pd

df = pd.read_csv("data\\df_initial.csv", 
               sep = ";", 
               index_col = 0)

print(df.head())

df_loan = df.query("Loan_Status == False")
#print(df_loan.head())

df_eduself = df.query("Education == False and Self_Employed == False")
#print(df_eduself.head())

df_largeloan = df.query("LoanAmount > 500")
#print(df_largeloan.head())

df_neet = df.query("Education == False and ApplicantIncome < 2000")
#print(df_neet.head())

df_credit = df.query("Loan_Status == False")
print(df_credit.head())

df_credit.to_csv("data\\df_credit.csv",
                 sep = ";")