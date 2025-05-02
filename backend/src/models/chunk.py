from dataclasses import dataclass, field

@dataclass
class DocChunk:
    name: str             # logical name or file base name
    path: str             # relative path in the repo
    section: str          # "root", "srv", "db", etc.
    type: str             # "cds", "js", "xml", etc.
    content: str          # raw file content
    metadata: dict = field(default_factory=dict) # additional metadata
