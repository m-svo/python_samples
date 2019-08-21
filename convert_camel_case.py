#!/usr/bin/env python3

def camel(new,separator="_"):
	for index in range(len(new)):
		if (new[index]).lower() != new[index]:
				if index == 0:
					s = ""
				else:
					s = separator
				new = new[0:index] + s +(new[index]).lower() + new[index+1:]
	return new

print (camel("CaseIsCamel","-"))
