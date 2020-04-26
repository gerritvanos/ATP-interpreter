# ATP-interpreter
Deze repo bevat de uitwerking van het ATP practicum jaar 3 TI.
Hieronder zullen een aantal algemene zaken besproken worden zoals de [bestands structuur](#filestructure) en de stappen die de interpreter zet.
Daarnaast wordt de gemaakte taal toegelicht op basis van een commando lijst en een stuk voorbeeld code, waar mogelijk zal er een C equivalent gegeven worden.

|Contents|
|-|
|[Bestands structuur](#Bestandsstructuur)| 
|[interpreter structuur](#interpreterstructuur)|
|[Programeertaal](#Programeertaal )| 
|[How to run](#howtorun)|

## Bestands structuur
 - <b>interpreter.py :</b> In deze file staat het interpret gedeelte, dus het doorlopen van de AST en uiteindelijk een output genereren.
 - <b>lex.py :</b> In deze file staat het lexer gedeelte, het omvormen van de file met text naar bruikbare tokens.
 - <b>nodes.py : </b> In deze file staan alle mogelijke nodes van de AST, dit zijn puur classes voor het opslaan van data en hebben alleen een __str__() functie maar geen andere methods.
 - <b>operators.py :</b> In deze file staan alle operators o.a. voor +,-,= maar ook voor bijvoorbeeld de if en functies om de program state te bewerken.
 - <b>parser_atp.py :</b> In deze file staan alle functies om te parsen(de token lijst omvormen naar een AST), de file name is parser_atp.py omdat parser.py een build in python functie.
 - <b>program_state.py :</b> In deze file staat de class voor mijn program state waarin ik de huidige staat van het programma bij houd zoals bijvoorbeeld het huidige regelnummer en de variabelen.
 - <b>token_class.py :</b> In deze file staat de basis token klasse die gebruikt wordt om tokens aan te maken in de lexer.
 - <b>token_types.py : </b> In deze file staat een enum met alle verschillende token types zoals een INTEGER en een OPERATOR_KEER bijvoorbeeld.

De test.py file en de .txt files zijn voornamelijk voor testen tijdens het maken van het project.

## interpreter structuur

## Programeertaal 
### keywords
|keyword|uitleg|C equivalent|
|-|-|-|
|<b>als_waar</b> conditie|een if statement die kijkt of de conditie waar* is, als dit zo is dan wordt de "body" van de if uitgevoerd anders wordt er gesprongen naar de bijbehorende einde_als. | if |
|<b>einde_als</b>|geeft het einde van een if statement aan| de afsluitende } van een if|
|<b>zolang</b> conditie|een statement die de "body" uitvoert als de conditie waar is, anders wordt er gesprongen naar de bijbehorende einde_zolang | while |
|<b>einde_zolang</b>| geeft het einde van een zolang loop aan en springt terug naar de bijbehorende zolang en kijkt dan weer opnieuw of de loop uitgevoerd wordt of geskipt.|
|<b>laat_zien</b>| print de variabele of uitkomst van een expressie die achter de laat_zien staat, het is alleen mogelijk om 1 variabele of 1 uitkomst tegelijk te printen bijvoobeeld laat_zien var1,var2 is niet mogelijk op dit moment.| printf()|

### operators
|operator|uitleg|C equivalent|
|-|-|-|
|var1 <b>plus</b> var2| berkent de optelling van de 2 variabeles| var1 + var2|
|var1 <b>min</b> var2| trekt de 2 variabelen van elkaar af| var1 - var2|
|var1 <b>delen</b> var2| berkent de deling van de 2 variabeles| var1 / var2|
|var1 <b>keer</b> var2| berkent de vermenigvuldiging van de 2 variabeles| var1 * var2|
|var1 <b>macht</b> var2| berkent var1 tot de macht var2 (var1<sup>var2</sup>) |pow(var1,var2)|
|var1 <b>kleiner_dan</b> var2| geeft 1 als var1 kleiner is dan var2 anders 0| var1 < var2|
|var1 <b>groter_dan</b> var2| geeft 1 als var1 groter is dan var2 anders 0| var1 > var2|
|var1 <b>gelijk_aan</b> var2| geeft 1 als var1 gelijk is aan var2 anders 0| var1 == var2|


## How to run