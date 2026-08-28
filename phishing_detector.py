# PHISHING DETECTOR — STARTER FILE
# Your job: complete the program through the missions.
# Do not delete this comment. Add your own code below.

sender = ""
subject = ""
email_body = ""


# Mission 2:
# Display the email information.

print()
sender = "no-reply@pnb.com.ph"
subject = "It's All About YOU Today - Warm Birthday Greetings from PNB"
email_body = "Celebrate the gift of life with a gift from us. when you use your PNB Credit, Debit, or Prepaid Card!"

print("Email for Today!")
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

print("SUSPICIOUS INDICATORS")

suspicious_words = [
    "urgent",
    "verify",
    "password",
    "click",
    "suspended",
    "immediately"
]

print()

email_text = (subject + " " + email_body).lower()
risk_score = 0

print()

for word in suspicious_words:
    if word in email_text:
        print("[!] " + word)
        risk_score += 1

print()


# Mission 4:
# Calculate the risk score.

print("RISK SCORE")

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

[LINKNI SIYA]

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
    print("[!] DeadlineNi?")

print()


# Mission 7:
# Add at least three new detection rules.

print("IMPROVED PHISHING DETECTOR")

score = 0

new_rules = [
    "account information",
    "[link]",
    "won"
]

for rule in new_rules:
    if rule in targeted_text:
        print("[!] " + rule)
        score += 1
        
for word in suspicious_words:
    if word in targeted_text:
        print("[!] " + word)
        score += 1

print("RISK SCORE:", score)

if score <= 1:
    print("RISK LEVEL: LOW")
    print("RECOMMENDATION: Email appears low risk, but stay careful.")
elif score <= 3:
    print("RISK LEVEL: MEDIUM")
    print("RECOMMENDATION: Be careful and verify the sender.")
else:
    print("RISK LEVEL: HIGH")
    print("RECOMMENDATION: Do not click links or provide information.")


# Final Mission:
# Produce a Security Analyst Report.

print()
print("====================================")
print("       PHISHING EMAIL DETECTOR")
print("====================================")

sender = "maria.santos@school-example.com"

subject = "Important: Missing ITE 403 Activity"

email_body = """
Hi Alvin,

Your ITE 403 Week 5 activity is missing.
Please click the link to verify your account immediately.

[link ni]

I need to check your submission today.

Thank you,
Dr. Maria Santos
"""

email_text = (subject + " " + email_body).lower()

score = 0

print()
print("Sender:")
print(sender)

print()
print("Subject:")
print(subject)

print()
print("INDICATORS FOUND")
print("------------------------------------")

for word in suspicious_words:
    if word in email_text:
        print("[!] " + word)
        score += 1

for rule in new_rules:
    if rule in email_text:
        print("[!] " + rule)
        score += 1

print()
print("RISK SCORE:", score)

if score <= 1:
    print("RISK LEVEL: LOW")
elif score <= 3:
    print("RISK LEVEL: MEDIUM")
else:
    print("RISK LEVEL: HIGH")

print()

if "alvin" in email_text:
    print("POSSIBLE ATTACK: Spear Phishing")
else:
    print("POSSIBLE ATTACK: Phishing")

print()
print("RECOMMENDATION:")
print("Do not click the link. Verify the sender first.")

print()
print("====================================")