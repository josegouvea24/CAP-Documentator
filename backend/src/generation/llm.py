from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

from gen_ai_hub.proxy.native.openai import chat

def generate_cds_documentation(relevant_file_content, llm_model = "gpt-4o", temperature = 0):
    
    system_prompt = """
        You are a technical documentation assistant specialized in SAP CAP (Cloud Application Programming Model). 
        You will be provided with the full content of a CAP project, including all relevant .cds files, service implementations (.js), and metadata files.

        Your task is to generate comprehensive, structured technical documentation in **Markdown** format. The documentation must include the following clearly separated sections:

        1. **Project File Structure**  
        - Show a complete hierarchical folder and file structure of the CAP project.

        2. **CAP Application Files Overview**  
        - Present a two-column table:  
            | File Name | Description |
        - Describe the role and relevance of each application file.

        3. **Data Model Representation**  
        - Render an entity data model Markdown diagram showing:  
            - All entities, their attributes (name, type)
            - Keys
            - Associations and compositions with their cardinality and navigation

        4. **Tables, Views and Types**  
        - Present a table with 4 columns:  
            - Name
            - Type (Table/View/Type) 
            - Fields (name, key, type, default, annotations, etc.) separated by a new line
            - Annotations
            - Description

        5. **CDS Definitions**  
        - For each CDS entity definition, include:
            - Name
            - DB entity of which it is a projection
            - CRUD operations supported (Create/Read/Update/Delete)
            - Fields with types and annotations
            - Description
            - Annotations (access control, semantics, etc.)

        6. **Function and Action Imports**  
        - List each function or action with:
            - Name and description
            - Supported operations
            - Associated entities (if any)

        7. **Event Handlers**  
        - Provide a table with:
            - Handler type (on/before/after)
            - Event type (create/update/delete/get/post)
            - Associated entity,function or action
            - Description of handler
            - Implementation description
            - Helper functions used
            
        8. **Server Helper Functions**
        - Table all helper functions found in "srv/" folder files with:
            - Name
            - Location (file name)
            - Description
            - Parameters
            - Return type
            - Implementation description
        
        
        **Formatting & Completeness Instructions**:
        - Format the full output using Markdown headers, bullet points, and tables.
        - Do not omit any requested section.
        - Be explicit. If a detail cannot be found or deduced, mark it as `[UNKNOWN]`. If a detail is not applicable, mark it as `[NA]`.
        - Include no raw code unless required as an example under a relevant section.
        - Aim for maximum completeness, clarity, and usefulness for developers, especially in implementation descriptions.

        The documentation is intended to be rendered in tools like Microsoft Word or Markdown viewers.

        """

    user_prompt = f"""
                    Here are the CAP project files and their contents:

                    {relevant_file_content}
                    """

    
    response = chat.completions.create(
                    model=llm_model,
                    temperature=temperature,
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_prompt}
                    ]
                )
    
    return response.choices[0].message.content