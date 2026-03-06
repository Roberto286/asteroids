# Asteroids

Un classico gioco Asteroids implementato in Python con Pygame a scopo didattico.

## Descrizione

Questo progetto è una ricreazione del celebre gioco arcade Asteroids. Il giocatore controlla un'astronave che deve distruggere gli asteroidi sparando proiettili, evitando le collisioni. Gli asteroidi si dividono in pezzi più piccoli quando colpiti, aumentando la difficoltà.

## Caratteristiche

- Controllo intuitivo dell'astronave con rotazione e movimento
- Sistema di sparo con cooldown
- Asteroidi che si dividono progressivamente
- Collisioni tra astronave, proiettili e asteroidi
- Spawn automatico di nuovi asteroidi
- Logging degli eventi di gioco per analisi

## Requisiti

- Python 3.13+
- Pygame 2.6.1

## Installazione

```bash
# Clona il repository
git clone https://github.com/roberto286/asteroids.git
cd asteroids

# Crea un ambiente virtuale e installa le dipendenze
python -m venv .venv
source .venv/bin/activate  # Su Windows: .venv\Scripts\activate
pip install pygame
```

## Come Giocare

```bash
python src/main.py
```

### Controlli

- **W**: Muovi avanti
- **S**: Muovi indietro
- **A**: Ruota a sinistra
- **D**: Ruota a destra
- **SPAZIO**: Spara

## Struttura del Progetto

```
asteroids/
├── src/
│   ├── main.py          # Entry point del gioco e game loop
│   ├── player.py        # Classe per l'astronave del giocatore
│   ├── asteroid.py      # Classe per gli asteroidi
│   ├── asteroidfield.py # Generatore di asteroidi
│   ├── shot.py          # Classe per i proiettili
│   ├── circleshape.py   # Classe base per oggetti circolari
│   └── logger.py        # Sistema di logging eventi
├── constants.py         # Costanti di gioco configurabili
└── pyproject.toml       # Configurazione del progetto
```

## Obiettivo Didattico

Questo progetto è stato creato per scopi educativi e dimostra:

- Programmazione orientata agli oggetti in Python
- Gestione del game loop con Pygame
- Sistema di sprite e gruppi
- Rilevamento delle collisioni
- Gestione dell'input da tastiera
- Vettori 2D e trasformazioni geometriche

## Licenza

Progetto didattico open source.
