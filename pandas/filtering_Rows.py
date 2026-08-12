import pandas as pd

data = {
    "Name": ['Ram', 'Shyam', 'Ghanashyam', 'Radha', 'Rani', 'Bani', 'Chiru', 'Ravi', 'Soma'],
    "Age": [10, 20, 30, 40, 50, 60, 70, 80, 90],
    "City": ['Nagpur', 'Kolkata', 'Delhi', 'Mumbai', 'Bengalore', 'Pune', 'Jaipur', 'Kota', 'Jalpaiguri'],
    "Salary": [50000, 85000, 95000, 68000, 70000, 90000, 100000, 150000, 60000]
}

df = pd.DataFrame(data)

high_salary = df[df['Salary']>50000]

print("Employees with Salary > 50000: ")
print(high_salary)

filtered = df[(df[Age] > 30) & (df['Salary'] > 50000)]
print(f'Employee list Age' > 30 + Salary >50000')
print(filteredd)