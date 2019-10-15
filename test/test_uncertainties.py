
from LabTools.utils.uncertainties import *

from uncertainties import ufloat


def test_unarray_unpackuarray():
    a = numpy.array([ufloat(2, 3), ufloat(4, 5), ufloat(6., 7.)])
    b = numpy.array([2, 4, 6.])
    c = numpy.array([3, 5, 7.])
    d = numpy.array([3.])
    
    b_, c_ = unpack_unarray(a)
    assert(b.all() == b_.all())
    assert(c.all() == c_.all())
    
    a_ = unarray(b, c)
    # We need str beacuse uncertainties behavior with comparsion
    assert(str(a_.all()) == str(a.all()))
    
    assert(str(a.all()) == str(unarray(*unpack_unarray(a)).all()))
    b__, c__ = unpack_unarray(unarray(b, c))
    assert(b__.all() == b.all())
    assert(c__.all() == c.all())
    try:
        unarray(a, d)
    except IndexError:
        pass

def test_de2unc():
    # Test Lab3
    assert(str(de2unc(1.673, 0.001, 0.5)) == '1.673+/-0.008')
    assert(str(de2unc(1.673, 0.001, 0.5, False)) == '1.673+/-0.009')
    
    assert(str(de2unc(0.167, 0.001, 0.5)) == '0.1670+/-0.0013')
    assert(str(de2unc(0.167, 0.001, 0.5, False)) == '0.1670+/-0.0018')
    
    a = numpy.array([1.0, 2.0])
    b = numpy.array([0.1, 0.2])
    c = numpy.array([1, 1])
    res = numpy.array([ufloat(1.0, 0.100498), ufloat(2.00, 0.2009)])
    
    assert(str(de2unc(a, b, c).all()) == str(res.all()))
    