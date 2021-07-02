employees = ['Kelly', 'Emma', 'John']
defaults = {"designation": 'Application Developer', "salary": 8000}
r=dict.fromkeys(employees,defaults)
print(r)
print(r["Kelly"])