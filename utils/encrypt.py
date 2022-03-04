import hashlib

def encrypt_language(lang: str):
    """Encrypt using SHA1 

    Args:
        lang (str): language to be encrypted

    Returns:
        _type_: encrypted language
    """
    hashed_language = hashlib.sha1(lang.encode('UTF-8'))
    return hashed_language.hexdigest()