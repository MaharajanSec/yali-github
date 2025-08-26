# Subtrace

A simple subdomain enumeration tool inspired by [OWASP Amass](https://github.com/owasp-amass/amass).  
Unlike Amass, this is a **lightweight Python script** meant for learning and quick reconnaissance.

---

## Features
- Queries **crt.sh** (Certificate Transparency logs) for subdomains
- Optionally checks which subdomains are alive
- Saves output in console (can be extended to files)

---

## Why Subtrace?
[Amass](https://github.com/owasp-amass/amass) is a powerful open-source tool with advanced features (multiple data sources, graph databases, integrations).  
**Subtrace** is a **simplified educational script** to practice:
- Working with HTTP requests
- Parsing JSON responses
- Automating reconnaissance in Python

---

## Usage
```bash
python subtrace.py
