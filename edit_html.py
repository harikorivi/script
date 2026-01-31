#!/usr/bin/env python3
import sys
import io

from bs4 import BeautifulSoup
# Set stdout to use UTF-8 encoding
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sample_file = 'ACT_Invoice_JUNE_2024.html'
# Read the HTML content from the file
with open(sample_file, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html_content, 'lxml')

# Find all <td> elements
td_elements = soup.find_all('td')

# Modify the content of each <td> element, including nested content
# for i, td in enumerate(td_elements, start=1):
#     # Update the main content of the <td>
#     #td.string = f'Updated content {i}'

#     # Optionally, you can modify the nested structures within <td>
#     # For example, find nested <table> tags inside the current <td>
#     nested_tables = td.find_all('table')
#     for table in nested_tables:
#         print(f"{dir(table)}")
#         # Modify the nested table as needed
#         table_caption = table.find('caption')
        #print(f"caption = {table_caption}")
        # if table_caption:
        #     table_caption.string = f'Updated caption {i}'

    # Print the updated <td> for debugging
    #print(f"Updated TD Element: {td}")

for i, td in enumerate(td_elements, start=1):
    # Update the main content of the <td>
    #td.string = f'Updated content {i}'

    # Find nested <table> tags within the current <td>
    nested_tables = td.find_all('table')
    
    for j, table in enumerate(nested_tables, start=1):
        #print(f"Nested Table {j} found in TD {i}:")
        
        # Iterate over <tr> (rows) in the nested table
        for k, tr in enumerate(table.find_all('tr'), start=1):
            #print(f"  Row {k} in Nested Table {j}:")
            
            # Iterate over <td> (cells) in each row
            for l, cell in enumerate(tr.find_all('td'), start=1):
                # Example update: modify the content of each cell
                #cell.string = f'Updated Nested Cell {l} in Row {k} of Table {j}'
                #print(f"    Updated Cell {l}: {cell}")
                  # Find nested <table> tags within the current <td>
                nested_tables_2 = cell.find_all('table')
                
                for j_2, table_2 in enumerate(nested_tables_2, start=1):
                    #print(f"Nested Table {j} found in TD {i}:")
                    
                    # Iterate over <tr> (rows) in the nested table
                    for k_2, tr_2 in enumerate(table_2.find_all('tr'), start=1):
                        #print(f"  Row {k} in Nested Table {j}:")
                        
                        # Iterate over <td> (cells) in each row
                        for l_2, cell_2 in enumerate(tr_2.find_all('td'), start=1):
                            # Example update: modify the content of each cell
                            #cell.string = f'Updated Nested Cell {l} in Row {k} of Table {j}'
                            print(f"    Updated Cell {l_2}: {cell_2}")
# Write the modified HTML content back to the file
with open(sample_file, 'w', encoding='utf-8') as file:
    file.write(str(soup))

print("HTML file updated successfully.")
