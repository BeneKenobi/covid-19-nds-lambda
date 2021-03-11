import pandas

df = pandas.read_csv('https://www.apps.nlga.niedersachsen.de/corona/download.php?csv_tag_region-file',
                     delimiter=";",
                     header=0,
                     usecols=['GKZ', 'Landkreis']
                     ).drop_duplicates()

print(df.to_string(index=False))
