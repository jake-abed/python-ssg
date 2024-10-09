def markdown_to_blocks(markdown):
    lines = markdown.split("\n\n")
    for i in range(0, len(lines)):
        if lines[i].isspace():
            lines[i] = ""
    filtered_lines = filter(lambda line: line != "", lines)
    return list(filtered_lines)

