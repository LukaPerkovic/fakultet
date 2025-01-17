import streamlit as st


st.title("Edukativna aplikacija za prikaz normalizacije i CRUD operacija")
st.write("**Ime:** Luka Perkovic")
st.write("**Broj indeksa:** 2023410428")
st.write("\n\n")
st.write("\n\n")


with st.container():
    st.subheader("Opis projekta")
    st.markdown("---")
    st.write(
        """
    Ova aplikacija ima za cilj edukaciju korisnika o procesu normalizacije podataka kao i CRUD operacijama. 
    """
    )

    st.write(
        """
    Normalizacija je iterativni proces tokom koga se vrsi reorganizacija baze podataka u cilju izbegavanja redundanse i povecanja stabilnosti baze podataka(Veinovic, Simic, Jevremovic, Tair; 2022).
    """
    )

    st.write(
        """
    CRUD (Create, Read, Update, Delete) operacije su fundamentale operacije u radu sa bazom podataka. Ove operacije omogucavaju 
    kreiranje novih unosa, citanje podataka, izmenu, i brisanje nezeljenih podataka.
    U ovoj aplikaciji, kroz prakticne primere, prikazano je kako se ove operacije izvode u teoretskom okruzenju.
    """
    )
    st.markdown("---")
st.write("\n\n")
