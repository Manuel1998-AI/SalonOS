# Receptionist AI SalonOS

def rispondi_cliente(messaggio):
    messaggio = messaggio.lower()

    if "prezzo" in messaggio or "costo" in messaggio:
        return "Posso aiutarti con le informazioni sui prezzi dei servizi del salone."

    if "appuntamento" in messaggio or "prenotare" in messaggio:
        return "Posso aiutarti a trovare un appuntamento disponibile."

    if "orari" in messaggio or "aperto" in messaggio:
        return "Posso fornirti gli orari di apertura del salone."

    return "Ciao! Sono l'assistente SalonOS. Come posso aiutarti?"
