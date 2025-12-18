in0 = 0
in1 = 0
val = 0
print("Welcome to orca calculator")

mode = input("+ or - or / or x please enter:")

in0 = int(input("first num: "))
in1 = int(input("second num: "))

if mode == "+":
  val = in0 + in1
  print("answer: ",val)

elif mode == "-":
  val = in0 - in1
  print("answer: ",val)
elif mode == "/":
  val = in0 / in1
  print("answer:",val)
elif mode == "x":
  val = in0 * in1
  print("answer:",val)
else:
  print("not support")
