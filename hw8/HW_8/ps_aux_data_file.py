from hw8.configuration import decoding

with open('ps_aux_data.txt', 'w') as file:
    terminal_command = "ps aux"
    result_command = decoding(terminal_command)
    for row in result_command:
        file.write(row)

with open("ps_aux_data.txt", "r") as file:
    start_titles = [i.replace("%", "") for i in file.readline().split()]
    start_data = file.readlines()
