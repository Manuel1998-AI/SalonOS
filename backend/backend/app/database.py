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


    conn.commit()
    conn.close()


def get_database_info():

    return {
        "database": DATABASE_NAME,
        "stato": "SQLite attivo"
    }
