<div align="center">

![BibTeX Sanity banner](https://capsule-render.vercel.app/api?type=waving&color=0:#7c2d12,100:#0f766e&height=170&section=header&text=BibTeX%20Sanity&fontSize=34&fontColor=ffffff)

<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=18&pause=1000&color=0f766e&center=true&vCenter=true&width=720&lines=Find%20bibliography%20issues%20before%20compiling%3BFast%20local%20BibTeX%20checks" alt="Typing SVG" />

[![MIT](https://img.shields.io/badge/license-MIT-0f766e.svg)](LICENSE)
[![Python](https://img.shields.io/badge/language-Python-blue.svg)](https://www.python.org/)
[![Stars](https://img.shields.io/github/stars/CyberLoop-dev/bibtex-sanity?style=flat)](https://github.com/CyberLoop-dev/bibtex-sanity/stargazers)
[![Last commit](https://img.shields.io/github/last-commit/CyberLoop-dev/bibtex-sanity)](https://github.com/CyberLoop-dev/bibtex-sanity/commits/main)

**A practical, dependency-free validator for BibTeX libraries.**

<img src="assets/illustration.svg" alt="BibTeX Sanity illustration" width="560" />

</div>

## 🧭 Overview

BibTeX Sanity checks local .bib files for duplicate citation keys, missing required fields by entry type, empty values, and malformed entry boundaries. It reports line numbers and can emit JSON for scripts.

## ✨ Features

- 🔎 Detects duplicate citation keys.
- 📚 Checks common required fields for article, book, and inproceedings entries.
- ⚠️ Reports empty fields and malformed entry boundaries.
- 🤖 Offers JSON output for editor or CI integration.
- 🐍 Uses the Python standard library only.

## 🖥️ Demo

```bash
python main.py references.bib
python main.py references.bib --json
```
The report lists each issue with its entry key and source line.

## 🚀 Quick Start

```bash
git clone https://github.com/CyberLoop-dev/bibtex-sanity.git
cd bibtex-sanity
python main.py examples/library.bib
```

## 🧱 Tech Stack

- 🐍 Python 3.10+
- 📦 Standard library: argparse, json, re, pathlib

## 🗂️ Folder Structure

```text
bibtex-sanity/
├── main.py
├── examples/library.bib
├── tests/test_main.py
├── pyproject.toml
├── assets/illustration.svg
├── .gitignore
└── README.md
```

## 🛣️ Roadmap

- - [x] Common BibTeX entry types and required fields
- - [x] Duplicate-key and empty-field checks
- - [ ] Optional strict field-name mode

## 🤝 Contributing

Issues and pull requests are welcome. Please include a clear reproduction or sample input and keep changes focused.

## 📄 License

Released under the [MIT License](LICENSE).

<div align="center">

![Footer](https://capsule-render.vercel.app/api?type=waving&color=0:#0f766e,100:#7c2d12&height=100&section=footer)

</div>
