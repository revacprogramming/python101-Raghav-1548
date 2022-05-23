hrs=float(input("Enter Hours: "))
rph=float(input("Enter rate: "))
gpay=hrs*rph
if hrs<=40:
    print(gpay)
else:
	print(40*rph+1.5*(rph)*(hrs-40))
          
