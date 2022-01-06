gar=float(input("Ievadi malas garumu: "))
if gar>=5:
  lauk=gar*gar
  lauk2=(gar+5)*(gar+5)
  print("Procenti ir ", 100*(lauk2/lauk),"%")
else:
  print("Ievadīts nepareizs skaitlis")