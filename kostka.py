#Napiš program, který simuluje tuto hru:
#
#První hráč hází kostkou (t.j. vybírají se náhodná čísla od 1 do 6), dokud #nepadne šestka. Potom hází další hráč, dokud nepadne šestka i jemu. Potom hází #hráč třetí a nakonec čtvrtý. Vyhrává ten, kdo na hození šestky potřeboval nejvíc #hodů. (V případě shody vyhraje ten, kdo házel dřív.)
#
#Program by měl vypisovat všechny hody a nakonec napsat, kdo vyhrál.

from random import randrange
import os


nejvyssi_hod = 0
vitezny_hrac = 0


for hod in range(1,5):
  hra_bezi = True
  pocet_hodu = 0
  print(f">>>Hazi hrac cislo {hod}<<<\n")
  while hra_bezi:
    hod_kostkou = randrange(1,7)
    pocet_hodu += 1
    print(f"Toto je {pocet_hodu} pokus")
    if hod_kostkou < 6:
      print(f"Padla Ti {hod_kostkou}")
    else: 
      hod_kostkou == 6
      hra_bezi = False
      print(f"Hodil jsi sestku na {pocet_hodu} pokus(u)\n")

    if nejvyssi_hod < pocet_hodu:
      vitezny_hrac = hod
      nejvyssi_hod = pocet_hodu

print(f"\nVitezny hrac cislo {vitezny_hrac} hodil sestku na {nejvyssi_hod} pokusu")









  

  


 




