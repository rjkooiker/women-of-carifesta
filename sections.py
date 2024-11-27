import os
import json

sections = []

# Get the path to the _sections directory
sections_dir = './_sections'

# Initialize variables for the current letter and index
current_letter = None
index = 1

# Iterate over the files in the _sections directory
for filename in sorted(os.listdir(sections_dir)):
    # Check if the file is a Markdown file and not "introduction.md"
    if filename.endswith('.md') and filename != 'a-introduction.md':
        # Extract the title from the filename
        title = os.path.splitext(filename)[0]
        # Remove the first "*-" letters from the title
        title = title.split('-', 1)[-1]
        # Transform the title into a section
        section = ' '.join(word.capitalize() for word in title.split('-'))
        # Check if the first letter of the filename has changed
        if filename[0] != current_letter:
            # Update the current letter and reset the index
            current_letter = filename[0]
            index = 1
        # Create the objectid
        objectid = current_letter + str(index).zfill(2)
        # Append the section and objectid to the sections list
        sections.append({"section": section, "objectid": objectid})
        # Increment the index
        index += 1

# Save the sections to a JSON file
with open('_data/sections.json', 'w') as f:
    json.dump(sections, f)