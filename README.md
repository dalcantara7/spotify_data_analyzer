# spotify_data_analyzer
A project which takes Spotify listening data and creates visualizations of the data. 

I made this project to get some practice using the tools I learned in my Data Science Cetification.

The notebooks contained within this project contain more information on my thought process and exploratory analysis as well as some insights I generated into my personal data.
**Note: notebooks need to be updated to reflect new file structure**

Through my month to month listening, I noticed that the amount of time I listened to Carly Rae Jepsen was far beyond any other artist that I listed to, so I wanted to see how well her features of music represented my listening habits.

The features of Carly's music that were particularly different from my other music is

* her songs are higher tempo
* her songs are higher valence (musical positivity)
* her songs are less acoustic
* her songs are louder
* her songs have higher energy
* her songs are more danceable
* her songs are more often in a major key

This project contains a script which will run the artist per month analysis and generate the month by month visualizations. 

Example of top artist from every month:
![top artist every month](https://github.com/dalcantara7/spotify_data_analyzer/blob/master/Top%20Spotify%20Artists%20of%20Each%20Month.png)

The libraries I used are listed in the __requirements.txt__ file.

Running the script is as simple as running this command 
``` 
python3 PATH_TO_SCRIPT PATH_TO_SPOTIFY_DATA
``` 


