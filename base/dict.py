#dictionary uses

tamil = {"name":"Tamilselvan", "city":"Chennai", "miles":"310"}
mini = {"name":"Padmini", "city":"Bangalore", "miles":"509"}

print(tamil)
print(mini)

navya = {}
navya["name"]="Navya Tamilselvan"
navya["city"]="Boca Raton"
navya["miles"]="200"

print(navya)

tarun = dict(name="Tarun Karthik", city="Bangalore", miles="101")
print(tarun)

myfamily = [tamil, mini, tarun, navya]

for person in myfamily:
    print("--------------------------")
    print(person)