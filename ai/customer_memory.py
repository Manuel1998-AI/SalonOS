# Memoria Cliente AI SalonOS

clienti = {}


def salva_cliente(
    telefono,
    nome,
    ultimo_servizio,
    parrucchiere,
    ultima_visita
):

    clienti[telefono] = {
        "nome": nome,
        "ultimo_servizio": ultimo_servizio,
        "parrucchiere": parrucchiere,
        "ultima_visita": ultima_visita
    }


def cerca_cliente(telefono):

    return clienti.get(telefono)


def cliente_esiste(telefono):

    return telefono in clienti
