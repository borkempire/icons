import os


def generate_icon_urls(directory):
    icon_urls = []
    for filename in os.listdir(directory):
        if filename.endswith(".png"):  # Adjust file extension as needed
            raw_url = f"https://raw.githubusercontent.com/borkempire/icons/actions/icons/{filename}"
            icon_urls.append(f"- [{filename}]({raw_url})")
    return icon_urls


def update_readme(readme_path, icon_urls):
    with open(readme_path, "r") as f:
        lines = f.readlines()

    # Find the section where you want to insert the URLs, e.g., <!-- ICONS START --> and <!-- ICONS END -->
    start_marker = "<!-- ICONS START -->"
    end_marker = "<!-- ICONS END -->"
    start_index = None
    end_index = None

    for i, line in enumerate(lines):
        if start_marker in line:
            start_index = i
        if end_marker in line:
            end_index = i

    if start_index is not None and end_index is not None:
        # Update the section with the generated URLs
        updated_lines = lines[: start_index + 1] + icon_urls + lines[end_index:]

        with open(readme_path, "w") as f:
            f.writelines(updated_lines)


if __name__ == "__main__":
    icons_directory = "icons"  # Update with your icons directory path
    readme_file = "README.md"  # Update with your README.md file path

    icon_urls = generate_icon_urls(icons_directory)
    update_readme(readme_file, icon_urls)
