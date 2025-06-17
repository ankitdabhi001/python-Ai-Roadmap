import schedule
import time
import smtplib as s
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def job():
    print("🚀 Job running: Sending email...")

    # Connect to Gmail
    ob = s.SMTP('smtp.gmail.com', 587)
    ob.starttls()
    ob.login("a1000aje@gmail.com", 'zbvh aidd ahgv vqzh')  # App password

    # Email content
    sub = "[NOTICE] ₹5,837.00 Debited for HF Deluxe Bike Insurance"
    ss = "Nikul Jambukiya"
    body = f"""Dear Customer, {ss}

We are pleased to inform you that your Premium Bike Insurance has been activated successfully.

Vehicle: HF Deluxe (Honda)  
Policy Start Date: Today  
Amount Debited: ₹5,837.00  
Policy No: HF420LOL-INZ  
Coverage: Full body, engine, tire air, and horn sound

Your bike is now protected against:
-> Accidental skids while showing off  
-> Engine trauma from over-speeding at 40 km/h  
-> Damage caused by jealous friends sitting without asking  
-> Theft by aliens (with terms & conditions)

If this insurance was not initiated by you:
1. Send “WHY HF?!” to our WhatsApp bot  
2. Visit our branch in Kanchanpur Nagar (only open on Tuesdays from 3 AM to 4 AM)  
3. Try not to panic. The bike loves you.

Sincerely,  
SafeRide™ Auto Insurance Pvt. Ltd.  
“Insuring riders who don’t insure themselves.”
"""

    # Compose email
    msg = MIMEMultipart()
    msg['From'] = "a1000aje@gmail.com"
    msg['To'] = "nikuljambukiya0@gmail.com"
    msg['Subject'] = sub
    msg.attach(MIMEText(body, 'plain', 'utf-8'))

    # Send email
    ob.sendmail(msg['From'], msg['To'], msg.as_string())
    ob.quit()
    print("✅ Email sent successfully.")

# 🕒 Schedule Setup — keep outside the function!
schedule.every(3).seconds.do(job)
# schedule.every().minute.at(":20").do(job)  # Optional: run every minute at :20 seconds

# 🔁 Keep script running
while True:
    schedule.run_pending()
    time.sleep(1)
