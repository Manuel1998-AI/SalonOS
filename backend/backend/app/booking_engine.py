# Motore prenotazioni SalonOS v0.1


from backend.backend.app.services import lista_servizi
from backend.backend.app.calendar import verifica_disponibilita, crea_appuntamento



def trova_servizio(nome_servizio):

    servizi = lista_servizi()

    for servizio in servizi:

        if servizio["nome"].lower() == nome_servizio.lower():
            return servizio

    return None



def crea_prenotazione(cliente, servizio, data, ora):

    disponibile = verifica_disponibilita(
        data,
        ora
    )


    if disponibile:

        appuntamento = crea_appuntamento(
            cliente,
            servizio,
            data,
            ora
        )


        return {
            "stato": "confermata",
            "appuntamento": appuntamento
        }


    return {
        "stato": "non disponibile",
        "messaggio": "Orario già occupato"
    }
