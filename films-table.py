import csv
import html
import os

def create_excerpt(text, max_length=50):
    words = text.split()
    if len(text) <= max_length or len(words) < 8:
        return text  # Return original if it's short enough or doesn't have enough words to excerpt

    # Construct the excerpt: first three words + ellipsis + last three words
    excerpt = ' '.join(words[:3]) + ' ... ' + ' '.join(words[-3:])
    return excerpt

def csv_to_bootstrap_table(csv_file_path, output_html_path):
    table_html = """
<div class="table-responsive">
    <table class="table">
        <caption class="caption-top">Detailed Filmography of Caribbean Cultural Documentaries</caption>
        <thead>
            <tr>
                <th>Title</th>
                <th>Date</th>
                <th>Country</th>
                <th>Genre</th>
                <th>Format</th>
                <th>Time</th>
                <th>Color</th>
                <th>Production Company</th>
                <th>Production</th>
                <th>Director</th>
                <th>Screenplay</th>
                <th>Editor</th>
                <th>Sound</th>
                <th>Camera</th>
                <th>Synopsis</th>
            </tr>
        </thead>
        <tbody>
    """
    
    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header row
        for row in reader:
            row_html = '<tr>'
            for cell in row:
                excerpt = create_excerpt(cell)
                row_html += f'<td data-bs-toggle="tooltip" data-bs-placement="top" data-bs-custom-class="custom-tooltip" title="{html.escape(cell)}">{html.escape(excerpt)}</td>'
            row_html += '</tr>\n'
            table_html += row_html
    
    table_html += """
        </tbody>
    </table>
</div>
    """
    
    os.makedirs(os.path.dirname(output_html_path), exist_ok=True)
    with open(output_html_path, 'w', encoding='utf-8') as htmlfile:
        htmlfile.write(table_html)

# Usage example:
csv_path = '_data/filmography.csv'
html_output_path = '_includes/filmography.html'
csv_to_bootstrap_table(csv_path, html_output_path)
