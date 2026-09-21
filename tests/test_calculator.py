import sys
import os

# 让 pytest 能找到 src 目录
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from calculator import add, divide
import pytest


def test_add():
    assert add(1, 2) == 3


def test_add_negative():
    assert add(-1, 1) == 0


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(1, 0)