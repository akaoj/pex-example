import setuptools

install_requires = [
    "flask",
    "Jinja2",
]

setuptools.setup(
    name="api",
    version="1.0",
    description="Simple API",

    packages=setuptools.find_packages(),
    include_package_data=True,

    install_requires=install_requires,

    entry_points={
        "console_scripts": [
            "api = api.__main__:main",
        ],
    },
)
