import json

def merge_duplicates(data):
    processed = {}

    for problem in data:
        slug = problem["slug"]
        
        if slug in processed:
            existing_tags = set(processed[slug]["topicTags"])
            new_tags = set(problem["topicTags"])
            # Merge tags without keeping order
            combined_tags = existing_tags | new_tags
            
            # Update the tags
            processed[slug]["topicTags"] = list(combined_tags)

            # Merge likes and dislikes
            processed[slug]["likes"] += problem.get("likes", 0)
            processed[slug]["dislikes"] += problem.get("dislikes", 0)
        else:
            # Add the problem to the dictionary
            processed[slug] = problem
    
    # Convert back to list format
    return list(processed.values())

def main():
    # Read input JSON file
    input_file = "problems (1).json"
    with open(input_file, "r") as f:
        data = json.load(f)

    # Process data to remove duplicates and merge tags
    cleaned_data = merge_duplicates(data)

    # Write output to a new JSON file
    output_file = "output.json"
    with open(output_file, "w") as f:
        json.dump(cleaned_data, f, indent=4)

    print(f"✅ Processed {len(cleaned_data)} unique problems and saved to '{output_file}'.")

if __name__ == "__main__":
    main()
