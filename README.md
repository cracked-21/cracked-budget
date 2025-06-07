# 💸 cracked-budget CLI Tracker

```
  /$$$$$$  /$$$$$$$   /$$$$$$   /$$$$$$  /$$   /$$ /$$$$$$$$ /$$$$$$$          /$$$$$$$  /$$   /$$ /$$$$$$$   /$$$$$$  /$$$$$$$$ /$$$$$$$$
 /$$__  $$| $$__  $$ /$$__  $$ /$$__  $$| $$  /$$/| $$_____/| $$__  $$        | $$__  $$| $$  | $$| $$__  $$ /$$__  $$| $$_____/|__  $$__/
| $$  \__/| $$  \ $$| $$  \ $$| $$  \__/| $$ /$$/ | $$      | $$  \ $$        | $$  \ $$| $$  | $$| $$  \ $$| $$  \__/| $$         | $$   
| $$      | $$$$$$$/| $$$$$$$$| $$      | $$$$$/  | $$$$$   | $$  | $$ /$$$$$$| $$$$$$$ | $$  | $$| $$  | $$| $$ /$$$$| $$$$$      | $$   
| $$      | $$__  $$| $$__  $$| $$      | $$  $$  | $$__/   | $$  | $$|______/| $$__  $$| $$  | $$| $$  | $$| $$|_  $$| $$__/      | $$   
| $$    $$| $$  \ $$| $$  | $$| $$    $$| $$\  $$ | $$      | $$  | $$        | $$  \ $$| $$  | $$| $$  | $$| $$  \ $$| $$         | $$   
|  $$$$$$/| $$  | $$| $$  | $$|  $$$$$$/| $$ \  $$| $$$$$$$$| $$$$$$$/        | $$$$$$$/|  $$$$$$/| $$$$$$$/|  $$$$$$/| $$$$$$$$   | $$   
 \______/ |__/  |__/|__/  |__/ \______/ |__/  \__/|________/|_______/         |_______/  \______/ |_______/  \______/ |________/   |__/   
```

Cracked Budget is a **feature-complete** command-line app for tracking income, expenses, and logs using labeled buckets. Built to be simple, functional, and fast — with no unnecessary bloat.

---

## 📦 Features

- ✅ Add, rename, delete financial buckets
- 💰 Log income and expense transactions
- 📝 Add logs (non-financial notes)
- 📊 View current bucket balances
- 🔁 Move funds between buckets
- 🧾 View all transaction history
- 🕒 Modify transaction timestamps
- 💾 Autosaves to `cracked_budget.json`
- 🔢 Float support with smart formatting

---

## 🛠️ Setup

1. Clone the repo:
   ```bash
   git clone https://github.com/cracked-21/cracked_budget.git
   cd cracked_budget
   ```

2. Run it:
   ```bash
   python cracked_budget.py
   ```

3. Your data will be saved in `cracked_budget.json`.

---

## 🎮 How to Use

Upon launch, you'll be asked if you'd like to load an existing file or create a new one.

### 🔹 Main Menu

| Option | Description                      |
|--------|----------------------------------|
| 1      | Add transaction or log           |
| 2      | View all transaction history     |
| 3      | Manage buckets                   |
| 4      | Edit a transaction timestamp     |
| 5      | Help (coming soon)               |
| 6      | Quit the app                     |

---

## 🪣 Buckets

Think of buckets like budget categories. Examples:

- `Rent`
- `Groceries`
- `Savings`
- `Emergency`

You can:
- Create buckets
- Rename buckets
- Delete them (with warning if balance > 0)
- Move money between buckets

---

## 🧾 Transactions

Two main types:
- `income`: Adds funds to a bucket
- `expense`: Deducts funds from a bucket (even if it goes negative — you'll get a warning)

Also supports a `log` type, which adds non-financial entries with purpose + note.

Each transaction is timestamped (`YYYY-MM-DD` format), and editable.

---

## 📁 File Structure

```bash
.
├── cracked_budget.py       # Main Python script
└── README.md               # You're here
```

---

## 🧱 Built With

- Python 3.x
- Standard Library (`json`, `datetime`, `sys`)

No dependencies. Just run it.

---

Made by **@cracked-21**  
Clean, simple, local budget tracking. Zero bloat, zero sync, total control.

---

## 📄 License

MIT License — do anything you want to my code i dont care. any problems you make are your fault tho.
