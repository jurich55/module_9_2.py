
strings1 = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
strings2 = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']
strings3 = strings1 + strings2

result1 = [len(x) for x in strings1 if len(x) >= 5]
result2 = [(x, y) for x in strings1 for y in strings2 if len(x) == len(y)]
result3 = {z: len(z) for z in strings3 if len(z) % 2 == 0}
# result3_1 = {x: len(x) for x in strings1 if len(x) % 2 == 0}
# result3_2 = {y: len(y) for y in strings2 if len(y) % 2 == 0}

print(result1)
print(result2)
print(result3)

