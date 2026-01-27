# Copilot Instructions for DS3001-SP2

## Project Structure & Key Components
- **programming/**: Contains programming review, assignments, and class/package demos. Notebooks and Python modules are organized by topic.
  - `python_classes/packageName/moduleName.py`: Example matrix class for OOP concepts.
  - `assignment/assignment_programming.ipynb`: Assignment notebook, often with a corresponding solutions file.
- **wrangling/**: Focuses on data wrangling, cleaning, and analysis using Pandas and Numpy.
  - `assignment/HW2.py`: Script for data cleaning tasks, using explicit file paths for CSVs.
  - `assignment/assignment.ipynb`: Notebook with detailed instructions and markdown explanations for each question.
  - `lab/lab_notebook.ipynb`: Demonstrates web scraping and data collection from online sources.
- **Data files** are stored in `data/` subfolders within each topic directory. Paths are often absolute or relative to the assignment script.

## Developer Workflows
- **Notebooks** are the primary interface for assignments and demonstrations. Each question is typically answered in a markdown cell, with code and explanation.
- **Python scripts** (e.g., `HW2.py`) are used for batch data cleaning and analysis. Run directly with the Python interpreter.
- **No formal test or build system** is present. Outputs are validated by running scripts or cells and inspecting results.
- **Virtual environment**: `.venv/` is used for dependency isolation. Activate before installing packages or running scripts.
- **Data cleaning**: Use Pandas for CSVs, handle missing values explicitly, and document cleaning logic in markdown.

## Patterns & Conventions
- **Explicit file paths**: Data files are referenced with full or relative paths. Update paths if moving files or running on a different system.
- **Separation of code and explanation**: Markdown cells explain the reasoning and results for each code block.
- **Class/package demos**: Custom classes (e.g., `Mx` in `moduleName.py`) are used for teaching, not for production use. Prefer Numpy for real analysis.
- **No automated tests**: Validation is manual, via print statements or notebook output.

## Integration & Dependencies
- **Pandas, Numpy**: Core libraries for data wrangling and analysis. Install in `.venv` if missing.
- **Jupyter**: Notebooks are central; ensure Jupyter is installed in the environment.
- **Web scraping**: Use `requests` and `beautifulsoup4` for scraping tasks (see `lab_notebook.ipynb`).

## Examples
- See `wrangling/assignment/HW2.py` for data cleaning workflow.
- See `programming/python_classes/packageName/moduleName.py` for class structure and OOP patterns.
- See `wrangling/lab/lab_notebook.ipynb` for web scraping and parsing HTML.

## Tips for AI Agents
- Always check and update file paths for data files.
- Prefer Numpy/Pandas for data operations unless demonstrating OOP/class concepts.
- Document all data cleaning and transformation steps in markdown for reproducibility.
- No CI/CD or test automation; manual validation is expected.
