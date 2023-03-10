def creating_gen(index):  
    months = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']  
    yield months[index]  
    yield months[index+2]  
next_month = creating_gen(3)  
print(next(next_month), next(next_month))  


output: apr jun


Explanation:

The function creating_gen takes an index as an input and defines a list of months.
It uses the yield keyword to create a generator object that yields the month at the given index and the month two positions ahead of it.
The variable next_month is assigned the generator object returned by calling the creating_gen function with an argument of 3, which corresponds to the month of April in the months list.
The next function is called twice on next_month to iterate through the generator object and print the yielded values.
The first call to next(next_month) returns the first yielded value, which is 'apr'.
The second call to next(next_month) returns the second yielded value, which is 'jun'.
Therefore, the output of the print statement is 'apr jun'.
