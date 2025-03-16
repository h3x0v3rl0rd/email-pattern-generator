# Email Pattern Generator

![Python](https://img.shields.io/badge/Python-3.x-blue)
![License](https://img.shields.io/badge/License-MIT-green)

A Python script to generate email patterns from a given first name, last name, and domain. The script supports generating over 100 email patterns and allows saving the results in `.txt`, `.json`, or `.xml` format.

---

## Features

- Generates **100+ email patterns** based on the provided inputs.
- Supports common email formats:
  - `firstname.lastname@domain.com`
  - `firstname_lastname@domain.com`
  - `firstname-lastname@domain.com`
  - `firstname@domain.com`
  - `lastname@domain.com`
  - And many more!
- Saves the generated patterns to:
  - `.txt` (plain text)
  - `.json` (structured JSON)
  - `.xml` (structured XML)

---

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/n3rdh4x0r/email-pattern-generator.git
   ```




```
┌──(kali㉿kali)-[~]
└─$ python3 email_generator.py

============================================================
                  Email Pattern Generator                   
                  Developed by (n3rdh4x0r)                  
============================================================
Enter the following details:
First Name: firstname
Last Name: lastname
Domain Name (e.g., example.com): example.com

Choose a file format to save the email patterns:
1. Save as .txt
2. Save as .json
3. Save as .xml
Choose an option (1/2/3): 1
Email patterns saved to email_patterns.txt
```

