# Edukativna aplikacija za prikaz normalizacije i CRUD operacija

**Ime:** Luka Perkovic  
**Broj indeksa:** 2023410428

## Opis projekta

Ova aplikacija ima za cilj edukaciju korisnika o procesu normalizacije podataka kao i CRUD operacijama. 

Normalizacija je iterativni proces tokom koga se vrsi reorganizacija baze podataka u cilju izbegavanja redundanse i povecanja stabilnosti baze podataka(Veinovic, Simic, Jevremovic, Tair; 2022).

CRUD (Create, Read, Update, Delete) operacije su fundamentale operacije u radu sa bazom podataka. Ove operacije omogucavaju 
kreiranje novih unosa, citanje podataka, izmenu, i brisanje nezeljenih podataka.
U ovoj aplikaciji, kroz prakticne primere, prikazano je kako se ove operacije izvode u teoretskom okruzenju.

Pomocu ove aplikacije korisnici ce bolje razumeti:
- Proces normalizacije i njene faze (1NF, 2NF, 3NF).
- Osnovne CRUD operacije i njihovo izvodjenje.
- Prednosti pravilno normalizovanih podataka.

## Instalacija

1. Klonirajte repozitorijum:
    ```sh
    git clone https://github.com/LukaPerkovic/fakultet/transparentne_baze_projekat.git
    ```

2. Podesite virtuelno okruzenje:
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # (Linux/Mac)
    .\venv\Scripts\activate  # (Windows)
    ```

3. Instalirajte `requirements.txt`:
    ```sh
    pip install -r requirements.txt
    ```

4. Pokrenite Streamlit aplikaciju:
    ```sh
    streamlit run App.py
    ```