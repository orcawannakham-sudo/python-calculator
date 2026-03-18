input("danger this may freeze your device -- press enter to continue")
ram = int(input("tell me your ram(in GB (intenger)) so it not boom your device(that i can use): "))
print("how to use --> type down number and enter when want to calculate type calculate then enter")
bits = (ram * 1024 * 1024 *1024 // 4) * 30
infi = (1 << bits) - 1
i = 0
sumn = 0
minn = 0
max = 0
min = infi
minn = int(input("""
-------setup-------
number to minus: """))
while True:
 inp = input("num" + str(i + 1) + ": ")
 if inp == "calculate":
   print("average:" + str(sumn / i))
   print("plus:" + str(sumn))
   print("minus:" + str(minn))
   print("max:" + str(max))
   print("min:" + str(min))
   break
 else:
   sumn = int(inp) + sumn
   minn = minn - int(inp)
   if int(inp) < min:
     min = int(inp)
   if int(inp) > max:
     max = int(inp)
 i += 1
