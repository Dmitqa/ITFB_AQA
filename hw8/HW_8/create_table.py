import psycopg2
from hw8.configuration import TABLE_NAME, MyConfig
from hw8.ps_aux_data_file import start_titles

connection = psycopg2.connect(**MyConfig().as_dict())
cursor = connection.cursor()

create_table = f"""
CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
    ID SERIAL PRIMARY KEY,
    linux_{start_titles[0]} VARCHAR(10) NOT NULL,
    {start_titles[1]} SMALLINT NOT NULL,
    {start_titles[2]} FLOAT NOT NULL,
    {start_titles[3]} FLOAT NOT NULL,
    {start_titles[4]} INT NOT NULL,
    {start_titles[5]} INT NOT NULL,
    {start_titles[6]} VARCHAR(6) NOT NULL,
    {start_titles[7]} VARCHAR(5) NOT NULL,
    {start_titles[8]} TIME NOT NULL,
    {start_titles[9]} TIME NOT NULL,
    {start_titles[10]} VARCHAR(50) NOT NULL
);
"""

cursor.execute(create_table)
connection.commit()

cursor.close()
connection.close()
