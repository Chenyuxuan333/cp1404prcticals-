"""
Estimate: 20 minutes
Actual: 15 minutes
"""


def main():
    email_to_name = {}

    while True:
        email = input("Email: ").strip()
        if not email:
            break

        name = extract_name(email)
        if input(f"Is your name {name}? (Y/n) ").strip().lower() not in ("y", ""):
            name = input("Enter your name: ").strip()

        email_to_name[email] = name

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_name(email):
    """Extract a formatted name from the given email address."""
    name_part = email.split("@")[0]
    name = " ".join(name_part.replace("_", " ").split(".")).title()
    return name


if __name__ == "__main__":
    main()