from setuptools import find_packages, setup


setup(
    name="semx",
    version="0.1.0",
    description="Semantic Stack Extractor CLI",
    python_requires=">=3.9",
    install_requires=[
        "typer>=0.12.0",
    ],
    packages=find_packages(include=["semx", "semx.*"]),
    package_data={
        "semx": ["prompts/*.md", "schemas/*.json"],
    },
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "semx=semx.cli:app",
        ],
    },
)
