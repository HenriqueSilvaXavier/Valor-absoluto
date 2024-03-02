n=input("Digite um número: ")
f=len(n)
while f>=0:
	if f==len(n)-1:
		print("Unidade: {}".format(n[f]))
	if f==len(n)-2:
		print("Dezena: {}".format(n[f]))
	if f==len(n)-3:
		print("Centena: {}".format(n[f]))
	if f==len(n)-4:
		print("Milhar: {}".format(n[f]))
	f=f-1