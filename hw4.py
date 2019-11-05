import pandas as pd
dr = pd.read_csv("Plaza_Coffee.txt", sep = ";", header = 0)
print(dr)

columns = ["Company","Payment"]
print( dr.groupby(columns)["Quantity"].sum() )

Companies = {"Deloite & Touche": {"Cash": 0, "Credit": 0},
 "EY": {"Cash": 0, "Credit": 0},
 "KPMG": {"Cash": 0, "Credit": 0},
 "PWC": {"Cash": 0, "Credit": 0}}

for i in range(len(dr)):
    Names, payment, quantity = dr.iloc[i]["Company"], dr.iloc[i]["Payment"], dr.iloc[i]["Quantity"]
    Companies[Names][payment] = quantity  

for key,value in Companies.items():
    Names = key
    cashCount = value["Cash"]
    creditCount = value["Credit"]
    print("From {0} {1} people have bought stuff on discount and paid in cash, also assistants got {2} servings of coffee on credit".format(Names,cashCount,creditCount))