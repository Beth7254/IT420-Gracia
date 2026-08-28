# PHISHING DETECTOR — STARTER FILE
# Your job: complete the program through the missions.
# Do not delete this comment. Add your own code below.

sender = ""
subject = ""
email_body = ""

# Mission 2:
# Display the email information.
title= ""
sender = "no-reply@pnb.com.ph"
subject = "It's All About YOU Today - Warm Birthday Greetings from PNB"
email_body = "Celebrate the gift of life with a gift from us. when you use your PNB Credit, Debit, or Prepaid Card!"


print("Email")
print(title)
print()

print("Sender")
print(sender)
print()

print("Subject")
print(subject)
print()

print("Body")
print(email_body)
print()

# Mission 3:
# Detect suspicious words.

suspicious_words = [
    "urgent",
    "verify",
    "password",
    "click",
    "suspended",
    "immediately"
]

print("SUSPICIOUS INDICATORS")
print()

email_text = (subject + " " + email_body).lower()

risk_score = 0

for word in suspicious_words:
    if word in email_text:
        print("[!] " + word)
        risk_score += 1

# Mission 4:
# Calculate the risk score.

if risk_score <= 1:
    risk_level = "LOW"
elif risk_score <= 3:
    risk_level = "MEDIUM"
else:
    risk_level = "HIGH"

print()
print("RISK SCORE:", risk_score)
print("RISK LEVEL:", risk_level)
print()

# Mission 5:
# Test multiple emails.

print()
print("MULTIPLE EMAIL CHECKER")

print()
emails = [
    "Your account will expire today. Click here to verify your account immediately.",
    "ITE 403 Week 5 Submission. Please review your submission before 3 PM.",
    "Congratulations! You Won! You have won ₱50,000. Send your account information to claim your prize."
]

for email in emails:
    score = 0

    print("EMAIL")
    print(email)

    for word in suspicious_words:
        if word in email.lower():
            print("[!] " + word)
            score += 1

    print("RISK SCORE:", score)

    if score <= 1:
        print("RISK LEVEL: LOW")
    elif score <= 3:
        print("RISK LEVEL: MEDIUM")
    else:
        print("RISK LEVEL: HIGH")

    print()


# Mission 6:
# Add spear-phishing indicators.

targeted_email = """
Hi Alvin,

I'm checking the submissions for our ITE 403 class.
Your Week 5 activity appears to be missing from the submission list.
Please review your submission here:

[LINK]

I need to finalize the grades today.

Thank you,

Dr. Maria Santos
"""

print("SPEAR-PHISHING ANALYSIS")
print()

targeted_text = targeted_email.lower()

if "alvin" in targeted_text:
    print("[!] Name")

if "today" in targeted_text:
    print("[!] Deadline ata?")
    
print()

# Mission 7:
# Add at least three new detection rules.

# Final Mission:
# Produce a Security Analyst Report.