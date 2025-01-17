import pandas as pd
import streamlit as st


# Initialize session state if it doesn't exist
if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame(
        {"id": [1, 2, 3], "ime": ["Jovan", "Petar", "Sanja"], "godine": [25, 30, 35]}
    )
    st.session_state.next_id = 4
    st.session_state.sql_statements = []


# Function to reset SQL statements
def reset_sql_statements():
    st.session_state.sql_statements = []


# Function to add a new row
def add_row(name, age):
    row_id = st.session_state.next_id
    new_row = pd.DataFrame({"id": [row_id], "ime": [name], "godine": [age]})
    st.session_state.data = pd.concat(
        [st.session_state.data, new_row], ignore_index=True
    )
    st.session_state.next_id += 1
    reset_sql_statements()
    st.session_state.sql_statements.append(
        f"INSERT INTO Studenti (id, ime, godine) VALUES ({row_id}, '{name}', {age});"
    )


# Function to delete a row by id
def delete_row(row_id):
    st.session_state.data = st.session_state.data[st.session_state.data["id"] != row_id]
    reset_sql_statements()
    st.session_state.sql_statements.append(f"DELETE FROM Studenti WHERE id = {row_id};")


# Function to edit a row
def edit_row(row_id, name, age):
    st.session_state.data.loc[
        st.session_state.data["id"] == row_id, ["ime", "godine"]
    ] = [name, age]
    reset_sql_statements()
    st.session_state.sql_statements.append(
        f"UPDATE Studenti SET ime = '{name}', godine = {age} WHERE id = {row_id};"
    )


# Layout the app with three columns with more space given to SQL Commands and Current Data
st.title("CRUD operacije sa SQL komandama")

# Three-column layout with the first column narrower
left_column, middle_column, right_column = st.columns([1, 2, 2])

with left_column:
    st.header("CRUD Operacije")

    # Define a consistent layout for CRUD operations
    st.subheader("Dodaj red")
    with st.form(key="add_form"):
        name = st.text_input("Ime")
        age = st.number_input("Godine", min_value=0)
        add_submit_button = st.form_submit_button(label="Dodaj")
        if add_submit_button:
            add_row(name, age)

    st.subheader("Promeni red")
    with st.form(key="edit_form"):
        row_id = st.number_input("Promeni ID", min_value=1, format="%d", step=1)
        new_name = st.text_input("Novo ime")
        new_age = st.number_input("Nove godine", min_value=0)
        edit_submit_button = st.form_submit_button(label="Promeni")
        if edit_submit_button:
            edit_row(row_id, new_name, new_age)

    st.subheader("Izbrisi red")
    with st.form(key="delete_form"):
        row_id_to_delete = st.number_input(
            "Izbrisi ID", min_value=1, format="%d", step=1
        )
        delete_submit_button = st.form_submit_button(label="Izbrisi")
        if delete_submit_button:
            delete_row(row_id_to_delete)

with middle_column:
    st.header("SQL komanda")
    for sql in st.session_state.sql_statements:
        st.code(sql, language="sql")

with right_column:
    st.header("Podaci")
    st.dataframe(st.session_state.data, use_container_width=True)
