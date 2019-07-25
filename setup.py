from setuptools import setup, find_packages

setup(
    name="eyra_tools",
    description="EYRA tools",
    version="0.0.1",
    packages=find_packages(include="eyra_tools"),
    entry_points={
        "console_scripts":
            [
                "eyra-generate = eyra_tools.generate:generate"
            ]
    },
)
