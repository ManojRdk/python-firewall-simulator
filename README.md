# 🛡️ Python Firewall Simulator

A simple Python project that simulates how a firewall processes incoming network traffic based on predefined rules.

## 📖 Overview

This project randomly generates IP addresses and checks whether each IP should be **Allowed** or **Blocked** according to firewall rules defined in the program.

It is a beginner-friendly project for understanding basic firewall concepts and Python programming.

---

## 🚀 Features

- Generates random IP addresses
- Simulates firewall filtering
- Blocks specific IP addresses
- Allows all other IP addresses
- Generates a random request ID for each connection
- Easy to customize firewall rules

---

## 🛠️ Technologies Used

- Python 3
- Random Module

---

## 📂 Project Structure

```
firewall.py
README.md
```

---

## ⚙️ How It Works

1. A random IP address is generated.
2. The firewall checks whether the IP exists in the blocked IP list.
3. If the IP is found:
   - ❌ Block
4. Otherwise:
   - ✅ Allow
5. A random request number is generated and displayed.

Example Output:

```
IP: 191.162.1.7, Action: Block, Random_Number: 5831
IP: 191.162.1.10, Action: Allow, Random_Number: 1245
IP: 191.162.1.18, Action: Block, Random_Number: 7923
```

---

## ▶️ Running the Project

Clone the repository:

```bash
git clone https://github.com/your-username/python-firewall-simulator.git
```

Navigate into the project folder:

```bash
cd python-firewall-simulator
```

Run the program:

```bash
python firewall.py
```

## 👨‍💻 Author

Built as part of my Cybersecurity & Python learning journey.
