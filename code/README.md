# Code

De code is opgedeeld in drie verschillende categorieën; algorithms, classes en helpers.

## Algorithms

In deze folder zijn de algoritmen die wij hebben toegepast op deze case ingedeeld in losse Python bestanden.

#### Random

Het random algoritme maakt een wijk aan waarbij de huizen op willekeurige plekken worden geplaatst die voldoen aan de restricties. Uiteindelijk wordt van alle iteraties de wijk met de beste score bewaard.

#### Greedy

Het greedy algoritme kijkt per huis welke beschikbare positie in het gebied de beste score voor de gehele wijk zou opleveren. Het eerste huis wordt zo ver mogelijk in een hoek geplaatst, voor de volgende huizen wordt er per huis naar alle beschikbare (x,y)-coördinaten gekeken om de beste positie te vinden.

#### Hill Climber

Het hill climber algoritme begint met een complete wijk en zal vervolgens per iteratie een willekeurig huis uitkiezen, om deze vervolgens op een nieuwe beschikbare plek te plaatsen. Indien de nieuwe positie een hogere score heeft opgeleverd voor de gehele wijk, wordt de wijziging geaccepteerd. Indien de score hetzelfde blijft of omlaag gaat, wordt de wijziging teruggedraaid. Op die manier worden wijzigingen alleen geaccepteerd als deze een positief effect hebben op de score van de wijk.

## Classes

In `objects.py` worden objecten geinitieerd. Deze objecten zijn dan door de hele code te gebruiken en beschikken over verschillende eigenschappen naar keuze. In de code worden verschillende objecten gebruikt zoals Border, Water en House.

#### Border

De class Border is belangrijk, omdat deze ervoor zorgt dat er in de hele repository met dezelfde grid-dimensies van wordt gewerkt. Deze dimensies zijn op te roepen met Borders().maxX en Borders().maxY. 

#### Water & House

De belangrijkste objecten zijn Water en House, dit zijn de objecten die geplaatst worden op het gebied.
Water heeft verschillende eigenschappen die geiniteerd moeten worden, zoals breedte en lengte en de coordinaten van alle hoekpunten. House heeft een aantal extra attributen, zoals de standaardprijs van het huis, de minimale vrijstand en de prijsverbetering per meter vrijstand.

## Helpers

Naast algoritmen en classes maken wij gebruik van diverse functies die een algemene, ondersteunende taak hebben.

#### builder.py & location.py

Het bestand `builder.py` bevat de functies `waterbuilder` en `housebuilder`. Zoals de namen al voorspellen hebben deze functies de taak om objecten aan te maken en in de wijk te plaatsen. De functie `housebuilder` maakt gebruik van de functie `location_checker` van `location.py` om te controleren of er wordt voldaan aan de restricties. Hierbij wordt er onder andere gecontroleerd of er bij een huis geen één hoekpunt op oppervlaktewater is geplaatst.

#### score.py

Het bestand `score.py` bevat twee functies om de score van de gehele wijk te berekenen. Allereerst berekent de functie `distance_check` voor ieder huis de vrijstand. Deze informatie kan vervolgens door de functie `scorecalculator` gebruikt worden om de score van de complete wijk te berekenen.
In `scorecalculator` kan op twee verschillende manieren de score van de totale waarde van de wijk worden berekend. In de opdracht staat dat alleen de extra vrijstand bijdroeg aan de prijsverhoging per meter maar in check50 werd hier geen rekening meegehouden en werd de kortste afstand tot het dichstbijzijnde huis inclusief verplichte vrijstand gebruikt. Hier kwamen we achter door verschillende mogelijkheden te testen, wanneer verplichte vrijstand wel wordt meegenomen in de berekening van de score dan gaf check50 wel een goede respons. Hierdoor hebben we gekozen om de check50 manier te hanteren en de manier van de opdracht in een comment erbij te zetten.

#### visualize.py, performance.py & output_generator.py

Zodra de code is uitgevoerd is het natuurlijk gewenst dat er output wordt geproduceerd. Het bestand `visualize.py` bevat de functie `create_map`, deze functie zorgt ervoor dat de kaart van de samengestelde wijk wordt gevisualiseerd. 

Het bestand `performance.py` bevat de functie `performanceplot`, deze heeft als taak om een diagram van de prestaties van het gebruikte algoritme te visualiseren. Bij het random algoritme wordt er een histogram gemaakt, bij de overige algoritmen een lijndiagram.

Tot slot bevat het bestand `output_generator.py` de functie `output`, deze functie zorgt ervoor dat er een CSV-bestand wordt aangemaakt waarin de coördinaten van alle objecten in een wijk en de score van die wijk vermeld zijn.
