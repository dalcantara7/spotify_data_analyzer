# spotify_data_analyzer
A project which takes Spotify listening data and creates visualizations of the data. 

Initially this was a script I wrote where I created my own data structure of a nested dictionary ordered by month and then artists within those months i.e.

{ month : 
  { artist : playTime, ..., artist : playTime }
  , ..., 
  finalMonth : 
  { artist : playTime, ... } 
}

That script still exists. However, I converted this script to a notebook with more information (and plans for more analysis/visualization).

When writing the ipynb I decided it would be best to use pandas to structure the data instead of my own data type so the analysis within the ipynb is done with pandas and is more updated.
