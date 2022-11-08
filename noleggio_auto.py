#1
diz={"AA123BB":[("Giugno",9,1293),("Luglio",7,3231),("Agosto",7,4020),("Settembre",6,3928)],
    "AB345CD":[("Giugno",8,1291),("Luglio",6,1234),("Agosto",9,4932),("	Settembre",8,2872)],
    "CD456FF":[("Giugno",7,2872),("Luglio",6,3273),("Agosto",4,3211),("	Settembre",8,2872)]}
#2
diz["ZZ999LG"] = [("Giugno",10,10000),("Luglio",10,10000),("Agosto",10,10000),("Settembre",10,10000)]
#3
print(diz["AA123BB"][1])
#4
print(diz["AA123BB"][1][1])
#5
tot = 0
for i in range(len(diz["AB345CD"])):
  tot += diz["AB345CD"][i][2]
print(tot)
#6
tot = 0
for c in diz:
  for i in range(len(diz["AB345CD"])):
    tot += diz[c][i][2]
print(tot)
#7
pos = 0
for i in range(len(diz["AB345CD"])-1):
  if(diz["CD456FF"][pos][2] < diz["CD456FF"][i][2]):
    pos = i

print(diz["CD456FF"][pos][2])
