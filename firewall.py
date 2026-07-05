import random


def generate_ip_address():
    return f"191.162.1.{random.randint(1, 20)}"


def check_firewall(ip_address, firewall_rules):
    return firewall_rules.get(ip_address, "Allow")


def main():
    firewall_rules = {
        "191.162.1.2": "Block",
        "191.162.1.5": "Block",
        "191.162.1.12": "Block",
        "191.162.1.18": "Block",
        "191.162.1.7": "Block",
    }

    for _ in range(20):
        ip_address = generate_ip_address()
        action = check_firewall(ip_address, firewall_rules)
        random_number=random.randint(1,9999)
        print(f"IP:{ip_address},Action: {action},Random_Number:{random_number}")


if __name__ == "__main__":
    main()
