from time import sleep
import numpy as np
import plotly.express as px
import csv

def get_data_source(data_path):
    coffee=[]
    sleep=[]
    with open(data_path) as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            coffee.append(float(row["Coffee"]))
            sleep.append(float(row["Sleep"]))
    return{
        "x":coffee,"y":sleep
    }

def find_correlation(data_source):
    correlation=np.corrcoef(data_source["x"],data_source["y"])
    print("correlation between coffee consumed and hours of sleep is : ",correlation[0,1])

def setup():
    data_path="./coffee_sleep.csv"
    data_source=get_data_source(data_path)
    find_correlation(data_source)

setup()