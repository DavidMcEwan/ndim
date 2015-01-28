# Math functions for calculating attributes of circular arcs.

# arcinfo_* functions fill in the unknown attributes of an N-dimensional arc.
# Attributes to be filled in by arcinfo_*():
#   radius:         float
#   center:         (float, float)
#   start_pt:       (float, float, ...)
#   end_pt:         (float, float, ...)
#   start_angle:    [float, ...]; 0 <= x <= 2*pi
#   end_angle:      [float, ...]; 0 <= x <= 2*pi
#   diff_angle:     [float, ...]; -2*pi <= x <= 2*pi
#   direction:      bool; True=counter-clockwise, False=clockwise
#   big:            [bool, ...]
#   length:         float
# These are extrapolated to N

from ndim_base import *

def arc_is_big(start_a=[0.0], end_a=[0.0], direction=True):
    '''Return True if arc is the long way round the center.
Direction follows the right-hand-rule so positive is counter-clockwise.
    '''
    assert isinstance(start_a, list)
    assert isinstance(end_a, list)
    l_angle = len(start_a)
    assert l_angle > 0
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
    assert l_angle > 0
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


def arcinfo_center_angles(center=(0.0, 0.0),
                          radius=0.0,
                          start_a=[0.0],
                          end_a=[0.0],
                          direction=True):
    ret = dict()
    ret['center'] = center
    ret['radius'] = radius
    ret['start_a'] = start_a
    ret['end_a'] = end_a
    ret['direction'] = direction
    ret['start_pt'] = pt_relative(center, [radius, 0.0], start_a)
    ret['end_pt'] = pt_relative(center, [radius, 0.0], end_a)
    ret['diff_a'] = angle_diff(start_a, end_a, direction)
    ret['big'] = arc_is_big(start_a, end_a, direction)
    ret['length'] = arc_length(start_a, end_a, radius)
    return ret

