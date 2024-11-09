def markdown_to_blocks(markdown):
    # takes a raw Markdown string (representing a full document) as input and returns a list of "block" strings.
    # Strip any leading or trailing whitespace from each block.
    # Remove any "empty" blocks due to excessive newlines.
    
    # Split the input text into blocks based on an empty line between blocks.
    blocks = markdown.split("\n\n")
    # Initialize a list to store the cleaned blocks.
    cleaned_blocks = []
    # Iterate over the blocks.
    for block in blocks:
        # Strip any leading or trailing whitespace from the block.
        block = block.strip()
        # If the block is not empty, add it to the cleaned blocks list.
        if block:
            cleaned_blocks.append(block)

    return cleaned_blocks