import os
import pandas as pd

# Load the extracted details from the CSV file
file_path = 'extracted_details.csv'

# Check if the file exists
if not os.path.isfile(file_path):
    # If the file does not exist, create it with the appropriate headers
    pd.DataFrame(columns=['Filename', 'Name', 'Contact Information', 'Education', 'Work Experience', 'Skills']).to_csv(file_path, index=False)

# Load the data
data = pd.read_csv(file_path)

# Define personality traits associations with skills
def read_traits_from_file(file_path):
    traits_mapping = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                trait, skills = line.strip().split(':')
                trait = trait.strip()
                skills = [skill.strip() for skill in skills.split(',')]
                traits_mapping[trait] = skills
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"Error while reading traits file: {e}")
    return traits_mapping

# Usage:
traits_file = 'traits.txt'  # Path to your traits file
traits_mapping = read_traits_from_file(traits_file)

def assign_personality_traits(row):
    traits_scores = {trait: 0 for trait in traits_mapping}
    if not pd.isna(row['Skills']):  # Check if 'Skills' is not NaN
        skills_list = row['Skills'].split(', ')  # Ensure skills are separated correctly
        for trait, associated_skills in traits_mapping.items():
            for skill in associated_skills:
                if skill in skills_list:
                    traits_scores[trait] += 1

    return pd.Series(traits_scores)

# Apply the function to the dataframe to assign personality traits
personality_traits = data.apply(assign_personality_traits, axis=1)

# Concatenate the original data with the assigned personality traits
data_with_traits = pd.concat([data, personality_traits], axis=1)

# Save the updated data to a new CSV file
output_file_path = 'extracted_detailsWith_traits.csv'
data_with_traits.to_csv(output_file_path, index=False)
print(f"Updated data with personality traits saved to '{output_file_path}'.")
