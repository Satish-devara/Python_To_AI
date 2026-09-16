students = {
    "101":{
        "name":"Rahul",
        "marks":[10, 9,8]
    },

    "102":{
        "name":"Satish",
        "marks":[10,9,9]
    }
}

students["103"] = {"name":"Ankit", "marks":[10,9,9]}
print(students)
students["102"] = {"marks": [10,10,10]}
print(students)


students.pop("102")
print(students)

x = input("Enter the key")

students.get(x)

x = int(input("Enter the number: \n"))

if x > 0:
    print("postive")
else:
    print("negative")

numbers = [10, 25, 3, 78, 45, 12]
high = max(numbers)
low = min(numbers)
total = sum(numbers)
avg = total//len(numbers)
print(high, low, total, avg)


