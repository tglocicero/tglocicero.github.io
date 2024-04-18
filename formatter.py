# Import the necessary library
import re


def format_html(file_path):
    try:
        # Open the input file
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Prepare the output file to store the HTML list items
        with open('formatted_links.html', 'w') as output_file:
            output_file.write('<ul>\n')

            # Process each line (URL)
            for line in lines:
                line = line.strip()
                if line:
                    # Extract the article title from the URL using regex
                    match = re.search(r'/articles/\d+-(.*)', line)
                    if match:
                        title = match.group(1).replace('-', ' ').title()
                        # Write the formatted line to the output file
                        output_file.write(
                            f'    <li><a href="{line}">{title}</a></li>\n')

            output_file.write('</ul>\n')

    except Exception as e:
        print(f"An error occurred: {e}")


# Replace the path below with the actual path to your file
file_path = "unique_urls.txt"
format_html(file_path)
