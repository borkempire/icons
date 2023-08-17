import os

def generate_icon_urls(directory):
    icon_urls = []
    for filename in os.listdir(directory):
        if filename.endswith(".png"):  # Adjust file extension as needed
            raw_url = f"https://raw.githubusercontent.com/borkempire/icons/actions/icons/{filename}"
            icon_urls.append(raw_url)  # Append raw_url to the list
    return icon_urls

def update_readme(readme_path, icon_urls):
    with open(readme_path, "r") as f:
        readme_content = f.read()

    # Find the section where you want to insert the URLs, e.g., <!-- ICONS START --> and <!-- ICONS END -->
    start_marker = "<!-- ICONS START -->"
    end_marker = "<!-- ICONS END -->"

    start_index = readme_content.find(start_marker)
    end_index = readme_content.find(end_marker)

    if start_index != -1 and end_index != -1:
        # Generate the Markdown list of raw URLs
        raw_urls_list = "\n".join([f"- {url}" for url in icon_urls])

        # Update the section with the generated URLs
        updated_readme = (
            readme_content[:start_index + len(start_marker)] +
            f"\n{raw_urls_list}\n" +
            readme_content[end_index:]
        )

        with open(readme_path, "w") as f:
            f.write(updated_readme)

if __name__ == "__main__":
    icons_directory = "icons"  # Update with your icons directory path
    readme_file = "README.md"   # Update with your README.md file path
    
    icon_urls = generate_icon_urls(icons_directory)
    update_readme(readme_file, icon_urls)
