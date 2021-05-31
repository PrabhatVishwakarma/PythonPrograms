totalMoney = int(input("Enter money :"))
quantity = int(input("Enter Quantity :"))
price = float(input("Enter Prize :"))
statment1= "I have {0} dollars so I can buy {1} football for {2:.2f} dollars"
print(statment1.format(totalMoney,quantity,price))