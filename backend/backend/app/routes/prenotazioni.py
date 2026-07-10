from fastapi import APIRouter
from calendar import verifica_disponibilita, crea_appuntamento

router = APIRouter()


@router.get("/prenotazioni")
def lista_prenotazioni():
    return {
        "prenotazioni": "Sistema attivo"
    }


@router.post("/prenotazioni")
def nuova_prenotazione(
    cliente: str,
    servizio: str,
    data: str,
    orario: str
):

    disponibile = verifica_disponibilita(data, orario)

    if disponibile:
        appuntamento = crea_appuntamento(
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
