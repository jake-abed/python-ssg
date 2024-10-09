def markdown_to_blocks(markdown):
    lines = markdown.split("\n\n")
    for i in range(0, len(lines)):
        if lines[i].isspace():
            lines[i] = ""
    filtered_lines = filter(lambda line: line != "", lines)
    return list(filtered_lines)


def block_to_block_type(block):
    if is_heading(block):
        return "heading"
    elif is_code(block):
        return "code"
    elif is_quote(block):
        return "quote"
    elif is_ul(block):
        return "unordered_list"
    elif is_ol(block):
        return "ordered_list"
    else:
        return "paragraph"


def is_heading(block):
    no_hashtag = block.strip("#")
    return block.startswith("#") and no_hashtag.startswith(" ")


def is_code(block):
    return block.startswith("```") and block.endswith("```")


def is_quote(block):
    lines = block.splitlines()
    all_quotes = True
    for line in lines:
        if not line.lstrip().startswith(">"):
            all_quotes = False
        print(line)
    return all_quotes


def is_ul(block):
    lines = block.splitlines()
    all_li = True
    for line in lines:
        if not (line.lstrip().startswith("* ") or line.lstrip().startswith("- ")):
            all_li = False
    return all_li


def is_ol(block):
    lines = block.splitlines()
    all_li = True
    position = 1
    for line in lines:
        if not line.lstrip().startswith(f"{position}. "):
            all_li = False
        position += 1
    return all_li

