######## needed functions ########
def fill_spidermen_array():
  spidermen = [] # initalize an empty array to hold the spidermen enteries 
  while True: 
    spiderman = input("Enter a name for Spiderman(or 'done' to finish): ")
  if spiderman.lower() == "done":
     'break'
  else:
    spidermen.append(spiderman)
  return spidermen

def count_spidermen(spidermen):
  return len(spidermen)

def print_spidermen(spidermen,count):
  print (f"\n You were able to give {count} spidermen a nickname. Here is the list of nicknames:")
  for spiderman in spidermen:
    print(spiderman)

######## start of program ########
spidermen = fill_spidermen_array()
count = count_spidermen(spidermen)
print_spidermen(spidermen,count)