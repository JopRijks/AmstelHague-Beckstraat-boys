# Resultaten (Results)
In deze folder worden de resultaten van de algoritmen opgeslagen. De drie bestanden output.csv, map.png en plot.png worden aangepast zodra de code is uitgevoerd. Om te voorkomen dat oudere data wordt verwijderd wordt deze ook opgeslagen in subfolders. In `archive` worden de resultaten in de vorm van csv-bestanden opgeslagen, de visualisaties van plattegronden worden in `maps` opgeslagen en de diagrammen van de prestaties van een algoritme worden in `plots` opgeslagen.

Het bestand output.csv hanteert de volgende structuur:
* `structure` bevat de naam van een object (zoals maison_11)
* `corner_1` bevat de (x,y)-coördinaten van de linkeronderhoek van een object
* `corner_2` bevat de (x,y)-coördinaten van de rechteronderhoek van een object
* `corner_3` bevat de (x,y)-coördinaten van de rechterbovenhoek van een object
* `corner_4` bevat de (x,y)-coördinaten van de linkerbovenhoek van een object
* `type` bevat het type van een object (zoals "BUNGALOW")

In de laatste regel staat naast `networth` in de kolom `corner_1` de netto waarde (oftewel de score) van de gehele wijk in euro's vermeld.