from setuptools import setup

setup(name="systeminfo",
      version="0.1",
      description="Basic system info for comp30670",
      url="",
      author="Sophie Heseltine",
      author_email="sophie.heseltine@ucdconnect.ie",
      licence="GPL3",
      packages=['systeminfo'],
      entry_points={'console_scripts':['comp30670_syteminfo=systeminfo.main:main']}
      )
