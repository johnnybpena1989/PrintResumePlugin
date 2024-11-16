from setuptools import setup

setup(
    name="PrintResumePlugin",
    version="0.1.0",
    description="A plugin to pause and resume 3D prints for OctoPrint",
    author="JohnnyBPena",
    author_email="johnny@grindinglunacy.com",
    url="https://github.com/johnnybpena1989/print_resume_plugin",
    license="MIT",
    packages=["print_resume_plugin"],
    install_requires=["OctoPrint"],
    entry_points={
        "octoprint.plugin": [
            "printresumeplugin = print_resume_plugin"
        ]
    }
)
