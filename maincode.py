a_value = complex(input("Enter a Value: "))
b_value = complex(input("Enter b Value: "))

def one_calc(a):
  a = int(a.real)
  if a > 1:
    while a > 1:
      a = a - 1
      return a
  elif a < 1:
    while a < 1:
      a = a + 1
    return a

def two_calc(b):
  b = int(b.real)
  if b > 2:
    while b > 2:
      b = b - 1
    return b
  elif b < 2: 
    while b < 2:
      b = b + 1
    return b



number_one = one_calc(a=a_value)

number_two = two_calc(b=b_value)

print(f"{int(complex(number_one).real)} + {int(complex(number_two).real)}")
