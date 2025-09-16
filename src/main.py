import shutil
import sys
import os
from generatepage import generate_pages_recursive

def main():
    basepath = sys.argv[1] if len(sys.argv) > 1 else '/'
    copy_static_to_public()
    generate_pages_recursive('content', 'template.html', 'docs', basepath)
def copy_static_to_public():
    # Delete contents of the `docs` folder
    if os.path.exists('docs'):
        shutil.rmtree('docs')
    # recursively copy the contents of the `static` folder to the `docs` folder
    shutil.copytree('static', 'docs')

if __name__ == "__main__":
    main()