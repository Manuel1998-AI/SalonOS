# Receptionist AI SalonOS

def rispondi_cliente(messaggio):
    messaggio = messaggio.lower()

    parole_prezzo = [
        "prezzo",
        "costo",
        "quanto costa",
        "quanto viene",
        "tariffa"
    ]

    parole_prenotazione = [
        "appuntamento",
        "prenotare",
        "prenota",
        "avete posto",
        "disponibilità"
    ]

    parole_orari = [
        "orari",
        "aperto",
        "chiuso"
    ]

    if any(parola in messaggio for parola in parole_prezzo):
        return "Posso aiutarti con i prezzi dei servizi del salone."

    if any(parola in messaggio for parola in parole_prenotazione):
        return "Posso aiutarti a trovare un appuntamento disponibile."

    if any(parola in messaggio for parola in parole_orari):
        return "Posso fornirti gli orari di apertura del salone."

    return "Ciao! Sono l'assistente SalonOS. Dimmi pure come posso aiutarti."
