<style>
green{
    color:green;
    font-weight:bolder;
}
</style>

# `Ready -> Set -> Code!`
<p>My program snippets following multiple Python courses from Udemy and youtube, specifically Angela Yu's, Codestar's, ArjanCodes, Tech with Tim, Neural Nine, Indently and Neetcode. Additionally, It contains my practice problems from leetcode and web development related stuff to strengthen my journey of mastering python.</p>

## `Full Curriculum`

### `Commands`:

1. `Virtual environment`:\
    Windows:
    ```sh
    Create: python -m venv .venv
    Activate: .\.venv\Scripts\activate
    ```
    Mac:
    ```sh
    Create: python -m venv .venv
    Activate: source .venv/bin/activate
    ```

### `Topics`

#### `Knowledge Check`:
- `Core Python Concepts`:
    - if, loops, functions - <green>&check;</green>
    - tuple, list, set, dictionary
    - named tuple, default dictionary
    - OOP, classes
    - Dunder methods(__method__)
    - file handling
    - json files
    - error handling
    - memory management
- `Language Paragigm`
    - What type of language is Python?
- `Concurrency & Parallelism`
    - Threading
    - Multi Processing
    - Asyncronous Programming in Python
- `Niche Features`
    - Decorators
    - Generators
    - Context Managers
    - List Comprehensions
    - What makes Python specific and unique from other languages?
- `Libraries and Frameworks`
    - Django Framework
    - questions on specific libraries

#### `Hands-On Check`:
- `Leetcode`
- `Data Structures`:
    - Array
    - List
    - Stack
    - Queue
    - Heap(Min, Max)
    - Tree
    - Graph
    - DP
    - Trie

### `Libraries for Web Development`

#### 1. `Web Frameworks`
- **Django**: High-level framework for complex, database-driven web applications.
- **Flask**: Lightweight and flexible micro-framework for smaller projects.
- **FastAPI**: Modern and fast framework for building APIs with type hints.
- **Pyramid**: Flexible framework suitable for both small and large applications.

#### 2. `Database Interaction`
- **SQLAlchemy**: A powerful ORM for database operations.
- **Django ORM**: Simplifies database interaction within the Django framework.
- **Tortoise ORM**: Async ORM, ideal for pairing with FastAPI.

#### 3. `API Development`
- **Flask-RESTful**: Extension for Flask to build REST APIs.
- **Django REST Framework (DRF)**: Comprehensive toolkit for building APIs in Django.
- **Graphene**: Library for building GraphQL APIs.

#### 4. `Frontend Integration`
- **Jinja2**: Templating engine used with Flask.
- **Django Templates**: Built-in solution for rendering HTML in Django.

#### 5. `Web Scraping`
- **BeautifulSoup**: For parsing HTML and XML documents.
- **Scrapy**: Framework for building web scrapers.
- **Requests**: Library for making HTTP requests.

#### 6. `Testing`
- **Pytest**: Versatile framework for testing Python applications.
- **Selenium**: For browser automation and end-to-end testing.
- **Locust**: Load testing framework for web applications.

#### 7. `Asynchronous Programming`
- **Asyncio**: Standard library for asynchronous tasks.
- **Aiohttp**: Framework for building async web applications.

#### 8. `Security`
- **Authlib**: For implementing OAuth and OpenID Connect.
- **Django Security Middleware**: Built-in security features in Django.

#### 9. `Deployment`
- **Gunicorn**: WSGI HTTP server for Python web apps.
- **Uvicorn**: ASGI server, often used with FastAPI.

#### 10. `Other Useful Libraries`
- **Celery**: For managing background tasks.
- **Redis**: For caching and message brokering.
- **Pillow**: Library for image processing.

### `Most Used Inbuilt Modules in Python`

#### 1. `os`
- Helps interact with the operating system.
- Useful for file and directory management, environment variables, and process control.

#### 2. `sys`
- Provides access to system-specific parameters and functions.
- Commonly used for command-line arguments and system path manipulation.

#### 3. `math`
- Contains mathematical functions like trigonometry, logarithms, and constants (e.g., pi).
- Ideal for calculations requiring precision.

#### 4. `datetime`
- Enables date and time manipulation.
- Useful for formatting, parsing, and performing arithmetic with dates and times.

#### 5. `random`
- Used for generating random numbers, shuffling sequences, or picking random elements.

#### 6. `time`
- Provides functions related to time, such as pausing execution or measuring performance.

#### 7. `json`
- Handles JSON data.
- Used for parsing and serializing JSON objects, essential for web applications and APIs.

#### 8. `re`
- Enables regular expression operations.
- Ideal for pattern matching, searching, and modifying strings.

#### 9. `collections`
- Provides specialized data structures like `deque`, `namedtuple`, `Counter`, and `defaultdict`.

#### 10. `itertools`
- Offers tools for creating iterators, such as combinations, permutations, and infinite iterators.

#### 11. `functools`
- Contains higher-order functions like `reduce`, `partial`, and decorators like `lru_cache`.

#### 12. `logging`
- Facilitates logging in applications, helpful for debugging and tracking program execution.

#### 13. `shutil`
- Simplifies high-level file operations like copying, moving, and archiving files.

#### 14. `argparse`
- Provides tools for building command-line interfaces (CLIs).
- Great for parsing arguments and options.

#### 15. `csv`
- Handles CSV files.
- Ideal for reading and writing tabular data.

#### 16. `os.path`
- Contains utilities for manipulating and interacting with file paths.

#### 17. `hashlib`
- Helps create secure hashes and message digests, often used for cryptographic operations.

#### 18. `gzip`
- For working with `.gz` compressed files.

#### 19. `pickle`
- Enables serialization and deserialization of Python objects.

#### 20. `subprocess`
- Provides tools for running and interacting with subprocesses.
- Used for executing shell commands within Python programs.

#### 21. `typing`
- Introduces type hints for function arguments, return values, and variables.
- Improves code readability and helps with static type checking.
- Useful for handling complex data structures (e.g., `List`, `Dict`, `Union`, `Optional`, `Callable`).
    ```python
    from typing import List, Dict, Optional

    def greet_users(users: List[str], message: Optional[str] = None) -> Dict[str, str]:
        return {user: message or "Hello!" for user in users}
    ```