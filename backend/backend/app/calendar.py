# Calendario SalonOS

appuntamenti = []


def verifica_disponibilita(data, orario):

    for appuntamento in appuntamenti:
        if (
            appuntamento["data"] == data
            and appuntamento["orario"] == orario
        ):
            return False

    return True


def crea_appuntamento(cliente, servizio, data, orario):

    nuovo_appuntamento = {
        "cliente": cliente,
        "servizio": servizio,
        "data": data,
        "orario": orario
    }

    appuntamenti.append(nuovo_appuntamento)

    return nuovo_appuntamento
