import json
import xml.etree.ElementTree as ET
from itertools import permutations

def generate_email_patterns(first_name, last_name, domain):
    """
    Generates a list of email patterns based on the first name, last name, and domain.
    
    :param first_name: The first name of the user.
    :param last_name: The last name of the user.
    :param domain: The domain name (e.g., example.com).
    :return: A list of generated email patterns.
    """
    # Convert names to lowercase for consistency
    first_name = first_name.lower()
    last_name = last_name.lower()
    domain = domain.lower()

    # Extract initials
    first_initial = first_name[0]
    last_initial = last_name[0]

    # Generate a wide variety of email patterns
    email_patterns = [
        # Basic patterns
        f"{first_name}@{domain}",                     # john@example.com
        f"{last_name}@{domain}",                      # doe@example.com
        f"{first_name}.{last_name}@{domain}",         # john.doe@example.com
        f"{first_name}_{last_name}@{domain}",         # john_doe@example.com
        f"{first_name}-{last_name}@{domain}",         # john-doe@example.com
        f"{first_name}{last_name}@{domain}",          # johndoe@example.com
        f"{last_name}.{first_name}@{domain}",         # doe.john@example.com
        f"{last_name}{first_name}@{domain}",          # doejohn@example.com
        f"{first_initial}{last_name}@{domain}",       # jdoe@example.com
        f"{first_initial}.{last_name}@{domain}",      # j.doe@example.com
        f"{first_name}{last_initial}@{domain}",       # john.d@example.com
        f"{first_name}.{last_initial}@{domain}",      # john.d@example.com
        f"{first_initial}{last_initial}@{domain}",    # jd@example.com
        f"{first_initial}.{last_initial}@{domain}",   # j.d@example.com

        # Patterns with numbers
        f"{first_name}1@{domain}",                    # john1@example.com
        f"{first_name}123@{domain}",                  # john123@example.com
        f"{first_name}.{last_name}1@{domain}",        # john.doe1@example.com
        f"{first_name}_{last_name}123@{domain}",      # john_doe123@example.com
        f"{first_name}{last_name}2025@{domain}",     # johndoe2023@example.com
        f"{first_initial}{last_name}99@{domain}",    # jdoe99@example.com

        # Patterns with reversed names
        f"{last_name}.{first_name}1@{domain}",       # doe.john1@example.com
        f"{last_name}{first_name}2025@{domain}",      # doejohn2023@example.com

        # Patterns with separators and initials
        f"{first_name}-{last_initial}@{domain}",     # john-d@example.com
        f"{first_initial}-{last_name}@{domain}",     # j-doe@example.com
        f"{first_initial}_{last_name}@{domain}",      # j_doe@example.com
        f"{first_name}_{last_initial}@{domain}",      # john_d@example.com

        # Patterns with multiple initials
        f"{first_initial}{last_initial}1@{domain}",  # jd1@example.com
        f"{first_initial}.{last_initial}2023@{domain}",  # j.d2023@example.com

        # Patterns with mixed case (optional)
        f"{first_name.capitalize()}{last_name.capitalize()}@{domain}",  # JohnDoe@example.com
        f"{first_name.capitalize()}.{last_name.capitalize()}@{domain}",  # John.Doe@example.com

        # Patterns with middle initials (if provided)
        # Assuming middle name is not provided, but you can add it if needed
    ]

    # Add more patterns using permutations and combinations
    separators = [".", "_", "-", ""]
    for sep in separators:
        email_patterns.append(f"{first_name}{sep}{last_name}@{domain}")  # john.doe@example.com, john_doe@example.com, etc.
        email_patterns.append(f"{first_initial}{sep}{last_name}@{domain}")  # j.doe@example.com, j_doe@example.com, etc.
        email_patterns.append(f"{first_name}{sep}{last_initial}@{domain}")  # john.d@example.com, john_d@example.com, etc.

    # Add patterns with numbers and separators
    for i in range(1, 10):
        email_patterns.append(f"{first_name}{sep}{last_name}{i}@{domain}")  # john.doe1@example.com, john_doe2@example.com, etc.
        email_patterns.append(f"{first_initial}{sep}{last_name}{i}@{domain}")  # j.doe1@example.com, j_doe2@example.com, etc.

    # Add patterns with reversed names and separators
    for sep in separators:
        email_patterns.append(f"{last_name}{sep}{first_name}@{domain}")  # doe.john@example.com, doe_john@example.com, etc.
        email_patterns.append(f"{last_name}{sep}{first_initial}@{domain}")  # doe.j@example.com, doe_j@example.com, etc.

    # Add patterns with mixed separators and numbers
    for i in range(1, 10):
        email_patterns.append(f"{first_name}{i}{sep}{last_name}@{domain}")  # john1.doe@example.com, john2_doe@example.com, etc.
        email_patterns.append(f"{first_initial}{i}{sep}{last_name}@{domain}")  # j1.doe@example.com, j2_doe@example.com, etc.

    # Ensure at least 100 patterns
    while len(email_patterns) < 100:
        for i in range(10, 100):
            email_patterns.append(f"{first_name}{i}@{domain}")  # john10@example.com, john11@example.com, etc.
            email_patterns.append(f"{last_name}{i}@{domain}")  # doe10@example.com, doe11@example.com, etc.
            email_patterns.append(f"{first_name}{sep}{last_name}{i}@{domain}")  # john.doe10@example.com, john_doe11@example.com, etc.

    # Remove duplicates (if any)
    email_patterns = list(set(email_patterns))

    return email_patterns


def save_to_txt(email_patterns, filename):
    """
    Saves the email patterns to a .txt file.
    
    :param email_patterns: List of email patterns.
    :param filename: Name of the output file.
    """
    with open(filename, "w") as file:
        for email in email_patterns:
            file.write(email + "\n")
    print(f"Email patterns saved to {filename}")


def save_to_json(email_patterns, filename):
    """
    Saves the email patterns to a .json file.
    
    :param email_patterns: List of email patterns.
    :param filename: Name of the output file.
    """
    data = {"email_patterns": email_patterns}
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)
    print(f"Email patterns saved to {filename}")


def save_to_xml(email_patterns, filename):
    """
    Saves the email patterns to a .xml file.
    
    :param email_patterns: List of email patterns.
    :param filename: Name of the output file.
    """
    root = ET.Element("EmailPatterns")
    for email in email_patterns:
        ET.SubElement(root, "Email").text = email
    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)
    print(f"Email patterns saved to {filename}")


def main():
    # Display author information
    print("\n" + "=" * 60)
    print("Email Pattern Generator".center(60))
    print("Developed by (n3rdh4x0r)".center(60))
    print("=" * 60)

    # Take inputs one by one
    print("Enter the following details:")
    first_name = input("First Name: ").strip()
    last_name = input("Last Name: ").strip()
    domain = input("Domain Name (e.g., example.com): ").strip()

    # Generate email patterns
    email_patterns = generate_email_patterns(first_name, last_name, domain)

    # Ask for file format to save
    print("\nChoose a file format to save the email patterns:")
    print("1. Save as .txt")
    print("2. Save as .json")
    print("3. Save as .xml")
    choice = input("Choose an option (1/2/3): ").strip()

    if choice == "1":
        save_to_txt(email_patterns, "email_patterns.txt")
    elif choice == "2":
        save_to_json(email_patterns, "email_patterns.json")
    elif choice == "3":
        save_to_xml(email_patterns, "email_patterns.xml")
    else:
        print("Invalid choice. No file saved.")


if __name__ == "__main__":
    main()
