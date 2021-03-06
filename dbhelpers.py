import time
from tinydb import Query
from tinydb import where

def new_temperature(db, temperature):
    temps = db.table('temps')
    return temps.insert({'temperature' : temperature, 'time': time.time()})

def new_stations(db, station, temperature):
    stations = db.table('stations')
    return stations.insert(station.getStationInfo(temperature))

def get_stations(db):
    station_data = db.table('stations')
    stations = station_data.all()
    return stations

def get_temperature(db):
    temp_data = db.table('temps')
    temp = temp_data.all()
    return temp

def reset_temperature(db):
    temps = db.table('temps')
    temps.truncate()

def reset_stations(db):
    station_data = db.table('stations')
    station_data.truncate()

def new_treatment(db, station):
    treatments = db.table('treatments')
    return treatments.insert({'station' : station ,'time' : time.time()})

def get_treatments(db):
    treatments = db.table('treatments')
    return treatments.all()

def reset_treatments(db):
    treatments = db.table('treatments')
    treatments.truncate()

def delete_treatment(db, station):
    treatments = db.table('treatments')
    treatments.remove(where('station') == station)