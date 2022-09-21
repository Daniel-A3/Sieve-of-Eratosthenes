# Sieve Of Eratosthenes, mathematical prime number generation algorithm.

number_list = []
count = 0

end_number = int(input("This program demonstrates the Sieve Of Eratosthenes"
                  "\nEnter a number for all of the primes below that number = "))
                
for i in range(2, end_number):
    number_list.append(i)

while True:
    removed = 0
    flag = False
    check_value = number_list[count]
    for i in range(count + 1, len(number_list)):
        current = number_list[i - removed]
        if (current % check_value == 0) and (current != check_value):
            number_list.remove(current)
            flag = True
            removed += 1
    
    if flag == False and (check_value != 2 or end_number < 5):
        break
    else:
        count += 1     

print(number_list)
