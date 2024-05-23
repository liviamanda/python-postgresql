'''
API

Name  : Livia Amanda Annafiah
Batch : BSD-005

Program Description
This program aims to find anomalies in a rent properties database and make an API.

'''

# Import library
from fastapi import FastAPI, HTTPException
import pandas as pd

# Define app
app = FastAPI()

# Load the CSV data into a DataFrame
table = pd.read_csv('livia_amanda.csv')

# Show menu
@app.get("/")
def root():
    return {"message": "Welcome to Rent Price Data! Here is our menu:",
            "menu": {1: "See price (/data)",
                     2: "Delete price (/delete/index)",
                     3: "Update price (/update)",
                     4: "Add new price (/add)"}}

# Show data (Mandatory)
@app.get("/data")
def getData():
    global table 
    data = table.to_dict()
    return data

# Delete data (Optional)
@app.delete("/delete/{index}")
def deleteData(index: int):
    global table
    if index not in table.index:
        raise HTTPException(status_code=404, detail=f"Index {index} not found")
    else:
        table.drop(index, inplace=True)
        return {"message": f"Index {index} has been deleted successfully."}

# Update data (Optional)
@app.put("/update/{index}")
def updateData(index: int, new_data: dict):
    global table
    if index not in table.index:
        raise HTTPException(status_code=404, detail=f"Index {index} not found")
    else:
        for key, value in new_data.items():
            table.loc[index, key] = value
        return {"message": f"Data at index {index} has been updated successfully."}

# Add data (Optional)
@app.post("/add")
def addData(data: dict):
    global table
    new_row = pd.DataFrame([data]) 
    table = pd.concat([table, new_row], ignore_index=True)
    return {"message": "New price has been added successfully."}