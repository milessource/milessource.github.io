from __future__ import annotations

import os

from dataclasses import dataclass

@dataclass
class configurations:
    rules_file: str = "RULES.md"
    html_output_path: str = "rules.html"

def parse_rules(file_content: list) -> list:
    """Parse the rules from text format and convert to structured data."""
    sections: list = []; current_section: bool = None
    for line in file_content:
        line: str = line.strip()
        if line.startswith("###"):
            if current_section: sections.append(current_section)
            current_section = {"header": line[4:], "rules": []}
        elif line.startswith("-"):
            if current_section: current_section["rules"].append({"type": "element", "content": line[2:]})
        elif line.startswith("1.") or line.startswith("2.") or line.startswith("3."):
            if current_section: current_section["rules"].append({"type": "list", "content": line})
        elif line.startswith("   -"):
            if current_section and current_section["rules"]: current_section["rules"][-1].setdefault("subelements", []).append(line[5:])

    if current_section: sections.append(current_section)
    return sections

def generate_html(sections: list) -> str:
    """Generate HTML from the structured rule data."""
    html: str = '<div class="container_try">\n'
    for section in sections:
        html += f'    <h1 class="try_header">{section["header"]}</h1>\n'
        html += '    <div class="try_list">\n'
        for rule in section["rules"]:
            if rule["type"] == "list":
                html += f'        <span class="list_element">{rule["content"]}</span><br>\n'
                if "subelements" in rule:
                    for sub in rule["subelements"]:
                        html += f'        <span class="list_subelement">* {sub}</span><br>\n'
            elif rule["type"] == "element":
                html += f'        <span class="list_element">* {rule["content"]}</span><br>\n'
        html += '    </div>\n'
    html += '</div>'
    return html

def read_rules_file(file_path: str) -> list:
    """Read the rules file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.readlines()

def write_html_file(file_path: str, html_content: str) -> None:
    """Write the HTML content to a file."""
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(html_content)

if __name__ == "__main__":
    if not os.path.exists(configurations.rules_file): exit(1)

    file_content: list = read_rules_file(configurations.rules_file)
    sections: list = parse_rules(file_content)

    html_content: str = generate_html(sections)

    write_html_file(configurations.html_output_path, html_content)
