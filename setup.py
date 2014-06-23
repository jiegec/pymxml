try:
    import setuptools
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    
from setuptools import setup, Extension
import glob

files = glob.glob('mxml/*.c')
files.append('pymxml.i')



setup(name="pymxml",
      description="Python wrapper for mini-xml(http://www.msweet.org/projects.php?Z3)",
      version="2.8",
      author="Wiadufa Chen",
      author_email="wiadufachen@gmail.com",
      url="https://github.com/wiadufachen/pymxml",
      py_modules=['pymxml'],
      ext_modules=[
                    Extension("_pymxml", sources=files)
                    ],
      classifiers=["Programming Language :: Python",
             "Programming Language :: Python :: 3",
             "License :: OSI Approved :: Apache Software License",
             "Development Status :: 4 - Beta",
             "Operating System :: OS Independent",
             ]
)