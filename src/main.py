import os
import shutil
import markdown


def main():
    print("Starting SSG")
    copy_dir("./static", "./public")
    generate_pages_recursively("./content", "template.html", "./public")


def copy_dir(src_dir, target_dir):
    print(f"Starting transfer of {src_dir} to {target_dir}...")
    if not os.path.exists(src_dir):
        raise NotADirectoryError(f"{src_dir} does not exist.")
    if os.path.exists(target_dir):
        shutil.rmtree(target_dir)
    os.mkdir(target_dir)
    src_contents = os.listdir(src_dir)
    if len(src_contents) == 0:
        print("Empty dir, nothing copied")
        return
    for item in src_contents:
        item_path = os.path.join(src_dir, item)
        if os.path.isfile(item_path):
            shutil.copy(item_path, target_dir)
        else:
            new_target_dir = os.path.join(target_dir, item)
            copy_dir(item_path, new_target_dir)
    print(f"Completed transfer from {src_dir} to {target_dir}!")
    return


def generate_page(src_path, template_path, target_path):
    print(f"Generating page from {src_path} to {target_path} using {template_path}")
    md_file = open(src_path)
    md = md_file.read()
    template_file = open(template_path)
    template = template_file.read()
    title = markdown.extract_title(md)
    content = markdown.markdown_to_html_node(md).to_html()
    page = template.replace("{{ Title }}", title).replace("{{ Content }}", content)
    target_dir = os.path.dirname(target_path)
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    target_file = open(target_path, mode='w')
    target_file.write(page)
    target_file.close()


def generate_pages_recursively(content_dir, template_path, target_dir):
    print(content_dir, template_path, target_dir)
    contents = os.listdir(content_dir)
    for content in contents:
        content_path = os.path.join(content_dir, content)
        target_path = os.path.join(target_dir, content)
        if os.path.isfile(content_path):
            generate_page(content_path, template_path, target_path.replace(".md", ".html"))
        else:
            generate_pages_recursively(content_path, template_path, target_path)


main()

