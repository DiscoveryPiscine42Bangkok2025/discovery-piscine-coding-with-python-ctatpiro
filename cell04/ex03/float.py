num=str(input("Give me a number: "))
num_float= float(num)
if num_float == int(num_float):
  num_int = int(num_float)
  print("This number is a integer.")
else:
  print("This number is a decimal.")