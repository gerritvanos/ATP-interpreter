# ATP-interpreter
Deze repo bevat de uitwerking van het ATP practicum jaar 3 TI.
Hieronder zullen een aantal algemene zaken besproken worden zoals de bestands structuur en de stappen die de interpreter zet.<br>
Daarnaast wordt de gemaakte taal toegelicht op basis tabellen met de mogelijke keywords/operators en met stukken voorbeeld code. <br>
Ook wordt uitgelegd hoe de interpreter gestart en gebruikt kan worden.

|Contents|
|-|
|[Bestands structuur](##bestands-structuur)| 
|[interpreter structuur](#interpreter-structuur)|
|[Programeertaal (gerrit--)](#programeertaal-gerrit--)| 
|[How to run](#how-to-run)|

## Bestands structuur
 - <b>interpreter.py :</b> In deze file staat het interpret gedeelte, dus het doorlopen van de AST en uiteindelijk een output genereren.
 - <b>lex.py :</b> In deze file staat het lexer gedeelte, het omvormen van de file met text naar bruikbare tokens.
 - <b>nodes.py : </b> In deze file staan alle mogelijke nodes van de AST, dit zijn puur classes voor het opslaan van data en hebben alleen een __str__() functie maar geen andere methods.
 - <b>operators.py :</b> In deze file staan alle operators o.a. voor +,-,= maar ook voor bijvoorbeeld de if en functies om de program state te bewerken.
 - <b>parser_atp.py :</b> In deze file staan alle functies om te parsen(de token lijst omvormen naar een AST), de file name is parser_atp.py omdat parser.py een build in python functie.
 - <b>program_state.py :</b> In deze file staat de class voor mijn program state waarin ik de huidige staat van het programma bij houd zoals bijvoorbeeld het huidige regelnummer en de variabelen.
 - <b>token_class.py :</b> In deze file staat de basis token klasse die gebruikt wordt om tokens aan te maken in de lexer.
 - <b>token_types.py : </b> In deze file staat een enum met alle verschillende token types zoals een GETAL en een OPERATOR_KEER bijvoorbeeld.

De test.py file en de .txt files zijn voornamelijk voor testen tijdens het maken van het project.

## interpreter structuur

## Programeertaal (gerrit--) 
### Algemene info
Ik heb er voor gekozen om mijn eigen programeertaal te maken, mijn doel was om een "vernederlandste" versie van C te maken. In de loop van het proces heb ik er meer een combinatie van preprocessor macro's en C van gemaakt in het nederlands. Hieronder staan alle op dit moment mogelijke commando's uitgelegd met ook wat voorbeeldcode. Het is geen volledige vervanger van C zo is het bijvoorbeeld "nog" niet mogelijk om functies te maken of andere types op te slaan dan getallen. De naam van de taal is "gerrit--" geworden, voornamelijk omdat het door mij bedacht is en nogal vervelend is om in te programeren(vandaar de --).

### Operators
|operator|uitleg|C equivalent|
|-|-|-|
|var1 <b>plus</b> var2| berkent de optelling van de 2 variabeles| var1 + var2|
|var1 <b>min</b> var2| trekt de 2 variabelen van elkaar af| var1 - var2|
|var1 <b>delen_door</b> var2| berkent de deling van de 2 variabeles| var1 / var2|
|var1 <b>keer</b> var2| berkent de vermenigvuldiging van de 2 variabeles| var1 * var2|
|var1 <b>macht</b> var2| berkent var1 tot de macht var2 (var1<sup>var2</sup>) |pow(var1,var2)|
|var1 <b>kleiner_dan</b> var2| geeft 1 als var1 kleiner is dan var2 anders 0| var1 < var2|
|var1 <b>groter_dan</b> var2| geeft 1 als var1 groter is dan var2 anders 0| var1 > var2|
|var1 <b>gelijk_aan</b> var2| geeft 1 als var1 gelijk is aan var2 anders 0| var1 == var2|
|var_name <b>wordt</b> const/expr/var_name| slaat de waarde aan de rechterkant van de <b>wordt</b> op in de gespecificeerde variabele naam| var_name = 1 / var_name = 1 + 2 / var_name = var2|

bij alle operators is het mogelijk om deze te combineren, er wordt rekening gehouden met de rekenregels hieronder een lijst met de prioriteit van de operators. Daarnaast kunnen alle variabeles die aangemaakt zijn binnen het programma gebruikt worden op de plaats van var1/var2 in bovenstaande tabel. Tevens kunnen hier ook constantes staan.

1. macht
2. delen/vermenigvuldigen
3. plus/min
4. gelijk_aan,groter_dan,kleiner_dan en assignment(wordt)

Een aantal voorbeelden voor het gebruik van operators.
```c
var1 = 1            //var1 wordt 1
1 + 2               //1 plus 2
var2 = 1 + 2        //var2 wordt 1 plus 2
3 + pow(2,4)        //3 plus 2 macht 4
3 * 5/4 + 10        //3 keer 5 delen_door 4 plus 10
```
### keywords
|keyword|uitleg|C equivalent|
|-|-|-|
|<b>als_waar</b> conditie|een if statement die kijkt of de conditie waar* is, als dit zo is dan wordt de "body" van de if uitgevoerd anders wordt er gesprongen naar de bijbehorende einde_als. | if |
|<b>einde_als</b>|geeft het einde van een if statement aan| de afsluitende } van een if|
|<b>zolang</b> conditie|een statement die de "body" uitvoert als de conditie waar is, anders wordt er gesprongen naar de bijbehorende einde_zolang | while |
|<b>einde_zolang</b>| geeft het einde van een zolang loop aan en springt terug naar de bijbehorende zolang en kijkt dan weer opnieuw of de loop uitgevoerd wordt of geskipt.|
|<b>laat_zien</b>| print de variabele of uitkomst van een expressie die achter de laat_zien staat, het is alleen mogelijk om 1 variabele of 1 uitkomst tegelijk te printen bijvoobeeld laat_zien var1,var2 is niet mogelijk op dit moment.| printf()|

Hieronder een stukje voorbeeldcode voor het gebruik van als statements en de zolang loop
```c
//if statements
to_print wordt 10                   //to_print = 10
als_waar 10 gelijk_aan to_print     //if(10==to_print){
    laat_zien to_print              //  printf(to_print)
einde_als                           //}
/*
output van dit programma:
    10
*/

//while loops
run wordt 10                //run = 10
zolang run                  //while(run){
    laat_zien run           //  prinf(run)
    run wordt run min 1     //  run--
einde_zolang                //}

/*
output van dit programma:
    10
    9
    8
    7
    6
    5
    4
    3
    2
    1
*/
```
### Belangrijk
#### Getallen
Op dit moment kunnen er alleen maar getallen aangemaakt worden dit kunnen floats of integers zijn, er hoeft niet gespecificeerd te worden welk type het is dit wordt automatisch gedetecteerd. Daarna is het mogelijk om operaties uit te voeren met zowel integers als floats
```c
test_var wordt 10 delen_door 4  //word opgeslagen als 2.5
test_var2 wordt 2.5             //word opgeslagen als 2.5
test_var3 wordt 10              //word opgeslagen als 10
test_var4 wordt -10             //word opgeslagen als -10
```
#### Variabelen
Variabelen kunnen pas in operators of statements gebruikt worden als deze aangemaakt zijn, de eerste keer dat een variabele naam dus gebruikt wordt moet in combinatie met een <b>wordt</b> operator. Variabelen aanmaken zonder start waarde is niet toegestaan.
```c
//do
var1 wordt 10               //var1 = 10
var2 wordt var1 min 5       //var2 = 5

//don't
var3 wordt var4 min var1    //var4 is nog nooit aangemaakt en kan dus niet gebruikt worden
```

## How to run
De interpreter kan op verschillende mannieren gerunt worden. Alle mannieren gaan ervaruit dat python(minimaal versie 3.6) in het path staat en aangeroepen kan worden vanuit de commandline. Gezien de recursieve functies en het vele gebruik van de stack wordt bij de start van het programma de stack grote veranderd naar de waardes hieronder.
- linux: <b>2GB</b>
- windows: <b>256MB</b>
De voorkeur gaat uit naar een 32-bit versie van python hier is de memory footprint kleiner en zal het programma minder snel aan de limieten komen.
Voor linux kan het zijn dat voor onderstaande commando's "python3" gebruikt moet worden i.p.v. "python"

De interpreter kan op de volgende mannier gestart worden:<br>
`python interpreter.py file_name`<br>
Hierbij is file_name de naam van het bestand wat geinterpret dient te worden. Alle file extenties zijn op dit moment ondersteund maar het makkelijkste is een standaard ".txt" bestand gezien deze makkelijk te bewerken is.

Om meer informatie te verkrijgen kan de `-v` optie toegevoegd worden aan het commando, door deze flag toe te voegen wordt er meer informatie geprint zoals de parser output en de tijd die nodig was om het programma te draaien.

Daarnaast verzordt de `-h` of `--help` optie een verkorte versie van bovenstaande uitleg.

Het volledige commando kan er dus als volgt uit zien:<br>
`python interpreter.py test_file.txt -v`