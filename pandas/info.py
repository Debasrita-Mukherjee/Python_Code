import pandas as pd

df = pd.read_json("student_records.json")

print("Displaying the info of the dataset: ")
print(df.info())