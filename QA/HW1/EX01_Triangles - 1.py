answer = True
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
	triangle = True
	if (a<(b+c)) and (b<(a+c)) and (c<(a+b)):
		triangle = True
	else:
		triangle = False
	return triangle

answer = isTriangle()

if answer == True:
	print("The input is a triangle")
else:
	print("The input is not a triangle")