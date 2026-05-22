#!/usr/bin/env python3
import os
import sys
import re
import argparse
import subprocess

def get_latest_project_dir():
    projects_dir = "projects"
    if not os.path.exists(projects_dir):
        return None
    
    subdirs = [os.path.join(projects_dir, d) for d in os.listdir(projects_dir)]
    subdirs = [d for d in subdirs if os.path.isdir(d)]
    
    if not subdirs:
        return None
        
    # Pick the most recently modified project folder
    return max(subdirs, key=os.path.getmtime)

def get_proposal_header(final_proposal_path, project_name):
    default_title = f"Proposal: {project_name.replace('-', ' ').title()}"
    default_header = f"""# {default_title}
**Author**: Ryan Nguyen
**Date**: 2026-05-18
**Version**: Final

"""
    if not os.path.exists(final_proposal_path):
        return default_header
        
    try:
        with open(final_proposal_path, 'r', encoding='utf-8') as f:
            lines = []
            for _ in range(10):  # Read first few lines
                line = f.readline()
                if not line:
                    break
                # Stop if we hit a main header that isn't part of the metadata block
                if line.startswith("## ") or (len(lines) > 0 and line.startswith("# ")):
                    break
                lines.append(line)
            
            header_text = "".join(lines)
            if header_text.strip():
                return header_text
    except Exception as e:
        print(f"Warning: Could not read existing header: {e}")
        
    return default_header

def run_concat(project_path):
    workspace_dir = os.path.join(project_path, "workspace")
    proposal_dir = os.path.join(workspace_dir, "proposal")
    final_proposal_path = os.path.join(workspace_dir, "final-proposal.md")
    
    if not os.path.exists(proposal_dir):
        print(f"Error: Proposal directory not found at {proposal_dir}")
        return False
        
    # Get all .md section files (excluding _index.md or template files)
    files = [f for f in os.listdir(proposal_dir) if f.endswith(".md") and f != "_index.md" and not f.startswith(".")]
    files.sort()  # Sort alphabetically to guarantee 01 to 08 order
    
    if not files:
        print(f"Error: No markdown files found in {proposal_dir}")
        return False
        
    project_name = os.path.basename(os.path.abspath(project_path))
    header = get_proposal_header(final_proposal_path, project_name)
    
    body_parts = []
    for f_name in files:
        f_path = os.path.join(proposal_dir, f_name)
        print(f"Reading section file: {f_name}")
        with open(f_path, 'r', encoding='utf-8') as f:
            content = f.read().strip()
            # Replace any image references to avoid broken paths
            content = content.replace("../assets/", "assets/")
            body_parts.append(content)
            
    combined = header.rstrip() + "\n\n" + "\n\n".join(body_parts) + "\n"
    
    with open(final_proposal_path, 'w', encoding='utf-8') as f:
        f.write(combined)
        
    print(f"✔ Successfully concatenated {len(files)} files into {final_proposal_path}")
    return True

def strip_wbs_columns(markdown_content):
    lines = markdown_content.split('\n')
    new_lines = []
    indices_to_keep = None
    
    for line in lines:
        striped_line = line.strip()
        if striped_line.startswith('|'):
            parts = line.split('|')
            trimmed_parts = [p.strip() for p in parts]
            
            # Detect WBS table header row
            if 'WBS ID' in trimmed_parts and ('Acceptance Criteria' in trimmed_parts or 'Scope Ref' in trimmed_parts):
                indices_to_keep = []
                for i, part in enumerate(trimmed_parts):
                    if i == 0 or i == len(trimmed_parts) - 1:
                        indices_to_keep.append(i)
                    elif part not in ['Acceptance Criteria', 'Scope Ref']:
                        indices_to_keep.append(i)
                new_parts = [parts[idx] for idx in indices_to_keep]
                new_lines.append("|".join(new_parts))
            elif indices_to_keep is not None:
                # Filter data and separator rows to match the header columns
                new_parts = [parts[idx] for idx in indices_to_keep if idx < len(parts)]
                new_lines.append("|".join(new_parts))
            else:
                new_lines.append(line)
        else:
            indices_to_keep = None
            new_lines.append(line)
            
    return "\n".join(new_lines)

