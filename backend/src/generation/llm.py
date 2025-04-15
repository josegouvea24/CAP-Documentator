from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

from gen_ai_hub.proxy.native.openai import chat

def generate_cds_documentation(relevant_file_content, llm_model = "gemini-1.5-pro", temperature = 0):
    
    system_prompt = """
        You are a technical documentation assistant specialized in SAP CAP (Cloud Application Programming Model). 
        You will receive the full content of a CAP project, including all relevant .cds files, service implementations (.js), and metadata/configuration files.

        Your task is to generate complete, structured, and developer-friendly technical documentation in **Markdown** format. The documentation must be organized into the following clearly labeled sections:

        ---

        1. **Project File Structure**  
        - Provide a full hierarchical folder and file structure of the CAP project using indentation or tree-style formatting.

        2. **CAP Application Files Overview**  
        - Present a two-column table:  
            | File Name | Description |
        - Describe the purpose and role of each file in the application context.

        3. **Data Model Representation**  
        - Use a Markdown diagram or text-based representation showing:
            - All entities
            - Attributes (name, type, default, key)
            - Associations and compositions with cardinality (1:1, 1:n, etc.)
            - Navigation paths between entities

        4. **DB Schema**  
        - Cover all Tables, Views, and Types.
        - Use a table with the following columns:  
            | Name | Type (Table/View/Type) | Fields (name, key, type, default, annotations) | Annotations | Description |

        5. **CDS Definitions**  
        - For each CDS definition, present a table including:
            | Name | Projected DB Entity | Supported CRUD Operations | Fields (name, type, annotations) | Description | Annotations |

        6. **Function and Action Imports**  
        - Provide a table with the following columns:  
            | Name | Type (Function/Action) | Description | Supported Operation (GET/POST) | Parameters (name, type, default) | Return Type | Annotations | Associated Entities |

        7. **Event Handlers**  
        - For every handler in the implementation layer, document:  
            | Handler Type (on/before/after) | Operation (Create/Read/Update/Delete/Custom) | Target (Entity/Function/Action) | Implementation Description | Helper Functions Used |

        8. **Server Helper Functions**  
        - Extract and describe reusable helper functions defined in the `srv/` folder:  
            | Function Name | Location (relative file path) | Description | Parameters (name, type, default) | Return Type | Implementation Logic Summary |

        ---

        **⚠️ Output Instructions – Must Follow Without Exception**:
        - **Do not** omit or leave any section blank.
        - For **every detail requested**, include a placeholder if the value is missing:
            - `[N/A]` — Not applicable for this context.
            - `[EMPTY]` — Expected but no value was found in the input.
            - `[UNKNOWN]` — Could not be deduced or inferred confidently.
        - **Never** leave any field or table cell empty.
        - Avoid raw code unless absolutely necessary.
        - Provide clear, concise, and technical descriptions suitable for SAP CAP developers.

        The documentation must be copy-paste ready for Markdown viewers or Microsoft Word.
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