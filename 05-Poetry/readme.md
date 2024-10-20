# **Let's Learn About Poetry:**

## **What is Poetry:**

**Poetry** is a **dependency management** and **packaging tool** for Python projects. It helps developers manage their project dependencies, handle virtual environments, and publish Python packages in a simple and organized way.

### Key Features of Poetry:

1. **Dependency Management**:

   - Poetry allows you to easily define, add, and manage dependencies for your project in a file called `pyproject.toml`.
   - It takes care of version conflicts, ensuring you have the right versions of libraries without breaking your project.

2. **Virtual Environment Management**:

   - Poetry automatically creates and manages a virtual environment for your project, isolating your dependencies from the global environment.

3. **Package Building and Publishing**:

   - If you’re building a library or a Python package, Poetry helps you build and publish your package to **PyPI** (Python Package Index) or any other package repository.

4. **Lock File for Consistency**:
   - Poetry generates a `poetry.lock` file, which ensures that everyone working on the project uses the exact same versions of dependencies, improving consistency across different environments.

### Why Use Poetry?

- **Simplifies Dependency Management**: It makes adding and managing dependencies easier, handling version conflicts automatically.
- **Project Isolation**: It ensures that your project dependencies are isolated, avoiding issues between projects.
- **Easy Package Publishing**: It provides built-in commands to package your Python project and publish it online.
- **Better Control**: With the `pyproject.toml` and `poetry.lock` files, you have better control over your project's dependencies and environment.

### Example of a `pyproject.toml` File (Poetry's Configuration File):

```toml
[tool.poetry]
name = "my_project"
version = "0.1.0"
description = "A simple example project"
authors = ["Your Name <your.email@example.com>"]

[tool.poetry.dependencies]
python = "^3.9"
requests = "^2.25.1"

[tool.poetry.dev-dependencies]
pytest = "^6.2"

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"
```

This file defines the project details, dependencies, and versions, which Poetry will use to manage your project.

In short, **Poetry** is a powerful tool for handling Python project dependencies, virtual environments, and package management, making it much easier to maintain Python projects efficiently.

## **General Poetry Project Structure for Any End-to-End Project:**

```graphql
project_name/
│
├── project_name/               # Main source code directory
│   ├── __init__.py             # Makes it a package
│   ├── config/                 # Configuration files (environment variables, settings)
│   │   └── settings.py         # Application settings and configuration logic
│   │
│   ├── core/                   # Core business logic (main functionality)
│   │   ├── __init__.py
│   │   └── main_logic.py       # Main business logic of the project
│   │   └── helpers.py          # Helper functions that support main logic
│   │
│   ├── models/                 # For models (database or machine learning)
│   │   ├── __init__.py
│   │   ├── database.py         # If using a database, define models here
│   │   └── ml_model.py         # If it's an ML project, define ML model here
│   │
│   ├── data/                   # Data folder (if applicable)
│   │   ├── raw/                # Raw data or dataset
│   │   └── processed/          # Cleaned and processed data
│   │
│   ├── api/                    # API routes if serving your app over HTTP
│   │   ├── __init__.py
│   │   ├── routes.py           # API route definitions (e.g., FastAPI/Flask)
│   │   └── schemas.py          # Request and response schemas (validation)
│   │
│   ├── services/               # External services (e.g., external APIs, integrations)
│   │   ├── __init__.py
│   │   └── third_party_service.py  # Integration with 3rd party services
│   │
│   ├── tests/                  # Unit and integration tests
│   │   ├── __init__.py
│   │   └── test_main_logic.py   # Tests for core logic
│   │   └── test_api.py          # Tests for API routes (if applicable)
│   │
│   ├── scripts/                # For one-time scripts, utilities, etc.
│   │   └── data_cleaning.py    # Example script for cleaning data
│   │
│   └── main.py                 # Entry point of the application (if it's a CLI or app)
│
├── pyproject.toml              # Poetry or project dependency management file
├── requirements.txt            # (If using pip) Dependency management file
├── Dockerfile                  # Dockerfile for containerizing the project (if needed)
├── .env                        # Environment variables file
├── README.md                   # Project documentation
├── .gitignore                  # Git ignore file (for files you don't want to commit)
└── LICENSE                     # License file for open-source projects (optional)

```

## **Benefits of This Structure:**

