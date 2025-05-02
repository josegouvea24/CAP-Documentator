from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

from gen_ai_hub.proxy.native.openai import chat

def call_llm(prompt: str, model: str = "gpt-4o", temperature: float = 0) -> str:
    """
    Calls LLM with a given prompt through AI Core and returns the response.
    
    Args:
        prompt (str): The user prompt.
        model (str): LLM model name (e.g., "gpt-4o").
    
    Returns:
        str: The LLM-generated response.
    """
    
    try:
        response = chat.completions.create(
                        model=model,
                        temperature=temperature,
                        messages=[
                            {"role": "system", "content": "You are a documentation assistant."},
                            {"role": "user", "content": prompt}
                        ]
                    )
    
        return response.choices[0].message.content
    
    except Exception as e:
        print(f"❌ LLM call failed: {e}")
        return "[ERROR: failed to get LLM response]"