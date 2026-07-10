# Receptionist AI SalonOS

from database import salone_config
from backend.app.services import lista_servizi


def rispondi_cliente(messaggio):

    messaggio = messaggio.lower()

    servizi = lista_servizi()

    for servizio in servizi:

        if servizio["nome"].lower() in messaggio:

            return (
                f"{servizio['nome']} costa "
                f"{servizio['prezzo']} euro "
                f"e dura circa "
                f"{servizio['durata']} minuti."
            )

    if "prezzo" in messaggio or "costo" in messaggio:

        return (
            "Dimmi quale servizio ti interessa "
            "e ti comunicherò prezzo e durata."
        )

    if "appuntamento" in messaggio or "prenotare" in messaggio:

        return (
            "Posso aiutarti a trovare "
            "un orario disponibile."
        )

    return (
        "Ciao! Sono l'assistente SalonOS. "
        "Come posso aiutarti?"
    )
