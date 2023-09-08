  # 1.1 Recursive function to calculate the factorial of the given number

def factrec(n):
  if n==0 or n==1:
    return 1
  else:
    return n*factrec(n-1)

number=int(input("Enter a number:"))
res=factrec(number)

print("The factorial of {} is {}.".format(number,res))