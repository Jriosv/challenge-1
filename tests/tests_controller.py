import pytest 
from controller import Controller
test_response = {
    
        "name": {
            "common": "Angola",
            "official": "Republic of Angola",
            "nativeName": {
                "por": {
                    "official": "República de Angola",
                    "common": "Angola"
                }
            }
        },
        "tld": [
            ".ao"
        ],
        "cca2": "AO",
        "ccn3": "024",
        "cca3": "AGO",
        "cioc": "ANG",
        "independent": True,
        "status": "officially-assigned",
        "unMember": True,
        "currencies": {
            "AOA": {
                "name": "Angolan kwanza",
                "symbol": "Kz"
            }
        },
        "idd": {
            "root": "+2",
            "suffixes": [
                "44"
            ]
        },
        "capital": [
            "Luanda"
        ],
        "altSpellings": [
            "AO",
            "República de Angola",
            "ʁɛpublika de an'ɡɔla"
        ],
        "region": "Africa",
        "subregion": "Middle Africa",
        "languages": {
            "por": "Portuguese"
        },
        "translations": {
            "ara": {
                "official": "أنغولا",
                "common": "جمهورية أنغولا"
            },
            "ces": {
                "official": "Angolská republika",
                "common": "Angola"
            },
            "cym": {
                "official": "Gweriniaeth Angola",
                "common": "Angola"
            },
            "deu": {
                "official": "Republik Angola",
                "common": "Angola"
            },
            "est": {
                "official": "Angola Vabariik",
                "common": "Angola"
            },
            "fin": {
                "official": "Angolan tasavalta",
                "common": "Angola"
            },
            "fra": {
                "official": "République d'Angola",
                "common": "Angola"
            },
            "hrv": {
                "official": "Republika Angola",
                "common": "Angola"
            },
            "hun": {
                "official": "Angola",
                "common": "Angola"
            },
            "ita": {
                "official": "Repubblica dell'Angola",
                "common": "Angola"
            },
            "jpn": {
                "official": "アンゴラ共和国",
                "common": "アンゴラ"
            },
            "kor": {
                "official": "앙골라 공화국",
                "common": "앙골라"
            },
            "nld": {
                "official": "Republiek Angola",
                "common": "Angola"
            },
            "per": {
                "official": "جمهوری آنگولا",
                "common": "آنگولا"
            },
            "pol": {
                "official": "Republika Angoli",
                "common": "Angola"
            },
            "por": {
                "official": "República de Angola",
                "common": "Angola"
            },
            "rus": {
                "official": "Республика Ангола",
                "common": "Ангола"
            },
            "slk": {
                "official": "Angolská republika",
                "common": "Angola"
            },
            "spa": {
                "official": "República de Angola",
                "common": "Angola"
            },
            "swe": {
                "official": "Republiken Angola",
                "common": "Angola"
            },
            "urd": {
                "official": "جمہوریہ انگولہ",
                "common": "انگولہ"
            },
            "zho": {
                "official": "安哥拉共和国",
                "common": "安哥拉"
            }
        },
        "latlng": [
            -12.5,
            18.5
        ],
        "landlocked": False,
        "borders": [
            "COG",
            "COD",
            "ZMB",
            "NAM"
        ],
        "area": 1246700.0,
        "demonyms": {
            "eng": {
                "f": "Angolan",
                "m": "Angolan"
            },
            "fra": {
                "f": "Angolaise",
                "m": "Angolais"
            }
        },
        "flag": "🇦🇴",
        "maps": {
            "googleMaps": "https://goo.gl/maps/q42Qbf1BmQL3fuZg9",
            "openStreetMaps": "https://www.openstreetmap.org/relation/195267"
        },
        "population": 32866268,
        "gini": {
            "2018": 51.3
        },
        "fifa": "ANG",
        "car": {
            "signs": [
                "ANG"
            ],
            "side": "right"
        },
        "timezones": [
            "UTC+01:00"
        ],
        "continents": [
            "Africa"
        ],
        "flags": {
            "png": "https://flagcdn.com/w320/ao.png",
            "svg": "https://flagcdn.com/ao.svg"
        },
        "coatOfArms": {
            "png": "https://mainfacts.com/media/images/coats_of_arms/ao.png",
            "svg": "https://mainfacts.com/media/images/coats_of_arms/ao.svg"
        },
        "startOfWeek": "monday",
        "capitalInfo": {
            "latlng": [
                -8.83,
                13.22
            ]
        }
}

def test_take_data_from_json():
    controller_test = Controller()
    response_dict = controller_test.take_data_from_json(test_response)
    assert response_dict['region'] == 'Africa'
    assert response_dict['city_name'] == 'Angola'
    assert isinstance(response_dict['languages'],dict)
    