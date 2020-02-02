import logging,pytest
from Tensile.SolutionStructs import Convolution,ExactConv
log =logging.getLogger("testlog")

def test_stride2x3():
    z={} # problemType definition
    conv = Convolution(z, 'ConvolutionForward',
                          config={'TensorAFormat': 'NCHW',
                                  'Stride': '2x3',
                           })
    log.debug(conv.printUsage(z))
    e= { 'n':64, 'c':256, 'h':20, 'w':14, 'k':1024, 'x':1, 'y':1, 'u':3, 'v':2 }
    ec = ExactConv(e, conv)
    assert (ec.sizes == [4, 10, e['k'], e['n'], e['c']])
    assert (ec.stridesA == [3, 28, -1, -1])

def test_stride2x3_defaults():
    z={} # problemType definition
    conv = Convolution(z, 'ConvolutionForward',
                          config={'TensorAFormat': 'NCHW',
                                  'Stride': '2x3',
                           })
    log.debug(conv.printUsage(z))
    e= { 'n':64, 'c':256, 'h':20, 'w':14, 'k':1024}
    ec = ExactConv(e, conv)
    assert (ec.sizes == [4, 10, e['k'], e['n'], e['c']])
    assert (ec.stridesA == [3, 28, -1, -1])

def test_bad_filter():
    z={} # problemType definition
    conv = Convolution(z, 'ConvolutionForward',
                          config={'TensorAFormat': 'NCHW',
                           })
    log.debug(conv.printUsage(z))
    e= { 'n':64, 'c':256, 'h':20, 'w':14, 'k':1024, 'x':2, 'y':1, 'u':1, 'v':1 }
    with pytest.raises(RuntimeError, \
            match="Mismatch between ConvolutionConfig value \(1\) and specified value \(2\) for filter."):
        ec = ExactConv(e, conv)


def test_bad_stride():
    z={} # problemType definition
    conv = Convolution(z, 'ConvolutionForward',
                          config={'TensorAFormat': 'NCHW',
                                  'Stride': '2x3',
                           })
    log.debug(conv.printUsage(z))
    e= { 'n':64, 'c':256, 'h':20, 'w':14, 'k':1024, 'x':1, 'y':1, 'u':7, 'v':2 }
    with pytest.raises(RuntimeError, \
            match="Mismatch between ConvolutionConfig value \(3\) and specified value \(7\) for stride."):
        ec = ExactConv(e, conv)

def test_bad_missing_field():
    z={} # problemType definition
    conv = Convolution(z, 'ConvolutionForward',
                          config={'TensorAFormat': 'NCHW',
                                  'Stride': '2x3',
                           })
    log.debug(conv.printUsage(z))
    e= { 'c':256, 'h':20, 'w':14, 'k':1024, 'x':1, 'y':1, 'u':1, 'v':1 }
    with pytest.raises(Exception, match="required ExactConv field 'n' not present in ExactConv"):
        ec = ExactConv(e, conv)

def test_bad_invalid_field():
    z={} # problemType definition
    conv = Convolution(z, 'ConvolutionForward',
                          config={'TensorAFormat': 'NCHW',
                                  'Stride': '2x3',
                           })
    log.debug(conv.printUsage(z))
    e= { 'A': 123, 'n':64, 'c':256, 'h':20, 'w':14, 'k':1024, 'x':1, 'y':1, 'u':1, 'v':1 }
    with pytest.raises(Exception, match="unknown ExactConv field 'A'"):
        ec = ExactConv(e, conv)

def test_bad_invalid_list():
    z={} # problemType definition
    conv = Convolution(z, 'ConvolutionForward',
                          config={'TensorAFormat': 'NCHW',
                                  'Stride': '2x3',
                           })
    log.debug(conv.printUsage(z))
    e= [1,2,3,4]
    ec = ExactConv(e, conv)

