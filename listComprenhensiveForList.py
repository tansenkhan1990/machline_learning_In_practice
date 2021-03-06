new_numbers = [0, 1, 2, 3, 4,5,6,7,8,9,10]
new_numbers = [number if number < 5 else 
               'seven' if number == 7 else 
               'big' for number in new_numbers]
print(new_numbers)