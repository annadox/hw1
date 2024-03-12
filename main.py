import pandas as pd
import numpy as np

DATA_FILE = "eurovision_song_contest_1957_2023.xlsx"

def create_country_vectors(df):
    all_countries = df["From country"].unique()

    all_country_vectors = dict.fromkeys(all_countries, None)

    for country in all_countries:  
        c_votes = df.loc[df['From country'] == country]
        c_votes_sum = c_votes.groupby("To country").sum()

        c_vector = dict.fromkeys(all_countries, 0)

        #print(c_votes_sum.columns)

        for i in c_votes_sum.index:
            c_vector[i] = c_votes_sum.loc[i, "Points"]

        print(country)
        print(c_vector)

        all_country_vectors[country] = c_vector
        
    return all_country_vectors 

if __name__ == "__main__":
    df = pd.read_excel(DATA_FILE)
    all_country_vectors = create_country_vectors(df)