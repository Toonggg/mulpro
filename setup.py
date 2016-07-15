#!/usr/bin/env python

from warnings import warn

try:
    import multiprocessing
    multiprocessing_av = True
except ImportError:
    multiprocessing_av = False
        
if multiprocessing_av:
        
    from setuptools import setup

    setup(name='h5writer',
          version='0.1.0',
          description='Running a worker function in parallel with serial result logging. This package builds on the multiprocessing package and uses the pipe object for IPC.',
          author='Max F. Hantke',
          author_email='maxhantke@gmail.com',
          url='https://github.com/mhantke/mulpro',
          #install_requires=['numpy', 'h5py', 'mpi4py>=2.0.0'],
          packages = ['mulpro'],
          #package_dir={'h5writer':'src'},
    )   
    
else:
    
    print 100*"*"

    print "\tThe multiprocessing package cannot be imported! Please install multiprocessing."

    print 100*"*"

