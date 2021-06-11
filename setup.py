import datetime
import re
import subprocess

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

import os

with open("geoacumen_city/__init__.py") as f:
    version = re.search(r'__version__ = "(.*?)"', f.read()).group(1)


def read(fname):
    try:
        with open(os.path.join(os.path.dirname(__file__), fname), "r") as fp:
            return fp.read().strip()
    except IOError:
        return ""

year_month = datetime.datetime.now().strftime("%Y-%m")
subprocess.call(["curl", "-O", f"https://download.db-ip.com/free/dbip-city-lite-{year_month}.mmdb.gz"])
subprocess.call(["gunzip", "-f", f"dbip-city-lite-{year_month}.mmdb.gz"])
subprocess.call(["mv", f"dbip-city-lite-{year_month}.mmdb", "geoacumen_city/db/dbip-city-lite-latest.mmdb"])


setup(
    name="python-geoacumen-city",
    version=version,
    author="Kevin Chung",
    author_email="kchung@nyu.edu",
    license="Apache 2.0",
    description="Library to access/distribute DB-IP IP to City Lite Database",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    classifiers=[],
    install_requires=["maxminddb==1.5.4"],
    packages=find_packages(include=["geoacumen_city", "geoacumen_city.*"]),
    include_package_data=True,
)
