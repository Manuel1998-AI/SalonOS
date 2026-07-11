# Motore prenotazioni SalonOS

from service import lista_servizi


def trova_servizio(nome_servizio):

    servizi = lista_servizi()

    for servizio in servizi:
        if servizio["nome"].lower() == nome_servizio.lower():
            return servizio

    return None


def verifica_disponibilita(data, ora):

    # Collegamento futuro con calendario
    disponibilita = True

    return disponibilita


def crea_prenotazione(cliente, servizio, data, ora):

    prenotazione = {
        "cliente": cliente,
        "servizio": servizio,
        "data": data,
        "ora": ora,
        "stato": "confermata"
    }

    return prenotazione