def run_wbs_finalize(project_path):
    workspace_dir = os.path.join(project_path, "workspace")
    wbs_path = os.path.join(workspace_dir, "wbs.md")
    final_wbs_path = os.path.join(workspace_dir, "final-wbs.md")
    
    if not os.path.exists(wbs_path):
        print(f"Error: WBS file not found at {wbs_path}")
        return False
        
    with open(wbs_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Ensure WBS has final status metadata
    content = content.replace("Status: Draft", "Status: Approved")
    content = content.replace("Status: Pending", "Status: Approved")
    content = content.replace("Version: 2.0 (Pivot)", "Version: Final")
    content = content.replace("Version: 1.0", "Version: Final")
    content = content.replace("Version: Draft", "Version: Final")
    
    # Strip internal columns for customer-facing final WBS
    content = strip_wbs_columns(content)
    
    with open(final_wbs_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"✔ Successfully finalized WBS into {final_wbs_path}")
    return True

def merge_html_tables(html_content):
    table_pattern = re.compile(r'<table>.*?</table>', re.DOTALL)
    
    def process_table(table_match):
        table_html = table_match.group(0)
        
        thead_match = re.search(r'<thead>(.*?)</thead>', table_html, re.DOTALL)
        if not thead_match:
            return f'<div class="table-container">\n{table_html}\n</div>'
            
        headers = re.findall(r'<th>(.*?)</th>', thead_match.group(1), re.DOTALL)
        headers = [re.sub(r'<[^>]*>', '', h).strip() for h in headers]
        
        columns_to_merge = ['Category', 'Module', 'Function', 'Sub-function']
        column_indices = []
        for col_name in columns_to_merge:
            for idx, h in enumerate(headers):
                if h.lower() == col_name.lower():
                    column_indices.append(idx)
                    break
                    
        if not column_indices:
            return f'<div class="table-container">\n{table_html}\n</div>'
            
        tbody_match = re.search(r'<tbody>(.*?)</tbody>', table_html, re.DOTALL)
        if not tbody_match:
            return f'<div class="table-container">\n{table_html}\n</div>'
            
        tbody_content = tbody_match.group(1)
        
        tr_matches = re.findall(r'<tr>(.*?)</tr>', tbody_content, re.DOTALL)
        if not tr_matches:
            return f'<div class="table-container">\n{table_html}\n</div>'
            
        rows_cells = []
        for tr in tr_matches:
            tds = re.findall(r'<td[^>]*>(.*?)</td>', tr, re.DOTALL)
            rows_cells.append([{'content': td, 'rowspan': 1, 'visible': True} for td in tds])
            
        if not rows_cells:
            return f'<div class="table-container">\n{table_html}\n</div>'
            
        num_rows = len(rows_cells)
        for list_idx, col_idx in enumerate(column_indices):
            prev_cell_dict = None
            rowspan = 1
            
            for row_idx in range(num_rows):
                if col_idx >= len(rows_cells[row_idx]):
                    continue
                cell = rows_cells[row_idx][col_idx]
                cell_text = re.sub(r'<[^>]*>', '', cell['content']).strip()
                
                should_merge = cell_text != "" and cell_text != "—" and cell_text != "-"
                
                parents_match = True
                for k in range(list_idx):
                    parent_col_idx = column_indices[k]
                    if row_idx > 0:
                        if parent_col_idx < len(rows_cells[row_idx]) and parent_col_idx < len(rows_cells[row_idx - 1]):
                            current_parent_text = re.sub(r'<[^>]*>', '', rows_cells[row_idx][parent_col_idx]['content']).strip()
                            prev_parent_text = re.sub(r'<[^>]*>', '', rows_cells[row_idx - 1][parent_col_idx]['content']).strip()
                            if current_parent_text != prev_parent_text:
                                parents_match = False
                                break
                        else:
                            parents_match = False
                            break
                    else:
                        parents_match = False
                        
                if prev_cell_dict and should_merge and parents_match and cell_text == re.sub(r'<[^>]*>', '', prev_cell_dict['content']).strip():
                    rowspan += 1
                    prev_cell_dict['rowspan'] = rowspan
                    cell['visible'] = False
                else:
                    prev_cell_dict = cell
                    rowspan = 1
                    
        new_tbody_lines = []
        for row in rows_cells:
            new_tbody_lines.append("  <tr>")
            for cell in row:
                if not cell['visible']:
                    continue
                if cell['rowspan'] > 1:
                    new_tbody_lines.append(f'    <td rowspan="{cell["rowspan"]}">{cell["content"]}</td>')
                else:
                    new_tbody_lines.append(f'    <td>{cell["content"]}</td>')
            new_tbody_lines.append("  </tr>")
            
        new_tbody_content = "\n" + "\n".join(new_tbody_lines) + "\n"
        
        new_table_html = table_html.replace(tbody_content, new_tbody_content)
        return f'<div class="table-container">\n{new_table_html}\n</div>'
        
    return table_pattern.sub(process_table, html_content)

def format_cover_date(date_str):
    date_str = date_str.strip()
    match = re.match(r'^(\d{4})-(\d{2})-(\d{2})$', date_str)
    if match:
        year, month_num, day_num = match.groups()
    else:
        match = re.match(r'^(\d{1,2})[/-](\d{1,2})[/-](\d{4})$', date_str)
        if match:
            day_num, month_num, year = match.groups()
            month_num = month_num.zfill(2)
        else:
            return date_str
            
    months = {
        "01": "January", "02": "February", "03": "March", "04": "April",
        "05": "May", "06": "June", "07": "July", "08": "August",
        "09": "September", "10": "October", "11": "November", "12": "December"
    }
    month = months.get(month_num, "January")
    
    day = int(day_num)
    if 11 <= day <= 13:
        suffix = "th"
    else:
        suffix = {1: "st", 2: "nd", 3: "rd"}.get(day % 10, "th")
        
    return f"{month} {day}{suffix} {year}"

def generate_proposal_pages(md_content):
    lines = md_content.split('\n')
    title = "ĐỀ XUẤT GIẢI PHÁP"
    author = "Ryan Nguyen"
    date = "2026-05-22"
    version = "Final"
    status = "Approved"
    
    metadata_lines_count = 0
    for idx, line in enumerate(lines[:10]):
        stripped = line.strip()
        if stripped.startswith("# "):
            if idx == 0:
                title = stripped.replace("# ", "").strip()
                metadata_lines_count = idx + 1
            else:
                break
        elif "**Tác giả**" in line or "**Author**" in line or "**Tác giả**" in stripped or "**Author**" in stripped:
            parts = line.split(":")
            if len(parts) > 1:
                author = parts[1].replace("**", "").strip()
            metadata_lines_count = idx + 1
        elif "**Ngày**" in line or "**Date**" in line or "**Ngày**" in stripped or "**Date**" in stripped:
            parts = line.split(":")
            if len(parts) > 1:
                date = parts[1].replace("**", "").strip()
            metadata_lines_count = idx + 1
        elif "**Phiên bản**" in line or "**Version**" in line or "**Phiên bản**" in stripped or "**Version**" in stripped:
            parts = line.split(":")
            if len(parts) > 1:
                version = parts[1].replace("**", "").strip()
            metadata_lines_count = idx + 1
        elif "**Trạng thái**" in line or "**Status**" in line or "**Trạng thái**" in stripped or "**Status**" in stripped:
            parts = line.split(":")
            if len(parts) > 1:
                status = parts[1].replace("**", "").strip()
            metadata_lines_count = idx + 1
        elif stripped == "":
            metadata_lines_count = idx + 1
        else:
            break
            
    # Clean main content (strip title and metadata block)
    main_content_lines = lines[metadata_lines_count:]
    main_content = "\n".join(main_content_lines).strip()
    
    # Detect the heading level for main sections
    heading_level = 1
    m = re.search(r'^(#{1,3})\s*[0-9]+\s*[\.\-]\s*', main_content, re.MULTILINE)
    if m:
        heading_level = len(m.group(1))
    
    # Based on the heading level, we define the regex patterns
    main_pattern = r'^' + ('#' * heading_level) + r'\s*(([0-9]+)\s*[\.\-]\s*.*)'
    sub_pattern = r'^' + ('#' * (heading_level + 1)) + r'\s*(([0-9]+\.[0-9]+(?:\.[0-9]+)?)\s+.*)'
    
    # Extract sections & subheadings for TOC
    h1_matches = list(re.finditer(main_pattern, main_content, re.MULTILINE))
    
    # Hardcoded or estimated page numbers for TOC
    toc_pages = {
        "01": 3,
        "02": 4,
        "03": 5,
        "04": 6,
        "05": 7,
        "06": 9,
        "07": 10,
        "08": 11
    }
    
    if ":" in title:
        title_parts = title.split(":", 1)
        project_name_meta = title_parts[1].strip()
    else:
        project_name_meta = "TranslatorAI"
        
    project_name_display = project_name_meta
    date_formatted = format_cover_date(date)
    
    cover_html = f"""
<div class="word-page cover-page">
  <div class="cover-bg-shape-1"></div>
  <div class="cover-bg-shape-2"></div>
  
  <div class="cover-title-area">
    <div class="cover-subtitle">Project Proposal</div>
    <h1 class="cover-main-title">{project_name_display}</h1>
  </div>
  
  <div class="cover-metadata-area">
    <div class="cover-meta-item">Version: {version}</div>
    <div class="cover-meta-item">Authored by: {author}</div>
    <div class="cover-meta-date">Hanoi, {date_formatted}</div>
  </div>
</div>
"""

    toc_items = []
    for idx, match in enumerate(h1_matches):
        sec_text = match.group(1).strip()
        sec_num = match.group(2).strip()
        sec_prefix = f"{int(sec_num):02d}"
        parent_page = toc_pages.get(sec_prefix, "")
        
        # Add parent section to TOC
        toc_items.append(f"""    <li>
      <span class="toc-name">{sec_text}</span>
      <span class="toc-dots"></span>
      <span class="toc-page-num">{parent_page}</span>
    </li>""")
        
        # Determine the text block range for this section
        start_pos = match.end()
        end_pos = h1_matches[idx + 1].start() if idx + 1 < len(h1_matches) else len(main_content)
        section_content = main_content[start_pos:end_pos]
        
        # Find all subheadings in this section
        h2_matches = list(re.finditer(sub_pattern, section_content, re.MULTILINE))
        
        # Determine the page span for this section
        if parent_page:
            parent_page_num = int(parent_page)
            next_page_num = None
            if idx + 1 < len(h1_matches):
                next_sec_num = h1_matches[idx + 1].group(2).strip()
                next_page_str = toc_pages.get(f"{int(next_sec_num):02d}", "")
                if next_page_str:
                    next_page_num = int(next_page_str)
            
            num_pages = max(1, next_page_num - parent_page_num) if next_page_num else 1
        else:
            parent_page_num = None
            num_pages = 1
            
        for h2_match in h2_matches:
            sub_text = h2_match.group(1).strip()
            if parent_page_num is not None:
                offset = h2_match.start()
                total_len = len(section_content)
                if total_len > 0 and num_pages > 1:
                    # Calculate page offset based on position in section text
                    page_offset = int((offset / total_len) * num_pages)
                    sub_page = parent_page_num + page_offset
                    # Ensure sub_page doesn't exceed parent_page + num_pages - 1
                    sub_page = min(sub_page, parent_page_num + num_pages - 1)
                else:
                    sub_page = parent_page_num
            else:
                sub_page = ""
                
            toc_items.append(f"""    <li class="toc-sub-item">
      <span class="toc-name">{sub_text}</span>
      <span class="toc-dots"></span>
      <span class="toc-page-num">{sub_page}</span>
    </li>""")
        
    toc_list_html = "\n".join(toc_items)
    
    toc_html = f"""
<div class="word-page toc-page">
  <h1 class="toc-title">MỤC LỤC</h1>
  <div class="toc-divider"></div>
  <ul class="toc-list">
{toc_list_html}
  </ul>
</div>
"""
    
    return cover_html, toc_html, main_content, heading_level

def convert_md_to_html(md_path, html_path, title, default_template_path, project_path):
    if not os.path.exists(md_path):
        print(f"File not found for HTML conversion: {md_path}")
        return False
        
    # Check for project-specific template first
    custom_template = os.path.join(project_path, "_delivery/export-template.html")
    template_to_use = custom_template if os.path.exists(custom_template) else default_template_path
    
    print(f"Converting {md_path} to HTML using template: {template_to_use}...")
    
    with open(md_path, 'r', encoding='utf-8') as f:
        md_content = f.read()
        
    # Exclude internal-only sections from the HTML export
    md_content = re.sub(r'## Scope Coverage Check.*?(?=## |\Z)', '', md_content, flags=re.DOTALL)
    
    is_proposal = "proposal" in html_path.lower() or "proposal" in md_path.lower()
    
    if is_proposal:
        cover_html, toc_html, cleaned_md, heading_level = generate_proposal_pages(md_content)
        result = subprocess.run(['npx', 'marked', '--gfm'], input=cleaned_md, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Error converting markdown via marked: {result.stderr}")
            return False
        main_html = result.stdout
        main_html = merge_html_tables(main_html)
        
        # Split main_html into separate sections by H1/H2 tags to layout them as separate pages
        split_tag = f"h{heading_level}"
        sections_html = re.split(rf'(?=<{split_tag}[^>]*>)', main_html)
        wrapped_sections = []
        for sec in sections_html:
            sec = sec.strip()
            if sec:
                wrapped_sections.append(f'<div class="word-page">\n{sec}\n</div>')
        html_body = f"{cover_html}\n{toc_html}\n" + "\n".join(wrapped_sections)
    else:
        result = subprocess.run(['npx', 'marked', '--gfm'], input=md_content, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Error converting markdown via marked: {result.stderr}")
            return False
        html_body = result.stdout
        html_body = merge_html_tables(html_body)
        
    with open(template_to_use, 'r', encoding='utf-8') as f:
        template = f.read()
        
    # Check for project-specific custom CSS overrides
    custom_css_path = os.path.join(project_path, "_delivery/style.css")
    if os.path.exists(custom_css_path):
        with open(custom_css_path, 'r', encoding='utf-8') as css_file:
            custom_css = css_file.read()
        # Inject custom CSS style block before closing head tag
        css_tag = f"<style>\n{custom_css}\n</style>\n</head>"
        template = template.replace("</head>", css_tag)
        print(f"ℹ Injected custom styles from {custom_css_path}")
        
    if is_proposal:
        output_html = template.replace("{{title}}", title)
        output_html = re.sub(r'<div class="word-page">\s*\{\{body\}\}\s*</div>', html_body, output_html)
    else:
        output_html = template.replace("{{title}}", title).replace("{{body}}", html_body)
    
    # Apply landscape classes if it's WBS
    is_landscape = "wbs" in html_path.lower() or "wbs" in md_path.lower() or "wbs" in title.lower()
    if is_landscape:
        output_html = output_html.replace('class="word-page"', 'class="word-page landscape"')
        output_html = output_html.replace('<body>', '<body class="has-landscape">')
    
    os.makedirs(os.path.dirname(html_path), exist_ok=True)
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(output_html)
        
    print(f"✔ Exported styled HTML to {html_path}")
    return True

def run_export(project_path):
    workspace_dir = os.path.join(project_path, "workspace")
    delivery_dir = os.path.join(project_path, "_delivery")
    template_path = ".agent/references/designs/export-template.html"
    
    if not os.path.exists(template_path):
        print(f"Error: Export template not found at {template_path}")
        return False
        
    project_name = os.path.basename(os.path.abspath(project_path))
    
    # 1. Export Proposal HTML
    prop_md = os.path.join(workspace_dir, "final-proposal.md")
    prop_html = os.path.join(delivery_dir, "final-proposal.html")
    convert_md_to_html(prop_md, prop_html, f"Proposal: {project_name.replace('-', ' ').title()}", template_path, project_path)
    
    # 2. Export WBS HTML
    wbs_md = os.path.join(workspace_dir, "final-wbs.md")
    wbs_html = os.path.join(delivery_dir, "final-wbs.html")
    convert_md_to_html(wbs_md, wbs_html, f"WBS: {project_name.replace('-', ' ').title()}", template_path, project_path)
    
    return True

def main():
    parser = argparse.ArgumentParser(description="Automate presale proposal concatenation, WBS finalization, and HTML exports.")
    parser.add_argument("--project", help="Path to the project directory (e.g., projects/2026-05-11-terrafuse)")
    parser.add_argument("--concat", action="store_true", help="Concatenate proposal sections into final-proposal.md")
    parser.add_argument("--wbs", action="store_true", help="Finalize WBS into final-wbs.md")
    parser.add_argument("--export", action="store_true", help="Compile and export documents into _delivery/ HTML formats")
    parser.add_argument("--all", action="store_true", help="Execute all steps (concat, wbs, export)")
    
    args = parser.parse_args()
    
    # Determine project directory
    project_path = args.project
    if not project_path:
        project_path = get_latest_project_dir()
        if not project_path:
            print("Error: No project specified and no projects found in 'projects/' directory.")
            sys.exit(1)
        print(f"No --project specified. Using most recently modified project: {project_path}")
        
    if not os.path.exists(project_path):
        print(f"Error: Project directory '{project_path}' does not exist.")
        sys.exit(1)
        
    print(f"=== Presale Helper Target: {project_path} ===")
    
    success = True
    
    # Default behavior if no action specified is --all
    run_all = args.all or (not args.concat and not args.wbs and not args.export)
    
    if run_all or args.concat:
        print("\n--- Step 1: Concatenating Proposal ---")
        if not run_concat(project_path):
            success = False
            
    if run_all or args.wbs:
        print("\n--- Step 2: Finalizing WBS ---")
        if not run_wbs_finalize(project_path):
            success = False
            
    if run_all or args.export:
        print("\n--- Step 3: Exporting Deliverables ---")
        if not run_export(project_path):
            success = False
            
    if success:
        print("\n🎉 Presale automation finished successfully!")
    else:
        print("\n❌ Presale automation completed with errors.")
        sys.exit(1)

if __name__ == "__main__":
    main()
