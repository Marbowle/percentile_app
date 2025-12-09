import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

if 'form_submitted' not in st.session_state:
    st.session_state['form_submitted'] = False

st.title("To jest strona na której będziesz mógł obliczyć na którym punkcie centylowym jestes")
st.sidebar.markdown("O autorach")

data = {
    'age': [83, 38, 12, 23],
    'sex': ['female', 'male', 'male', 'female'],
    'distance': [8, 1, 11, 22]
}

df = pd.DataFrame(data)
df['distance'] = df['distance'] * 1000

if st.session_state['form_submitted'] == False:
    sex = st.selectbox("Choose your sex : ", ("female", "male"), index=None, placeholder="Select your sex ")
    age = st.number_input("Insert your age: ", min_value=0, max_value=100, step=1, placeholder="Insert your age ")
    distance = st.number_input("Insert your distance: ", min_value=0, step=10, placeholder="Insert your distance ")
    conf_button = st.button("Confirm info")

    if conf_button:
        st.session_state['form_submitted'] = True
        st.session_state.sex = sex
        st.session_state.age = age
        st.session_state.distance = distance
        st.rerun()

else:
    # obliczenia do wykresu
    sex = st.session_state.sex
    age = st.session_state.age
    distance = st.session_state.distance
    df_filtered = df[df['sex'] == sex]
    total_people = len(df_filtered)
    people_worse = len(df_filtered[df_filtered['distance'] < distance])
    percentile = (people_worse / total_people) * 100
    st.write(f"Twój wynik jest lepszy od {percentile:.0f}% osób biorących udział w tym badaniu ")
    # wykres
    fig, ax = plt.subplots()
    ax.scatter(df_filtered['age'], df_filtered['distance'], color='blue')
    ax.scatter(age, distance, color='red')
    st.pyplot(fig)
    if st.button("Edit info"):
        st.session_state['form_submitted'] = False
        st.rerun()








