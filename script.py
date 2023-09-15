import pandas as pd

encoding = 'ISO-8859-1'
delimiter = ';'

# Load the CSV file into a DataFrame with the specified encoding and delimiter
df = pd.read_csv('llista.csv', encoding=encoding, delimiter=delimiter, dtype=str)

# Define the mapping of day abbreviations to corresponding column names
day_mapping = {
    'Dl': 'Dilluns',
    'Dt': 'Dimarts',
    'Dc': 'Dimecres',
    'Dj': 'Dijous',
    'Dv': 'Divendres'
}

# Generate the columns with the names with type string
for day_abbr, day_name in day_mapping.items():
    df[day_name] = ''

# Iterate through each row and update columns D, E, F, G, H based on the values in the "Dies d'inscripció" column
for index, row in df.iterrows():
    if pd.notna(row["Dies d'inscripció"]):
        for day_abbr, day_name in day_mapping.items():
            if day_abbr in row["Dies d'inscripció"]:
                df.at[index, day_name] = "X"
    if pd.notna(row["Núm."]) and pd.isna(row["Dies d'inscripció"]):
        for day_abbr, day_name in day_mapping.items():
            df.at[index, day_name] = day_name

# Remove old column
df.drop("Dies d'inscripció", axis=1, inplace=True)

# Save the modified DataFrame back to a new CSV file using the same delimiter and encoding
df.to_csv('llista_modificada.csv', index=False, sep=delimiter, encoding=encoding)

print("\n ### LLISTA MODIFICADA AMB ÈXIT ###")
print(' Arxiu "llista_modificada.csv" creat ')

#input("\n Presiona una tecla per sortir...")