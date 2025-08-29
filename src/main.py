import pandas as pd

from __version__ import __version__

if __name__ == "__main__":
  print("project version:", __version__)

read = pd.read_excel("input.xlsx")
print(read)

column = "Name"
if column in read:
  print(read[["Name","Age"]])