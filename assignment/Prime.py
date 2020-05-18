#generate prime numbers for given first n
  
for val in range(100,300): 
    if (val > 1): 
       for n in range(2, val): 
           if (val % n) == 0: 
               break
       else: 
            print(val) 
    

