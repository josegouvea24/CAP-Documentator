import os

def load_file_content(file_list, only_relevant=True):
    content = ""

    for file in file_list: 
        header = (
                    f"\n\n===== FILE: {file['name']} =====\n"
                    f"Path   : {file['rel_path']}\n"
                    f"Format : {file['format']}\n"
                )
        
        if only_relevant and not file["is_relevant"]:
            file_content = "THIS FILE'S CONTENT IS IRRELEVANT FOR CAP PROJECT DOCUMENTATION"
        else:
            try:
                with open(file["full_path"], "r", encoding="utf-8") as f:
                    file_content = f.read()
            except Exception as e:
                file_content = f"⚠️ Skipping file {file.get('rel_path', 'unknown')} due to error: {e}"

        content += f"{header}\n{file_content}\n"
    
    return content