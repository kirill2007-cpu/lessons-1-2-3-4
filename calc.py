def expr2(a,b,x,y):
  return div(mult(x,plus(a,b)),y)

def expr(a,b,x,y):
  return x*(a+b)/y

def div(a,b):
  return a/b

def mult(a,b):
  return a*b

def minus(a,b):
  return a-b

def plus(a,b):
  return a+b

print(expr2(2,3,4,6))

