import csv

def save(data, filename, map_name):
    path = './resources/Maps/' + filename + '/' + map_name + '.csv'
    with open(path, 'w', newline='\n', encoding='utf-8') as file:
        csv_writer = csv.writer(file, delimiter=',')
        csv_writer.writerows(data)

    return

def load(filename, map_name):
    path = './resources/Maps/' + filename + '/' + map_name + '.csv'
    with open(path, 'r', newline='\n', encoding='utf-8') as file:
        csv_reader = csv.reader(file, delimiter=',')
        csv_stuff = csv_reader

        data = []

        for line in csv_stuff:
            l_data = []

            for row in line:
                l_data.append(row)

            data.append(l_data)
    return data
