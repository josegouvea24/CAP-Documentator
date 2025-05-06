from pathlib import Path
from models.doc_chunk import DocChunk

def chunk_files(repo_path: Path, files_by_section: dict) -> list[DocChunk]:
    """
    Chunk files into a list of DocChunks objects with metadata.
    
    Args:
        repo_path (Path): The path to the repository.
        files_by_section (dict): A dictionary containing files grouped by section and then type.
        
    Returns:
        list: A list of DocChunks objects representing the chunked files.
    """
    chunks = []

    for section, files in files_by_section.items():
        for file_type, file_paths in files.items():
            for file_path in file_paths:
                full_path = repo_path / file_path
                try:
                    with open(full_path, 'r', encoding='utf-8') as f:
                        content = f.read()
  
                    chunk = DocChunk(
                        name=file_path.stem,
                        path=str(file_path),
                        section=section,
                        type=file_type,
                        content=content,
                        summary="",
                    )
                    chunks.append(chunk)
                
                except Exception as e:
                    print(f"❌ Failed to read {file_path}: {e}")

    return chunks