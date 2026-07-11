from fastapi import APIRouter
from booking_engine import (
    verifica_disponibilita,
    crea_prenotazione
)

router = APIRouter()


@router.get("/prenotazioni")
def lista_prenotazioni():

    return {
        "stato": "Sistema prenotazioni attivo"
    }


@router.post("/prenotazioni")
def nuova_prenotazione(
    cliente: str,
    servizio: str,
    data: str,
    orario: str
):

    disponibile = verifica_disponibilita(
        data,
        orario
    )

    if disponibile:

        appuntamento = crea_prenotazione(
            cliente,
            servizio,
            data,
            orario
        )

        return {
            "stato": "Confermato",
            "appuntamento": appuntamento
        }

    return {
        "stato": "Non disponibile",
        "messaggio": "Orario già occupato"
    }
