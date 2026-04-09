# 🧠 Web Scraper Architecture & Logic

## 🎯 Project Overview

This web scraper is built using a **🧩 modular, layered architecture** that separates concerns into 4 distinct layers:

1. **🎮 Orchestration Layer** ([main.py](main.py)) - User interface & workflow coordination
2. **🌐 Fetching Layer** ([scraper/fetcher.py](scraper/fetcher.py)) - Network & browser management
3. **🔍 Parsing Layer** ([scraper/parser.py](scraper/parser.py)) - Data extraction from HTML
4. **💾 Export Layer** ([scraper/exporter.py](scraper/exporter.py)) - Multi-format data export

---

## 📊 Architecture Diagram

```text
┌─────────────────────────────────────────────────────────────────┐
│                      USER INTERFACE (main.py)                   │
│  Prompts user for: URL, Mode (Static/Dynamic), Authentication   │
└────────────────────────────┬──────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                  ORCHESTRATION (main.scrape())                   │
│  Coordinates workflow: Fetch → Parse → Export                   │
└────────────────────────────┬──────────────────────────────────┘
                             │
         ┌───────────────────┼───────────────────┐
         ▼                   ▼                   ▼
    ┌─────────────┐  ┌─────────────┐  ┌──────────────────┐
    │   FETCHER   │  │   PARSER    │  │     EXPORTER     │
    │             │  │             │  │                  │
    │ • HTTP Req. │  │ • BeautifulSoup │ • Excel Export  │
    │ • Selenium  │  │ • Extract data  │ • JSON Export   │
    │ • Login     │  │ • Structuring   │ • PDF Report    │
    │ • Screenshot│  │               │ • Text Export   │
    └─────────────┘  └─────────────┘  │ • HTML Export   │
                                      │ • Screenshots   │
                                      └──────────────────┘
         │                   │                   │
         └───────────────────┼───────────────────┘
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                      OUTPUT FOLDER                              │
│  • output.xlsx    • output.pdf     • page.png                   │
│  • output.json    • output.html    • output.txt                │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🔄 Complete Workflow

### Step 1: User Input (main.py)

```text
START
  ├─ Ask for URL
  ├─ Ask for Mode (Static/Dynamic)
  ├─ Ask for Authentication (if Dynamic)
  └─ Call scrape() function
```

### Step 2: Fetch HTML (fetcher.py)

**If Static Mode:**

```text
  ├─ Use requests library
  ├─ Send GET request with headers
  ├─ Return HTML content
  └─ Capture screenshot separately
```

**If Dynamic Mode:**

```text
  ├─ Initialize headless Chrome browser
  ├─ Navigate to URL
  ├─ If credentials provided:
  │   ├─ Find login form
  │   ├─ Fill username field
  │   ├─ Fill password field
  │   ├─ Click submit button
  │   └─ Wait for login (3 sec)
  ├─ Wait for JS to render (5 sec)
  ├─ Set window size to content
  ├─ Capture screenshot
  ├─ Return HTML content
  └─ Close browser safely
```

### Step 3: Parse HTML (parser.py)

```text
  ├─ Initialize BeautifulSoup
  ├─ Extract:
  │   ├─ Page title
  │   ├─ All H1, H2, H3 headings
  │   ├─ All paragraph text
  │   ├─ All links (href attributes)
  │   └─ All images (src attributes)
  ├─ Clean & structure data
  └─ Return dictionary
```

### Step 4: Export Data (exporter.py)

```text
  ├─ Create output directory
  ├─ Export to Excel (.xlsx)
  ├─ Export to JSON (.json)
  ├─ Export to PDF (.pdf with formatting)
  ├─ Export to Text (.txt)
  ├─ Export to HTML (.html with full content)
  └─ Verify screenshot exists (.png)
```

### Step 5: Complete

```text
  └─ Display success message
