# Math functions for calculating attributes of circular arcs.

from ndim_base import *

def arc_is_big(start_a=[0.0], end_a=[0.0], direction=True):
    '''Return True if arc is the long way round the center.
Direction follows the right-hand-rule so positive is counter-clockwise.
    '''
    assert isinstance(start_a, list)
    assert isinstance(end_a, list)
    l_angle = len(start_a)
    assert l_angle == len(end_a)
    for i in start_a:
        assert isinstance(i, float)
        assert abs(i) <= 2*pi
    for i in end_a:
        assert isinstance(i, float)
        assert abs(i) <= 2*pi
    assert isinstance(direction, bool)

    diff = [end_a[i] - start_a[i] for i in range(l_angle)]
    diff = [(d < 0.0) != (abs(d) > pi) for d in diff]
    return [d if direction else not d for d in diff]


def arc_length(start_a=[0.0], end_a=[0.0], radius=0.0):
    '''Return Euclidean length of arc.
    '''
    assert isinstance(start_a, list)
    assert isinstance(end_a, list)
    l_angle = len(start_a)
    assert l_angle == len(end_a)
    for i in start_a:
        assert isinstance(i, float)
        assert abs(i) <= 2*pi
    for i in end_a:
        assert isinstance(i, float)
        assert abs(i) <= 2*pi
    assert isinstance(radius, float)
    # Allow negative radius

    full = pi * radius*2
    diff = angle_diff(start_a, end_a, True)
    vec = [full * abs(d)/(2*pi) for d in diff]
    return sqrt(sum([v**2 for v in vec]))

