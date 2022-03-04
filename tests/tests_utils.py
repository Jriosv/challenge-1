import string
import pytest
from utils.encrypt import encrypt_language
from utils.time_decorator import take_time
import time

def test_ecrypt_language():
    lang = 'Spanish'
    encrypted_language = encrypt_language(lang)
    assert lang != encrypted_language
    assert isinstance(encrypted_language,str) #must continue being string
    
def test_time_decorator():
    @take_time
    def do_anything():
        time.sleep(2)

    how_many = do_anything()
    assert how_many is not None
    assert isinstance(how_many,float)
    