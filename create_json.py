import csv
import json

#Create json file for image labels from prexisiting csv file for use in hugging face dataset

csv_file_path = '/Users/louis/Documents/MLX3/week8/code/louis.csv'  
jsonl_file_path = '/Users/louis/Documents/MLX3/week8/code/metadata.jsonl'  

# Open the CSV file and create a JSON Lines file
with open(csv_file_path, 'r', encoding='utf-8') as csv_file, open(jsonl_file_path, 'w', encoding='utf-8') as jsonl_file:
    csv_reader = csv.DictReader(csv_file)
    
    # Iterate through each row in the CSV file
    for row in csv_reader:
        # Create a dictionary with the desired keys and values
        json_dict = {
            "file_name": row["file_name"].strip(),
            "text": row["text"].lower()  # Convert text to lowercase as per your example
        }

        # Write the JSON dictionary as a line in the JSON Lines file
        jsonl_file.write(json.dumps(json_dict, ensure_ascii=False) + '\n')