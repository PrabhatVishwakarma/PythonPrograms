name=input("Enter Your Name -")
marks=int(input("Enter Your Marks-"))
phone=int(input("Enter Your Phone Number-"))

template="Name of The Student - {}, Marks of the Student - {}%, Phone Number of the Student - {}"
output=template.format(name,marks,phone)
print(output)