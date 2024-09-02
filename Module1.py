# create list of 100 randon number from 0 to 1000
import random
random_list = random.choices(range(1, 1000), k=100)
# sort list from min to max without using sort()
for i in range(0, len(random_list)):
    for j in range(i+1, len(random_list)):
        if random_list[i] > random_list[j]:
            random_list[i], random_list[j] = random_list[j], random_list[i]
# create lists of even and odd numbers from random list
even_numbers = []
odd_numbers = []
for i in random_list:
    if i % 2 == 0:
        even_numbers.append(i)
    else:
        odd_numbers.append(i)
# get avg from list of even numbers
avg_even = sum(even_numbers) / len(even_numbers)
# get avg from list of odd numbers
avg_odd = sum(odd_numbers) / len(odd_numbers)
#print both average result in console
print("Average of even numbers: ", avg_even, "\nAverage of odd numbers: ", avg_odd)