# Database SQLite SalonOS v0.1

import sqlite3


DATABASE_NAME = "salonos.db"


def get_connection():

    conn = sqlite3.connect(DATABASE_NAME)

    return conn



def inizializza_database():

    conn = get_connection()
    cursor = conn.cursor()


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS saloni (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        citta TEXT,
        lingua TEXT
    )
    """)


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS clienti (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        telefono TEXT UNIQUE
    )
    """)


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS servizi (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        prezzo INTEGER,
        durata INTEGER
    )
    """)


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS appuntamenti (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cliente TEXT,
        servizio TEXT,
        data TEXT,
        orario TEXT
    )
    """)


    # Servizi iniziali SalonOS

    servizi_base = [
        ("Taglio uomo", 25, 30),
        ("Barba", 15, 20),
        ("Taglio donna", 40, 60),
        ("Colore", 50, 90)
    ]


    for servizio in servizi_base:

        cursor.execute(
            """
            SELECT * FROM servizi
            WHERE nome = ?
            """,
            (servizio[0],)
        )

        esiste = cursor.fetchone()


        if not esiste:

            cursor.execute(
                """
                INSERT INTO servizi
                (nome, prezzo, durata)
                VALUES (?, ?, ?)
                """,
                servizio
            )


    conn.commit()

    conn.close()



def get_database_info():

    return {
        "database": DATABASE_NAME,
        "stato": "SQLite attivo"
    }
