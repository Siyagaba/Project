from datetime import datetime
import smtplib
from email.mime.text import MIMEText

# 🔹 Toggle email ON/OFF
SEND_EMAIL = False   # change to True if you want email

# 🔹 STEP 1: Generate report
def generate_report():
    return f"""
    <html>
    <body style="font-family: Arial; padding:20px;">
        <h2>📊 Metadata Health Report</h2>
        <p>Date: {datetime.now().strftime('%Y-%m-%d')}</p>

        <h3>Data Quality</h3>
        <ul>
            <li>Domain A: 98%</li>
            <li>Domain B: 95%</li>
        </ul>

        <h3>Stale Assets</h3>
        <ul>
            <li>table1</li>
            <li>table2</li>
        </ul>

        <h3>Anomalies</h3>
        <ul>
            <li>Null spike detected</li>
        </ul>
    </body>
    </html>
    """

# 🔹 STEP 2: Save report
def save_report(report):
    with open("report.html", "w") as file:
        file.write(report)
    print("✅ Report saved as report.html")

# 🔹 STEP 3: Send email (optional)
def send_email(report):
    EMAIL = "your_email@gmail.com"
    PASSWORD = "your_app_password"
    TO = "your_email@gmail.com"

    msg = MIMEText(report, "html")
    msg["Subject"] = "Metadata Report"
    msg["From"] = EMAIL
    msg["To"] = TO

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(EMAIL, PASSWORD)
            server.send_message(msg)

        print("📧 Email sent successfully!")

    except Exception as e:
        print("❌ Email failed:", e)

# 🔹 MAIN
if __name__ == "__main__":
    report = generate_report()
    save_report(report)

    if SEND_EMAIL:
        send_email(report)
    else:
        print("📭 Email sending is OFF (demo mode)")