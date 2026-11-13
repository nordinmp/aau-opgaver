import pytest
import lektion9 as l9

def test_draw_grid():
    assert l9.draw_grid(0, 0) == []
    assert l9.draw_grid(None, 0) == []
    assert l9.draw_grid(0, None) == []
    assert l9.draw_grid(None, None) == []

def test_draw_grid_valid():
    assert l9.draw_grid(1, 1) == [['0']]
    assert l9.draw_grid(2, 2) == [['0', '0'], ['0', '0']]
    assert l9.draw_grid(3, 3) == [['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
    assert l9.draw_grid(4, 4) == [['0', '0', '0', '0'], ['0', '0', '0', '0'], ['0', '0', '0', '0'], ['0', '0', '0', '0']]
