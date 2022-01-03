from setuptools import setup

setup(
    long_description="A demonstrational package to https://delb.readthedocs.io/en/latest/extending.html",
    name="delb-reference-plugins",
    version="0.2",
    description="A package with spare non-sense plugins for delb as developer's reference.",
    python_requires=">=3.6.0",
    author="Frank Sachsenheim",
    author_email="funkyfuture@riseup.net",
    license="AGPL-3.0",
    entry_points={
        "delb": [
            "custom-loader = delb_reference_plugins.custom_loader",
            "tei-header-properties = delb_reference_plugins.tei_header_properties",
        ]
    },
    packages=["delb_reference_plugins"],
    install_requires=["delb[https-loader]==0.3b5"],
)
