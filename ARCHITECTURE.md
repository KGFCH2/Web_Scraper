# 🏗️ Web Scraper - Architecture & Process Flow Diagrams

## 📊 System Architecture

```mermaid
graph TB
    User["👤 User Input<br/>URL, Mode, Auth"]
    Main["🎯 main.py<br/>Orchestration"]
    
    Fetcher["🌐 fetcher.py<br/>Network & Browser"]
    Static["📄 Static Mode<br/>requests"]
    Dynamic["⚙️ Dynamic Mode<br/>Selenium"]
    Screenshot["📸 Screenshot<br/>Capture"]
    
    Parser["🔍 parser.py<br/>HTML Parsing"]
    
    Exporter["💾 exporter.py<br/>Multi-Format Export"]
    Excel["📊 Excel"]
    JSON["📦 JSON"]
    PDF["📄 PDF"]
    Text["📋 Text"]
    HTML["🌐 HTML"]
    Image["🖼️ Image"]
    
    Output["📁 output/<br/>All files"]
    
    User -->|Input| Main
    Main -->|URL, Mode| Fetcher
    
    Fetcher -->|Dynamic| Dynamic
    Fetcher -->|Static + Screenshot| Static
    
    Dynamic --> Screenshot
    Static --> Screenshot
    
    Screenshot -->|HTML| Parser
    Parser -->|Data Dict| Exporter
    
    Exporter --> Excel
    Exporter --> JSON
    Exporter --> PDF
    Exporter --> Text
    Exporter --> HTML
    Exporter --> Image
    
    Excel --> Output
    JSON --> Output
    PDF --> Output
    Text --> Output
    HTML --> Output
    Image --> Output
    
    style User fill:#fff4e6
    style Main fill:#e3f2fd
    style Fetcher fill:#f3e5f5
    style Static fill:#f3e5f5
    style Dynamic fill:#f3e5f5
    style Screenshot fill:#f3e5f5
    style Parser fill:#e8f5e9
    style Exporter fill:#fce4ec
    style Output fill:#f1f8e9
```

---

## 🔄 Complete Workflow Process

```mermaid
flowchart TD
    A["🟢 START"] --> B["📝 User Enters URL"]
    B --> C{"Static or<br/>Dynamic?"}
    
    C -->|Static| D["🌐 Fetch with<br/>requests.get"]
    C -->|Dynamic| E["⚙️ Start Chrome<br/>Headless Browser"]
    
    E --> F{"Need<br/>Login?"}
    F -->|Yes| G["🔐 Fill Login Form<br/>& Submit"]
    F -->|No| H["⏳ Wait 5s for JS<br/>to Render"]
    G --> I["⏳ Wait 3s<br/>for Login"]
    I --> H
    
    D --> J["📸 Capture<br/>Screenshot"]
    H --> K["📸 Capture<br/>Screenshot"]
    
    J --> L{"HTML<br/>Retrieved?"}
    K --> L
    
    L -->|No| M["❌ Error:<br/>Return"]
    L -->|Yes| N["🔍 Parse HTML<br/>with BeautifulSoup"]
    
    N --> O["📊 Extract:<br/>Title, Headings,<br/>Links, Images,<br/>Paragraphs"]
    
    O --> P["📦 Create Data<br/>Dictionary"]
    
    P --> Q["💾 Export to<br/>Excel"]
    Q --> R["💾 Export to<br/>JSON"]
    R --> S["💾 Export to<br/>PDF"]
    S --> T["💾 Export to<br/>Text"]
    T --> U["💾 Export to<br/>HTML"]
    U --> V["💾 Verify<br/>Screenshot"]
    
    V --> W["📁 All files in<br/>output/"]
    W --> X["✅ SUCCESS:<br/>Scraping Complete"]
    M --> Y["❌ END"]
    X --> Y["🟢 END"]
    
    style A fill:#90EE90
    style Y fill:#FFB6C6
    style X fill:#90EE90
    style M fill:#FFB6C6
    style D fill:#87CEEB
    style E fill:#87CEEB
    style G fill:#FFD700
    style N fill:#98FB98
    style W fill:#F0E68C
```

---

## 🌐 Static Mode Detailed Flow

```mermaid
sequenceDiagram
    actor User
    participant main.py
    participant fetcher.py
    participant parser.py
    participant exporter.py
    participant output
    
    User->>main.py: Enter URL + Mode=Static
    main.py->>fetcher.py: fetch_static(url)
    fetcher.py->>fetcher.py: requests.get(url)
    fetcher.py-->>main.py: Return HTML
    
    main.py->>fetcher.py: fetch_static_screenshot(url)
    fetcher.py->>fetcher.py: Selenium screenshot
    fetcher.py-->>main.py: Screenshot saved
    
    main.py->>parser.py: parse_html(html)
    parser.py->>parser.py: BeautifulSoup parse
    parser.py->>parser.py: Extract data
    parser.py-->>main.py: Return data dict
    
    main.py->>exporter.py: export_excel(data)
    main.py->>exporter.py: export_json(data)
    main.py->>exporter.py: export_pdf(data)
    main.py->>exporter.py: export_txt(data)
    main.py->>exporter.py: export_html(data)
    main.py->>exporter.py: export_screenshot()
    
    exporter.py->>output: Write all files
    exporter.py-->>main.py: Done
    
    main.py-->>User: Success! Check output/
```

