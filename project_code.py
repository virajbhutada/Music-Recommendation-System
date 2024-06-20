# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

#importing and merging two csv files
df = pd.concat(
    map(pd.read_csv,['meditationandrelaxation1.csv', 'meditationandrelaxation2.csv', 'meditationandrelaxation3.csv', 'meditationandrelaxation4.csv', 'meditationandrelaxation5.csv']), ignore_index=True)
print(df)

df.head()

"""## EDA (Exploratory Data Analysis)"""

#finding total NaN values in dataset
df.isna().sum()

#displaying all rows having all NaN values
df[df.isnull().any(axis=1)]

#coverting dtype of object to datetime
df['Album Release Date'] = pd.to_datetime(df['Album Release Date'])
df.dtypes

df.shape

df.describe()

#displaying column name
df.columns

df.dtypes

#creating random user names
nodes=['{0}'.format(i) for i in range(1,151)]

print(nodes)

import numpy as np

#inserting random user name
df["user"] = np.random.choice(nodes, size=len(df))

df.dtypes

df.head()

df.user

df

#droping unwanted columns in the dataset
music=df.drop(["Artist URI(s)","Album URI","Album Artist URI(s)","Album Artist Name(s)","Album Image URL","Disc Number","Track Preview URL"],axis=1)
music.columns

#poping last user column
first_column=music.pop("user")

music.columns

#inserting user column at first place
music.insert(0,"user", first_column)

music.columns

len(music)

df.dtypes

#coverting dtype of object to datetime
music['Added At'] =pd.to_datetime(music['Added At'])

df.dtypes

#extrating date from datetime format
music["Added At"]=music["Added At"].dt.date

music["Added At"]

#coverting datatype (object to datetime), displaying only date
music['Added At'] = pd.to_datetime(music['Added At'])

#filling Na values in Time Signature with 0
music['Time Signature'] = music['Time Signature'].fillna(0)

#converting datatype of Time Signature column from float to int
music['Time Signature'] = music['Time Signature'].astype(np.int64)

music.dtypes

music

#rename all the columns which have space in between bcs it considers as a series type

music=music.rename(columns= {"Track URI":"Track_URI","Track Name":"Track_Name","Artist Name(s)":"Artist_Name","Album Name":"Album_Name","Album Release Date":"Album_Release_Date","Track Number":"Track_Number","Track Duration (ms)":"Track_Duration(ms)","Added By":"Added_By","Added At":"Added_At","Time Signature":"Time_Signature","user":"user_id"})
#df.columns = df.columns.str.replace(' ','_')

music.head()

music.sort_values('user_id', ascending=True)

music["Added_At"]

"""#### checking Na values in columns"""

music["Added_At"].isna().sum()

music["Album_Release_Date"].isna().sum()

date_mean=(music.Album_Release_Date-music.Album_Release_Date.min()).mean()+music.Album_Release_Date.min()

date_mean

d='2019-01-12 01:07:39.060402688'
date=pd.to_datetime(d).date()
print(date)

end = pd.to_datetime('2019-01-12')
music["Album_Release_Date"]=music["Album_Release_Date"].fillna(end)

music

#Replacing NaN values in Danceability column with mean value as column is of contineous type and non-categorical
Danceability_mean=music["Danceability"].mean()
music['Danceability'] = music['Danceability'].fillna(Danceability_mean)

#Replacing NaN values in Energy column with mean value as column is of contineous type and non-categorical
Energy_mean=music["Energy"].mean()
music['Energy'] = music['Energy'].fillna(Energy_mean)

#Replacing NaN values in key column with mean value as column is of contineous type and non-categorical
Key_mean=music["Key"].mean()
music['Key'] = music['Key'].fillna(Key_mean)

#Replacing NaN values in loudness column with mean value as column is of contineous type and non-categorical
Loudness_mean=music["Loudness"].mean()
music['Loudness'] = music['Loudness'].fillna(Loudness_mean)

