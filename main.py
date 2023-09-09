#1.1 implement a recursive function to calculate the facterial of a given numberfact _


def fact_rec(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n * fact_rec(n - 1)


number = 2
res = fact_rec(number)

print("the factor of {}is{}.".format(number, res))
