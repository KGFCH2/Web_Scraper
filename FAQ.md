# ❓ Frequently Asked Questions (FAQ)

This document provides answers to common questions regarding the Web Scraper Tool, its outputs, and its functionality.

---

## 📂 Output Files & Formats

### Q1: Why do I need an HTML output if the content is the same as the PDF?

**A:** While the content is similar, the HTML format offers unique advantages:

- **Interactive Links:** All extracted URLs are clickable and open directly in your browser.
- **Easy Data Recovery:** You can easily copy individual sections or large blocks of text without the formatting issues often found in PDFs.
- **Verification:** The HTML file includes a "Full HTML Content" section at the bottom, allowing you to see exactly what the scraper "saw" on the page.
- **Responsive:** It scales perfectly on mobile devices and tablets.

### Q2: What is the best format for data analysis?

**A:** **Excel (`output.xlsx`)** is the best choice for data analysis. It organizes the information into structured columns (Title, Headings, Links, etc.), making it easy to filter, sort, and perform calculations.

### Q3: When should I use the JSON output?

**A:** **JSON (`output.json`)** is intended for developers. It is a machine-readable format that allows the scraped data to be easily imported into other applications, databases, or web APIs.

---

## ⚙️ Scraping Modes

### Q4: What is the difference between "Static" and "Dynamic" mode?

**A:**

- **Static Mode:** Uses the `requests` library. It is extremely fast but can only see the initial HTML sent by the server. Use this for simple blogs or news sites.
- **Dynamic Mode:** Uses `Selenium` to open a real Chrome browser. It can execute JavaScript, handle pop-ups, and wait for content to load. Use this for modern web apps (React, Vue, etc.).

### Q5: Why is Dynamic mode slower?

**A:** Dynamic mode requires launching a browser instance and waiting for the website's scripts to finish running (usually 5-10 seconds). Static mode, which just downloads a single file, typically finishes in under 1 second.

---

## 🔐 Authentication & Access

### Q6: Can I scrape websites that require a login?

**A:** **Yes**, but only in **Dynamic mode**. The tool will look for common login fields (username, password) and attempt to sign in using the credentials you provide during the prompt.

### Q7: Is my password saved anywhere?

**A:** **No.** Credentials are used in-memory during the active session and are never written to disk or logs.

---

## 🛠️ Troubleshooting

### Q8: Why is my screenshot blank?

**A:** This usually happens if the website has anti-bot protections or if the page didn't finish loading before the screenshot was taken. You can try increasing the `WAIT_TIME` in `scraper/fetcher.py`.

### Q9: I'm getting a "ChromeDriver version mismatch" error. How do I fix it?

**A:** This happens when your Chrome browser updates to a version newer than the driver. Run `pip install --upgrade selenium` or ensure your Google Chrome is up to date; the `webdriver-manager` inside the script usually handles the rest automatically on the next run.

### Q10: Why does the PDF show "None" for some images?

**A:** This occurs when an image tag on the website doesn't have a valid `src` attribute or uses "lazy loading" that hasn't triggered yet.

---

## 📦 Libraries & Technology

### Q12: Which Python packages are used to extract information from webpages?

**A:** This tool uses a combination of several industry-standard libraries, each with a specific role:

- **`requests`**: Used in **Static Mode** to quickly download the HTML content of a webpage. It is lightweight and fast but does not execute JavaScript.
- **`selenium`**: Used in **Dynamic Mode** to automate a real Chrome browser. It handles JavaScript rendering, clicks, and login forms.
- **`beautifulsoup4` (BS4)**: The "brain" of the parsing process. It takes the HTML from either `requests` or `selenium` and extracts specific pieces of data like titles, links, and text.
- **`webdriver-manager`**: Automatically manages the connection between the script and your Chrome browser, ensuring you always have the correct version of `chromedriver`.

## 🎓 Project Origin & Goals

### Q13: What was the primary goal of creating this tool?

**A:** This project was developed as a hands-on **educational exercise**. The goal was to gain a deep understanding of:

- **Modular Python Design**: How to structure a project into folders and specialized modules.
- **Web Technologies**: The difference between static HTML and dynamic JavaScript-rendered content.
- **Data Automation**: How to transform raw website data into professional formats like Excel, JSON, and PDF.
- **Problem Solving**: Navigating real-world challenges like website logins and browser automation.

### Q14: Is this a commercial product?

**A:** No. This is a personal knowledge-building project created for **learning and understanding purposes** as part of a self-driven assignment.

---

## ⚖️ Legal & Ethics

### Q11: Is it legal to scrape any website?

**A:** You should always check a website's `robots.txt` (e.g., `example.com/robots.txt`) and their Terms of Service. Scraping public data is generally acceptable for personal use, but avoid scraping private user data or overloading a server with too many requests.
