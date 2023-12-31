import os


def generate_icon_urls(directory: str) -> list:
    icon_urls = []
    for filename in os.listdir(directory):
        if filename.endswith(".png") or filename.endswith(".svg"):
            raw_url = f"https://raw.githubusercontent.com/borkempire/icons/main/icons/{filename}"
            icon_urls.append((filename, raw_url))
    return icon_urls


def update_readme(readme_path: str, icon_urls: list) -> None:
    sorted_icon_urls = sorted(icon_urls, key=lambda x: x[0])

    with open(readme_path, "r") as f:
        readme_content = f.read()

    # section to insert the table
    start_marker = "<!-- ICONS START -->"
    end_marker = "<!-- ICONS END -->"

    start_index = readme_content.find(start_marker)
    end_index = readme_content.find(end_marker)

    if start_index != -1 and end_index != -1:
        # Generate the Markdown table of filenames and raw URLs
        table_header = "| filename | raw url |\n| --- | --- |"
        table_rows = "\n".join(
            [f"| {filename} | {raw_url} |" for filename, raw_url in sorted_icon_urls]
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
    icons_directory = "icons"
    readme_file = "README.md"

    icon_urls = generate_icon_urls(icons_directory)
    update_readme(readme_file, icon_urls)
