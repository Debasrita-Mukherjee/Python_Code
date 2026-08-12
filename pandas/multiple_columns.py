import pandas as pd

data = {
    "Name" : ['Ram', 'Shyam', 'Ghanashyam', 'Radha', 'Rani', 'Bani', 'Chiru', 'Ravi', 'Soma'],
    "Age" : [10,20,30,40, 50, 60, 70, 80, 90],
    "City" : ['Nagpur', 'Kolkata', 'Delhi', 'Mumbai', 'Bengalore', 'Pune', 'Jaipur', 'Kota', 'Jalpaiguri'],
    "Salary": [50000, 85000, 95000, 68000, 70000, 90000, 100000, 150000, 60000]
}

subset = df[["Name"], ["Salary"]]
print("\n Subset with Name and Salary: ")
Print(subset)