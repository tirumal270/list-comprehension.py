
result = ["Even" if i % 2 == 0 else "Odd" for i in range(1, 11)]
print(result)


words = ["Ajay", "Python", "Django"]
lengths = [len(word) for word in words]
print(lengths)


files = ["data.csv", "report.pdf", "image.png"]
extensions = [file.split(".")[1] for file in files]
print(extensions)


squares = {i: i**2 for i in range(1, 6)}
print(squares)


ascii_dict = {ch: ord(ch) for ch in "ABC"}
print(ascii_dict)


keys = ['a', 'b', 'c']
values = [1, 2, 3]
result = {k: v for k, v in zip(keys, values)}
print(result)



primes = [n for n in range(2, 101)
          if all(n % i != 0 for i in range(2, int(n**0.5) + 1))]
print(primes)


pairs = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(pairs)


palindromes = [n for n in range(1, 101) if str(n) == str(n)[::-1]]
print(palindromes)


list1 = [1, 2, 3]
list2 = [10, 20, 30]
result = [x + y for x, y in zip(list1, list2)]
print(result)


students = [
    {'name': 'Ajay', 'marks': 80},
    {'name': 'Riya', 'marks': 90}
]
names = [student['name'] for student in students]
print(names)



palindromes = [n for n in range(1, 1001) if str(n) == str(n)[::-1]]
print(palindromes)


words = ['apple', 'ant', 'banana', 'ball']
result = [word for word in words if word.startswith('a')]
print(result)


numbers = [n for n in range(1, 21) if n % 2 == 0 or n % 3 == 0]
print(numbers)


coordinates = [[x, y] for x in range(3) for y in range(3)]
print(coordinates)
