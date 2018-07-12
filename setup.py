from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

if __name__ == "__main__":
    setup(
        name="gcptracelogging",
        version="0.1.0",
        author="Datalab",
        author_email="datalab@bbc.co.uk",
        description="Adds distributed tracing information to logger output and sends traces to the Stackdriver "
                    "Trace API.",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/bbc/python-gcp-trace-logging",
        packages=find_packages(),
        classifiers=(
            "Programming Language :: Python :: 3.6",
            "Operating System :: OS Independent",
        ),
        install_requires=[
            'python-json-logger==0.1.9',
            'B3-Propagation==0.1.5',
            'google-cloud-trace==0.19.0'
        ]
    )
