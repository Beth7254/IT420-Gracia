# Final Mission:
# Produce a Security Analyst Report.

print()
print("====================================")
print("       PHISHING EMAIL DETECTOR")
print("====================================")

emails = [
    "Your account will expire today. Click here to verify your account immediately.",
    "Hi Alvin, your Week 5 activity is missing. Please review your submission here: [LINK]. I need to finalize the grades today.",
    "Congratulations! You Won! You have won ₱50,000. Send your account information to claim your prize."
]

for email in emails:
    score = 0

    print()
    print("Email:")
    print(email)
    print()
    print("INDICATORS FOUND")
    print("------------------------------------")

    for word in suspicious_words:
        if word in email.lower():
            print("[!] " + word)
            score += 1

    for rule in new_rules:
        if rule in email.lower():
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

    if "alvin" in email.lower():
        print("POSSIBLE ATTACK: Spear Phishing")
    else:
        print("POSSIBLE ATTACK: Phishing")

    print()
    print("RECOMMENDATION:")
    print("Do not click suspicious links or share personal information.")
    print()
    print("====================================")