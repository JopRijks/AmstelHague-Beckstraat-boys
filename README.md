# Programmeertheorie: Amstelhaege

Er zijn plannen om in de Duivendrechtse polder op een stuk land van 180 bij 160 meter een nieuwe woonwijk te bouwen. Een aantal strenge restricties zorgt vanuit een planologisch perspectief voor een grote uitdaging. De gemeente overweegt drie varianten wat betreft het aantal huizen, namelijk twintig, veertig of zestig huizen in totaal. Er wordt aangemnomen dat een huis meer waard wordt naarmate de vrijstand toeneemt.

De woonwijk zal voor 60% uit eengezinswoningen bestaan, voor 25% uit bungalows en tot slot voor 15% uit maisons.

Aan de hand van deze informatie is geprobeerd om diverse algoritmen en principes uit het vakgebied van de Heuristieken toe te passen om een zo optimaal mogelijke oplossing te vinden.

## Aan de slag (Getting Started)

### Vereisten (Prerequisites)

Deze codebase is volledig geschreven in Python [3.8.3](https://www.python.org/downloads/). In requirements.txt zijn alle packages vermeld die nodig zijn om de code succesvol uit te voeren. Deze packages kunnen eenvoudig geinstalleerd worden door middel van onderstaande instructie:

```
pip install -r requirements.txt
```

### Structuur (Structure)

Op `main.py` na staan alle Python scripts in de folder Code. Alle input waardes staan in de map Data en alle resultaten worden opgeslagen in de folder Results.

### Test

Om de code uit te voeren dient u de onderstaande instructie uit te voeren:

```
python main.py <ALGORITME> <AANTAL ITERATIES> <AANTAL HUIZEN> <WIJK CONFIGURATIE>
```

Met betrekking tot het algoritme kunt u kiezen uit "random", "hillclimber" en "greedy". Het aantal huizen moet minimaal 1 zijn en kan maximaal 80 zijn. Voor de configuratie van de wijk kunt u met 0 voor wijk_1 kiezen, met 1 voor wijk_2 en met 2 voor wijk_3.

Indien er een incorrect aantal argumenten wordt meegegeven als input, wordt er een random algoritme uitgevoerd voor 20 huizen in wijk_1 met 100 iteraties.

## Auteurs (Authors)

### Beckstraat Boys

* Jop Rijksbaron (11685514) - jop.rijksbaron@student.uva.nl
* Robin Spiers (11829494) - rspiers@hotmail.nl
* Vincent Kleiman (11884622) - vinniekleiman1@gmail.com

## Dankwoord (Acknowledgements)

* Minor Programmeren
* Jasper den Duijf
* Okke van Eck
* Quinten van der Post
* Julien Fer
* Wouter Vrielink
* Bas Terwijn
* Martijn Stegeman