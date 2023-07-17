def number_composition(a_number):
  tens = a_number // 10
  ones = a_number % 10
  output = ""
  tens_list = {
    0: "Zero Tens, ", 
    1: "One Ten, ", 
    2: "Two Tens, "
  }
  ones_list = {
    0: "Zero Ones", 
    1: "One One", 
    2: "Two Ones", 
    3: "Three Ones", 
    4: "Four Ones", 
    5: "Five Ones", 
    6: "Six Ones", 
    7: "Seven Ones", 
    8: "Eight Ones", 
    9: "Nine Ones"
  }
  if tens in tens_list:
    output += tens_list[tens] 
  if ones in ones_list:
    output += ones_list[ones] 
  return output

print(number_composition(int(input("Enter a number between 1 and 25: "))))
