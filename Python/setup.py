

def configuration(parent_package='',top_path=None):
    base = '../../'
    from numpy.distutils.misc_util import Configuration
    config = Configuration('',parent_package,top_path)
    config.add_extension('ajplanet',sources=[base+'ajplanet/Python/ajplanet.pyf', base+'ajplanet/convlib.c',base+'ajplanet/true_anomaly.c',base+'ajplanet/rv.c',base+'ajplanet/orbit.c',base+'ajplanet/occultquad.f',base+'ajplanet/occultnl.f'],include_dirs=[base+'ajplanet/', '/usr/local/include'],library_dirs=['/usr/local/lib'], libraries=['gsl','gslcblas','m'])
    return config

if __name__ == "__main__":
    from numpy.distutils.core import setup
    setup(**configuration(top_path='').todict())