---

## ⚙️ Dynamic Mode Detailed Flow (with Authentication)

```mermaid
sequenceDiagram
    actor User
    participant main.py
    participant selenium
    participant target_site
    participant parser.py
    participant exporter.py
    
    User->>main.py: URL + Mode=Dynamic + Auth
    main.py->>selenium: Initialize Chrome (headless)
    selenium->>target_site: Navigate to URL
    
    alt Authentication Required
        selenium->>target_site: Find login form
        selenium->>target_site: Fill username
        selenium->>target_site: Fill password
        selenium->>target_site: Click submit
        selenium->>selenium: Wait 3s for login
        target_site-->>selenium: Redirected (logged in)
    end
    
    selenium->>selenium: Wait 5s for JS render
    selenium->>target_site: Capture full page screenshot
    target_site-->>selenium: Screenshot taken (.png)
    selenium->>target_site: Get page source (HTML)
    target_site-->>selenium: Return HTML
    selenium-->>main.py: Return HTML
    
    main.py->>parser.py: parse_html(html)
    parser.py-->>main.py: Return data dict
    
    main.py->>exporter.py: Export to all formats
    exporter.py-->>main.py: Done
    
    main.py-->>User: Success! Check output/
```

---

## 📊 Data Transformation Pipeline

```mermaid
graph LR
    A["Raw URL<br/>https://example.com"]
    B["🌐 Fetcher<br/>requests or<br/>Selenium"]
    C["📄 Raw HTML<br/>String<br/>10,000+ chars"]
    D["🔍 Parser<br/>BeautifulSoup"]
    E["📊 Structured Data<br/>{title, headings,<br/>links, images,<br/>paragraphs}"]
    F["💾 Exporters<br/>Convert Format"]
    G["📁 Output Files<br/>6 formats"]
    
    A --> B
    B --> C
    C --> D
    D --> E
    E --> F
    F --> G
    
    style A fill:#FFE4B5
    style C fill:#ADD8E6
    style E fill:#98FB98
    style G fill:#FFE4B5
```

---

## 🔀 Module Interaction Map

```mermaid
graph TB
    Main["main.py<br/>🎯 Orchestrator"]
    
    Fetcher["fetcher.py<br/>🌐 Network Layer"]
    Parser["parser.py<br/>🔍 Parse Layer"]
    Exporter["exporter.py<br/>💾 Export Layer"]
    
    Requests["requests<br/>Library"]
    Selenium["Selenium<br/>WebDriver"]
    BeautifulSoup["BeautifulSoup<br/>Library"]
    Pandas["pandas<br/>Library"]
    FPDF["fpdf<br/>Library"]
    JSON["json<br/>Library"]
    
    Main -->|fetch_static| Fetcher
    Main -->|fetch_dynamic| Fetcher
    Main -->|parse_html| Parser
    Main -->|export_*| Exporter
    
    Fetcher -->|uses| Requests
    Fetcher -->|uses| Selenium
    
    Parser -->|uses| BeautifulSoup
    
    Exporter -->|uses| Pandas
    Exporter -->|uses| FPDF
    Exporter -->|uses| JSON
    
    style Main fill:#E3F2FD
    style Fetcher fill:#F3E5F5
    style Parser fill:#E8F5E9
    style Exporter fill:#FCE4EC
```

---

## 🔗 Error Handling Zones

```mermaid
graph TB
    A["Input"] 
    
    B["Fetcher Zone<br/>Network Errors"]
    C["Parser Zone<br/>HTML Errors"]
    D["Export Zone<br/>File Errors"]
    
    E["Recovery"]
    F["Logging"]
    
    A --> B
    B --> C
    C --> D
    
    B -->|Error| E
    B -->|Error| F
    
    C -->|Error| E
    C -->|Error| F
    
    D -->|Error| E
    D -->|Error| F
    
    E --> G["Continue/Retry"]
    F --> H["User Feedback"]
    
    style B fill:#FFE4E1
    style C fill:#FFE4E1
    style D fill:#FFE4E1
    style E fill:#98FB98
    style F fill:#FFD700
```

---

## ⏱️ Performance Timeline

### Static Mode (Fast Path)

