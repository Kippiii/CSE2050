# Author: Ian Orzel, iorzel2019@my.fit.edu
# Course: CSE 2050, Fall 2020
# Project: Birth Date Heat map
"""Create a heat map based on the number of births each day."""

import mysql.connector
import numpy
import matplotlib.pyplot

months = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
days = [i + 1 for i in range(31)]


def read_database():
    db = mysql.connector.connect(host='andrew.cs.fit.edu',database='stansifer',user='cse2050', password="fall2020")
    cursor = db.cursor()
    cursor.execute("SELECT DOB, COUNT(*) FROM SSDI GROUP BY DOB")

    freq_table = [[[0 for _ in range(12)] for _ in range(31)] for _ in range(120)]
    while True:
        (tup) = cursor.fetchone()
        if not tup:
            break
        date, count = tup
        year = int(date[:4])
        month = int(date[5:7])
        day = int(date[8:10])
        freq_table[year-1880][day-1][month-1] += count

    return freq_table


def read_file():
    freq_table = [[[0 for _ in range(12)] for _ in range(31)] for _ in range(121)]
    with open("input.in", "r") as f:
        while True:
            line = f.readline()
            if not line:
                break
            date, count = line.split()
            count = int(count)
            year = int(date[:4])
            month = int(date[5:7])
            day = int(date[8:10])
            if 1880 <= year <= 2000:
                freq_table[year-1880][day-1][month-1] += count

    return freq_table


freq_table_with_year = read_file()


def get_freq_table(start, end):
    freq_table = [[0 for _ in range(12)] for _ in range(31)]
    for y in range(start-1880, end-1880+1):
        for d in range(31):
            for m in range(12):
                freq_table[d][m] += freq_table_with_year[y][d][m]
    return freq_table


freq_table = get_freq_table(1880, 2000)

max_val = 1
min_val = 9999999999999999
for table in freq_table:
    for entry in table:
        if entry > max_val:
            max_val = entry
        if entry < min_val and entry != 0:
            min_val = entry
print(min_val)
print(max_val)
for i in range(len(freq_table)):
    for j in range(len(freq_table[i])):
        freq_table[i][j] = max_val**2 - freq_table[i][j]**2

fig, ax = matplotlib.pyplot.subplots(figsize=(10, 15))
im = ax.imshow(freq_table, cmap="copper")
ax.set_xticks(numpy.arange(12))
ax.set_yticks(numpy.arange(31))
ax.set_xticklabels(months, fontsize=7)
ax.set_yticklabels(days)

start_axis = matplotlib.pyplot.axes((0.25, 0.05, 0.65, 0.03))
year_axis = matplotlib.pyplot.axes((0.25, 0.02, 0.65, 0.03))
start_slider = matplotlib.widgets.Slider(start_axis, "Start", 1880, 2000, valinit=1880, valstep=1)
year_slider = matplotlib.widgets.Slider(year_axis, "Years", 0, 120, valinit=120, valstep=1)


def update_graph(*args):
    start_year = start_slider.val
    year_count = year_slider.val
    freq_table = get_freq_table(start_year, min(start_year + year_count, 2000))
    ax.imshow(freq_table, cmap="copper")


start_slider.on_changed(update_graph)
year_slider.on_changed(update_graph)
matplotlib.pyplot.show()
