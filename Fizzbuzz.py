#print numbers 0 to 100
#for numbers are evenly divisible by 3, print Fizz instead of printing the number
#for numbers are evenly divisible by 5, print Fizz instead of printing the number
counter = 0

while counter <= 100: 
    if counter % 3 == 0 and counter % 5 == 0:
      print('FizzBuzz')
    elif counter % 3 == 0:
       print('Fizz')
    elif counter % 5 == 0:
        print("Buzz")
    else: 
      print(counter)
    
    counter += 1