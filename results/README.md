# Resultaten (Results)
Vanuit deze folder worden de input-bestanden geraadpleegd. Het gaat in dit geval om drie verschillende CSV-bestanden, ieder bestand bevat de coördinaten van alle objecten in een samengestelde wijk.

De bestanden hanteren de volgende structuur:
* `structure` bevat de naam van een object (zoals maison_11)
* `corner_1` bevat de (x,y)-coördinaten van de linkeronderhoek van een object
* `corner_2` bevat de (x,y)-coördinaten van de linkerbovenhoek van een object
* `corner_3` bevat de (x,y)-coördinaten van de rechterbovenhoek van een object
* `corner_4` bevat de (x,y)-coördinaten van de rechteronderhoek van een object
* `type` bevat het type van een object (zoals 'BUNGALOW')

In de laatste regel staat bij `networth` de score van de gehele wijk in euro's.