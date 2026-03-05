# python-task-automation

Python notebooks and scripts to automate repetitive tasks (bots/RPA), built as a growing collection of practical automations.

## About
This repository is a hands-on space for building **small, reusable automations** with Python. The goal is to automate repetitive workflows and keep each automation organized in its own folder, so new projects can be added over time without clutter.

Part of the immersion hub:  
https://github.com/YOUR_USERNAME/python-immersion-hashtag-2026

---

## Automations included

### 1) Product registration bot (UI automation with PyAutoGUI + CSV)
This automation simulates a real-world scenario: registering many products in a system automatically by controlling the **mouse and keyboard**, as if a person was doing it.

**What it does**
- Opens the browser and navigates to the system
- Logs in (user + password)
- Reads a CSV file with product data
- Fills the form fields for each row (code, brand, type, price, cost, optional notes)
- Submits each record and repeats until the CSV ends

Reference (Jornada Python — Class 1: Task Automation & Bots):  
https://www.youtube.com/watch?v=ts986Np0kNw

---

## Tech stack
- Python
- Jupyter Notebook
- `pandas` (CSV input)
- `pyautogui` (mouse/keyboard automation)
