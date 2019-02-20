from setuptools import setup, find_packages

setup(
    name="eyra_tools",
    description="EYRA tools",
    version="0.0.1",
    packages=find_packages(include="eyra_tools"),
    entry_points={
        "console_scripts":
            [
                "eyra_submission = eyra_tools.__main__:submission",
                "eyra_evaluation = eyra_tools.__main__:evaluation"
            ]
    },
)
