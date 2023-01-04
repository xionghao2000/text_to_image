from setuptools import setup

setup(
    name="meta2d",
    packages=[
        "meta2d",
        "meta2d.common",
        "meta2d.services",
    ],
    install_requires=[
        "torch",
        "boto3",
        "python-dotenv",
        "flask",
    ],
    author="meta2d_model",
    description="meta2d_model",
    long_description=open("README.md").read(),
    version="1.0.0"
)
