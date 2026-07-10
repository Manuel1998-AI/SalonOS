# Receptionist AI SalonOS

from database import salone_config


def rispondi_cliente(messaggio):
    messaggio = messaggio.lower()

    servizi = salone_config.salone["servizi"]
    nome_salone = salone_config.salone["nome"]

    for servizio in servizi:
        if servizio["nome"].lower() in messaggio:
            return (
                f"{servizio['nome']} costa "
                f"{servizio['prezzo']} euro "
                f"e dura circa {servizio['durata']} minuti."
            )

    parole_prezzo = [
        "prezzo",
        "costo",
        "quanto costa",
        "quanto viene",
        "tariffa"
    ]

    if any(parola in messaggio for parola in parole_prezzo):
        return (
            f"Sono l'assistente di {nome_salone}. "
            "Dimmi quale servizio ti interessa e ti comunicherò il prezzo."
        )

    if "appuntamento" in messaggio or "prenotare" in messaggio:
        return "Posso aiutarti a trovare un appuntamento disponibile."

    if "orari" in messaggio or "aperto" in messaggio:
        return "Posso fornirti gli orari del salone."

    return (
        f"Ciao! Sono l'assistente di {nome_salone}. "
        "Come posso aiutarti?"
    )
