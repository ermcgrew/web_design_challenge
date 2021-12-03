import pandas as pd

df = pd.read_csv("cities.csv")
table = df.to_html('table.html', classes='table table-striped')