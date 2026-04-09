# 🕵️ Web Scraper Tool

A powerful, 🧩 modular Python web scraper that extracts structured data from websites and exports it in multiple formats.

## 🚀 Features

- **⚡ Static & Dynamic Scraping**: Handle both regular HTML and JavaScript-rendered content
- **🔐 Authentication Support**: Login capability for protected pages
- **📂 Multiple Export Formats**:
  - 📊 Excel (.xlsx)
  - 📄 PDF (.pdf)
  - 📋 Text (.txt)
  - 🌐 HTML (.html)
  - 📦 JSON (.json)
  - 🖼️ PNG Screenshots (.png)

- **🔍 Structured Data Extraction**:
  - 🏷️ Page title
  - 📑 All headings (H1, H2, H3)
  - 📝 All paragraph text
  - 🔗 All links (URLs)
  - 📷 All images (image sources)

- **📈 Professional Reports**: Formatted PDF and HTML reports
- **📸 Webpage Screenshots**: Full-page visual captures

---

## 📋 Requirements

- **🐍 Python 3.8+**
- **🌐 Google Chrome** (required for Selenium screenshot functionality)
- **⚙️ ChromeDriver** (automatically managed by Selenium, but Chrome must be installed)

---

## 🔧 Installation

### 🔢 1️⃣ Clone or Download the Project

```bash
cd c:\Users\babin\Desktop\web_scraper_project
```

### 🔢 2️⃣ Create Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
venv\Scripts\activate
```

### 🔢 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 🔢 4️⃣ Verify Installation

```bash
python -c "from scraper import *; print('✓ All modules loaded successfully!')"
```

---

## 📖 Quick Start

### 🚀 Basic Usage

```bash
python main.py
```

This will start an interactive prompt:

```text
Enter URL: https://example.com
Dynamic? (y/n): n
Scraping completed! Check output folder.
```

### ⚙️ Options Explained

| Prompt | Options | Purpose |
| -------- | --------- | --------- |
| **URL** | Any valid website URL | The website to scrape |
| **Dynamic?** | `y` / `n` | Use JavaScript rendering (for dynamic sites) |
| **Need authentication?** | `y` / `n` | Login required (only for dynamic mode) |

---

## 🎯 Usage Examples

### 💡 Example 1: Scrape Static HTML Website

```bash
python main.py
# Input: https://example.com
# Dynamic: n
```

### 💡 Example 2: Scrape JavaScript-Heavy Site

```bash
python main.py
# Input: https://example.com
# Dynamic: y
```

### 💡 Example 3: Scrape Protected Content (with Login)

```bash
python main.py
# Input: https://example.com/protected
# Dynamic: y
# Need authentication: y
# Username: myusername
# Password: mypassword
```

---

## 📁 Project Structure

```text
web_scraper_project/
├── main.py                 # 🎯 Entry point & main orchestration
├── requirements.txt        # 📦 Python dependencies
├── README.md               # 📖 This file
├── LOGIC.md                # 🧠 Architecture & logic documentation
│
├── scraper/                # 📂 Core scraper package
│   ├── __init__.py         # 🧩 Package initialization & exports
│   ├── fetcher.py          # 🌐 HTTP requests & Selenium handling
│   ├── parser.py           # 🔍 HTML parsing with BeautifulSoup
│   └── exporter.py         # 💾 Export to multiple formats
│
└── output/                 # 📥 Generated output files (created after first run)
    ├── output.xlsx         # 📊 Structured data in Excel
    ├── output.json         # 📦 Structured data in JSON
    ├── output.pdf          # 📄 Formatted PDF report
    ├── output.txt          # 📋 Plain text report
    ├── output.html         # 🌐 Interactive HTML report
    └── page.png            # 🖼️ Full webpage screenshot
```

---

## 📊 Output Files Explained

| File | Format | Content | Best For |
| ------ | -------- | --------- | ---------- |
| `output.xlsx` | 📊 Excel | Structured data in columns | Data analysis |
| `output.json` | 📦 JSON | Machine-readable format | API integration |
| `output.pdf` | 📄 PDF | Formatted report | Sharing/printing |
| `output.txt` | 📋 Plain text | Human-readable | Quick review |
| `output.html` | 🌐 Web page | Interactive report + full HTML | Complete information |
| `page.png` | 🖼️ Screenshot | Visual representation | Documentation |

---

## 🛠️ Module Descriptions

### `main.py`

**Purpose**: 🎯 Main entry point and orchestration  
**Functions**:

- `scrape()`: Coordinates the entire scraping workflow
- Interactive user prompt for configuration

### `scraper/fetcher.py`

**Purpose**: 🌐 HTTP requests and webpage fetching  
**Functions**:

- `fetch_static()`: Fetch static HTML using requests library
- `fetch_dynamic()`: Render JavaScript and handle authentication
- `fetch_static_screenshot()`: Capture static page screenshots

### `scraper/parser.py`

**Purpose**: 🔍 Extract structured data from HTML  
**Functions**:

- `parse_html()`: Extract title, headings, links, images, paragraphs

### `scraper/exporter.py`

**Purpose**: 💾 Export data to multiple formats  
**Functions**:

- `export_excel()`: Save to Excel format
- `export_json()`: Save to JSON format
- `export_pdf()`: Create formatted PDF report
- `export_txt()`: Create plain text report
- `export_html()`: Create interactive HTML report
- `export_screenshot()`: Manage screenshot files

### `scraper/__init__.py`

**Purpose**: 🧩 Package initialization  
**Exports**: All public functions for easy importing

---

## 🔐 Authentication Support

When scraping protected sites with `Dynamic` mode:

1. **🕵️ Automatic Form Detection**: Looks for common login field names:
   - `username`, `email`, `user` (for username field)
   - `password` (for password field)
   - Submit buttons

2. **🔑 Credentials Provided**: Enter credentials when prompted

3. **🛡️ Security**: Credentials are used in-memory only, never stored

**Note**: For complex login forms (2FA, CAPTCHA), manual handling may be required.

---

## ⚠️ Troubleshooting

### 🛑 Issue: ChromeDriver Not Found

**Error**: `ChromeDriver version mismatch`  
**Solution**: Update Chrome browser to the latest version

```bash
pip install --upgrade selenium
```

### 🛑 Issue: "ModuleNotFoundError: No module named 'scraper'"

**Error**: Import fails when running from scraper directory  
**Solution**: Always run from project root

```bash
# ✅ Correct
cd c:\Users\babin\Desktop\web_scraper_project
python main.py

