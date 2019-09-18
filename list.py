listname=["Batuhan", "Yagiz", "Metin", "Ece", "Emir", "Alp", "Ekim"]
listname.sort()
first_name=listname[0]
first_name=first_name[0:-1]
print(first_name)
shortest=""
for name in listname:
	if len(name)>len(shortest):
		shortest=name
print(shortest)
