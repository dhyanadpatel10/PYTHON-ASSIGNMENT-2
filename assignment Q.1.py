import re
from collections import defaultdict

def extract_emails(file_path):
    # Regex pattern for valid emails with com, edu, org
    pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.(com|edu|org)\b')

    domain_users = defaultdict(set)

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            matches = pattern.findall(line)
            # re.findall returns only the TLD group if not careful, so use re.finditer
            for match in re.finditer(pattern, line):
                email = match.group(0).lower()
                domain = email.split("@")[1]
                domain_users[domain].add(email)

    # Print results in lexicographic order of domain
    for domain in sorted(domain_users.keys()):
        emails = sorted(domain_users[domain])
        print(domain, len(emails), emails[0])


# ---------------- SAMPLE INPUT FILE ----------------
# Save this as "emails.txt" before running
"""
Hello, please contact us at support@techworld.com or admin@school.edu.
Invalid email: user@@wrong.com should be ignored.
Reach out to test_user@open.org and support@techworld.com again.
Another one: hello.world@school.edu
"""

# Run the function
extract_emails("emails.txt")
