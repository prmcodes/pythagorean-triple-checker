# Ask user for three sides of a triangle
def ask_for_side(a):
  answer = int(input("Enter the " + a + " side of the triangle:\n"))
  return answer

a = ask_for_side("first")
b = ask_for_side("second")
c = ask_for_side("third")

# sort the three inputed values from smallest to largest
sides = [a, b, c]
sides.sort()

a = sides[0]
b = sides[1]
c = sides[2]

# Raise each side to the 2nd power
a = a**2
b = b**2
c = c**2

# Check whether the two smallest sides raised to the second power equal the longest side raised to the second power
if a + b == c:
    print("\nCongratulations, your triangle is a pythagorean triple!\n")
else:
    print("\nSorry, your triangle isn't a pythagorean triple.\n")
