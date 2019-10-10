import json
import csv
f=open("employ.json")
data=json.load(f)
f.close()

dict1={}
csv_file=csv.writer(open("data.csv","w"))
lis1=[]

for item in data:
	print(item)
	item["first_name"]=item["first_name"]+" "+item["last_name"]
	print(item["first_name"])
	if ("last_name" in item):
		item.pop("last_name")
	item["Name"]=item.pop("first_name")
	
	#head=item.keys()
	#print(head)
	lis=list(item.keys())
	print("item keys:",lis)
	print("length:",len(lis))
for x in range(len(lis)):
	y=str(lis[x])
	print(y,"y")
	z=y.capitalize()
	print(z)
	lis1.append(z)
lis2=('\033[1m'+str(lis1))
print(type(lis2))
print(lis2)
lis=list(lis2)
print("lis",lis)
csv_file.writerow(lis1)
print("dict:",item)
print("lis1:",lis1)
for i in data:
	csv_file.writerow(i.values())


		


