import os
from extracttitle import extract_title
from markdowntohtmlnode import markdown_to_html_node


def generate_page(from_path, template_path, dest_path, basepath):
    print("Generating page from {} to {} using {}", from_path, dest_path, template_path)
   
    with open(from_path, 'r') as f:
        markdown = f.read()
        
    with open(template_path, 'r') as f:
        template = f.read()
        
    html = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    
    template = template.replace('{{ Title }}', title)
    template = template.replace('{{ Content }}', html)
    template = template.replace('href="/', f'href="{ basepath }')
    template = template.replace('src="/', f'src="{ basepath }')

    with open(dest_path, 'w') as f:
        f.write(template)
    
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    # crawl every entry in the `dir_path_content` directory
    # for each markdown file, generate a new `.html` file using the same template, written to the `dest_dir_path`
    # directory structure from `dir_path_content` should be maintained in `dest_dir_path`
    # if an entry is a directory, call this function recursively
    
    for entry in os.listdir(dir_path_content):
        entry_path = os.path.join(dir_path_content, entry)
        dest_entry_path = os.path.join(dest_dir_path, entry)
        
        if os.path.isdir(entry_path):
            os.makedirs(dest_entry_path, exist_ok=True)
            generate_pages_recursive(entry_path, template_path, dest_entry_path, basepath)
        elif entry.endswith('.md'):
            dest_entry_path = os.path.splitext(dest_entry_path)[0] + '.html'
            generate_page(entry_path, template_path, dest_entry_path, basepath)
        else:
            os.makedirs(dest_entry_path, exist_ok=True)