def extract_title(markdown):
    # pull the `h1` header from the markdown file and return it
    # if there is no h1 header, raise an exception
    lines = markdown.strip().split('\n')
    for line in lines:
        print(line)
        if line.startswith('# '):
            return line[2:]
    raise ValueError('No h1 header found')