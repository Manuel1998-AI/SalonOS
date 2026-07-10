# Gestione servizi SalonOS

servizi = []


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
