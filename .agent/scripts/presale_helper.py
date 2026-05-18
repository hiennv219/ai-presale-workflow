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
**Author**: Sotek Engineering
**Date**: 2026-05-18
**Version**: Final (8-Section Standardized)

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
                if line.startswith("## "):
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

def convert_md_to_html(md_path, html_path, title, default_template_path, project_path):
    if not os.path.exists(md_path):
        print(f"File not found for HTML conversion: {md_path}")
        return False
        
    # Check for project-specific template first
    custom_template = os.path.join(project_path, "_delivery/export-template.html")
    template_to_use = custom_template if os.path.exists(custom_template) else default_template_path
    
    print(f"Converting {md_path} to HTML using template: {template_to_use}...")
    result = subprocess.run(['npx', 'marked', '-i', md_path, '--gfm'], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error converting markdown via marked: {result.stderr}")
        return False
        
    html_body = result.stdout
    
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
        
    output_html = template.replace("{{title}}", title).replace("{{body}}", html_body)
    
    os.makedirs(os.path.dirname(html_path), exist_ok=True)
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(output_html)
        
    print(f"✔ Exported styled HTML to {html_path}")
    return True

def compile_marp_deck(deck_path, html_path):
    if not os.path.exists(deck_path):
        print(f"Slide deck {deck_path} not found. Skipping Marp compile.")
        return False
        
    print(f"Compiling Marp deck {deck_path} to HTML...")
    result = subprocess.run(['npx', '@marp-team/marp-cli', deck_path, '-o', html_path], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error compiling Marp deck: {result.stderr}")
        return False
        
    print(f"✔ Compiled Marp slide deck to {html_path}")
    return True

def run_export(project_path):
    workspace_dir = os.path.join(project_path, "workspace")
    delivery_dir = os.path.join(project_path, "_delivery")
    template_path = ".agent/references/export-template.html"
    
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
    
    # 3. Compile Slide Deck via Marp
    deck_md = os.path.join(workspace_dir, "slide-deck.md")
    deck_html = os.path.join(delivery_dir, "slide-deck.html")
    compile_marp_deck(deck_md, deck_html)
    
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
