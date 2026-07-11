# Receptionist AI SalonOS

from service import lista_servizi
from booking_engine import verifica_disponibilita, crea_prenotazione
from booking_parser import estrai_dati_prenotazione


def rispondi_cliente(messaggio):

    messaggio = messaggio.lower()

    # Analizza eventuale richiesta di prenotazione
    dati_prenotazione = estrai_dati_prenotazione(messaggio)

    servizi = lista_servizi()


    # Controllo informazioni servizi
    for servizio in servizi:

        if servizio["nome"].lower() in messaggio:

            return (
                f"{servizio['nome']} costa "
                f"{servizio['prezzo']} euro "
                f"e dura circa "
                f"{servizio['durata']} minuti."
            )


    # Gestione prenotazione
    if dati_prenotazione["servizio"]:

        if dati_prenotazione["giorno"] and dati_prenotazione["ora"]:

            disponibile = verifica_disponibilita(
                dati_prenotazione["giorno"],
                dati_prenotazione["ora"]
            )


            if disponibile:

                appuntamento = crea_prenotazione(
                    "Cliente",
                    dati_prenotazione["servizio"],
                    dati_prenotazione["giorno"],
                    dati_prenotazione["ora"]
                )

                return (
                    "Perfetto! Ho preparato la tua prenotazione:\n"
                    f"Servizio: {appuntamento['servizio']}\n"
                    f"Giorno: {appuntamento['data']}\n"
                    f"Ora: {appuntamento['ora']}"
                )


        return (
            "Perfetto, posso aiutarti con la prenotazione. "
            "Mi serve solo il giorno e l'orario preferito."
        )


    if "prezzo" in messaggio or "costo" in messaggio:

        return (
            "Dimmi quale servizio ti interessa "
            "e ti comunicherò prezzo e durata."
        )


    if "appuntamento" in messaggio or "prenotare" in messaggio:

        return (
            "Certo, posso aiutarti a prenotare. "
            "Dimmi quale servizio vuoi scegliere."
        )


    return (
        "Ciao! Sono l'assistente SalonOS. "
        "Come posso aiutarti?"
    )
