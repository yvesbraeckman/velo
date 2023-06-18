# Werking
### Interface
De interface beidt 4 opties aan wanneer het programma gestart wordt. Men kan kiezen uit simulatie, lenen/terugplaatsen, HTML en Quit. Deze kunnen gekozen worden door hun overeenkomstige getal in te geven als in input in de terminal. 

### Simulatie
De simulatie kan direct opgestart worden door het programma te starten met het 
-s argument. De simulatie kan ook gestart worden door in het start menu 1 in te geven als input.

Er kan, indien er al een eerder simulatie gelopen heeft, nu kiezen om verder te gaan van deze situatie of men kan kiezen om opnieuw te starten zoals wordt aangegeven in de terminal. De data van deze simulatie wordt opgeslagen in het "logje.json" bestand.


### Lenen / tergplaatsen
Fietsen kunenn als gebruiker of transporteur ook manueel geleend worden of teruggeplaatst worden door in het menu 2 te kiezen. Voor deze implementatie heb ik een globaal object voorzien voor een user en een transporter. Een transporteur kan zo veel fietsen meenemen als hij wil en een user 1 fiets.


### HTML
Wanneer deze optie gekozen wordt, worden er 2 HTML output bestanden gemaakt met daarin de data van de simulatie verwerkt. Ik heb er voor gekozen om hier te checken of er wel een simulatie uitgevoerd is, door te checken of het bestand "logje.json" bestaat.


### Quit
Stopt het programma.


### Files
<ins>[transporters.html](transporters.html)</ins> is een HTML template om de data van de transporteurs in weer te geven.

<ins>[users.html](users.html)</ins> is een HTML template om de data van de users in weer te geven.

<ins>[velo.geojson](velo.geojson)velo.geojson</ins> bevat alle informatie over de stations.

<ins>[main.py](main.py)</ins> is het main programma en dient in de terminal gestart te worden om het programma te starten.

<ins>[classes.py](classes.py)</ins> bevat alle gebruikte classes 

<ins>[functions.py](functions.py)</ins> bevat alle functies die de functionaliteit van het programma verzorgen.

<ins>[logje.json](logje.json)</ins> bevat de data van de simulatie

<ins>[pickle.dat](pickle.dat)</ins> bevat de data van de vorige simulatie

<ins>[log_transporters.html](log_transporters.html)</ins> bevat een HTML pagina met de data van de simulatie over de transporters

<ins>[log_users.html](log_users.html)</ins> bevat een HTML pagina met de data van de simulatie over de users