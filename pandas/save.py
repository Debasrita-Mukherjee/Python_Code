import pandas as pd

data = {
    "Name" : ['Ram', 'Shyam', 'Ghanashyam'],
    "Age" : [10,20,30],
    "City" : ['Nagpur', 'Birati', 'Delhi']
}

df = pd.DataFrame(data)

#print(df)

df.to_csv("data.csv", index = False)