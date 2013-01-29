from distutils.core import setup
import py2exe

setup(windows=["Binary_Conversion.py",{"script":"Binary_Conversion.py","icon_resources":[(1,"bitmap//binary.ico")]}],\
      data_files=[("bitmap",["bitmap\\binary.ico"])])
