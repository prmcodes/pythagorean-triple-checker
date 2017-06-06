def ask_for_side(a):
  answer = int(input("Enter the " + a + " side of the triangle:\n"))
  return answer

another_question = 'yes'

while another_question == 'yes':
  a = ask_for_side("first")
  b = ask_for_side("second")
  c = ask_for_side("third")

  sides = [a, b, c]
  sides.sort()

  a = sides[0]
  b = sides[1]
  c = sides[2]

  a = a**2
  b = b**2
  c = c**2

  if a + b == c:
      print("\nCongratulations, your triangle is a pythagorean triple!\n")
      another_question = input("Would you like to check another triangle? If so, type yes:")
  else:
      print("\nSorry, your triangle isn't a pythagorean triple.\n")
      another_question = input("Would you like to check another triangle? If so, type yes:")
