# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

MAPFILE = 'data/map1.html'

import folium


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    m = folium.Map(location=(35.61,-82.44), zoom=6)
    m.save(MAPFILE)
    

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
