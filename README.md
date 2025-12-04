# Wave Survival RPG

[CONSIGNES](CONSIGNES.md)

> **Note:** 
> This README is in English because  I don't like writing docs in French lol. 
> The game itself is in French though !

A turn-based RPG where you build a team of 3 characters and survive waves of increasingly difficult monsters. 
It has class-based abilities, critical hits, and progressive difficulty scaling.

## What the heck is this?

A MongoDB-powered wave survival game where:
- Pick 3 characters from 10 unique classes (with cool unique abilities)
- You fight monsters in turn-based combat
- The waves progressively get harder
- Your team gets stronger, but monsters scale faster
- Eventually, you'll just die. Your score is how many waves you survived, pick your characters wisely.

## Installation

### Prerequisites

- Python 3.whatever
- MongoDB running locally on port 27017 (you can change the port in `db_init.py`)

### Setup

```bash
# clone my repo : 
git clone https://github.com/Aqu1tain/AdminBDD-SDV.git
cd AdminBDD-SDV

# install the dep :
pip install pymongo

# be sure MongoDB is running
# then start the game
python3 src/main.py
```

I wont explain here how the game flows, that's up to you to discover.

## Project Structure
```
src/
- constants/config.py    # game balance and settings
- constants/messages.py  # all UI text strings
- main.py                # entry point and menu
- models.py              # Entity, Character, Monster classes
- game.py                # combat logic and wave system
- abilities.py           # special ability implementations
- utils.py               # helper functions
- db_init.py             # database initialization
```

## Development
This was built for a Database Administration course at SUP DE VINCI. 
The goal was to practice MongoDB operations while making something fun.

## License
Made for educational purposes. Feel free to do whatever you want with it.