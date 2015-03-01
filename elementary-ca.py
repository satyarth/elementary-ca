import random
from PIL import Image

width = 512
height = 512
rulenumber = 126

true_pixel = (255, 255, 255)
false_pixel = (0, 0, 0)

def generate_rule(rulenumber):
	rule = {}
	for left in [False, True]:
		for middle in [False, True]:
			for right in [False, True]:
				rule[(left, middle, right)] = rulenumber%2 == 1
				rulenumber /= 2
	return rule

def generate_ca(rule):
	ca = []
	ca.append([])
	ca[0].append(False)
	for x in range(width-2):
		ca[0].append(bool(random.getrandbits(1)))
	ca[0].append(False)

	for y in range(1,height):
		ca.append([])
		ca[y].append(False)
		for x in range(1, width-1):
			ca[y].append(rule[(ca[y-1][x-1], ca[y-1][x], ca[y-1][x+1])])
		ca[y].append(False)
	return ca

rule = generate_rule(rulenumber)
ca = generate_ca(rule)

new = Image.new('RGB', [width, height])

print("Placing pixels...")
for y in range(height):
	for x in range(width):
		new.putpixel((x, y), true_pixel if ca[y][x] else false_pixel)

print("Saving image...")
new.save("out.png")
print "Done!"