import json

def filter_json(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:  # Specify encoding here
        data = json.load(file)

    filtered_data = [entry for entry in data if entry['model'] not in ['contenttypes.contenttype', 'sessions.session']]

    with open(output_file, 'w', encoding='utf-8') as file:  # Specify encoding here
        json.dump(filtered_data, file, indent=4)

if __name__ == "__main__":
    filter_json('data.json', 'filtered_data.json')
