army = ["orcs", "wizards", "zombies", "liches", "imps", "undead dragons"]

for enemy in army:
  if enemy == "orcs":
    print enemy[0].upper() + enemy[1:(len(enemy))].lower() +" are easy targets, move slowly."
  elif enemy == "wizards":
    print enemy[0].upper() + enemy[1:(len(enemy))].lower() +" are usually hiding. Use assasins or skilled archers."
  elif enemy == "zombies":
    print enemy[0].upper() + enemy[1:(len(enemy))].lower() +" are nasty. Beware of bites and \"body\" fluids."
  elif enemy == "liches":
    print enemy[0].upper() + enemy[1:(len(enemy))].lower() +" are dangerous summoners. Dispatch a spesial trained team to take one down."
  elif enemy == "imps":
    print enemy[0].upper() + enemy[1:(len(enemy))].lower() +" are fast but cowardly."
  else:
    print "No information about " + enemy[0].upper() + enemy[1:(len(enemy))].lower() +". Please exercise caution and consult your General."