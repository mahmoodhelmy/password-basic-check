def strength(password):
  l=[]

  for i in password:
    if i.isupper():
         l.append(1)
    elif i.isdigit():
         l.append(1)
    else:
        l.append(0)
  x ="Strong password" 
  if sum(l) >= 2 and len(password) >=8:
    x ="Strong password"
  else: 
    x ="Weak password"
  return x

z= input("Enter your password: ")
g=print(strength(z))