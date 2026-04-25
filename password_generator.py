import random
import string


LOWERCASE = string.ascii_lowercase
UPPERCASE = string.ascii_uppercase
DIGITS    = string.digits
SYMBOLS   = "!@#$%^&*()_+-=[]{}?"


def generate_password(length, use_upper, use_digits, use_symbols):
    char_pool = LOWERCASE

    if use_upper:
        char_pool += UPPERCASE
    if use_digits:
        char_pool += DIGITS
    if use_symbols:
        char_pool += SYMBOLS

    if not char_pool:
        char_pool = LOWERCASE

    required = []
    required.append(random.choice(LOWERCASE))

    if use_upper:
        required.append(random.choice(UPPERCASE))
    if use_digits:
        required.append(random.choice(DIGITS))
    if use_symbols:
        required.append(random.choice(SYMBOLS))

    remaining_length = length - len(required)
    rest = [random.choice(char_pool) for _ in range(remaining_length)]

    all_chars = required + rest
    random.shuffle(all_chars)

    password = "".join(all_chars)
    return password


def check_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if len(password) >= 16:
        score += 1

    if any(c in LOWERCASE for c in password):
        score += 1
    if any(c in UPPERCASE for c in password):
        score += 1
    if any(c in DIGITS for c in password):
        score += 1
    if any(c in SYMBOLS for c in password):
        score += 1

    if score <= 3:
        return "WEAK  ⚠️ "
    elif score <= 5:
        return "MEDIUM ⚡"
    else:
        return "STRONG ✅"


def ask_yes_no(question):
    while True:
        answer = input(question).strip().lower()
        if answer in ("y", "yes"):
            return True
        elif answer in ("n", "no"):
            return False
        else:
            print("  Please type y or n.")


def ask_number(question, min_val, max_val):
    while True:
        try:
            value = int(input(question).strip())
            if min_val <= value <= max_val:
                return value
            else:
                print(f"  Please enter a number between {min_val} and {max_val}.")
        except ValueError:
            print("  That's not a valid number. Try again.")


def show_password(password, index=None):
    strength = check_strength(password)
    label    = f"Password {index}" if index else "Password"
    print(f"\n  {label}: {password}")
    print(f"  Strength : {strength}")
    print(f"  Length   : {len(password)} characters")


def main():
    print("=" * 50)
    print("        🔐 PASSWORD GENERATOR 🔐")
    print("=" * 50)

    while True:
        print("\n--- Settings ---")

        length = ask_number("Password length (6-64): ", 6, 64)
        use_upper   = ask_yes_no("Include UPPERCASE letters? (y/n): ")
        use_digits  = ask_yes_no("Include NUMBERS?          (y/n): ")
        use_symbols = ask_yes_no("Include SYMBOLS (!@#...)?  (y/n): ")
        count = ask_number("How many passwords to generate? (1-10): ", 1, 10)

        print("\n" + "=" * 50)
        print("  YOUR GENERATED PASSWORDS")
        print("=" * 50)

        for i in range(count):
            pwd = generate_password(length, use_upper, use_digits, use_symbols)
            label = i + 1 if count > 1 else None
            show_password(pwd, label)

        print("\n" + "=" * 50)

        again = ask_yes_no("\nGenerate more passwords? (y/n): ")
        if not again:
            print("\n  Stay safe out there! 🔐")
            print("  Tip: Use a password manager to store these.\n")
            break


if __name__ == "__main__":
    main()
