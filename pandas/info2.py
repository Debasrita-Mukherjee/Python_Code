import pandas as pd

data = {
    "Name" : ['Ram', 'Shyam', 'Ghanashyam'],
    "Age" : [10,20,30],
    "City" : ['Nagpur', 'Birati', 'Delhi']
}

df = pd.DataFrame(data)
print("displaying the information of the dataset: ")
print(df.info())