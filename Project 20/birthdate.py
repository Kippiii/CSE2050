# Author: Ian Orzel, iorzel2019@my.fit.edu
# Course: CSE 2050, Fall 2020
# Project: Birth Date Heat map
"""Create a heat map based on the number of births each day."""

import mysql.connector
import numpy
import matplotlib.pyplot

# Creates the labels for the axes
months = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN",
          "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
days = [i + 1 for i in range(31)]


def read_database():
    """Transfer information from database to a frequency table."""
    # Queries the database
    db = mysql.connector.connect(host='andrew.cs.fit.edu',
                                 database='stansifer',
                                 user='cse2050',
                                 password="fall2020")
    cursor = db.cursor()
    cursor.execute("SELECT DOB, COUNT(*) FROM SSDI GROUP BY DOB")

    # Stores information from database in table
    freq_table = [[[0 for _ in range(12)] for _ in range(31)]
                  for _ in range(131)]
    while True:
        (tup) = cursor.fetchone()
        if not tup:
            break
        date, count = tup
        year = int(date[:4])
        month = int(date[5:7])
        day = int(date[8:10])
        if 1880 <= year <= 2010:
            freq_table[year-1880][day-1][month-1] += count

    return freq_table


freq_table_with_year = read_database()


def get_freq_table(start, end):
    """Get a frequency table independent of year based on range."""
    freq_table = [[0 for _ in range(12)] for _ in range(31)]
    # Loops through every date in the range
    for y in range(start-1880, end-1880):
        for d in range(31):
            for m in range(12):
                freq_table[d][m] += freq_table_with_year[y][d][m]
    return freq_table


freq_table = get_freq_table(1880, 1890)

# Creates the heatmap with axes and lables
fig, ax = matplotlib.pyplot.subplots(figsize=(10, 15))
im = ax.imshow(freq_table, cmap="YlOrRd")
ax.set_xticks(numpy.arange(12))
ax.set_yticks(numpy.arange(31))
ax.set_xticklabels(months, fontsize=7)
ax.set_yticklabels(days)

# Creates the two sliders under the heatmap
start_axis = matplotlib.pyplot.axes((0.25, 0.05, 0.65, 0.03))
year_axis = matplotlib.pyplot.axes((0.25, 0.02, 0.65, 0.03))
start_slider = matplotlib.widgets.Slider(start_axis, "Start", 1880, 2000,
                                         valinit=1880, valstep=1)
year_slider = matplotlib.widgets.Slider(year_axis, "Years", 1, 10,
                                        valinit=10, valstep=1)


def update_graph(*args):
    """Update the heatmap based on slider state."""
    start_year = start_slider.val
    year_count = year_slider.val
    freq_table = get_freq_table(start_year, start_year + year_count)
    ax.imshow(freq_table, cmap="YlOrRd")


# Adds the update function to slider and opens graphic
start_slider.on_changed(update_graph)
year_slider.on_changed(update_graph)
matplotlib.pyplot.show()
