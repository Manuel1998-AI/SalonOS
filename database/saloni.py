# Gestione saloni SalonOS

saloni = [
    {
        "id": 1,
        "nome": "Salon Demo",
        "citta": "Milano",
        "lingua": "italiano"
    }
]


def trova_salone(salone_id):
    for salone in saloni:
        if salone["id"] == salone_id:
            return salone

    return None