```

---

## 📁 Module Breakdown

### 1. **main.py** - Orchestration Layer

**Responsibility**: User interface & workflow coordination

**Key Function: `scrape(url, dynamic, username, password)`**

```python
def scrape(url, dynamic=False, username=None, password=None):
    # Step 1: Fetch HTML
    html = fetch_dynamic(...) if dynamic else fetch_static(...)
    
    # Step 2: Error check
    if not html:
        return
    
    # Step 3: Capture screenshot (static mode only)
    if not dynamic:
        fetch_static_screenshot(url)
    
    # Step 4: Parse HTML
    data = parse_html(html)
    
    # Step 5: Export to all formats
    export_excel(data)
    export_json(data)
    export_pdf(data)
    export_txt(data)
    export_html(data, html)
    export_screenshot()
    
    # Step 6: Complete
    print("Scraping completed!")
```

**Flow Logic**:

- `Static Mode`: Request → Parse → Export → Done
- `Dynamic Mode`: Browser → Wait for JS → Parse → Export → Done

**Error Handling**: Returns gracefully if HTML fetch fails

---

### 2. **scraper/fetcher.py** - Fetching Layer

**Responsibility**: Network requests & browser automation

**Function 1: `fetch_static(url)`**

```text
Purpose: Get HTML from static websites using HTTP requests
- Creates HTTP GET request with User-Agent header
- Handles timeouts (10 second limit)
- Catches network errors gracefully
- Returns raw HTML content
```

**Used For**: Websites with pre-rendered HTML

**Function 2: `fetch_dynamic(url, username, password)`**

```text
Purpose: Render JavaScript and handle authentication
- Starts headless Chrome browser
- Waits 5 seconds for JS to render
- Optional: Handles login form submission
- Takes full-page screenshot
- Returns rendered HTML content
```

**Key Features**:

- **Headless Mode**: No GUI window appears
- **Auto-Logout**: Safe browser cleanup with try-except
- **Form Detection**: Looks for common field names (username, email, password)
- **Wait Times**:
  - 3 sec after login
  - 5 sec for JS rendering
  - 2 sec for window resize

**Used For**: JavaScript-heavy sites, React/Vue/Angular apps

**Function 3: `fetch_static_screenshot(url)`**

```text
Purpose: Capture screenshot of static page
- Uses Selenium similar to dynamic mode
- Takes full-page screenshot
- Returns with no HTML
```

**Used For**: Getting visual representation of static pages

**Error Handling**:

- Network timeout: Caught, error printed
- Browser errors: Browser safely closed
- Login form not found: Continues without login
- ChromeDriver issues: Error message shown

---

### 3. **scraper/parser.py** - Parsing Layer

**Responsibility**: Extract structured data from HTML

**Function: `parse_html(html)`**

```text
Purpose: Convert raw HTML into structured data
Input: Raw HTML string from fetcher
Output: Dictionary with organized data

Process:
  ├─ Title: Get document title
  ├─ Headings: Find all H1, H2, H3 tags
  ├─ Links: Extract all href attributes
  ├─ Images: Extract all img src attributes
  └─ Paragraphs: Get all paragraph text
```

**Data Structure Output**:

```python
{
    "title": "Page Title",
    "headings": ["Heading 1", "Heading 2", ...],
    "links": ["https://...", "https://...", ...],
    "images": ["https://...", "https://...", ...],
    "paragraphs": ["Text 1", "Text 2", ...]
}
```

**Features**:

- BeautifulSoup for reliable HTML parsing
- Automatic text trimming (`.strip()`)
- Handles missing elements (returns empty if not found)
- Filters out None values for links/images

**Why This Matters**:

- Converts unstructured HTML → structured data
- Makes data machine-readable
- Foundation for all export formats

---

### 4. **scraper/exporter.py** - Export Layer

**Responsibility**: Convert parsed data into multiple formats

**Function 1: `export_excel(data)`**

```text
Output: output.xlsx
Format: Excel spreadsheet with columns
Use Case: Data analysis in spreadsheet tools
Limit: Shows all items (no truncation)
```

**Function 2: `export_json(data)`**

```text
Output: output.json
Format: JSON with 4-space indentation
Use Case: API integration, data interchange
Limit: All items included
Compatibility: Works with any JSON parser
```

**Function 3: `export_pdf(data)`**

```text
Output: output.pdf
Format: Formatted PDF report
Features:
  - Blue title with "Web Scraping Report"
  - Section headers with gray background
  - Bullet points for list items
  - Professional formatting