# ❌ Wrong
cd c:\Users\babin\Desktop\web_scraper_project\scraper
python fetcher.py
```

### 🛑 Issue: Authentication Not Working

**Error**: Login form not detected  
**Reason**: Form uses non-standard field names  
**Solution**: Edit `fetcher.py` function `fetch_dynamic()` to match your form's field names

### 🛑 Issue: Screenshot Blank or Error

**Error**: `Screenshot capture error`  
**Reason**: Headless Chrome can't render certain sites  
**Solution**: Some sites block headless browsers; try a different site

### 🛑 Issue: Timeout Error

**Error**: `requests.exceptions.Timeout`  
**Reason**: Website taking too long to respond  
**Solution**: Check internet connection or try a different URL

---

## 🔧 Advanced Configuration

### ⚙️ Modify Timeout (in `scraper/fetcher.py`)

```python
# Default: 10 seconds
res = requests.get(url, headers=HEADERS, timeout=10)

# Change to 20 seconds
res = requests.get(url, headers=HEADERS, timeout=20)
```

### ⚙️ Modify Wait Time for JavaScript (in `scraper/fetcher.py`)

```python
# Default: 5 seconds (wait for JS to render)
time.sleep(5)

# Increase or decrease based on site complexity
time.sleep(10)  # For heavy JS sites
```

### ⚙️ Modify PDF Content Limit (in `scraper/exporter.py`)

```python
# Default: Show first 20 items from each section
for v in values[:20]:

# Change to show all items
for v in values:
```

---

## 📝 Performance Considerations

| Mode | Speed | Best For |
| --------- | ----------------- | ----------------------- |
| ⚡ Static | Fast (2-3 sec) | Simple HTML sites |
| ⚙️ Dynamic | Slow (10-15 sec) | JavaScript-heavy sites |

**Tips**:

- 💡 Use `Static` mode when possible (faster)
- 💡 For dynamic sites, avoid logging in if not needed
- 💡 Large websites may take longer to screenshot

---

## 🎓 Learning Resources

- **📖 BeautifulSoup Documentation**: <https://www.crummy.com/software/BeautifulSoup/>
- **📖 Selenium Documentation**: <https://selenium.dev/>
- **📖 Requests Library**: <https://requests.readthedocs.io/>

---

## 📝 Example Workflows

### 📈 Workflow 1: Competitor Price Monitoring

```bash
# Scrape product pages regularly
python main.py
# Input: https://competitor.com/products
# Export to Excel for analysis
```

### 📈 Workflow 2: Content Research

```bash
# Collect blog content
python main.py
# Input: https://blog.example.com/article
# Export to JSON for NLP analysis
```

### 📈 Workflow 3: SEO Auditing

```bash
# Extract links and headings
python main.py
# Input: https://yoursite.com
# Export to PDF for documentation
```

---

## ⚖️ Legal & Ethical Guidelines

⚠️ **Important**: Before scraping any website:

1. ✅ **Check Terms of Service**: Ensure scraping is permitted
2. ✅ **Respect robots.txt**: Honor website scraping guidelines
3. ✅ **Rate Limiting**: Don't overload servers
4. ✅ **Attribution**: Credit original content sources
5. ⚠️ **Personal Data**: Don't scrape personal information without consent
6. ⚠️ **Copyright**: Respect intellectual property rights

---

## 🐛 Error Handling

The scraper includes comprehensive error handling:

- **🌐 Network Errors**: Gracefully handles timeouts and connection failures
- **🔗 Invalid URLs**: Returns appropriate error messages
- **🔍 Parse Errors**: Handles malformed HTML gracefully
- **🌐 Browser Errors**: Safely closes browser instances even on failure
- **📂 File I/O Errors**: Creates output directory automatically

---

## 🚀 Next Steps

1. **🧪 Verify Installation**: Run quick test

   ```bash
   python -c "from scraper import *; print('Ready!')"
   ```

2. **💡 Test with Sample Site**: Start with <https://example.com>

3. **📖 Read LOGIC.md**: Understand the architecture in detail

4. **⚙️ Explore Customization**: Modify functions for specific needs

---

## 📞 Support

For issues or questions:

1. 🔍 Check **Troubleshooting** section above
2. 📖 Review **LOGIC.md** for architecture details
3. 📦 Verify all dependencies: `pip install -r requirements.txt`
4. 🌐 Check Chrome browser is installed and updated

---

## 📄 License & Purpose

🎓 **Educational Project**: This application was developed as a self-learning exercise for knowledge gain and understanding of web scraping technologies, modular Python architecture, and automated reporting.

⚠️ **Disclaimer**: This project is provided as-is for educational purposes. Always ensure you have permission before scraping any website and comply with their `robots.txt` and Terms of Service.

---

**Last Updated**: April 2026  
**Python Version**: 3.8+  
**Status**: ✅ Production Ready
