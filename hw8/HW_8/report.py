from datetime import datetime
from hw8 import configuration

report = [
    'Отчёт о состоянии системы:',
    configuration.get_unique_users(),
    configuration.get_all_process_value(),
    configuration.get_users_process(),
    configuration.get_used_memory_value(),
    configuration.get_used_cpu_value(),
    configuration.get_max_memory_used_process(),
    configuration.get_max_cpu_used_process()
]

with open(f"{datetime.today().strftime('(%Y-%m-%d)_(%H-%M-%S)')}.txt", "w", encoding='utf-8') as file:
    for line in report:
        file.write(line + '\n')

configuration.cursor.close()
configuration.connection.close()
