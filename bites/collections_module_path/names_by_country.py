from collections import defaultdict

data = """last_name,first_name,country_code
Watsham,Husain,ID
Harrold,Alphonso,BR
Apdell,Margo,CN
Tomblings,Deerdre,RU
Wasielewski,Sula,ID
Jeffry,Rudolph,TD
Brenston,Luke,SE
Parrett,Ines,CN
Braunle,Kermit,PL
Halbard,Davie,CN"""

names_list = data.split('\n')
by_countries = defaultdict(list)
for name in names_list[1:]:
    person = name.split(',')
    by_countries[person[2]].append(f"{person[1]} {person[0]}")
print(by_countries)