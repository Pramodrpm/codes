quentity=3
itemno=567
price=90
myorder="i want {} piece of item {} for {} doller"
print(myorder.format(quentity,itemno,price))



output:i want 3 piece of item 567 for 90 doller

The variable myorder is a string template that contains three placeholders delimited by curly braces {}.
These placeholders will be replaced with the values of the variables passed to the format method.
The format method is called on the myorder string, and it takes three arguments: quentity, itemno, and price.
These values will be inserted into the string template, replacing the corresponding placeholders.
The resulting string is printed to the console using the print function.
