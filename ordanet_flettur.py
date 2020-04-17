"""
Orðanet Lemon Lemma Retrieval
"""

import pandas as pd
import psycopg2
import rdflib
import re

# Connect to the database
conn = psycopg2.connect(dbname='thesaurus', user='alecshaw',
                        host='130.208.188.57')

# Retrieve all lemmata from the flettur table
query = 'SELECT * FROM flettur;'

data = pd.read_sql(query, conn)

data.head()

data.dtypes

data.to_csv('flettur.csv')

data.fletta.head()

#  if data['fletta'].str.extract(r'(^[A-Za-z]+$)'):
