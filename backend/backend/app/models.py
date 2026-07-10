# Modelli dati SalonOS

class Salone:
    def __init__(self, nome, telefono):
        self.nome = nome
        self.telefono = telefono


class Cliente:
    def __init__(self, nome, telefono):
        self.nome = nome
        self.telefono = telefono


class Servizio:
    def __init__(self, nome, prezzo, durata):
        self.nome = nome
        self.prezzo = prezzo
        self.durata = durata


class Appuntamento:
    def __init__(self, cliente, servizio, data, orario):
        self.cliente = cliente
        self.servizio = servizio
        self.data = data
        self.orario = orario