- **Scalability:** Easy to add new features or modules without mixing code.
- **Maintainability:** Clear separation of concerns makes it easier to manage and debug.
- **Testing:** Isolating tests makes it easy to ensure each part of the project works correctly.
- **Flexibility:** You can switch out or upgrade individual parts (like the core logic, API, or database) without affecting the rest of the project.

## **Local & Global Packages:**

In Python, the terms **local package** and **global package** refer to where and how packages are installed and accessed. Let's break down what each term means:

### 1. **Local Package**:

A **local package** is a Python package that is installed or used only within the context of a specific project or virtual environment. It's isolated from the global Python environment, meaning it won’t interfere with packages installed globally or in other projects.

#### Key Features of Local Packages:

- **Project-specific**: These packages are only available for the project they are installed in.
- **Isolated environment**: Usually, local packages are installed inside a **virtual environment** (e.g., using `venv`, `virtualenv`, or **Poetry**). This ensures that each project can have its own versions of packages without affecting other projects.
- **Controlled dependencies**: Local packages allow you to maintain **dependency management** for each project. Different projects can have different versions of the same package without conflicts.

#### Example:

If you're working on a project and use a virtual environment (or Poetry), the packages are local to that project.

```bash
# Creating a virtual environment
python -m venv venv

# Activating the virtual environment (Windows)
venv\Scripts\activate

# Now, any package you install with pip will be local to this environment
pip install requests
```

After activating the virtual environment, `requests` is a local package, available only within this specific environment.

### 2. **Global Package**:

A **global package** is a Python package that is installed system-wide, meaning it’s available to any Python project running on your machine. These packages are installed in the **global Python environment** and are not tied to a specific project or virtual environment.

#### Key Features of Global Packages:

- **System-wide availability**: Global packages are available to all Python projects on your machine, as long as they are using the global Python environment.
- **Shared installation**: If you install a package globally, all projects have access to the same package, and the same version of it, which can sometimes cause **version conflicts** between different projects.
- **No isolation**: Global packages can lead to issues where different projects require different versions of the same package. Because there's no isolation, updating a package globally might break some projects.

#### Example:

When you install a package globally (without a virtual environment), it’s installed system-wide and available to all projects.

```bash
# Installing a global package
pip install requests
```

In this case, `requests` is installed in the global Python environment and can be used by any project on your machine, as long as they are not using their own virtual environments.

### Key Differences Between Local and Global Packages:

| Aspect                  | Local Package                                                     | Global Package                                                                         |
| ----------------------- | ----------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| **Scope**               | Available only to a specific project/virtual environment          | Available to all Python projects on the machine                                        |
| **Installation**        | Installed in a virtual environment (or isolated tool like Poetry) | Installed globally without isolation                                                   |
| **Conflict Prevention** | Prevents dependency conflicts between projects                    | Can cause version conflicts between projects                                           |
| **Usage**               | Project-specific and environment-specific                         | Available across the whole system                                                      |
| **Typical Use Case**    | Used for individual projects to manage dependencies locally       | Used for packages/tools that should be available system-wide (e.g., development tools) |

### Best Practice:

For most projects, it’s better to install packages **locally** using a virtual environment or a tool like **Poetry**. This ensures that each project has its own isolated environment, avoiding dependency conflicts between projects. **Global installations** are more suited for system-wide tools or packages you need for development, like `black` or `pylint`.

### When to Use Local Packages:

- When you have multiple projects that may need **different versions** of the same package.
- When you want to keep your project’s environment **isolated** to avoid accidental changes to dependencies.
- When you are deploying a project and need it to run in a consistent environment across machines (e.g., using Docker or virtual environments).

### When to Use Global Packages:

- For tools that you use across multiple projects or for system-wide tasks (e.g., **linters**, **code formatters**, or **development tools**).
- If you are building simple scripts that don’t require a specific isolated environment.

By using local packages, you keep each project’s dependencies isolated and safe from conflicts, while global packages can be useful for system-wide tools or utilities.

## **Why Make Directory as a Package:**

We make a directory a **package** in Python to **organize** code into smaller parts, making it easier to manage and reuse. It allows us to:

- **Group related code** together (e.g., all database functions in one package).
- **Avoid naming conflicts** by separating different parts of the project.
- **Easily import** code across different files or projects.

In short, it helps keep the project **clean, modular, and reusable**.
