"""
Checker plugins which executes various checks
"""
from __future__ import absolute_import
# make sure all modules will be loaded
from os.path import dirname, basename, isfile
import glob
modules = glob.glob(dirname(__file__)+"/*.py")
__all__ = [basename(f)[:-3] for f in modules if isfile(f)]
