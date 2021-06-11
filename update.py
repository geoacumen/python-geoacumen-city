import datetime
import fileinput

now = datetime.datetime.now()
year = now.strftime("%Y")
month = now.strftime("%m")
day = now.strftime("%d")
new_version = f"""__version__ = \"{year}.{month}.{day}\""""

for line in fileinput.FileInput("geoacumen_city/__init__.py", inplace=True):
    if line.startswith("__version__"):
        print(new_version)
    else:
        print(line.strip())
