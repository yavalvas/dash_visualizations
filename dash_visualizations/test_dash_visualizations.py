import pytest
import dash_html_components as html
from app import app

def test_debug_is_disabled():
    assert app.server.debug is False

def test_layout_is_a_function_that_returns_a_div_element():
    assert isinstance(app.layout(), html.Div)
