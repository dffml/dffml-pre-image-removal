import os
import sys
import ast
from pathlib import Path

ORG = "dust"
NAME = "dffml-model-spacy"
DESCRIPTION = "DFFML model dffml-model-spacy"
AUTHOR_NAME = "0dust"
AUTHOR_EMAIL = "himanshutripathi366@gmail.com"

IMPORT_NAME = (
    NAME
    if "replace_package_name".upper() != NAME
    else "replace_import_package_name".upper()
).replace("-", "_")

SELF_PATH = Path(sys.argv[0]).parent.resolve()
if not (SELF_PATH / Path(IMPORT_NAME, "version.py")).is_file():
    SELF_PATH = os.path.dirname(os.path.realpath(__file__))

VERSION = ast.literal_eval(
    Path(SELF_PATH, IMPORT_NAME, "version.py")
    .read_text()
    .split("=")[-1]
    .strip()
)

README = Path(SELF_PATH, "README.md").read_text()

KWARGS = dict(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=README,
    long_description_content_type="text/markdown",
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    maintainer=AUTHOR_NAME,
    maintainer_email=AUTHOR_EMAIL,
    url="https://github.com/intel/dffml/blob/master/model/spacy/README.md",
    license="MIT",
    keywords=["dffml"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
)