#Replacing NaN values in Mode column with mean value as column is of contineous type and non-categorical
Mode_mean=music["Mode"].mean()
music['Mode'] = music['Mode'].fillna(Mode_mean)

#Replacing NaN valuesin Speechiness column with mean value as column is of contineous type and non-categorical
Speechiness_mean=music["Speechiness"].mean()
music['Speechiness'] = music['Speechiness'].fillna(Speechiness_mean)

#Replacing NaN values in Acousticness column with mean value as column is of contineous type and non-categorical
Acousticness_mean=music["Acousticness"].mean()
music['Acousticness'] = music['Acousticness'].fillna(Acousticness_mean)

#Replacing NaN values in Instrumentalness column with mean value as column is of contineous type and non-categorical
Instrumentalness_mean=music["Instrumentalness"].mean()
music['Instrumentalness'] = music['Instrumentalness'].fillna(Instrumentalness_mean)

#Replacing NaN values in Liveness column with mean value as column is of contineous type and non-categorical
Liveness_mean=music["Liveness"].mean()
music['Liveness'] = music['Liveness'].fillna(Liveness_mean)

#Replacing NaN values in valence column with mean value as column is of contineous type and non-categorical
Valence_mean=music["Valence"].mean()
music['Valence'] = music['Valence'].fillna(Valence_mean)

#Replacing NaN values in Tempo column with mean value as column is of contineous type and non-categorical
Tempo_mean=music["Tempo"].mean()
music['Tempo'] = music['Tempo'].fillna(Tempo_mean)

#Replacing NaN values in Time_Signature column with mode value as column is categorical
Time_Signature_mode=music["Time_Signature"].mode()
Time_Signature_mode

music['Time_Signature'] = music['Time_Signature'].replace(0, 4)

music.isna().sum()

music

music=music.sort_values(by='Album_Release_Date',ascending=False)
music

#from sklearn.preprocessing import StandardScaler
#array= StandardScaler().fit_transform(music[['Danceability', 'Energy','Key','Loudness','Mode','Speechiness','Acousticness','Instrumentalness','Liveness','Valence','Tempo']])
#array

#stmusic= pd.DataFrame(array, columns=['Danceability', 'Energy','Key','Loudness','Mode','Speechiness','Acousticness','Instrumentalness','Liveness','Valence','Tempo'])
#stmusic

music.dtypes

#music.drop(music.iloc[:, 11:22], inplace = True, axis = 1)

music

#music['tmp'] = 1
#stmusic['tmp'] = 1

#music1= pd.merge(music, stmusic, on=['tmp'])
#music=music1.drop('tmp', axis=1)
#music

music.dtypes

"""### Visualizing the Data"""

import matplotlib.pyplot as plt
from matplotlib.pyplot import hist
import seaborn as sns
#hist=music.plot(x="Track_Name", y="Popularity", kind='hist')
plt.figure(figsize=(100,30))
plt.bar(music['Track_Name'], music['Popularity'], align='center')
plt.xlabel('Track_Name')
plt.xticks(rotation=90)
plt.ylabel('Popularity',fontsize=80)
plt.yticks(fontsize=50)
plt.title('Bar Chart',fontsize=120)
plt.show()

#counted popularity
popularity_count=music.groupby('Track_Name')['Popularity'].count().sort_values(ascending=False)
popularity_count

#creating a dataframe with popularity count
popularity_mean_count= pd.DataFrame(music.groupby('Track_Name')['Popularity'].mean())
popularity_mean_count

#adding popularity mean count to existing dataframe with popularity
popularity_mean_count['popularity_count'] = pd.DataFrame(music.groupby('Track_Name')['Popularity'].count())

popularity_mean_count

# Commented out IPython magic to ensure Python compatibility.
sns.set_style('dark')
# %matplotlib inline

plt.figure(figsize=(20,10))
plt.xlabel("popularity count", fontsize=20)
plt.ylabel("Track count", fontsize=20)
plt.title("Histogram of track count vs popularity", fontsize=30)
plt.rcParams['patch.force_edgecolor'] = True
popularity_mean_count['popularity_count'].hist(bins=50)

