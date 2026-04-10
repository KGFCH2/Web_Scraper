import pandas as pd
import json
from fpdf import FPDF
import os
import base64

def export_excel(data):
    os.makedirs("output", exist_ok=True)
    df = pd.DataFrame(dict([(k, pd.Series(v)) for k, v in data.items()]))
    df.to_excel("output/output.xlsx", index=False)

def export_json(data):
    os.makedirs("output", exist_ok=True)
    with open("output/output.json", "w") as f:
        json.dump(data, f, indent=4)

def export_pdf(data):
    os.makedirs("output", exist_ok=True)
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.set_text_color(0, 51, 102)  # Darker blue title
    pdf.cell(190, 15, txt="WEB SCRAPING REPORT", ln=True, align='C')
    pdf.set_font("Arial", "I", 8)
    pdf.set_text_color(128, 128, 128)
    pdf.cell(190, 10, txt="Generated on: " + pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S'), ln=True, align='R')
    pdf.ln(5)

    pdf.set_font("Arial", size=10)
    pdf.set_text_color(0, 0, 0)  # Black text

    for key, values in data.items():
        if not values: continue
        
        safe_key = key.replace('_', ' ').upper().encode('latin-1', 'replace').decode('latin-1')
        pdf.set_font("Arial", "B", 11)
        pdf.set_fill_color(220, 230, 241)  # Light blue background for headers
        pdf.set_text_color(0, 51, 102)
        pdf.cell(0, 8, txt=" " + safe_key, ln=True, fill=True)
        pdf.ln(2)
        
        pdf.set_font("Arial", size=9)
        pdf.set_text_color(30, 30, 30)
        pdf.set_fill_color(255, 255, 255)

        if isinstance(values, list):
            for i, v in enumerate(values[:50]): # Increased limit to 50
                safe_v = str(v).strip().encode('latin-1', 'replace').decode('latin-1')
                if not safe_v: continue
                
                # Check for page break
                if pdf.get_y() > 270:
                    pdf.add_page()
                
                pdf.set_font("Arial", "B", 9)
                pdf.write(5, f" {i+1}. ")
                pdf.set_font("Arial", size=9)
                pdf.multi_cell(0, 5, txt=safe_v)
                pdf.ln(1)
        else:
            safe_v = str(values).strip().encode('latin-1', 'replace').decode('latin-1')
            pdf.multi_cell(0, 5, txt=safe_v)
            pdf.ln(3)

        pdf.ln(4)

    pdf.output("output/output.pdf")

def export_txt(data):
    os.makedirs("output", exist_ok=True)
    with open("output/output.txt", "w", encoding='utf-8') as f:
        f.write("Web Scraping Report\n")
        f.write("=" * 50 + "\n\n")
        for key, values in data.items():
            f.write(f"{key.replace('_', ' ').title()}:\n")
            if isinstance(values, list):
                for v in values[:50]:
                    f.write(f"- {v}\n")
            else:
                f.write(f"{values}\n")
            f.write("\n")

def export_html(data, html_content=None):
    os.makedirs("output", exist_ok=True)
    with open("output/output.html", "w", encoding='utf-8') as f:
        f.write("<!DOCTYPE html>\n<html lang='en'>\n<head>\n")
        f.write("<meta charset='UTF-8'>\n")
        f.write("<meta name='viewport' content='width=device-width, initial-scale=1.0'>\n")
        f.write("<link rel='apple-touch-icon' href='data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNkYPhfDwAChwGA60e6kgAAAABJRU5ErkJggg=='>\n")
        f.write("<title>Web Scraping Report</title>\n")
        f.write("<style>\n")
        f.write("body { font-family: Arial, sans-serif; margin: 20px; }\n")
        f.write("h1 { color: #0066CC; }\n")
        f.write("h2 { color: #333; border-bottom: 1px solid #ccc; padding-bottom: 5px; }\n")
        f.write("ul { margin: 10px 0; }\n")
        f.write("li { margin: 5px 0; }\n")
        f.write("pre { background: #f0f0f0; padding: 10px; border: 1px solid #ccc; overflow-x: auto; white-space: pre-wrap; word-wrap: break-word; }\n")
        f.write("</style>\n")
        f.write("</head>\n<body>\n")
        f.write("<h1>Web Scraping Report</h1>\n")
        for key, values in data.items():
            f.write(f"<h2>{key.replace('_', ' ').title()}</h2>\n")
            if isinstance(values, list):
                f.write("<ul>\n")
                for v in values:
                    f.write(f"<li>{v}</li>\n")
                f.write("</ul>\n")
            else:
                f.write(f"<p>{values}</p>\n")
        if html_content:
            f.write("<h2>Full HTML Content</h2>\n<pre>")
            # Strip HTML structure tags and sanitize to avoid diagnostic issues
            import re
            sanitized_html = re.sub(r'<html[^>]*>.*?</html>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
            sanitized_html = re.sub(r'<head[^>]*>.*?</head>', '', sanitized_html, flags=re.DOTALL | re.IGNORECASE)
            sanitized_html = re.sub(r'<body[^>]*>', '', sanitized_html, flags=re.IGNORECASE)
            sanitized_html = re.sub(r'</body>', '', sanitized_html, flags=re.IGNORECASE)
            sanitized_html = re.sub(r'<meta[^>]*>', '', sanitized_html, flags=re.IGNORECASE)
            sanitized_html = re.sub(r'<link[^>]*>', '', sanitized_html, flags=re.IGNORECASE)
            sanitized_html = re.sub(r'<style[^>]*>.*?</style>', '', sanitized_html, flags=re.DOTALL | re.IGNORECASE)
            sanitized_html = re.sub(r'<script[^>]*>.*?</script>', '', sanitized_html, flags=re.DOTALL | re.IGNORECASE)
            sanitized_html = re.sub(r'style="[^"]*"', '', sanitized_html)
            sanitized_html = re.sub(r'style=\'[^"]*\'', '', sanitized_html)
            f.write(sanitized_html.strip())
            f.write("</pre>\n")
        f.write("</body>\n</html>")

def export_full_pdf(driver):
    """Export full webpage as PDF with styles using Selenium"""
    try:
        from selenium.webdriver.common.print_page_options import PrintOptions
        print_options = PrintOptions()
        pdf_data = driver.execute_cdp_cmd('Page.printToPDF', {})
        with open("output/full_page.pdf", "wb") as f:
            f.write(base64.b64decode(pdf_data['data']))
        print("Full page PDF saved")
    except Exception as e:
        print("Failed to export full PDF:", e)

def export_screenshot(url=None):
    """Export webpage screenshot. 
    Screenshot is already captured during fetch_dynamic/fetch_static_screenshot.
    This function can optionally capture additional screenshots if URL is provided.
    """
    import os
    output_file = "output/page.png"
    if os.path.exists(output_file):
        print(f"✓ Webpage screenshot available: {output_file}")
    else:
        print(f"⚠ Screenshot not found at {output_file}")