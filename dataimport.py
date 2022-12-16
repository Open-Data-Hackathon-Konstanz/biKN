#!/usr/bin/env python3
import pandas as pd

def import_zaehlstellen(filename):

    data = pd.read_csv(filename, delimiter=";")

    # convert to datatime objects
    data['Zeit'] =  pd.to_datetime(data['Zeit'], format="%d.%m.%Y %H:%M")

    data['Year'] = data['Zeit'].apply(lambda x: x.year)
    data['Month'] = data['Zeit'].apply(lambda x: x.month)
    data['Day'] = data['Zeit'].apply(lambda x: x.day)
    data['Hour'] = data['Zeit'].apply(lambda x: x.hour)
    data['Minute'] = data['Zeit'].apply(lambda x: x.minute)
    data['Dayname'] = data['Zeit'].apply(lambda x: x.day_name())

    return data
