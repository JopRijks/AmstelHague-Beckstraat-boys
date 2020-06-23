# Programmeertheorie: Amstelhaege

Na jarenlang getouwtrek is de knoop eindelijk doorgehakt: er komt een nieuwe woonwijk in de Duivendrechtse polder, net ten noorden van Ouderkerk aan de Amstel. De huisjes zijn bedoeld voor het midden- en bovensegment van de markt, met name expats en hoogopgeleide werknemers actief op de Amsterdamse Zuidas.

Omdat de Duivenderechtse polder ooit beschermd natuurgebied was, is de compromis dat er alleen lage vrijstaande woningen komen, om zo toch het landelijk karakter te behouden. Dit, gecombineerd met een aantal strenge restricties ten aanzien van woningaanbod en het oppervlaktewater, maakt het een planologisch uitdagende klus. De gemeente overweegt drie varianten: de 20-huizenvariant, de 40-huizenvariant en de 60-huizenvariant. Er wordt aangenomen dat een huis meer waard wordt naarmate de vrijstand toeneemt, de rekenpercentages zijn per huistype vastgesteld.

Om tot een oplossing te komen heeft de gemeente besloten om ons, de ***Beckstraat Boys*** (experts op het gebied van de planologie), te benaderen. Aan de hand van diverse principes uit het vakgebied van de heuristieken hebben wij een poging gewaagd om een goede oplossing te vinden voor dit probleem.

### Restricties voor de wijk (Requirements)

1. De wijk komt te staan op een stuk land van 180x160 meter (breed x diep). Er wordt door de planologen gerekend in hele meters.
2. Het aantal woningen in de wijk bestaat voor 60% uit eengezinswoningen, 25% uit bungalows en 15% uit maisons.
3. Een eengezinswoning is 8x8 meter (breed x diep) en heeft een waarde van €285.000,- De woning heeft rondom twee meter vrijstand nodig; iedere meter extra levert een prijsverbetering op van 3%.
4. Een bungalow is 11x7 meter (breed x diep) en heeft een waarde van €399.000,-. De woning heeft rondom drie meter vrijstand nodig, iedere meter extra levert een prijsverbetering op van 4%.
5. Een Maison is 12x10 meter (breed x diep) en heeft een waarde van €610.000,- De woning heeft rondom zes meter vrijstand nodig, iedere  meter extra levert een prijsverbetering op van 6%.
6. De vrijstand van een woning is de kleinste afstand tot de dichtstbijzijnde andere woning in de wijk. Oftewel, voor een vrijstand van 6 meter moeten alle andere woningen in de wijk op minimaal 6 meter afstand staan. Deze afstand is bepaald als de kortste afstand tussen twee muren, dus niet vanuit het centrum van de woning.
7. De verplichte vrijstand voor iedere woning moet binnen de kaart vallen. Overige vrijstand mag buiten de kaart worden meegerekend.
8. In geval van percentuele waardevermeerdering per meter is de toename niet cumulatief. Een maison met twee meter extra vrijstand is dus 12.0% meer waard, niet 12.36%.
9. De wijk bestaat voor een deel uit oppervlaktewater. Huizen mogen niet op het water worden geplaatst, maar hun vrijstand mag daar wel op vallen (zowel de verplichte als die voor de waarde berekening).

## Aan de slag (Getting Started)

### Vereisten (Prerequisites)

Deze codebase is volledig geschreven in [Python3](https://www.python.org/downloads/). In requirements.txt zijn alle packages vermeld die nodig zijn om de code succesvol uit te voeren. Deze packages kunnen eenvoudig geinstalleerd worden door de onderstaande instructie via een terminal uit te voeren:

```
pip install -r requirements.txt
```

### Structuur (Structure)

Op main.py na staan alle Python bestanden in de folder `Code`. Alle input-bestand staan in de map `Data` en alle resultaten worden opgeslagen in de folder `Results`.

### Test

Om de code uit te voeren dient u via een terminal in dezelfde folder als main.py de onderstaande instructie uit te voeren:

```
python main.py <ALGORITME> <AANTAL ITERATIES> <AANTAL HUIZEN> <WIJK CONFIGURATIE>
```
### Algoritme

#### Random

Het random algoritme maakt een wijk aan waarbij de huizen op willekeurige plekken worden geplaatst die voldoen aan de restricties. Uiteindelijk wordt van alle iteraties de wijk met de beste score bewaard.

Om het random algoritme uit te voeren dient u 'random' in te voeren als argument.

#### Greedy

Het greedy algoritme kijkt per huis welke beschikbare positie in het gebied de beste score voor de gehele wijk zou opleveren. Het eerste huis wordt zo ver mogelijk in een hoek geplaatst, voor de volgende huizen wordt er per huis naar alle beschikbare (x,y)-coördinaten gekeken om de beste positie te vinden.

Om het greedy algoritme uit te voeren dient u 'greedy' in te voeren als argument.

#### Hill Climber

Het hill climber algoritme begint met een complete wijk en zal vervolgens per iteratie een willekeurig huis uitkiezen, om deze vervolgens op een nieuwe beschikbare plek te plaatsen. Indien de nieuwe positie een hogere score heeft opgeleverd voor de gehele wijk, wordt de wijziging geaccepteerd. Indien de score hetzelfde blijft of omlaag gaat, wordt de wijziging teruggedraaid. Op die manier worden wijzigingen alleen geaccepteerd als deze een positief effect hebben op de score van de wijk.

Om een hill climber algoritme uit te voeren dient u één van de onderstaande drie opties in te voeren als argument.
* 'hillclimber-random' voor het hill climber algoritme dat met een willekeurige wijk begint
* 'hillclimber-bestrandom' voor het hill climber algoritme dat met de beste wijk van 1000 random oplossingen begint
* 'hillcimber-greedy' voor het hill climber algoritme dat met een wijk begint die door het greedy algoritme is samengesteld

### Iteraties

Het aantal iteraties moet een positieve integer zijn. In verband met duratie van het draaien van de code, wordt het aanbevolen om hoogstens 10.000 iteraties in te stellen.

### Aantal huizen

Zoals eerder vermeld overweegt de gemeente drie varianten, namelijk 20, 40 of 60 huizen. Indien een ander getal wordt ingevoerd wordt er gebruik gemaakt van de default instelling met 20 huizen.

### Wijk configuratie

In de onderstaande afbeeldingen zijn de visualisaties van de drie varianten met bettreking tot de ligging van het oppervlaktewater te zien. Van links naar rechts: wijk_1, wijk_2 en wijk_3.

<img src="https://github.com/JopRijks/Amstelhaege/blob/master/doc/wijk_1.png" width=32%> <img src="https://github.com/JopRijks/Amstelhaege/blob/master/doc/wijk_2.png" width=32%> <img src="https://github.com/JopRijks/Amstelhaege/blob/master/doc/wijk_3.png" width=32%>

Voor wijk_1 dient u `0` als argument mee te geven, voor wijk_2 `1` en voor wijk_3 `2`.

## Auteurs (Authors)

### Beckstraat Boys

* Jop Rijksbaron (11685514) - jop.rijksbaron@student.uva.nl
* Robin Spiers (11829494) - rspiers@hotmail.nl
* Vincent Kleiman (11884622) - vinniekleiman1@gmail.com

## Dankwoord (Acknowledgements)

* [Minor Programmeren](https://www.proglab.nl/)
* Jasper den Duijf
* Okke van Eck
* Quinten van der Post
* Julien Fer
* Wouter Vrielink
* Bas Terwijn
* Martijn Stegeman
