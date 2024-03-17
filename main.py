nric = input('Enter an NRIC number: ')
nric = nric.strip('')
nric = nric.upper()

prefix = nric[0]
digits = nric[1:8]
digitslist = list(digits)
suffix = nric[8:]
ST_suffix = list("JZIHGFEDCBA")
FG_suffix = list("XWUTRQPNMLK")
digitweight = list("2765432")
valid = "NRIC is valid."
invalid = "NRIC is invalid."
x = 0
total = 0

if prefix not in ["S", "T", "F", "G"]:
  print(invalid)

elif len(digits) != 7:
  print(invalid)

elif not digits.isdecimal():
  print(invalid)

elif len(suffix) != 1:
  print(invalid)

else :
  for x in range(7):
    Subtotal_list = int(digitweight[x]) * int(digitslist[x])
    total += Subtotal_list
  
  if prefix in ["T", "G"]:
    total = total + 4

  remainder = total % 11

  check_suffix = ''
  if prefix in ["S", "T"]:
    check_suffix = ST_suffix[remainder]
  elif prefix in ["F", "G"]:
    check_suffix = FG_suffix[remainder]

  if suffix == check_suffix :
    print(valid)
  else:
    print(invalid)

