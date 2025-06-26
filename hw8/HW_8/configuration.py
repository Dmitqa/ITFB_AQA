from dataclasses import dataclass, asdict
import psycopg2
from subprocess import run, PIPE

HOST = 'localhost'
PORT = '5432'
USER = 'pgs'
PASSWORD = '123'
DATABASE_NAME = 'postgres'
TABLE_NAME = 'ps_aux_data'


@dataclass
class MyConfig:
    host: str = HOST
    port: str = PORT
    user: str = USER
    password: str = PASSWORD
    database: str = DATABASE_NAME

    def as_dict(self) -> dict:
        return asdict(self)


def decoding(command: str):
    result = run(command.lower().split(' '), stdout=PIPE)
    return result.stdout.decode()


def insert_values(data: str):
    line = [i.strip()[:20] for i in data.split(None, 10)]
    return line


connection = psycopg2.connect(**MyConfig().as_dict())
cursor = connection.cursor()


def get_unique_users():
    cursor.execute(f"SELECT DISTINCT linux_user FROM {TABLE_NAME};")
    users = list(map(lambda x: ''.join(x), cursor.fetchall()))
    return f"Пользователи системы: {', '.join(users)}."


def get_all_process_value():
    cursor.execute(f"SELECT COUNT(linux_user) FROM {TABLE_NAME};")
    return f"Процессов запущено: {cursor.fetchall()[0][0]}."


def get_users_process():
    cursor.execute(f"SELECT DISTINCT linux_user FROM {TABLE_NAME};")
    process_list = []
    for user in cursor.fetchall():
        cursor.execute(f"SELECT linux_user, COUNT(linux_user) FROM {TABLE_NAME} GROUP BY linux_user "
                       f"HAVING linux_user = '{str(*user)}' ORDER BY COUNT(linux_user) DESC;")
        process, value = list(*cursor.fetchall())
        process_list.append(f'{process}: {value}')
    return f"Пользовательские процессы: {', '.join(process_list)}."


def get_used_memory_value():
    cursor.execute(f"SELECT SUM(mem) FROM {TABLE_NAME};")
    value = cursor.fetchall()[0][0]
    return f"Всего памяти используется: {value:.2f} mb."


def get_used_cpu_value():
    cursor.execute(f"SELECT SUM(cpu) FROM {TABLE_NAME};")
    value = cursor.fetchall()[0][0]
    return f"Всего CPU используется: {value:.2f}%."


def get_max_memory_used_process():
    cursor.execute(f"SELECT command, mem FROM {TABLE_NAME} WHERE mem = "
                   f"(SELECT MAX(mem)FROM {TABLE_NAME});")
    value = cursor.fetchall()[0]
    return f"Больше всего памяти использует процесс: '{value[0]}'= {value[1]}%."


def get_max_cpu_used_process():
    cursor.execute(f"SELECT command, cpu FROM {TABLE_NAME} WHERE cpu = "
                   f"(SELECT MAX(cpu)FROM {TABLE_NAME});")
    value = cursor.fetchall()[0]
    return f"Больше всего CPU использует процесс: '{value[0]}'= {value[1]}%."
