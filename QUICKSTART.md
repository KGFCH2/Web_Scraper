# ⚡ Quick Start Guide - Get Running in 5 Minutes

## 🚀 TL;DR (30 seconds)

```bash
# 1. Navigate to project
cd c:\Users\babin\Desktop\web_scraper_project

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run scraper
python main.py

# 4. Follow prompts
# Enter URL: https://example.com
# Dynamic? (y/n): n

# 5. Check output folder
```

---

## 📋 Detailed Quick Start

### 🔢 Step 1: Verify Python Installation

```bash
python --version
# Should show: Python 3.8 or higher
```

### 🔢 Step 2: Navigate to Project

```bash
cd c:\Users\babin\Desktop\web_scraper_project
```

### 🔢 Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

Expected output: `Successfully installed attrs beautifulsoup4 ...`

### 🔢 Step 4: Test Installation

```bash
python -c "from scraper import *; print('✓ Ready!')"
```

### Step 5: Run the Scraper

```bash
python main.py
```

### Step 6: Follow the Prompts

**Prompt 1**: Enter URL

```text
Enter URL: https://www.example.com
```

**Prompt 2**: Choose Mode

```text
Dynamic? (y/n): n
```

| Choose | Purpose                                      |
|--------|----------------------------------------------|
| `n`    | Simple HTML website (faster)                 |
| `y`    | JavaScript-heavy site (slower)               |

**Prompt 3 (Optional)**: Authentication

```text
Need authentication? (y/n): n
```

Only appears if you chose `y` for Dynamic mode.

### Step 7: Check Results

```bash
# Windows Explorer
output/

# Or via PowerShell
cd output
dir
```

You should see:

- ✅ output.xlsx
- ✅ output.json
- ✅ output.pdf
- ✅ output.txt
- ✅ output.html
- ✅ page.png

---

## 🎯 3 Common Scenarios

### Scenario 1: Scrape Simple Website

**Goal**: Get data from basic HTML site  
**Time**: ~5 seconds

```bash
python main.py
# URL: https://example.com
# Dynamic: n
# Done! Check output/
```

### Scenario 2: Scrape JavaScript Site (No Login)

**Goal**: Scrape React/Vue/Angular app  
**Time**: ~15 seconds

```bash
python main.py
# URL: https://example.com
# Dynamic: y
# Need auth: n
# Done! Check output/
```

### Scenario 3: Scrape Protected Site (With Login)

**Goal**: Scrape page behind login  
**Time**: ~20 seconds

```bash
python main.py
# URL: https://example.com/dashboard
# Dynamic: y
# Need auth: y
# Username: myusername
# Password: mypassword
# Done! Check output/
```

---

## 📁 Understanding the Output Files

After running, you'll have these files in `output/` folder:

| File | Open With | Best For |
| ------ | ----------- | ---------- |
| `output.xlsx` | Excel / Google Sheets | Data analysis |
| `output.json` | Text editor / Code editor | APIs / Processing |
| `output.pdf` | PDF Reader | Sharing / Printing |
| `output.txt` | Notepad / Text editor | Quick reading |
| `output.html` | Web browser | Complete information |
| `page.png` | Image viewer | Visual reference |

---

## ⚠️ Troubleshooting Quick Tips

| Problem | Solution |
| --------- | ---------- |
| **Python not found** | [Install Python 3.8+](https://python.org) |
| **Module not found** | `pip install -r requirements.txt` |
| **Chrome error** | Update Chrome browser |
| **Timeout error** | Website slow / internet issue |
| **Login fails** | Try without login / check credentials |

---

## 🚀 Next Steps

Once you understand the basics:

1. **Read README.md** - Full documentation
2. **Read LOGIC.md** - How it works
3. **Read ARCHITECTURE.md** - Visual diagrams
4. **Customize** - Modify for your needs

---

## 💡 Pro Tips

✅ **Use Static mode first** - It's faster and more reliable  
✅ **Test with example.com** - Safe, doesn't change  
✅ **Check robots.txt** - Before scraping any site  
✅ **Use dynamic mode only when needed** - JS sites only  
✅ **Save the outputs** - Before running again (they overwrite)

---

## 🆘 Help

- **Installation issues**: Check README.md → Troubleshooting
- **How it works**: Check LOGIC.md
- **Visual diagrams**: Check ARCHITECTURE.md
- **Advanced usage**: Check README.md → Advanced Configuration

---

**Version**: Quick Start 1.0  
**Status**: ✅ Ready to Use
