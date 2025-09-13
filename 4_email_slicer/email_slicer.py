def is_valid_email(email: str) -> bool:
    """
    Checks if the provided email is valid.
    """
    if email.count("@") == 1:
        email_splited = email.split("@")
        if "." in email_splited[1]:
            domain_splited = email_splited[1].split(".")
            if (
                len(email_splited[0]) > 0
                and len(domain_splited[0]) > 0
                and len(domain_splited[1]) > 0
            ):
                return True
    return False


def get_valid_email() -> str:
    """
    Prompts the user for a valid email address.
    """
    while True:
        email = input("Enter the email: ").strip()
        if is_valid_email(email):
            return email
        print("This Email is Invalid !!")


def slice_email(email: str) -> dict:
    """
    Slices the email into username, domain name, and TLD.
    """
    username, domain = email.split("@")
    domain_name, tld = domain.split(".", 1)
    return {
        "username": username,
        "domain_name": domain_name,
        "tld": tld,
    }


def email_details(email_parts: dict) -> str:
    """
    Formats the email details for display.
    """
    return (
        f"Username: {email_parts['username']}\n"
        f"Domain Name: {email_parts['domain_name']}\n"
        f"TLD: {email_parts['tld']}"
    )


def main():
    print("Welcome to the Email Slicer.")
    while True:
        email = get_valid_email()
        email_parts = slice_email(email)
        details = email_details(email_parts)
        print("--------------------\nYOUR EMAIL DETAILS\n--------------------")
        print(details)
        print("--------------------")
        should_exit = input("Do you want to exit? (Y/N): ")
        if should_exit.strip().lower() == "y":
            break
    print("Thank you for using my app\n made with 🖤 by Majed Abumathkour")


if __name__ == "__main__":
    main()
