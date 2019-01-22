from setuptools import setup, find_packages

setup(
    name="eyra_submission",
    description="EYRA submission template",
    version="0.0.1",
    packages=find_packages(include="eyra_submission"),
    entry_points={"console_scripts": ["eyra_submission = eyra_submission.__main__:main"]},
)
