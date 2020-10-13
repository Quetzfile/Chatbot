# -*- coding: utf-8 -*-

import random

zufallsantworten=["Oh, wirklich", "Interessant...", "Das kann man so sehen", "Ich verstehe..."]

reaktionsantworten = {"hallo": "aber Hallo", "geht": "Was verstehst du darunter?", "essen": "Ich habe leider keinen Geschmackssinn :("}

print("Willkommen beim Chatbot")
print("worüber würden Sie gerne heute sprechen?")
print("Zum beenden einfach 'bye' eintippen")
print("")

nutzereingabe = ""
nutzereingabe = input("Ihre Frage/Antwort: ")
print(nutzereingabe)
while nutzereingabe != "bye":
  nutzereingabe = ""
  while nutzereingabe == "":
    nutzereingabe = input("Ihre Frage/Antwort: ")
  nutzereingabe = nutzereingabe.lower()
  nutzerwoerter = nutzereingabe.split()
# print(nuterwoerter)
  intelligenteAntworten = False
  for einzelwörter in nuterwoerter:
    if einzelwoerter in reaktionsantworten:
      print(reaktionsantworten[einzelwoerter])
      intelligenteAntworten = True
  if intelligenteAntworten == False:
    print(random.choice(zufallsantworten))
  print("")
print("Einen schönen Tag wünsche ich Dir. Bis zum nächsten Mal")
