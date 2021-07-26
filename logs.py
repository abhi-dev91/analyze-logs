#!/bin/python3

x = open("/var/lib/docker/volumes/mithi_logs/_data/access.log", "r")

y = x.read()

new = str(y)

list1 = new.split(sep="\n")

noG = 0
noP = 0
noF = 0
for i  in list1:
    for  j in i.split(sep=" "):
        if j == '"GET':
           noG += 1
    for  j in i.split(sep=" "):
        if j == '"POST':
           noP += 1
    for  j in i.split(sep=" "):
        if j == "404":
           noF += 1


def max_connection(List):
	counter = 0
	num = List[0]
	
	for i in List:
		curr_frequency = List.count(i)
		if(curr_frequency> counter):
			counter = curr_frequency
			num = i

	return num

z = []

for i in list1:
    z.append(i.split(sep=" ")[0])



print("The Average GET requests per minute is ",noG//60)
print("The Average POST requests per minute is ",noP//60)
print("The Average Failed requests per minute is ",noF//60)
print("The IP making maximum connections in a day is", max_connection(z))


