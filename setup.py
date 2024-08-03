from setuptools import setup, find_packages

with open("README.md", 'r', encoding='utf-8') as f:
    long_description = f.read()

__version__ = "0.0.0"
REPO_NAME = "IPYNB_RENDERER"
AUTHOR_USER_NAME = 'Atiqur Rahman'
GITHUB_USER_NAME = "Atiqur78"
AUTHOR_EMAIL = "atikurrahman209@gmail.com"
SRC_REPO = "IPYNB_RENDERER"

setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description='A small python package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{GITHUB_USER_NAME}/{SRC_REPO}",
    project_urls={
        "Bug Tracker": f"https://github.com/{GITHUB_USER_NAME}/{SRC_REPO}/issues"
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        "ipywidgets",
        "notebook",
        "ensure",
        "py-youtube"
    ],
    extras_require={
        "dev": [
            "pytest",
            "tox",
            "black",
            "flake8",
            "mypy"
        ]
    },
)
