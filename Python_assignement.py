"""
--Assignement--
Create and call a python function that : 
- stores a random integer A between 1 and 9
- stores a random integer B between 1 and 9
- multiplies A and B together as C
- Prints A and C for every result until C = 4
- If C = 4 , print ‘Success!’ and the results for A and B
- Store your code on a GitHub account and share it with the email-address given in the SQL test, including your CV
"""

import random


while True:

    #stores a random integer A between 1 and 9
    Integer_A = random.randint(0, 9)

    #stores a random integer B between 1 and 9
    Integer_B = random.randint(0, 9)
 
    #multiplies A and B together as C
    Integer_C = Integer_A * Integer_B


    #Prints A and C for every result until C = 4

    for i in range(Integer_C):
        print(Integer_A, Integer_C)
        break

    #If C = 4 , print ‘Success!’ and the results for A and B

    if Integer_C == 4:
        print("‘Success!’ and the results for" ,Integer_A,"and" ,Integer_B)
        break
    

    
        
     
   
        
 
        

    

    
