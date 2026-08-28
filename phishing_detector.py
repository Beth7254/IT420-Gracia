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

for word in suspicious_words:
    if word in email_text:
        print("[!] " + word)

# Mission 4:
# Calculate the risk score.

# Mission 5:
# Test multiple emails.

# Mission 6:
# Add spear-phishing indicators.

# Mission 7:
# Add at least three new detection rules.

# Final Mission:
# Produce a Security Analyst Report.