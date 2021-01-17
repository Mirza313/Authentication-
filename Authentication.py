# Salman Mehdi Mirza, IC201, 500828131
# Het doel van deze applicatie is om het wachtwoord te encrypten met hashing en salting

# Het importeren van de uuid, wat ervoor zorgt dat er een random waarde van 128 bits wordt gegenereerd.
# Het importeren van hashlib zorgt ervoor dat de lengte van de variabel wordt omgezet in een standaard lengte.
import uuid
import hashlib


# Als eerst wordt er een functie aangemaakt genaamd "wachtwoordHashen".
# Met behulp van de salting die aanwezig is in de fucntie zal er een nieuwe random waar gegenereerd worden.
# Als return wordt er door de functie het wachtwoord geëncrypt in hexidecimaal.
def wachtwoordHashesn(wachtwoord):
    salting = uuid.uuid4().hex
    return hashlib.sha256(salting.encode() + wachtwoord.encode()).hexdigest() + ":" + salting

# De tweede functie die gemaakt wordt is "wachtwoordControleren".
# In deze fucntie wordt het wachtwoord en de salting samengevoegd.
# Als return wordt er door de fucntie het wachtwoord terug gegeven waar hashing en salting toegevoegd wordt.
def wachtwoordControleren(gehashteWachtwoord, gebruikersWachtwoord):
    wachtwoord, salting = gehashteWachtwoord.split(":")
    return wachtwoord == hashlib.sha256(salting.encode() + gebruikersWachtwoord.encode()).hexdigest()

# Als eerst wordt er aan de gebruiker gevraagd om het nieuw wachtwoord in te voeren.
nieuwWachtwoord = input("Kies een nieuwe wachtwoord die je wilt gebruiken: " )

# Om het nieuwe wachtwoord te encrypten wordt er gebruik gemaakt van hashing.
wachtwoordHashen = wachtwoordHashesn(nieuwWachtwoord)

# De gehashte wachtwoord wordt opgeslagen in ...........
print("De string die in de database wordt opgeslagen is: ", wachtwoordHashen )

# Nu wordt er aan de gebruiker gevraagd om het oude wachtwoord in te voeren om controleren
# of het wachtwoord overeenkomt.
# Als het blijkt dat het wachtwoord overeenkomt wordt het volgende aangegeven: "Dit is het juiste wachtwoord".
# Als er door de gebruiker een verkeerd wachtwoord wordt ingevoerd
# wordt het volgende aangegeven: "Het ingevoerde wachtwoord is onjuist en komt niet overeen".
oudWachtwoord = input("Voer het oude wachtwoord in, zodat de controle plaats kan vinden: ")
if wachtwoordControleren(wachtwoordHashen, oudWachtwoord):
    print("Dit is het juiste wachtwoord.")
else:
    print("Het ingevoerde wachtwoord is onjuist en komt niet overeen.")


