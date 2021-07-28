import csv
def intro():
  print('\nWelcome to the Spanish and French translator app. Please enter English word and press the "Enter" key.')
def exit():
  print('\nThanks for using the translator app. Have a great day!')
print('\nType "done" at any time to exit')
translations = {
 
}


with open("translations.csv", "r") as words:
  reader = csv.DictReader(words, delimiter=",")
  for line in reader:
    english = line["English"].lower()
    spanish = line["Spanish"].lower()
    french = line["French"].lower()
    translations[english ]= [spanish, french]


done = False

#done
#print('Type "done" at any time to exit')
intro()

while not done:
  word = input("\nType an English word to translate:  ")
  word = word.lower()
 
  if word == "done":
    done = True
  elif word in translations:
    #print(translations[word])
    print(f'\nSPANISH: {translations[word][0]}')
    print(f'\nFRENCH: {translations[word][1]}')
  
  elif word not in translations:
    print("\nYour word is not in the dictionary" )
  exit()