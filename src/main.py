from __version__ import __version__
from modules.utils import read_xlsx, show_data_by_column

if __name__ == "__main__":
  print("project version:", __version__)

  df = read_xlsx("\data\data.xlsx")
  show_data_by_column(df, "Name", "Age", "City")
