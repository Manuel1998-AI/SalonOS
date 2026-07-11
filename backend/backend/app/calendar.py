# Calendario SalonOS v0.1
# Collegato a database SQLite

from backend.backend.app.database import get_connection


def verifica_disponibilita(data, orario):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT * FROM appuntamenti
        WHERE data = ? AND orario = ?
        """,
        (data, orario)
    )

    risultato = cursor.fetchone()

    conn.close()

    if risultato:
        return False

    return True



def crea_appuntamento(cliente, servizio, data, orario):

    conn = get_connection()
    cursor = conn.cursor()


    cursor.execute(
        """
        INSERT INTO appuntamenti
        (cliente, servizio, data, orario)
        VALUES (?, ?, ?, ?)
        """,
        (
            cliente,
            servizio,
            data,
            orario
        )
    )


    conn.commit()
    conn.close()


    return {
        "cliente": cliente,
        "servizio": servizio,
        "data": data,
        "orario": orario
    }
