import pytest
from fastapi.testclient import TestClient

from app.config import Settings
from app.main import app as _app
from app.routes.routes import get_settings

client = TestClient(_app)


def get_settings_override():
    """
    Used to override the env variable that determines the root directory, we set to
    a directory within the /tests folder to manage test outcomes
    """
    return Settings(target_dir = 'tests/sample_dir')

def get_settings_override_invalid():
    """
    This function is used in some tests to override the environment variable
    that determines the root dir the user passes in. This is to test the case
    when a user enteres a root directory that is invalid
    """
    return Settings(target_dir = 'tests/sample_dir_invalid')


_app.dependency_overrides[get_settings] = get_settings_override


def process_404(response):
    assert response.status_code == 404
    assert response.json() == {"detail": "Item not found"}

def test_index_route():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == [
      {
        "name": ".hidden",
        "owner": "jkirsch",
        "size": 64,
        "permissions": 755
      },
      {
        "name": "foo",
        "owner": "jkirsch",
        "size": 64,
        "permissions": 755
      },
      {
        "name": "test.txt",
        "owner": "jkirsch",
        "size": 43,
        "permissions": 644
      },
      {
        "name": "bar",
        "owner": "jkirsch",
        "size": 128,
        "permissions": 755
      }
    ]

def test_index_route_invalid_root():
    _app.dependency_overrides[get_settings] = get_settings_override_invalid
    response = client.get('/')
    process_404(response)
    _app.dependency_overrides[get_settings] = get_settings_override

def test_hidden_directory():
    response = client.get('/')
    found_hidden = False
    for dir in response.json():
        if '.' in dir['name']:
            found_hidden=True
    assert found_hidden

def test_path_dir_l0_valid():
    response = client.get('/foo')
    assert response.status_code == 200
    assert response.json() == []

def test_path_dir_l0_invalid():
    response = client.get('/invalid_dir')
    process_404(response)

def test_path_file_l0_valid():
    response = client.get('/test.txt')
    assert response.status_code == 200
    assert response.json() == "this is a test file\nwith two lines of text\n"

def test_path_file_l0_invalid():
    response = client.get('/test_invalid.txt')
    process_404(response)


def test_path_dir_l1_valid():
    response = client.get('/bar')
    assert response.status_code == 200
    assert response.json() == [
                                  {
                                    "name": "text.txt",
                                    "owner": "jkirsch",
                                    "size": 52,
                                    "permissions": 644
                                  },
                                  {
                                    "name": "baz",
                                    "owner": "jkirsch",
                                    "size": 96,
                                    "permissions": 755
                                  }
                                ]

def test_path_dir_l2_valid():
    response = client.get('/bar/baz')
    assert response.status_code == 200
    assert response.json() == [
                                  {
                                    "name": "baz.txt",
                                    "owner": "jkirsch",
                                    "size": 40,
                                    "permissions": 644
                                  }
                                ]
