class Station:
    def __init__(self, sloten, naam, station_id):
        self.station_id = station_id
        self.sloten = sloten
        self.capaciteit = sloten
        self.sloten_list = [Slot() for _ in range(sloten)]
        self.naam = naam

    def add_bike(self, fiets):
        for slot in self.sloten_list:
            if slot.beschikbaar:
                slot.plaats_fiets(fiets)
                self.sloten -= 1
                return True
        return False

    def remove_bike(self, fiets):
        for slot in self.sloten_list:
            if not slot.beschikbaar and fiets.fiets_id == slot.fiets.fiets_id:
                slot.verwijder_fiets()
                self.sloten += 1
                return True
        return False

    def reveal_bikes(self):
        for slot in self.sloten_list:
            print(slot)

    def __str__(self):
        stringetje = f"ik ben station {self.naam} en ik heb {self.sloten} sloten. Mijn id is: {self.station_id}"
        return stringetje


class Slot:
    def __init__(self):
        self.beschikbaar = True
        self.fiets = None

    def plaats_fiets(self, fiets):
        self.fiets = fiets
        self.beschikbaar = False

    def verwijder_fiets(self):
        self.fiets = None
        self.beschikbaar = True

    def __str__(self):
        return f"{self.beschikbaar}, {self.fiets}"


class Fiets:
    def __init__(self, fiets_id):
        self.fiets_id = fiets_id
        self.is_beschikbaar = True
        self.log = []

    def beschikbaar(self):
        self.is_beschikbaar = not self.is_beschikbaar

    def __str__(self):
        return f"ik ben fiets {self.fiets_id}"


class Gebruiker:
    def __init__(self, gebruiker_id, naam, voornaam):
        self.naam = naam
        self.voornaam = voornaam
        self.gebruiker_id = gebruiker_id
        self.heeft_fiets = False
        self.fiets = None

    def neem_fiets(self, station):
        if not self.heeft_fiets:
            for slot in station.sloten_list:
                if not slot.beschikbaar:
                    self.fiets = slot.fiets
                    slot.verwijder_fiets()
                    station.sloten += 1
                    self.heeft_fiets = True
                return True
        return False

    def plaats_fiets(self, station):
        if self.heeft_fiets:
            if station.add_bike(self.fiets):
                self.fiets = None
                self.heeft_fiets = False
                return True
        return False

    def __str__(self):
        return str(self.gebruiker_id) + " " + self.naam + " " + self.voornaam


class Transporteur:
    def __init__(self, gebruiker_id):
        self.gebruiker_id = gebruiker_id
        self.heeft_fiets = False
        self.fietsen = []

    def neem_fietsen(self, station, aantal_fietsen):
        succes = 0
        for slot in station.sloten_list:
            if not slot.beschikbaar:
                succes += 1
                self.fietsen.append(slot.fiets)
                slot.verwijder_fiets()
                station.sloten += 1
                self.heeft_fiets = True
                if succes == aantal_fietsen:
                    break
        print(f"{len(self.fietsen)} fietsen uit {station.naam} gehaald")

    def plaats_fietsen(self, station, aantal_fietsen):
        succes = 0
        if self.heeft_fiets:
            for fiets in self.fietsen:
                if station.add_bike(fiets):
                    succes += 1
                    self.fietsen.pop()
                    if succes == aantal_fietsen:
                        break
            if len(self.fietsen) == 0:
                self.heeft_fiets = False
        else:
            print("je hebt geen fiets")


class Log:
    def __init__(self):
        pass
