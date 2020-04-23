# ATP-interpreter
Deze repo bevat de uitwerking van het ATP practicum jaar 3 TI.
Hieronder zullen een aantal algemene zaken besproken worden zoals de [file structure](#filestructure) en de stappen die de interpreter zet.
Daarnaast wordt de gemaakte taal toegelicht op basis van een commando lijst en een stuk voorbeeld code, waar mogelijk zal er een C equivalent gegeven worden.

## file structure
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


