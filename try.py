try: print(1)
except:print(2)
finally:print(3)
  
  
  
output is: 1 3

The try block attempts to execute print(1), which will successfully print 1.
Since there's no error in the try block, the except block is skipped and the code moves on to the finally block.
The finally block always executes, regardless of whether there was an error or not. So it will print 3.
Therefore, the output will be 1 followed by 3.
