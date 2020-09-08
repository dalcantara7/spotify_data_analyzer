# Spotify Data Analyzer
A project which takes Spotify listening data and creates visualizations of the data. 

I made this project to get some practice using the tools I learned in my Data Science Cetification.

The notebooks contained within this project contain more information on my thought process and exploratory analysis as well as some insights I generated into my personal data.

Through my month to month listening, I noticed that the amount of time I listened to Carly Rae Jepsen was far beyond any other artist that I listed to, so I wanted to see how well her features of music represented my listening habits.

The features of Carly's music that were particularly different from my other music is

* her songs are higher tempo
* her songs are higher valence (musical positivity)
* her songs are less acoustic
* her songs are louder
* her songs have higher energy
* her songs are more danceable
* her songs are more often in a major key

I also created a visual representation of the music in the form of Radar/Spider charts to illustrate the hunch that it is the combination of features that I like more than just the one feature individually.

Here they are:
 
![Carly Rae Jepsen Song Chart](https://github.com/dalcantara7/spotify_data_analyzer/blob/master/Images/crj.png)
![Non-Carly Rae Jepsen Song Chart](https://github.com/dalcantara7/spotify_data_analyzer/blob/master/Images/non-crj.png)
![Least Listened Non-Carly Rae Jepsen Song Chart](https://github.com/dalcantara7/spotify_data_analyzer/blob/master/Images/least%20non-crj.png)

Upon examining these plots, what do we learn?

1. I very much value features of loudness, energy, danceability, popularity, high valence, and high tempo
* Note: Popularity likely has no true bearing on my liking a song i.e. it is correlated with songs that I like, but probably not the cause. This is just an intuitive guess and not necessarily confirmed by the data
2. I do not value speechiness virtually at all
3. Carly Rae Jepsen is different from the rest of my other music in that they are less acoustic-y and shorter in length
* I won't give much weight to the high liveliness oberseved in the CRJ plot as this seems to only come from one song, so it's hardly a significant finding


This project contains a script which will run the artist per month analysis and generate the month by month visualizations. 

Example of top artist from every month:
![top artist every month](https://github.com/dalcantara7/spotify_data_analyzer/blob/master/Images/Top%20Spotify%20Artists%20of%20Each%20Month.png)

The libraries I used are listed in the __requirements.txt__ file.

Running the script is as simple as running this command 
``` 
python3 PATH_TO_SCRIPT PATH_TO_SPOTIFY_DATA
``` 


