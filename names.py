import os
import json

names = []

# Get the path to the _sections directory
sections_dir = './_sections'

# Iterate over the files in the _sections directory
for filename in sorted(os.listdir(sections_dir)):
    # Check if the file is a Markdown file and not "introduction.md"
    if filename.endswith('.md') and filename != 'a-introduction.md':
        # Extract the title from the filename
        title = os.path.splitext(filename)[0]
        # Remove the first "a-" letters from the title
        title = title.split('-', 1)[-1]
        # Transform the title into a name
        name = ' '.join(word.capitalize() for word in title.split('-'))
        # Append the name to the names list
        names.append(name)

# Save the names to a JSON file
with open('_data/names.json', 'w') as f:
    json.dump(names, f)
