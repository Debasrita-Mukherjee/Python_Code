import pandas as pd

df = pd.read_json("student_records.json")

print("Display 10 rpws of first: ")
print(df.head(10))

print("Display 10 rpws of last: ")
print(df.tail(10))
