[![Supported Nuke](https://img.shields.io/badge/supported_nuke-13+-yellow)](https://www.foundry.com/products/nuke-family/nuke)
[![Python Versions](https://img.shields.io/badge/python-3.7%20%7C%203.9%20%7C%203.10-blue.svg)](https://www.python.org/downloads/)
# NukeTesting
This project is focused on testing nuke nodes with python.
It can be used to enhance your plugin and gizmo development.
The main goal is to make pipelines and tools more stable.

The biggest benefit of tests is that you reduce the risk of regressions.
That's amazing if you constantly try to improve your tools. 
Tests allow you to be notified when you re-introduce known issues or unexpected behaviour.

## How to use
**This is still a big todo.** 
Its planned to do releases on pypi.
Ideally you can pip install this project as a package.
Until then, consider reading through the code.
The main starting point is our test runner.
This is used to run tests with nuke.

Once you have the testrunner configured, you can start writing your tests.
This project is not teaching the concepts of testing.
Search the web for best practises on that topic.

This project provides classes and methods that help you test common nuke operations.
Planned utilities are:
- image 2 image checks
- boundingbox checks
- metadata comparisons
- node tree comparisons

## Contribute to this project
Contributions are very welcome.
Try to follow the pep guide and consider using ruff for linting.
If possible try to document your classes and function on how to use them. 
Only use inline comments for very obscure and difficult to understand concepts.

### Contribute quickstart
It is easiest to use rye to setup this project. However it is not required, as you can also setup all packages using the .lock files.
However, if you are using rye, set the python version to py3.10:
```bash
rye pin 3.10
```

Once done, sync the dependancies:
```bash
rye sync
```

From now on, you can test the nuke-testrunner in the terminal with:

```bash
rye run nuke-testrunner --help
```

Disclaimer:
This package is developed in the spare time, so replies might not come as quickly as you might wish.
