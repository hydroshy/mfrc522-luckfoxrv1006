import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mfrc522",
    version="0.0.1",
    author="hydroshy",
    author_email="phanloi1403@gmail.com",
    description="A library to integrate the MFRC522 RFID readers with the LuckFox Pico Pro/Max",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hydroshy/mfrc522-luckfoxrv1006",
    packages=setuptools.find_packages(),
    install_requires=[
        'python-periphery'
        ],
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        "Operating System :: POSIX :: Linux",
        'Topic :: System :: Hardware',
    ],
)
