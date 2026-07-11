# Gestione servizi SalonOS v0.1
# Collegato a database SQLite

from backend.backend.app.database import get_connection


def aggiungi_servizio(nome, prezzo, durata):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO servizi
        (nome, prezzo, durata)
        VALUES (?, ?, ?)
        """,
        (
            nome,
            prezzo,
            durata
        )
    )

    conn.commit()
    conn.close()

    return {
        "nome": nome,
        "prezzo": prezzo,
        "durata": durata
    }



def lista_servizi():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT nome, prezzo, durata
        FROM servizi
        """
    )

    risultati = cursor.fetchall()

    conn.close()


    servizi = []

    for servizio in risultati:

        servizi.append({
            "nome": servizio[0],
            "prezzo": servizio[1],
            "durata": servizio[2]
        })


    return servizi
