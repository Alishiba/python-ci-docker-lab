# Register Number: URK22CS1140
import os
import sys

# Ensure the project root (parent of tests/) is on sys.path so CI can import app
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from app import add

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
