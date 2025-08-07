import csv

def save_csv(arquive_name, data, colums):
    with open(arquive_name, mode="w", newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=colums)
        writer.writeheader()
        for item in data:
            writer.writerow(item)

def read_csv(arquive_name):
    data = []
    try:
        with open(arquive_name, mode="w", newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append(dict(row))
    except FileNotFoundError:
        pass
    return data