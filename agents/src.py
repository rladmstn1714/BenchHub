import re

def get_translation_section(text: str) -> str:
    """
    Extracts and returns the text enclosed by <translation>...</translation>.
    Returns None if the tags are not found.
    """
    pattern = re.compile(r"<translation>(.*?)</translation>", re.DOTALL)
    match = pattern.search(text)
    if match:
        return match.group(1).strip()
    return None
    
def parse_litellm_response(responses):
    full_response = []
    translation = []
    for res in responses:
        try:
            fres = res.choices[0].message.content
            trans = get_translation_section(fres)
        except:
            fres = None
            trans = None
        full_response.append(fres)
        translation.append(trans)
    return full_response, translation