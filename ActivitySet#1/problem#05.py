def computepay(h, r):
	p=h*r
	if h>40:
		p=40*r+1.5*(r)*(h-40)
	return p

h=float(input("Enter Hours: "))
r=float(input("Enter rate: "))
if h<=40:
    pay=h*r
    print(pay)
else:
	p = computepay(h, r)
	print("Pay", p)