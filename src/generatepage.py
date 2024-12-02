from extracttitle import extract_title
from markdowntohtmlnode import markdown_to_html_node


def generate_page(from_path, template_path, dest_path):
    print("Generating page from {} to {} using {}", from_path, dest_path, template_path)
   
    with open(from_path, 'r') as f:
        markdown = f.read()
        
    with open(template_path, 'r') as f:
        template = f.read()
        
    html = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    
    template = template.replace('{{ Title }}', title)
    template = template.replace('{{ Content }}', html)
    
    with open(dest_path, 'w') as f:
        f.write(template)
    