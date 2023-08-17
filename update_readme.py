import os


def generate_icon_urls(directory):
    icon_urls = []
    for filename in os.listdir(directory):
        if filename.endswith(".png"):  # Adjust file extension as needed
            raw_url = f"https://raw.githubusercontent.com/borkempire/icons/actions/icons/{filename}"
            icon_urls.append(
                (filename, raw_url)
            )  # Append a tuple (filename, raw_url) to the list
    return icon_urls


def update_readme(readme_path, icon_urls):
    with open(readme_path, "r") as f:
        readme_content = f.read()

    # Find the section where you want to insert the table, e.g., <!-- ICONS START --> and <!-- ICONS END -->
    start_marker = "<!-- ICONS START -->"
    end_marker = "<!-- ICONS END -->"

    start_index = readme_content.find(start_marker)
    end_index = readme_content.find(end_marker)

    if start_index != -1 and end_index != -1:
        # Generate the Markdown table of filenames and raw URLs
        table_header = "| filename | raw url |\n| --- | --- |"
        table_rows = "\n".join(
            [f"| {filename} | {raw_url} |" for filename, raw_url in icon_urls]
        )
        markdown_table = f"{table_header}\n{table_rows}"

        # Update the section with the generated table
        updated_readme = (
            readme_content[: start_index + len(start_marker)]
            + f"\n{markdown_table}\n"
            + readme_content[end_index:]
        )

        with open(readme_path, "w") as f:
            f.write(updated_readme)


if __name__ == "__main__":
    icons_directory = "icons"  # Update with your icons directory path
    readme_file = "README.md"  # Update with your README.md file path

    icon_urls = generate_icon_urls(icons_directory)
    update_readme(readme_file, icon_urls)
