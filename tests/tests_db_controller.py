import pytest
from db_controller import DBController
@pytest.fixture
def disable_database_communication(monkeypatch):
    def mock_database(table_name,country_name,lang):
        return [{'Region':'Africa',
                 'City Name':'Angola',
                 'Language': 'test123456encrypted',
                 'Time(ms)': '0.4'
                 },
                 {'Region':'Americas',
                 'City Name':'Colombia',
                 'Language': 'test123456encrypted',
                 'Time(ms)': '0.9'
                 },
                ]
    
    monkeypatch.setattr(DBController,"get_by_country" ,mock_database('Languages','Angola','test123456encrypted'))
    
    


def test_get_by_country(disable_database_communication):
    test_db = DBController('testing.db')
    objects = test_db.get_by_country
    assert isinstance(objects,list)