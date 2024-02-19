import numpy as np
import pandas as pd

df = pd.read_csv("data\\train.csv",
                 sep = ",",
                 index_col = 0)

print(df.head(n = 10))

df_original = df.copy()

def value_checker(column, df = df):
    return df[column].value_counts().sort_values(ascending = False)
for column in df:
    print()
    if df[column].dtype == "object":
        print(value_checker(column))
    else:
        pass

df.loc[df["Married"] == "Yes", "Married"] = True
df.loc[df["Married"] == "No", "Married"] = False

df.loc[df["Education"] == "Graduate", "Education"] = True
df.loc[df["Education"] == "Not Graduate", "Education"] = False

df.loc[df["Self_Employed"] == "Yes", "Self_Employed"] = True
df.loc[df["Self_Employed"] == "No", "Self_Employed"] = False

df.loc[df["CoapplicantIncome"] == 0.0, "CoapplicantIncome"] = np.nan

df.loc[df["Credit_History"] == 1.0, "Credit_History"] = True
df.loc[df["Credit_History"] == 0.0, "Credit_History"] = False

df.loc[df["Loan_Status"] == "Y", "Loan_Status"] = True
df.loc[df["Loan_Status"] == "N", "Loan_Status"] = False

print(df.info(show_counts = True))

def value_checker(column, df = df):
    return df[column].value_counts().sort_values(ascending = False)
for column in df:
    print()
    if df[column].dtype == "object":
        print(value_checker(column))
    else:
        pass

df = df.dropna(subset = ["LoanAmount", "Loan_Amount_Term"], how = "any")

df = df[["Gender", "Education", "Self_Employed", "Credit_History", "Married", "Dependents", "Property_Area", "ApplicantIncome", "CoapplicantIncome", "LoanAmount", "Loan_Amount_Term", "Loan_Status"]]

print(df.head(n = 10), df.shape)

df.to_csv("data\\df_initial.csv",
          sep = ";")