import numpy as np
import plotly.express as px
import csv

def get_data_source(data_path):
    marks=[]
    days=[]
    with open(data_path) as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            marks.append(float(row["Marks"]))
            days.append(float(row["Days"]))
    return{
        "x":marks,"y":days
    }

def find_correlation(data_source):
    correlation=np.corrcoef(data_source["x"],data_source["y"])
    print("correlation between marks obtained and number of days present is : ",correlation[0,1])

def setup():
    data_path="./marks_days.csv"
    data_source=get_data_source(data_path)
    find_correlation(data_source)

setup()