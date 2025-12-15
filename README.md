<h1>SauceDemo Automation Framework</h1>

<h3>Overview</h3>
This repository contains a <b>Selenium automation framework</b> for the <b>SauceDemo</b> web application built using <b>Python, Pytest, and Allure Reports</b>.
The framework follows the <b>Page Object Model (POM)</b> design pattern and demonstrates real‑world automation practices.
<br/>
Web Application: <u>https://www.saucedemo.com/</u>
<br/><br/>
<h3>Table of Contents</h3>
Tech Requirement
Project Structure
Pre-requisites
Verify
Install Dependencies
Project Description

<h4>Tech Requirement</h4>
&bull; <b>Programming Language:</b> Python
&bull; <b>Automation Tool:</b> Selenium WebDriver
&bull; <b>Test Framework:</b> Pytest
&bull; <b>Design Patten:</b> Page Object Model (POM)
&bull; <b>Reporting:</b> Allure Report
&bull; <b>Browser:</b> Firefox
&bull; <b>IDE:</b> PyCharm
<br/><br/>
<h4>Project Structure</h4>
```
Saucedemo/
│
├── pages/ 			# Page Object classes
│ ├── login_page.py
│ ├── products_page.py
│ └── cart_page.py
│
├── tests/ 			# Test cases
│ └── test_saucedemo.py
│
├── utils/ 			# Utility files (Excel reader)
│ ├── __init__.py
│ └── excel_reader.py
│
├── screenshots/ 		# Screenshots captured during execution
├── allure-results/ 		# Allure raw results
├── logs/ 			# Execution logs
│
├── conftest.py 		# Pytest fixtures & hooks
├── config.ini 			# Application & environment configuration
├── readme.ini 			# Framework reference configuration
├── README.md 			# Project documentation
└── requirements.txt 		# Project dependencies
```

<h4>Prerequisites</h4>
&bull; Python 3.10 or above
&bull; Firefox
&bull; Allure Comandline
&bull; Git

<h4>Verify</h4>
```
python --version
pip --version
allure --version
```
<h4>Install Dependencies</h4>
```
pip install -r requirements.txt

<h4>Project Description:</h4>
Scope of project Saucedemo is to validate Login - Valid and Invalid Credentials. Validating Cart items. Functionality of "Add to Cart", "Remove". Checking the items in cart and checkout process of items and final checkout information.

Sorting of items in different mode like "highest price to lowest price", "lowest price to highest", Alphabetical sort (Ascending or Descending).

Also, menu's are validated for "Reset App Stat", "Logout".



