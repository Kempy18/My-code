from array import array

def average_age(ages):
    total_age = sum(ages)
    average = total_age / len(ages)
    return average

ages = array("i")
number_of_people = int(input("Enter the number of people: "))
counter = 0

while counter < number_of_people:
    age = int(input("Enter the age of person {}: ".format(counter + 1)))
    ages.append(age)
    counter += 1

average = average_age(ages)
print("The average age is:", average)
