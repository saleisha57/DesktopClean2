from enum import Enum

class Triangle(Enum):
	equilateral = 1
	scalene = 2
	isosceles = 3
	right = 4
	notatriangle = 5

loop_count = True

while loop_count == True:
	a = int(input("Enter a value between 1 and 200: "))
	if (a >= 0 and a <= 200):
		loop_count = False

loop_count = True

while loop_count == True:
	b = int(input("Enter a value between 1 and 200: "))
	if (b >= 0 and b <= 200):
		loop_count = False

loop_count = True

while loop_count == True:
	c = int(input("Enter a value between 1 and 200: "))
	if (c >= 0 and c <= 200):
		loop_count = False
		
def isTriangle():
	Triangles = enum('equilateral','scalene','isosceles','right','notatriangle')
	triangle = True
	if (a<(b+c)) and (b<(a+c)) and (c<(a+b)):
		if (a == b) and (b == c) and (a == c):
			print("The triangle is 'Equilateral'")
		elif(a != b) and (a != c) and (b != c):
			print("The input is 'Scalene'")
		elif((a == b) and (a != c)) or ((a == c) and (a != b)) or ((c == b) and (c != a)):
			print("The input is 'Isosceles'")
		elif():
			print("The input is 'Right'")
	else:
		print("The input is not a triangle")
	return Triangles.right

for x in range(0,10):
	answer = isTriangle()
	print(answer)