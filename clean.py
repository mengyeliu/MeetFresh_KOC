import json
import os
import glob
import argparse
def merge_json_files(input_folder, output_folder):
    """
    Merge JSON files from a folder (and subfolders) into a single JSON array.
    
    Args:
        input_folder (str): Path to the input folder containing JSON files.
        output_file (str): Path to foler containing the output JSON file.
    """
    # Find all JSON files starting with 'content_name_' recursively
    pattern = os.path.join(input_folder, '**', 'creator_creator_*.json')
    json_files = glob.glob(pattern, recursive=True)
    
    combined_data = []
    user_id_collection = []
    count_creator = 0
    for json_file in json_files:
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                for i in data:
                    count_creator += 1
                    user_id = i["user_id"]
                    if user_id not in user_id_collection:
                        combined_data.append(i)
                        user_id_collection.append(user_id)
            print(f"Successfully processed: {json_file}")
        except Exception as e:
            print(f"Error loading {json_file}: {e}")
    file_name = "creator.json"
    output_file = os.path.join(output_folder, file_name)
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(combined_data, f, indent=4,ensure_ascii=False)
    print(f"Successfully selected {len(user_id_collection)} unique creators from {count_creator} creators.")
    print(f"Successfully merged {len(json_files)} JSON files into {output_file}\n")

    pattern = os.path.join(input_folder, '**', 'creator_contents_*.json')
    json_files = glob.glob(pattern, recursive=True)
    
    combined_data = []
    note_id_collection = []
    count_note = 0
    for json_file in json_files:
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                for i in data:
                    count_note += 1
                    note_id = i["note_id"]
                    if note_id not in note_id_collection:
                        combined_data.append(i)
                        note_id_collection.append(note_id)
            print(f"Successfully processed: {json_file}")
        except Exception as e:
            print(f"Error loading {json_file}: {e}")
    file_name = "content.json"
    output_file = os.path.join(output_folder, file_name)
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(combined_data, f, indent=4,ensure_ascii=False)
    print(f"Successfully selected {len(note_id_collection)} unique notes from {count_note} notes." )
    print(f"Successfully merged {len(json_files)} JSON files into {output_file}\n")


if __name__ == "__main__":
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description='Merge JSON files')
    parser.add_argument('--input', '-i', required=True,
                        help='Input directory containing JSON files')
    parser.add_argument('--output', '-o', required=True,
                        help='Output JSON file folder path')
    
    args = parser.parse_args()
    
    # Validate input path
    if not os.path.isdir(args.input):
        print(f"Error: Input path '{args.input}' is not a valid directory")
        exit(1)
    
    merge_json_files(args.input, args.output)