#dictionary method

a={
    "name":"harsh",
     "from":"india",
     "marks":[91,98,96]
}

print(a.keys())   #print the keys of the dictionary

print(a.values())  #print the values of the dictionary

print(a.items())  #print the(keys,values)for all contants of the dictionary

print(a.get("singh")) #its return {none} when keys is not in dictionary


updatea={"friend":"sayam"} #update the dictionary with supplied key-value
a.update(updatea)
print(a)