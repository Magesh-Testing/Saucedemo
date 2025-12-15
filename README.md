<h1>SauceDemo Automation Framework</h1>

<h3>Overview</h3>
This repository contains a <b>Selenium automation framework</b> for the <b>SauceDemo</b> web application built using <b>Python, Pytest, and Allure Reports</b>.
The framework follows the <b>Page Object Model (POM)</b> design pattern and demonstrates real‑world automation practices.
<br/>
Web Application: <u>https://www.saucedemo.com/</u>
<br/><br/>
<h3>Table of Contents</h3>
Tech Requirement<br/>
Project Structure<br/>
Pre-requisites<br/>
Verify<br/>
Install Dependencies<br/>
Project Description

<h4>Tech Requirement</h4>
&bull; <b>Programming Language:</b> Python<br/>
&bull; <b>Automation Tool:</b> Selenium WebDriver<br/>
&bull; <b>Test Framework:</b> Pytest<br/>
&bull; <b>Design Patten:</b> Page Object Model (POM)<br/>
&bull; <b>Reporting:</b> Allure Report<br/>
&bull; <b>Browser:</b> Firefox<br/>
&bull; <b>IDE:</b> PyCharm<br/>
<br/>
<h4>Project Structure</h4>

Saucedemo/<br/>
│<br/>
├── pages/ 			              # Page Object classes<br/>
│ ├── login_page.py<br/>
│ ├── products_page.py<br/>
│ └── cart_page.py<br/>
│<br/>
├── tests/ 			              # Test cases<br/>
│ └── test_saucedemo.py<br/>
│<br/>
├── utils/ 			              # Utility files (Excel reader)<br/>
│ ├── __init__.py<br/>
│ └── excel_reader.py<br/>
│<br/>
├── screenshots/ 		          # Screenshots captured during execution<br/>
├── allure-results/ 		      # Allure raw results<br/>
├── logs/ 			              # Execution logs<br/>
│<br/>
├── conftest.py 		          # Pytest fixtures & hooks<br/>
├── config.ini 			          # Application & environment configuration<br/>
├── readme.ini 			          # Framework reference configuration<br/>
├── README.md 			          # Project documentation<br/>
└── requirements.txt 		      # Project dependencies<br/>


<h4>Prerequisites</h4>
&bull; Python 3.10 or above<br/>
&bull; Firefox<br/>  
&bull; Allure Comandline<br/>
&bull; Git<br/>

<h4>Verify</h4>
```
python --version<br/>
pip --version<br/>
allure --version
```
<h4>Install Dependencies</h4>
pip install -r requirements.txt

<h4>Project Description:</h4>
Scope of project Saucedemo is to validate Login - Valid and Invalid Credentials. Validating Cart items. Functionality of "Add to Cart", "Remove". Checking the items in cart and checkout process of items and final checkout information.<br/><br/>

Sorting of items in different mode like "highest price to lowest price", "lowest price to highest", Alphabetical sort (Ascending or Descending).<br/><br/>

Also, menu's are validated for "Reset App Stat", "Logout".
