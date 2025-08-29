import os
import pandas as pd

def read_xlsx(file_path : str):
  try:
    # Add current work directory to the file path
    file = os.path.join(os.getcwd() + file_path)

    return pd.read_excel(file)
  
  except FileNotFoundError:
    print("File not found")
  
  except Exception as e:
    print("Error in reading file", e)

def show_data_by_column (data, *args : str):
  columns = []

  for arg in args:
    columns.append(arg)

  try:
    print(data[columns])

  except Exception as e:
    print("Error in find xlsx file column name:", e)