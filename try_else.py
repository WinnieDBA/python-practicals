x = 'Winnie'
try:
    print(x)
except:
    print('There is an error')
else:
    print('There is no error')

# if there is name error it will print the first print but if the error is  of another type it will print the third print

try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")



try:
    print('Hello')
except:
    print('there is an error')
else:
    print('There is no an error')

Finally

try:
    print(x)
except:
    print('There is an error')
finally:
    print('There is an error but continue')
