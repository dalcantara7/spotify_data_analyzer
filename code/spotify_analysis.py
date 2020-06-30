import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
import matplotlib
import numpy as np
import operator
import time
import sys

N = 15
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'Septemeber', 'October', 'November', 'December']


def main(filename):
    df_data = pd.read_json(filename, orient='records')

    df_data['endTime'] = pd.to_datetime(df_data['endTime']) 

    df_by_artist = df_data.groupby([df_data['endTime'].dt.month, df_data['artistName']]).sum().reset_index()
    df_by_artist.rename(columns={'endTime': 'month'}, inplace=True)

    list_dfs_month = [None] * 12

    for i in range(len(list_dfs_month)):
        list_dfs_month[i] = df_by_artist[df_by_artist['month'] == i + 1].sort_values(by=['msPlayed'], ascending=False).reset_index()
        list_dfs_month[i].drop(['index', 'month'], axis=1, inplace=True)

    for month_df in list_dfs_month:
        month_df['msPlayed'] = month_df['msPlayed'] / 1000
        month_df.rename(columns={'msPlayed' : 'secPlayed'}, inplace=True)

    cmap = cm.get_cmap('cool', N)
    colors = []
    for i in range(cmap.N):
        colors.append(cmap(i))

    for i in range(12):
        n = min(list_dfs_month[i].shape[0], N)

        fig, ax = plt.subplots()
        y_pos = np.arange(n)
        plt.bar(y_pos, list_dfs_month[i].secPlayed[:n], align='center', alpha=0.9, color=colors)
        plt.xticks(y_pos, list_dfs_month[i].artistName[:n], rotation = 85)
        formatter = matplotlib.ticker.FuncFormatter(lambda sec, y: time.strftime('%H:%M:%S', time.gmtime(sec)))
        ax.yaxis.set_major_formatter(formatter)
        plt.gcf().subplots_adjust(bottom=0.4, left=0.2)
        plt.title("Top " + str(n) + " Spotify Artist Listening Time " + months[i] + " 2019")
        plt.ylabel('Listening Time')

        plt.show()


    top_artist_by_month = []
    time_played_by_month = []
    for i in range(len(list_dfs_month)):
        top_artist_by_month.append(list_dfs_month[i].iloc[0].artistName + " (" + str(months[i][0:3]) + ")")
        time_played_by_month.append(list_dfs_month[i].iloc[0].secPlayed)

    cmap = cm.get_cmap('cool', 12)
    colors = []
    for j in range(cmap.N):
        colors.append(cmap(j))

    fig, ax = plt.subplots()
    y_pos = np.arange(12)
    plt.bar(y_pos, time_played_by_month, align='center', alpha=0.9, color=colors)
    plt.xticks(y_pos, top_artist_by_month, rotation = 85)
    formatter = matplotlib.ticker.FuncFormatter(lambda sec, y: time.strftime('%H:%M:%S', time.gmtime(sec)))
    ax.yaxis.set_major_formatter(formatter)
    plt.gcf().subplots_adjust(bottom=0.5, left=0.2)
    plt.title("Top Spotify Artist Of Each Month")
    plt.ylabel('Listening Time')

    plt.show()


if __name__ == "__main__":
    main(sys.argv[1])