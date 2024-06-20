
import streamlit as st

st.write("check out this [link](https://share.streamlit.io/virajbhutada/streamlit_webapps/main/MC_pi/streamlit_app.py)")

import streamlit as st
import pickle
import pandas as pd
# from bokeh.models import HTMLTemplateFormatter



def recommend(musics):
    Index = music[music['Track_Name'] == musics].index[0]
    # no_recommend = st.sidebar.slider ( 'How many recommendation you want?', 5, 20)
    # st.sidebar.write ( "I want ", no_recommend, 'Recommendations' )
    distances = sorted(list(enumerate(similarity[Index])), reverse=True, key=lambda x: x[1])
    # no_recommend = int(input("How many recommandations you want? "))

    recommended_music_names=[]
    for i in distances [0:10]:
       recommended_music_names.append(music.iloc[i[0]].Track_Name)
    return recommended_music_names

st.header( " Music Recommender system " )
st.text('P-92(Group-6)')
music = pickle.load(open('music.pkl', 'rb'))
musicdf= pd.DataFrame(music)
similarity = pickle.load(open('similarity.pkl', 'rb'))

music_list = musicdf['Track_Name'].values
selected_music_name = st.selectbox("Search Music: Type or Select a Music from the Dropdown", music_list)


if st.button('Get Recommendations'):
    recommendations = recommend(selected_music_name)
    for i in recommendations:
     url = (musicdf[musicdf["Track_Name"] == i].index[0])
     st.write (i, "  =  ",  (musicdf ['Track_URI'][url]), unsafe_allow_html=False )
# st.write("check this [play](spotify:track:4wDkM4eonFlMpw07mQxZbM)")

