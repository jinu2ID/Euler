sum = 0

for i in range(0, 1000):
    if i % 3 == 0:
        sum += i

for j in range(0, 1000):
    if j % 5 == 0:
        sum += j
    
for k in range(0, 1000):
    if k % 15 == 0:
        sum -= k
    
print(sum)
    