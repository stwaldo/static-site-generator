import shutil
from generatepage import generate_pages_recursive
from node_types.textnode import TextNode

def main():
    copy_static_to_public()
    generate_pages_recursive('content', 'template.html', 'public')
    
def copy_static_to_public():
    # Delete contents of the `public` folder
    shutil.rmtree('public') 
    # recursively copy the contents of the `static` folder to the `public` folder
    shutil.copytree('static', 'public')

if __name__ == "__main__":
    main()