# Parser prenotazioni SalonOS


def estrai_dati_prenotazione(messaggio):

    dati = {
        "servizio": None,
        "giorno": None,
        "ora": None
    }


    parole = messaggio.lower()


    if "taglio" in parole:
        dati["servizio"] = "Taglio"


    if "barba" in parole:
        dati["servizio"] = "Barba"


    giorni = [
        "lunedi",
        "martedi",
        "mercoledi",
        "giovedi",
        "venerdi",
        "sabato",
        "domenica"
    ]


    for giorno in giorni:

        if giorno in parole:
            dati["giorno"] = giorno


    if "16" in parole:
        dati["ora"] = "16:00"


    if "17" in parole:
        dati["ora"] = "17:00"


    return dati
