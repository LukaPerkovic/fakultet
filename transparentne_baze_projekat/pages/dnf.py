import pandas as pd
import streamlit as st

# Initialize session state if it doesn't exist
if "step" not in st.session_state:
    st.session_state.step = 0

# Denormalized Data (with repeating groups that need to be split for 1NF)
denormalized_data = pd.DataFrame(
    {
        "StudentID": [1, 2, 3],
        "StudentIme": ["Jovan", "Petar", "Sanja"],
        "PredmetOcena": [
            "Diskretna matematika:10, Racunarske mreze:9",
            "Operativni sistemi:7, Kriptologija:8",
            "Osnove OOP:6, Algoritmi:9",
        ],
    }
)

# Convert denormalized data to 1NF
data_1nf = pd.DataFrame(
    {
        "StudentID": [1, 1, 2, 2, 3, 3],
        "StudentIme": ["Jovan", "Jovan", "Petar", "Petar", "Sanja", "Sanja"],
        "PredmetIme": [
            "Diskretna matematika",
            "Racunarske mreze",
            "Operativni sistemi",
            "Kriptologija",
            "Osnove OOP",
            "Algoritmi",
        ],
        "Ocena": ["10", "9", "7", "8", "6", "9"],
    }
)

# Convert 1NF to 2NF by removing pRacunarske mrezeial dependencies
data_2nf_students = pd.DataFrame(
    {"StudentID": [1, 2, 3], "StudentIme": ["Jovan", "Petar", "Sanja"]}
)

data_2nf_courses = pd.DataFrame(
    {
        "PredmetID": [101, 102, 103, 104, 105, 106],
        "PredmetIme": [
            "Diskretna matematika",
            "Racunarske mreze",
            "Operativni sistemi",
            "Kriptologija",
            "Osnove OOP",
            "Algoritmi",
        ],
        "Profesor": [
            "Prof. Petrovic",
            "Prof. Jovanovic",
            "Prof. Popovic",
            "Prof. Nikolic",
            "Prof. Mitic",
            "Prof. Markovic",
        ],
    }
)

data_2nf_grades = pd.DataFrame(
    {
        "StudentID": [1, 1, 2, 2, 3, 3],
        "PredmetID": [101, 102, 103, 104, 105, 106],
        "Ocena": ["10", "9", "7", "8", "6", "9"],
    }
)

# Convert 2NF to 3NF by removing transitive dependencies (Profesor dependency)
data_3nf_students = data_2nf_students.copy()

data_3nf_courses = pd.DataFrame(
    {
        "PredmetID": [101, 102, 103, 104, 105, 106],
        "PredmetIme": [
            "Diskretna matematika",
            "Racunarske mreze",
            "Operativni sistemi",
            "Kriptologija",
            "Osnove OOP",
            "Algoritmi",
        ],
    }
)

data_3nf_professors = pd.DataFrame(
    {
        "ProfesorID": [1, 2, 3, 4, 5, 6],
        "ProfesorPrezime": [
            "Prof. Petrovic",
            "Prof. Jovanovic",
            "Prof. Popovic",
            "Prof. Nikolic",
            "Prof. Mitic",
            "Prof. Markovic",
        ],
    }
)

data_3nf_course_professors = pd.DataFrame(
    {"PredmetID": [101, 102, 103, 104, 105, 106], "ProfesorID": [1, 2, 3, 4, 5, 6]}
)

data_3nf_grades = data_2nf_grades.copy()


def display_normalization(step):
    st.write(f"### Korak {step + 1}")

    if step == 0:
        st.write("### Denormalizovani podaci")
        st.dataframe(denormalized_data)
    elif step == 1:
        st.write("### Prva Normalna Forma (1NF)")
        st.dataframe(data_1nf)
    elif step == 2:
        st.write("### Druga Normalna Forma (2NF)")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.write("**Tabela Studenti**")
            st.dataframe(data_2nf_students)
        with col2:
            st.write("**Tabela Predmeti**")
            st.dataframe(data_2nf_courses)
        with col3:
            st.write("**Tabela Ocene**")
            st.dataframe(data_2nf_grades)
    elif step == 3:
        st.write("### Treca Normalna Forma (3NF)")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.write("**Tabela Studenti**")
            st.dataframe(data_3nf_students)
        with col2:
            st.write("**Tabela Predmeti**")
            st.dataframe(data_3nf_courses)
        with col3:
            st.write("**Tabela Profesori**")
            st.dataframe(data_3nf_professors)
        with col4:
            st.write("**Tabela ProfesoriPredmeti**")
            st.dataframe(data_3nf_course_professors)
        st.write("**Tabela Ocene**")
        st.dataframe(data_3nf_grades)


st.title("Primer procesa normalizacije")

display_normalization(st.session_state.step)


def next_step():
    if st.session_state.step < 3:
        st.session_state.step += 1


def reset():
    st.session_state.step = 0


if st.session_state.step < 3:
    if st.session_state.step == 0:
        next_label = "1NF"
    elif st.session_state.step == 1:
        next_label = "2NF"
    elif st.session_state.step == 2:
        next_label = "3NF"
    st.button(next_label, on_click=next_step)
else:
    st.button("Ponovi", on_click=reset)

if st.session_state.step == 1:
    st.write("**Prva Normalna Forma (1NF)**:")
    st.write(
        "Svaki atribut mora imati iskljucivo atomske vrednosti, i grupe koje se ne ponavljaju."
    )
    st.write("Primer: Podeliti `PredmetOcena` kolonu u atomske jedinice.")
elif st.session_state.step == 2:
    st.write("**Druga Normalna Forma (2NF)**:")
    st.write(
        "Delimicne zavisnosti se moraju eliminisati, odnosno atributi moraju biti funkcijsko zavisni."
    )
    st.write(
        "Primer: Napraviti odvojenu tabelu `Studenti` i `Predmeti`, samo sa referencom kljuca u `Ocene` tabeli."
    )
elif st.session_state.step == 3:
    st.write("**Treca Normalna Forma (3NF)**:")
    st.write("Ukloniti tranzitivne zavisnosti.")
    st.write(
        "Primer: Pomeriti `Profesor` atribut u zasebnu `Profesori` tabelu i povezati predmete putem `PredmetProfesor` tabele."
    )
