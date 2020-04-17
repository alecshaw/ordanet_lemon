"""
Orðanet Lemon Lemma Retrieval
"""

import pandas as pd
import psycopg2

# Connect to the database
conn = psycopg2.connect(dbname='thesaurus', user='alecshaw',
                        host='130.208.188.57')

# Retrieve all lemmata from the flettur table
query = 'SELECT * FROM flettur;'

flettur = pd.read_sql(query, conn)
flettur.to_csv('flettur.csv')
print(flettur.head())

# Retrieve all concepts from the vw_hugtak table
query = 'SELECT * FROM vw_hugtak;'

hugtak = pd.read_sql(query, conn)
hugtak.to_csv('hugtak.csv')
print(hugtak.head())

conn.close()
