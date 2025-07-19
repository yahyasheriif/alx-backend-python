## ✅ Final `README.md`

# 0x03. Unittests and Integration Tests

This project is part of the **ALX Backend Specialization**. It focuses on writing proper **unit tests** and **integration tests** for Python code using the `unittest` framework and mocking tools.

---

## 📘 Learning Objectives

By the end of this project, you should be able to explain the following without external help:

- The difference between unit and integration tests
- How to write unit tests for a Python function or class
- How to use `unittest.mock` to patch functions and classes
- How to parameterize tests using `parameterized`
- How to test memoized methods and properties
- How to write integration tests using fixtures
- How to mock HTTP requests with side effects

---

## 🛠️ Technologies

- Python 3.7+
- `unittest`
- `unittest.mock`
- `parameterized`
- `pycodestyle` (PEP8) style guide
- Ubuntu 18.04 (via checker)

---

## 🧪 Project Structure

```

0x03-unittests\_and\_integration\_tests/
│
├── client.py               # GithubOrgClient class (main client logic)
├── utils.py                # Utility functions (memoization, JSON fetch)
├── fixtures.py             # Test data fixtures for integration tests
├── test\_client.py          # Unit and integration tests for client.py
├── test\_utils.py           # Unit tests for utils.py
└── README.md               # Project documentation

````

---

## ✅ Tasks Covered

### Unit Testing (`test_utils.py`)
- `access_nested_map()` with standard and exception cases
- `get_json()` using mock for `requests.get`
- `memoize()` using mock for method caching

### Unit Testing (`test_client.py`)
- `.org` method using `@patch` and `@parameterized`
- `_public_repos_url` property using `PropertyMock`
- `.public_repos()` with and without `license` filtering
- `has_license()` static method with param tests

### Integration Testing (`test_client.py`)
- `.public_repos()` end-to-end test using `requests.get` mock
- Setup using `@parameterized_class` and test fixtures
- Side effects for dynamic API responses

---

## 📦 Usage

To run all tests:

```bash
PYTHONPATH=. python3 -m unittest test_utils.py
PYTHONPATH=. python3 -m unittest test_client.py
````

To check code style:

```bash
pycodestyle test_utils.py test_client.py client.py utils.py
```
