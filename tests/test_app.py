# Register Number: URK22CS1140
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import add

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