#jointplot
plt.figure(figsize=(8,6))
plt.rcParams['patch.force_edgecolor'] = True
sns.jointplot(x='Popularity', y='popularity_count', data=popularity_mean_count, alpha=0.4)

"""## Top Ten Popular Songs"""

#count how many rows we have by song, we show only the ten more popular songs
top_ten = music.groupby('Track_Name')['Popularity'].count().reset_index().sort_values(['Popularity', 'Track_Name'], ascending = [0,1])
top_ten['top_ten']  = round(top_ten['Popularity'].div(top_ten['Popularity'].sum())*100, 2)

top_ten = top_ten[:10]
top_ten

labels = top_ten['Track_Name'].tolist()
counts = top_ten['Popularity'].tolist()

plt.figure()
sns.barplot(x=counts, y=labels, palette='Set3')
sns.despine(left=True, bottom=True)

pip install plotly

import plotly.express as px
sound=px.data.gapminder()
sound_features=['Danceability', 'Energy', 'Key', 'Loudness', 'Mode', 'Speechiness', 'Acousticness', 'Instrumentalness', 'Liveness', 'Valence', 'Tempo']
figure=px.line(music, x="Album_Release_Date", y=sound_features)
figure.show()

# how many songs a user listend to
music_grouped=music.groupby(['user_id','Track_Name'])
music_grouped.first()

"""# Finding Similarities of Users by Pivot Table"""

music_pivot=music.pivot_table(index='user_id',columns='Track_Name', values='Popularity').reset_index(drop=True)
music_pivot

# Impute those NaNs with 0 values
music_pivot.fillna(0,inplace=True)
music_pivot

from sklearn.metrics import pairwise_distances
from scipy.spatial.distance import cosine,correlation

# Calculating Cosine Similarity between Users on array data
music_sim=1-pairwise_distances(music_pivot.values,metric='cosine')
music_sim

# Store the results in a dataframe format
music_sim1=pd.DataFrame(music_sim)
music_sim1

# Set the index and column names to music ids
#similarity of each users individually
music_sim1.index=music['user_id'].unique()
music_sim1.columns=music['user_id'].unique()
music_sim1

#every user is similar to themselves so not considering it
# Nullifying diagonal values
np.fill_diagonal(music_sim,0)
music_sim1

# displaying Most Similar Users
music_sim1.idxmax(axis=1)

music1=music.sort_index()
music1

music1.head(10)

"""## PCA"""

from sklearn.decomposition import PCA

# define transform
pca = PCA(n_components=1)
# prepare transform on dataset
pca.fit(music.iloc[:,12:23])
# apply transform to dataset
transformed = pca.transform(music.iloc[:,12:23])

transformed

pca.components_

# Final Dataframe
final_df=pd.DataFrame(transformed)
final_df

pca1= final_df.rename(columns={0: 'PC1'})
pca1

pc= music1.append(pca1, ignore_index=False)
pc

pc['PC1'].isnull()

"""## Music Similarity"""

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=500,stop_words='english')

vector = cv.fit_transform(music1['Track_Name'].unique()).toarray()

vector.shape

from sklearn.metrics.pairwise import cosine_similarity
similarity = cosine_similarity(vector)
similarity

similarity[2]

#index of perticular song
music1[music1['Track_Name'] == 'Yoga Top 100'].index[0]

"""# Deployment"""

def recommend(music):
    index = music1[music1['Track_Name'] == music].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])

    for i in distances[1:11]:
        a=[(music1.iloc[i[0]].Track_Name)],[(music1.iloc[i[0]].Artist_Name)]
#         data= pd.DataFrame(a, columns =['Track Name', 'Artist Name'],index =[i[0]])
        print(a)

recommend('Mindscape')

import pickle

pickle.dump(music1,open('music.pkl','wb'))

pickle.dump(similarity,open('similarity.pkl','wb'))