```mermaid
gantt
    title Static Mode Timeline
    dateFormat YYYY-MM-DD HH:mm:ss
    axisFormat %M:%S
    
    HTTP Request           :fetch, 2024-01-01 00:00:00, 3s
    Parse HTML            :parse, after fetch, 1s
    Export All Formats    :export, after parse, 2s
    TOTAL                 :crit, 2024-01-01 00:00:00, 6s
```

### Dynamic Mode (Slow Path)

```mermaid
gantt
    title Dynamic Mode Timeline
    dateFormat YYYY-MM-DD HH:mm:ss
    axisFormat %M:%S
    
    Chrome Startup        :start, 2024-01-01 00:00:00, 3s
    Navigate URL          :nav, after start, 2s
    JS Rendering Wait     :wait1, after nav, 5s
    Screenshot            :screen, after wait1, 2s
    Parse HTML            :parse, after screen, 1s
    Export All Formats    :export, after parse, 2s
    TOTAL                 :crit, 2024-01-01 00:00:00, 15s
```

---

## 📦 Data Structure Transformations

### Input: Raw HTML

```html
<!DOCTYPE html>
<html>
<head><title>Example Page</title></head>
<body>
<h1>Main Title</h1>
<p>Some text here</p>
<a href="https://link.com">Click Me</a>
<img src="image.jpg" />
</body>
</html>
```

### After Parsing

```python
{
    "title": "Example Page",
    "headings": ["Main Title"],
    "paragraphs": ["Some text here"],
    "links": ["https://link.com"],
    "images": ["image.jpg"]
}
```

### After Export to JSON

```json
{
  "title": "Example Page",
  "headings": ["Main Title"],
  "paragraphs": ["Some text here"],
  "links": ["https://link.com"],
  "images": ["image.jpg"]
}
```

### After Export to Excel

```text
| title        | headings    | paragraphs      | links              | images   |
|--------------|-------------|-----------------|--------------------|----------|
| Example Page | Main Title  | Some text here  | https://link.com   | image.jpg|
```

---

## 🎯 Use Case Workflows

### Use Case 1: Content Research

```mermaid
flowchart LR
    A["Website<br/>Article"] --> B["Static<br/>Scrape"]
    B --> C["Parse &<br/>Extract"]
    C --> D["Export to<br/>JSON"]
    D --> E["AI Analysis<br/>NLP Tool"]
    
    style A fill:#FFE4B5
    style B fill:#87CEEB
    style C fill:#98FB98
    style D fill:#FFD700
    style E fill:#FF69B4
```

### Use Case 2: Price Monitoring

```mermaid
flowchart LR
    A["E-Commerce<br/>Site"] --> B["Dynamic<br/>Scrape"]
    B --> C["Extract<br/>Prices"]
    C --> D["Export to<br/>Excel"]
    D --> E["Compare &<br/>Alert"]
    
    style A fill:#FFE4B5
    style B fill:#87CEEB
    style C fill:#98FB98
    style D fill:#FFD700
    style E fill:#FF69B4
```

### Use Case 3: SEO Audit

```mermaid
flowchart LR
    A["Your<br/>Website"] --> B["Scrape<br/>Pages"]
    B --> C["Extract<br/>Links & Headings"]
    C --> D["Export to<br/>PDF Report"]
    D --> E["Audit<br/>Review"]
    
    style A fill:#FFE4B5
    style B fill:#87CEEB
    style C fill:#98FB98
    style D fill:#FFD700
    style E fill:#FF69B4
```

---

## 🛡️ Security & Error Recovery

```mermaid
graph TB
    A["Operation Start"]
    
    B{"Error<br/>Detected?"}
    
    C["Fetch Error<br/>Network Issue"]
    D["Parse Error<br/>Invalid HTML"]
    E["Export Error<br/>File I/O"]
    
    F["Log Error<br/>Message"]
    G["Cleanup<br/>Resources"]
    H["Return/Skip<br/>Gracefully"]
    
    I["Success<br/>Complete"]
    
    A --> B
    
    B -->|Yes| C
    B -->|Yes| D
    B -->|Yes| E
    B -->|No| I
    
    C --> F
    D --> F
    E --> F
    
    F --> G
    G --> H
    H --> I
    
    style C fill:#FFB6C6
    style D fill:#FFB6C6
    style E fill:#FFB6C6
    style F fill:#FFD700
    style G fill:#FFD700
    style I fill:#90EE90
```

---

## 📋 Quick Reference: Flow Direction

```text
User Input
    ↓
main.py (orchestration)
    ↓
fetcher.py (get HTML)
    ├─ requests (static)
    └─ selenium (dynamic)
    ↓
parser.py (extract data)
    └─ BeautifulSoup
    ↓
exporter.py (6 formats)
    ├─ Excel
    ├─ JSON
    ├─ PDF
    ├─ Text
    ├─ HTML
    └─ Screenshot
    ↓
output/ (all files)
    ↓
User Retrieval
```

---

**Diagrams Version**: 1.0  
**Created**: April 2026  
**Tool**: Mermaid.js
