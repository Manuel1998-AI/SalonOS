# Gestione servizi SalonOS

servizi = [

    {
        "nome": "Taglio",
        "prezzo": 25,
        "durata": 30
    },

    {
        "nome": "Barba",
        "prezzo": 15,
        "durata": 20
    }
]


def aggiungi_servizio(nome, prezzo, durata):

    nuovo_servizio = {
        "nome": nome,
        "prezzo": prezzo,
        "durata": durata
    }

    servizi.append(nuovo_servizio)

    return nuovo_servizio


def lista_servizi():

    return servizi
