import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
import matplotlib
import numpy as np
import operator
import time

data = pd.read_json("Spotify Analysis/one_year_streaming_history0.json", orient='records')

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'Septemeber', 'October', 'November', 'December']

N = 15

month_dict = {}
for index, row in data.iterrows():
    month = str(row['endTime'])[5:7]
    artist_name = row['artistName']
    if month not in month_dict:
        month_dict[month] = {artist_name : row['msPlayed']}
    else:
        if artist_name not in month_dict[month]:
            month_dict[month][artist_name] = row['msPlayed']
        else:
            month_dict[month][artist_name] += row['msPlayed']

for i in range(0,12):
    if i < 9:
        artists = list(month_dict['0' + str(i+1)].keys())
        playtimes = list(month_dict['0' + str(i+1)].values())
    else:
        artists = list(month_dict[str(i+1)].keys())
        playtimes = list(month_dict[str(i+1)].values())

    sorted_artists = [x for _, x in sorted(zip(playtimes, artists), reverse=True)]
    sorted_artists = sorted_artists[0:N]
    sorted_playtimes = np.array(sorted(playtimes, reverse=True)) / 1000
    sorted_playtimes = sorted_playtimes[0:N]

    cmap = cm.get_cmap('cool', len(sorted_artists))
    colors = []
    for j in range(cmap.N):
        colors.append(cmap(j))

    fig, ax = plt.subplots()
    y_pos = np.arange(len(sorted_artists))
    plt.bar(y_pos, sorted_playtimes, align='center', alpha=0.9, color=colors)
    plt.xticks(y_pos, sorted_artists, rotation = 85)
    formatter = matplotlib.ticker.FuncFormatter(lambda sec, y: time.strftime('%H:%M:%S', time.gmtime(sec)))
    ax.yaxis.set_major_formatter(formatter)
    plt.gcf().subplots_adjust(bottom=0.4, left=0.2)
    plt.title("Top " + str(N) + " Spotify Artist Listening Time " + months[i] + " 2019")
    plt.ylabel('Listening Time')

    plt.show()

max_artist_per_month = []
values = []
i = 0
for month in month_dict.keys():
    max_artist_per_month.append(str(max(month_dict[month].items(), key=operator.itemgetter(1))[0]) + " (" + months[i][0:3] + ")")
    values.append(max(month_dict[month].values()))
    i+=1

values = np.array(values) / 1000

cmap = cm.get_cmap('cool', 12)
colors = []
for j in range(cmap.N):
    colors.append(cmap(j))

fig, ax = plt.subplots()
y_pos = np.arange(12)
plt.bar(y_pos, values, align='center', alpha=0.9, color=colors)
plt.xticks(y_pos, max_artist_per_month, rotation = 85)
formatter = matplotlib.ticker.FuncFormatter(lambda sec, y: time.strftime('%H:%M:%S', time.gmtime(sec)))
ax.yaxis.set_major_formatter(formatter)
plt.gcf().subplots_adjust(bottom=0.5, left=0.2)
plt.title("Top Spotify Artist Of Each Month")
plt.ylabel('Listening Time')

plt.show()