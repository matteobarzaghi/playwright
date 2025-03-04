# 🎭 **Playwright + Python: Web Testing Automation Framework**

## 📖 **Overview**

This project is a web testing automation framework utilizing [Playwright](https://playwright.dev/python/docs/intro) and Python. It enables reliable end-to-end testing for modern web applications, supporting multiple browsers such as Chromium, Firefox, and WebKit.

---

## 🚀 **Getting Started**

### **Prerequisites**

- **Python**: Ensure you have Python 3.7 or higher installed. You can download it from the [official Python website](https://www.python.org/downloads/).

- **pip**: Python's package installer should be available. It's typically included with Python installations.

### **Installation Steps**

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/matteobarzaghi/playwright.git
   cd playwright
   ```

2. **Install Dependencies**:

   It's recommended to use a virtual environment to manage dependencies:

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

   Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. **Install Playwright Browsers**:

   After installing the Playwright package, you need to install the browser binaries:

   ```bash
   playwright install
   ```

   This command downloads the necessary browser binaries for Chromium, Firefox, and WebKit.

---

## 🛠️ **Usage**

The framework provides both synchronous and asynchronous examples for interacting with web pages.

### **Synchronous Example**

```python
from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://example.com')
    print(page.title())
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
```

### **Asynchronous Example**

```python
import asyncio
from playwright.async_api import async_playwright

async def run(playwright):
    browser = await playwright.chromium.launch(headless=False)
    page = await browser.new_page()
    await page.goto('https://example.com')
    print(await page.title())
    await browser.close()

asyncio.run(async_playwright().start(run))
```

These scripts demonstrate how to launch a browser, navigate to a webpage, and print the page title using Playwright's synchronous and asynchronous APIs.

---

## 🧪 **Running Tests**

To execute tests using this framework:

1. **Navigate to the Project Directory**:

   ```bash
   cd playwright
   ```

2. **Run Tests**:

   Use `pytest` to discover and run tests:

   ```bash
   pytest
   ```

   Ensure that your test files are prefixed with `test_` to be automatically recognized by `pytest`.

---

## 📂 **Project Structure**

```
playwright/
├── inputs/
│   └── example_input.txt
├── pytest/
│   ├── test_example.py
│   └── conftest.py
├── .gitattributes
├── README.md
├── async.py
├── demo.png
├── requirements.txt
└── sync.py
```

- **`inputs/`**: Contains input files used during tests.
- **`pytest/`**: Directory for test cases and configurations.
- **`async.py`**: Example script demonstrating asynchronous Playwright usage.
- **`sync.py`**: Example script demonstrating synchronous Playwright usage.
- **`demo.png`**: Image file showcasing a demo or screenshot.
- **`requirements.txt`**: Lists Python dependencies for the project.

---

## 📄 **License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🤝 **Contributing**

Contributions are welcome! Please fork this repository and submit a pull request for any enhancements or bug fixes.

---

## 📧 **Contact**

For any inquiries or issues, please open an issue on the [GitHub repository](https://github.com/matteobarzaghi/playwright/issues).
