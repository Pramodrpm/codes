set1={1,2,3,int('4')}
set2={3,str(4)}
print(set1.union(set2))


The output will be: {1, 2, 3, 4, '4'}.



The set set1 contains elements 1, 2, 3, and 4 (converted from the string '4' using the int() function).
The set set2 contains elements 3 and 4 (converted from the string '4' using the str() function).
The union of two sets is a set that contains all unique elements from both sets. Hence, the union of set1 and set2 is {1, 2, 3, 4, '4'}.
