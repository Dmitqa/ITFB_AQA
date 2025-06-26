import psycopg2
from hw8.configuration import MyConfig, TABLE_NAME, insert_values
from hw8.ps_aux_data_file import start_data

connection = psycopg2.connect(**MyConfig().as_dict())
cursor = connection.cursor()

for i in range(len(start_data)):
    cursor.execute(f"INSERT INTO {TABLE_NAME} VALUES {tuple([i + 1] + insert_values(start_data[i]))};")
    connection.commit()

cursor.close()
connection.close()
