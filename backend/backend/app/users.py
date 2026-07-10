# Gestione utenti SalonOS

utenti = [
    {
        "id": 1,
        "nome": "Admin Demo",
        "ruolo": "proprietario",
        "salone_id": 1
    }
]


def trova_utente(utente_id):
    for utente in utenti:
        if utente["id"] == utente_id:
            return utente

    return None
