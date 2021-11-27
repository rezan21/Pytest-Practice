# Pytest-Practice

Practice *uncommon* Pytest use Cases & have these convenient scripts ready:
- Test Logging
- Test Print statements and stdout
- Test Error handling
- Test Error messages
- Test API calls (WIP)
- Test with ASYNC functions (WIP)
- Mocking, MagicMock & Patch (WIP)
- CI/CD and Automated Testing with Github Actions (WIP)


### Best Practices with Pytest:
- Make sure all packages include `__init__.py` file.
- It's good practice to group all test files in a tests directory at the root level.
- All test files should start with `test_`.
- all test functions should start with `test_`.
- Use Pytest with `-s` tag to see the print output of tests.

### Usage:
- Clone the repo: `git clone` and `cd` to the project.
- create a new environment: `virtualenv env`
- activate environment: `source env/bin/activate` (make sure your IDE interpreter is also the same as your environment)
- `pip install -r requirement.txt`
- `pytest tests/* -s` to run the tests
  