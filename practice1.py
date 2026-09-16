number = [10, 2, 4, 124, 44, 68, 90]

nums = [ n  for n in number if n%2 == 0]

def calcualte_satistics(number):
    highest_number = max(number)
    lowest_number = min(number)
    total = sum(number)
    avg = total//len(number)

    return highest_number, lowest_number, total, avg

print(calcualte_satistics(number))

def calcualte(*args):
    total = sum(args)
    print(total)

calcualte(10,20,30)

def create_user(**kwargs):
    for key, value in kwargs.items():
        print(key, " ",value)

create_user(name="Satish",
    age=22,
    skill="Python",
    goal="AI Engineer")

squares = [ n*n for n in number if n%2 == 0]
print(squares)

# square = list(map(lambda n : n*n , number))


def analyze_text(text):
    charcount = 0
    wordCount = 0
    for x in text:
        if x != ' ':
            charcount+= 1
    

    
    