Limit: First 20 items per section
Best For: Sharing, printing, archiving
```

**Function 4: `export_txt(data)`**

```text
Output: output.txt
Format: Plain text with headers
Features:
  - Section dividers
  - Bullet points
  - UTF-8 encoding
Limit: First 50 items per section
Best For: Quick human review
```

**Function 5: `export_html(data, html_content)`**

```text
Output: output.html
Format: Interactive HTML page
Features:
  - Professional CSS styling
  - Paragraph sections
  - Full HTML content preserved
  - Responsive design
  - Color-coded headers
Best For: Complete information, browser viewing
Includes: Full original HTML at bottom
```

**Function 6: `export_screenshot()`**

```text
Output: page.png (if exists from fetcher)
Format: PNG image
Size: Full webpage height
Best For: Visual documentation
Created By: Fetcher layer (not exporter)
```

**Export Workflow**:

```text
Data Dictionary
      ↓
For each export format:
  ├─ Create output folder
  ├─ Format data appropriately
  ├─ Handle encoding (UTF-8, Latin-1)
  ├─ Write to file
  └─ Success message
      ↓
All files ready in output/
```

---

## 🔗 Data Flow Through Layers

### Complete Journey of a URL

```text
1. User Input
   └─→ main.py receives: "https://example.com"

2. Fetch Layer
   └─→ fetcher.py: requests.get() or selenium
   └─→ Returns: Raw HTML string

3. Parse Layer
   └─→ parser.py: BeautifulSoup parsing
   └─→ Returns: Structured dictionary

4. Export Layer
   └─→ exporter.py: Converts to 6 formats
   └─→ Writes: 6 files to output/ folder

5. User
   └─→ Retrieves files from output/ folder
```

---

## 🧩 Module Dependencies

```text
main.py
  ├─ imports: scraper.fetcher
  ├─ imports: scraper.parser
  ├─ imports: scraper.exporter
  └─ runs: scrape() orchestration

scraper/__init__.py
  ├─ imports: all functions from below
  └─ exports: public API

scraper/fetcher.py
  ├─ requires: requests (static)
  ├─ requires: selenium + webdriver (dynamic)
  ├─ requires: time, os
  └─ independent: no internal imports

scraper/parser.py
  ├─ requires: beautifulsoup4
  └─ independent: no internal imports

scraper/exporter.py
  ├─ requires: pandas (Excel)
  ├─ requires: json (JSON)
  ├─ requires: fpdf (PDF)
  ├─ requires: pillow (for text to image)
  └─ independent: no internal imports
```

**Key Point**: Each layer is independent and can be tested separately!

---

## 🔒 Error Handling Strategy

### Layer 1: Fetcher (Network Level)

```text
- Timeout: 10-15 seconds
- Browser crashes: Safely close with try-finally
- Login fails: Continue without authentication
- Invalid URL: requests library shows error
```

### Layer 2: Parser (HTML Level)

```text
- Missing title: Returns empty string
- No headings: Returns empty list
- Malformed HTML: BeautifulSoup handles gracefully
- Empty page: Returns empty lists
```

### Layer 3: Exporter (File Level)

```text
- Missing output directory: Creates automatically
- File write errors: os.makedirs catches
- Invalid data: Skips gracefully
- Encoding issues: Uses latin-1 fallback
```

### Layer 4: Main (Orchestration)

```text
- Failed fetch: Prints error, returns
- No data: Returns before exporting
- Export errors: Shows which export failed
```

---

## 🚀 Performance Characteristics

### Static Mode Timeline

```text
1. HTTP Request: 1-3 seconds
2. Parse HTML: <1 second
3. Export (all formats): 1-2 seconds
4. Total: 2-6 seconds (depends on site)
```

### Dynamic Mode Timeline

```text
1. Start Chrome: 2-3 seconds
2. Navigate URL: 2-3 seconds
3. Wait for JS: 5 seconds (configurable)
4. Screenshot: 1-2 seconds
5. Parse HTML: <1 second
6. Export: 1-2 seconds
7. Total: 11-16 seconds (depends on site)
```

**Why Dynamic is Slower**:

- Browser startup overhead
- JavaScript rendering wait
- Screenshot capture time

**Optimization Tips**:

- Use static mode when possible
- Don't log in unless necessary
- Reduce wait times if site loads quickly
- Use threading for batch scraping

---

## 🔄 Reusability & Extensibility

### Why It's Modular

Each layer can be used independently:

```python
# Use just the fetcher
from scraper.fetcher import fetch_static
html = fetch_static("https://example.com")

