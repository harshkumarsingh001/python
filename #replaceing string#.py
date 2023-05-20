
#replaceing string#

letter='''dear<|name|>,
you are selected !
<|date|>'''

name=input("enter name:\n")
date=input("enter date:\n")
letter=letter.replace("name",name)
letter=letter.replace("date",date)
print(letter)
