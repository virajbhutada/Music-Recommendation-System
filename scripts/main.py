
import streamlit as st
import pickle
import pandas as pd
import webbrowser
# import link_button
# import HYPERLINK

no_recommend = st.sidebar.slider ( 'How many Recommendations you want?', 5, 20, 5)
st.sidebar.write ( "I want ", no_recommend, 'Recommendations' )
def recommend(musics):
    Index = music[music['Track_Name'] == musics].index[0]
    distances = sorted(list(enumerate(similarity[Index])), reverse=True, key=lambda x: x[1])
    # no_recommend = int(input("How many recommandations you want? "))

    recommended_music_names=[]
    for i in distances [0:no_recommend]:
       recommended_music_names.append(music.iloc[i[0]].Track_Name)
    return recommended_music_names


st.sidebar.title("Menu")
about = 'http://localhost:8501'
if st.sidebar.button('About System'):
    webbrowser.open_new_tab(about)

All_Tracks = 'http://localhost:8503'
if st.sidebar.button('All Tracks'):
    webbrowser.open_new_tab(All_Tracks)

st.title( " Music Recommender system " )
st.text('P-92(Group-6)')
music = pickle.load(open('music.pkl', 'rb'))
musicdf= pd.DataFrame(music)
similarity = pickle.load(open('similarity.pkl', 'rb'))

music_list = musicdf['Track_Name'].values
selected_music_name = st.selectbox("Search Music: Type or Select a Music from the Dropdown", music_list)


if st.button('Get Recommendations'):
    recommendations = recommend(selected_music_name)
    for i in recommendations:
        index_no = (musicdf [musicdf ["Track_Name"] == i].index [0]) #location access in url of each song
        preview_link = musicdf["Track_Preview"][index_no]
        # preview_button = st.button("preview link", preview_link)
        st.write(i, "  -----  ", (musicdf ['Track_URI'] [index_no]), "-----", preview_link)
        # st.write("Play Preview", musicdf["Track_Preview"][index_no])
        # if st.button("Play Preview"):
        #  play = musicdf["Track_Preview"][index_no]
        #







# cols = st.columns(2)
#     cols[0].write("Track Name")
#     cols[0].write(f'{i}')
#     cols[1].write("Track URL")
#     url = (musicdf [musicdf ["Track_Name"] == i].index [0])
#     cols[1].write(f'{musicdf ["Track_URI"][url]}')






# df = pd.DataFrame(['http://google.com', 'http://duckduckgo.com'])
# def make_clickable(val): return '<a href="{}">{}</a>'.format(val,val)
# df.style.format(make_clickable)
# st.markdown(df)