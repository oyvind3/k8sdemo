import os
import sys

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from app import app
import werkzeug

if not hasattr(werkzeug, "__version__"):
    werkzeug.__version__ = "0"


def test_index_contains_head_tag():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    html = response.data.decode('utf-8')
    assert '</head>' in html