# Use just the parser
from scraper.parser import parse_html
data = parse_html(html)

# Use just an exporter
from scraper.exporter import export_json
export_json(data)
```

### How to Extend

**Add a new export format** (e.g., CSV):

```python
# In scraper/exporter.py
def export_csv(data):
    import csv
    with open("output/data.csv", "w") as f:
        writer = csv.DictWriter(f, fieldnames=data.keys())
        writer.writeheader()
        # Write data...

# In scraper/__init__.py
from .exporter import ..., export_csv

# In main.py
export_csv(data)
```

**Add authentication method** (e.g., OAuth):

```python
# In scraper/fetcher.py
def fetch_oauth(url, client_id, client_secret):
    # OAuth logic here
    return html

# Call from main.py
```

---

## 💡 Key Design Decisions

### 1. **Why BeautifulSoup for Parsing?**

- ✅ Robust HTML parsing
- ✅ Handles malformed HTML
- ✅ Simple & readable syntax
- ✅ No JavaScript needed

### 2. **Why Both requests + Selenium?**

- ✅ `requests`: Fast for simple HTML
- ✅ `Selenium`: Can handle JavaScript
- ✅ User chooses based on site complexity

### 3. **Why Multiple Exports?**

- ✅ Different users prefer different formats
- ✅ Excel for analysis, JSON for APIs, PDF for reports
- ✅ Future tools can use any format

### 4. **Why Modular Architecture?**

- ✅ Easy to test each layer
- ✅ Easy to replace/upgrade components
- ✅ Reusable in other projects
- ✅ Follows Single Responsibility Principle

---

## 📈 Data Transformation Pipeline

```text
Raw URL
    ↓
(Fetcher) ──→ Raw HTML String
    ↓
(Parser) ──→ Dictionary {
              title: str,
              headings: [str],
              links: [str],
              images: [str],
              paragraphs: [str]
            }
    ↓
(Exporters) ──→ ┌─ output.xlsx
                ├─ output.json
                ├─ output.pdf
                ├─ output.txt
                ├─ output.html
                └─ page.png
```

---

## 🎓 Learning Path

If you want to understand this project:

1. **Start with**: `main.py` - See the big picture
2. **Then read**: This file - Understand architecture
3. **Then study**: `scraper/fetcher.py` - Learn fetching
4. **Then study**: `scraper/parser.py` - Learn parsing
5. **Then study**: `scraper/exporter.py` - Learn exporting
6. **Finally**: Modify and extend features!

---

## 🔬 Testing the Layers

### Test Fetcher

```python
from scraper.fetcher import fetch_static
html = fetch_static("https://example.com")
print(len(html), "bytes received")
```

### Test Parser

```python
from scraper.parser import parse_html
data = parse_html(html)
print(data.keys())  # Should show: title, headings, links, images, paragraphs
```

### Test Exporter

```python
from scraper.exporter import export_json
export_json(data)
# Check output/output.json
```

---

## 📊 Statistics

| Aspect | Value |
| -------- | ------- |
| Lines of Code | ~400 |
| Number of Modules | 4 |
| Export Formats | 6 |
| Data Points Extracted | 5 |
| Error Handlers | 8+ |
| Authentication Methods | 1 (basic form) |
| Dependencies | 7 major |

---

**Architecture Version**: 1.0  
**Last Updated**: April 2026  
**Status**: Production Ready
