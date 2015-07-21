
a = 600851475143
b = 2
c = 0

while(b != a):
	if a % b == 0:
		a = a / b
		b = 2
		if a > c:
			c = a
	else:
		b += 1

print a 
