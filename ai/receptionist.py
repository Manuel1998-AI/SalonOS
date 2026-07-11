# Receptionist AI SalonOS

from service import lista_servizi
from booking_engine import verifica_disponibilita, crea_prenotazione


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


    if "prenotare" in messaggio or "appuntamento" in messaggio:

        return (
            "Perfetto, posso aiutarti a prenotare. "
            "Dimmi quale servizio vuoi e il giorno preferito."
        )


    if "prezzo" in messaggio or "costo" in messaggio:

        return (
            "Dimmi quale servizio ti interessa "
            "e ti comunicherò prezzo e durata."
        )


    return (
        "Ciao! Sono l'assistente SalonOS. "
        "Come posso aiutarti?"
    )
