import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
import os

st.set_option('deprecation.showPyplotGlobalUse', False)

st.title('Exploration des Data avec Streamlit')

# DATE_COLUMN = 'date/time'
# DATA_URL = ('https://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz')
DATA_URL = 'ressource/Pokemon.csv'

# set cache request


@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    def lowercase(x): return str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    # data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

# function for file_selector


def file_selector(folder_path='./ressource'):
    filenames = os.listdir(folder_path)
    selected_filename = st.selectbox("Choissisez le fichier ", filenames)
    return os.path.join(folder_path, selected_filename)


filename = file_selector()
st.info("Vous avez choisi {}".format(filename))

# Read Data
df = pd.read_csv(filename)

# Show Columns
st.subheader(
    "Afficher le dataset chargé suivant un nombre de ligne entrées par l’utilisateur")
number = st.number_input("Choissez un nombre")
if st.button("Show dataset sample"):
    st.write(df.head(int(number)))

# Show Columns
st.subheader("Afficher le nom des colonnes du dataset")
if st.button("Montre les noms des colonnes"):
    st.write(df.columns)

# Show Columns
st.subheader(
    "Afficher le type des colonnes du dataset ainsi que les colonnes sélectionnées")
if st.button("Montre les types des colonnes"):
    st.write(df.dtypes())

# Show Columns
st.subheader("La shape du dataset, par lignes et par colonnes")
if st.button("Show shape"):
    st.write(df.describe())

# Show Columns
st.subheader("Afficher les statistiques descriptives du dataset")
if st.button("Summary"):
    st.write(df.describe().T)

# Show graph heatmap /
st.subheader("Afficher plusieurs type de graphique dans une partie visualisation avec notamment : *Une heatmap des corrélations avec Matplotlib et Seaborn (avec les valeurs annotés) | *Un graphique en barres afin de visualiser la taille du dataset par caractéristiques (on pourra notamment grouper les données afin d’avoir des graphiques plus précis) ")
if st.button("HeatMap"):
    dfHeatmap = sns.heatmap(df.corr(), annot=True)
    dfHeatmap.set_title('Heatmap')
    st.write(dfHeatmap)
    st.pyplot()

# Show Histrogram
dfColumnsName = df.columns.tolist()
selectedColumns = st.multiselect('Colonne à afficher', dfColumnsName)
if st.button('Show graph'):
    dfHist = df[selectedColumns].plot(kind='hist')
    st.write(dfHist)
    st.pyplot()

# Show Columns
st.subheader("Sélectionner le type de graphique à tracer")
selected_graphtype = st.selectbox("Choissisez le fichier ", "a")

# Show Columns
st.subheader(
    "Sélectionner des colonnes dans le jeux de données afin de générer le graphique")
selected_col1 = st.selectbox("Choissisez la première colonne ", df.columns)
selected_col2 = st.selectbox("Choissisez la deuxième colonne ", df.columns)

# Show Columns
st.subheader("**(bonus)**À noter que suivant certain jeux de données il y aura des graphiques qui n’auront pas de sens capturez les dans des exceptions 🧐")
