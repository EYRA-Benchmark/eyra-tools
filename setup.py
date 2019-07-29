from setuptools import setup, find_packages

setup(
    name="eyra_tools",
    description="EYRA tools",
    version="0.0.1",
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        "console_scripts":
            [
                "eyra-generate = eyra_tools.generate:generate"
            ]
    },
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
