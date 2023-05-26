# print by highest grade
grades = [("english", 88), ("science", 97), ("art", 93)]
print(sorted(grades, key=lambda x: x[1]))

# cube all elements
lst = [1, 3, 9]
print((lambda x: [i**3 for i in x])(lst))

# return true for even, false for odd
odd_even = [1, 2, 6, 5, 7, 19, 20]
print((lambda lst: [i % 2 == 0 for i in lst])(odd_even))

# use list comprehension to print 1 - 100
x = [y for y in range (101)]
print(x)

# dictionary comprehension to count length of each word in a sentence
sentence = "I am a sentence"
check_length = {word: len(word) for word in sentence.split(' ')}
print(check_length)