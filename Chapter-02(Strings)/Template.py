letter= """Dear <|Name|>
                You are Selected
                    Date = <|Date|>"""
name =input("Enter Your Name - ")
date=input("Enter Date - ")
letter=letter.replace("<|Name|>", name.capitalize())
letter=letter.replace("<|Date|>",date)
print(letter)