# Code Base Summary CLI

[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A lightweight Python CLI tool to recursively scan a directory, read every file (with robust error handling), and produce a single Markdown-formatted summary file. Ideal for quick code overviews, documentation snapshots, or audits.

## Table of Contents

- [Features](#features)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Contributing](#contributing)  
- [License](#license)  

## Features

- Recursively traverses directories (skips `.git`, `__pycache__`, etc.)  
- Normalizes and logs relative file paths  
- Reads files using UTF-8 (ignores binary/non-standard errors)  
- Wraps content in Markdown code blocks  
- Shows progress and handles I/O exceptions  
- Customizable output filename  

## Installation

```bash
git clone [https://github.com/Eng-M-Abdrabbou/Python-Recursive-Directory-CodeSummary-Tool.git](https://github.com/Eng-M-Abdrabbou/Python-Recursive-Directory-CodeSummary-Tool.git)
cd CodeBaseSummary-CLI-Python-Script
# No external dependencies; uses Python stdlib
````

## Usage
in the terminal run this command:
python CS.py <root_dir> [output_filename]

##Examples

** generate code_summary.txt in current folder **
python CS.py ./my_project

** custom output name **
python CS.py ~/workspace/my_project docs/project_code.md

## Contributing
Fork the repo
Create a feature branch (git checkout -b feature/xyz)
Commit your changes (git commit -m \"Add xyz\")
Push to your branch (git push origin feature/xyz)
Open a Pull Request
Please follow the existing code style and add tests where applicable.

## License
This project is licensed under the MIT License. See the LICENSE file for details."

