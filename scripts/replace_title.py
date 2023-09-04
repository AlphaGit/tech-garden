import os
import re

def process_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    title_match = re.search(r'^#\s(.+)$', content, re.MULTILINE)
    if title_match:
        title = title_match.group(1)
    else:
        title = os.path.basename(file_path).replace('.md', '')

    new_content = re.sub(r'title: "{{title}}"', f'title: "{title}"', content)

    with open(file_path, 'w') as file:
        file.write(new_content)

def main():
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".md"):
                process_file(os.path.join(root, file))

    print("Finished processing all markdown files.")

if __name__ == "__main__":
    main()
