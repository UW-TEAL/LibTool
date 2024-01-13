import json

def filter_json(input_file, output_file, exclude_models):
    with open(input_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    filtered_data = [item for item in data if item['model'] not in exclude_models]

    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(filtered_data, file, indent=4)

if __name__ == "__main__":
    input_filename = 'filtered_data.json'  # Your original JSON file
    output_filename = 'filtered_data_1.json'  # New filtered JSON file
    models_to_exclude = ['auth.permission', 'auth.group']  # Add more models as needed

    filter_json(input_filename, output_filename, models_to_exclude)
