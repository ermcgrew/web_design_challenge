import pandas as pd

df = pd.read_csv("cities.csv")
table = df.to_html()

text_file = open("datapage.html", "w")
text_file.write(table)
text_file.close()