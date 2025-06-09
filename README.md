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

cracked-budget is a **feature-complete** command-line app for tracking income, expenses, and logs using labeled buckets. Built to be simple, functional, and fast — with no unnecessary bloat.

---

## 📦 Features

- ✅ Add, rename, delete financial buckets
- 💰 Log income and expense transactions
- 📝 Add logs (non-financial notes)
- 📊 View current bucket balances
- 🔁 Move funds between buckets
- 🧾 View all transaction history
- 🕒 Modify transaction timestamps
- 💾 Autosaves to `cracked-budget.json`
- 🔢 Float support with smart formatting

---

## 🛠️ Setup

1. Clone the repo:
   ```bash
   git clone https://github.com/cracked-21/cracked-budget.git
   cd cracked-budget
   ```

2. Run it:
   ```bash
   python cracked-budget.py
   ```

3. Your data will be saved in `cracked-budget.json`.

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
| 5      | Help                             |
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
├── cracked-budget.py       # Main Python script
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

MIT License — Do whatever you want to with my code. Anything you do is YOUR responsibility.
