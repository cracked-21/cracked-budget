import json
import sys
from datetime import datetime
    
def format_money(value):
    return f"{int(value)}" if value == int(value) else f"{value:.2f}"

def load_or_create():
    data = {
        "starting_balance": 0,
        "buckets": {},
        "transactions": []
    }
    
    try:
        with open("cracked_budget.json", "r") as data_file:
            data = json.load(data_file)
            print("\nFile found!\nLoading environment...")
            return data
        
    except FileNotFoundError:
        print("Budget file must be named 'cracked_budget.json' and in the same directory as this program.\n")
        filenotfound = input("No budget file found, do you want to create a new one? y/n: ").strip().lower()

        if filenotfound != "y":
            print("\nExiting program.\n")
            sys.exit(0)

        try:
            balance_amt = float(input("Input how much money you want to track across everything: "))
            
            if not balance_amt:
                print("\nInput cannot be empty.\n")
                return
            
            balance_amt = float(balance_amt)
            if balance_amt < 0:
                print("\nInvalid input; must be non-negative.\n")
                return
                
        except ValueError:
            print("\nInvalid input; must be an integer.\n")
            return

        data["starting_balance"] = balance_amt
        print("\nBuckets are labeled containers used to allocate portions of your total money for a purpose/goal")

        try:
            bucket_amt = int(input("How many buckets do you have/want to maintain? You can have as many as you want: ").strip())
            if bucket_amt < 0:

                print("\nInvalid input; must be non-negative.\n")
                return
            
        except ValueError:
            print("\nInvalid input; must be an integer.\n")
            return

        remaining_balance = balance_amt
        for bucket_maker in range(1, bucket_amt + 1):

            while True:
                bucket_name = input(f"\nWhat's the name of bucket {bucket_maker}: ").strip().lower().title()
                if bucket_name == "":
                    bucket_name = "All"

                if bucket_name in data["buckets"]:
                    print("\nBucket already exists! Please try again.\n")
                    continue
                break

            try:
                bucket_money_amt = float(input(f"\nHow much money is in '{bucket_name}': ").strip())
                if bucket_money_amt < 0:
                    print("Invalid input; must be non-negative.\n")
                    continue

                if bucket_money_amt > remaining_balance:
                    print("\nInvalid input; bucket amount exceeds remaining balance.\n")
                    continue

            except ValueError:
                print("Invalid input; must be an integer.\n")
                continue

            remaining_balance -= bucket_money_amt
            data["buckets"][bucket_name] = bucket_money_amt

        with open("cracked_budget.json", "w") as data_file:
            json.dump(data, data_file, indent=4)
        print("\nBudget file creation successful! Loading environment...\n")
        return data
            

def tx_logger(data):
    while True:
        bucket_names = list(data["buckets"].keys())

        total_balance = sum(data["buckets"].values())
        if total_balance < 0:
            print(f"\n**Warning: You are spending ${-format_money(total_balance)} more than you have. Log the debt or update your income.**\n")

        # the terminal would print "1. add transaction 2. view all transactions 3. manage buckets 4. update timestamp 5. quit"
        print("\n--- Budget Tracker Menu ---\n")
        print("| 1.| Add transaction/log\n| 2.| View all transactions\n| 3.| Manage buckets\n| 4.| Update transaction timestamp\n| 5.| Help\n| 6.| Quit\n")
        try:
            main_question = float(input("Select an option: "))

            if main_question == 1:
                # 1 would add ask if it's an income or an expense tx
                tx_type = input("\nIs this a log or a transaction: ").strip().lower()
                
                if tx_type not in ("log", "transaction", "tx"):
                    print("\nInvalid input; must be either 'log' or 'transaction'\n")
                    continue
                
                if tx_type == "log":
                
                    tx_purpose = input("Input the subject of this log: ").strip()
                    tx_note = input("Input the body of your log. If you want to leave it empty simply press the ENTER key: ").strip()
                    tx_bucket = input("What bucket is the log going to be saved to: ").strip().lower().title()
                    try:
                        tx_amount = float(input("What is the amount of this transaction: $"))

                        if tx_amount < 0:
                            print("\nInvalid input; must be positive.\n")
                            continue

                    except ValueError:
                        print("Invalid input; must be an integer.\n")
                        continue

                    if tx_bucket not in data["buckets"]:
                        data["buckets"][tx_bucket] = 0
                        data["buckets"][tx_bucket] += tx_amount

                    # append log to the transaction key
                    data["transactions"].append({
                    "type": tx_type,
                    "amount": format_money(tx_amount),
                    "bucket": tx_bucket,
                    "purpose": tx_purpose,
                    "note": tx_note,
                    "timestamp": datetime.now().strftime("%Y-%m-%d")
                    })

                    # save data.
                    with open("cracked_budget.json", "w") as data_file:
                        json.dump(data, data_file, indent=4)
                    print("Transaction added.\n")

                elif tx_type == "transaction" or "tx":
                    tx_type = "transactions"

                    tx_type = input("\nIs this an income or expense transaction: ").strip().lower()

                        # then ask for the amount
                    try:
                        tx_amount = float(input("What is the amount of this transaction: $"))

                        if tx_amount < 0:
                            print("\nInvalid input; must be positive.\n")
                            continue

                    except ValueError:
                        print("Invalid input; must be an integer.\n")
                        continue

                    # and the bucket's purpose, also with a note system (or date)
                    tx_purpose = input("Input the origin/purpose of this transaction. Keep it short: ").strip()
                    tx_note = input("Add a note if you want to remember anything from this transaction. If you want to leave it empty simply press the ENTER key:\n").strip()

                    for idx, (bucket_name, bucket_amount) in enumerate(data["buckets"].items(), start=1):
                        print(f"| {idx}.| {bucket_name}: ${format_money(bucket_amount)}")

                    try:
                        tx_bucket = int(input("What bucket number is the transaction going through: "))

                        if not (1 <= tx_bucket <= len(bucket_names)):
                            print("\nInvalid selection.\n")
                            continue

                    except ValueError:
                        print("\nInvalid input; must be a number.\n")
                        continue

                    chosen_tx_bucket = bucket_names[tx_bucket - 1]

                    if chosen_tx_bucket not in data["buckets"]:
                        print("Invalid input; must be an existing bucket.\n")
                        continue

                    if tx_type == "income" or "in":
                        tx_type = "income"

                        # if the bucket doesnt exist create it, if it does add to it.
                        if tx_bucket not in data["buckets"]:
                            data["buckets"][tx_bucket] = 0
                        data["buckets"][tx_bucket] += tx_amount

                    elif tx_type == "expense" or "ex":

                        # if bucket doesnt exist ask for the bucket again with an error that it doesnt exist
                        if tx_bucket not in data["buckets"]:
                            print("Invalid input; Bucket not found.\n")
                            continue
                        
                        if tx_amount > data["buckets"][tx_bucket]:
                            
                            # if expense is over the bucket amount then allow it but print warning saying that before and after (are you sure)
                            print(f"The amount you inputted (${format_money(tx_amount)}) is higher than what's in the bucket.\n")
                            confirm = input("Are you sure you want to proceed? y/n: ").strip().lower()
                            if confirm != "y":
                                continue
                            
                            # then print "youve gone overboard by $x, create a new transaction from another bucket or update your income."
                            print(f"\nYou've gone overboard by ${format_money(data['buckets'][tx_bucket]) - format_money(tx_amount) / -1}")
                            print("please create a new transaction from another bucket by either")
                            print("1. subtracting from another bucket and adding here or 2. by updating your income and this bucket\n")
                            data["buckets"][tx_bucket] -= tx_amount
                    
                    else: 
                        print("Invalid input.")
                        continue
                        
                    # append all data to the transaction key
                    data["transactions"].append({
                        "type": tx_type,
                        "amount": format_money(tx_amount),
                        "bucket": chosen_tx_bucket,
                        "purpose": tx_purpose,
                        "note": tx_note,
                        "timestamp": datetime.now().strftime("%Y-%m-%d")
                    })

                    # save data.
                    with open("cracked_budget.json", "w") as data_file:
                        json.dump(data, data_file, indent=4)
                    print("Transaction added.\n")
                   
                else: 
                    print("\nInvalid input; must be either 'income' or 'expense'\n")
                    continue

            elif main_question == 2:

                # 2 would show all transactions loaded from a dictionary. 
                if not data["transactions"]:
                    print("\nNo transactions found.")
                print("\n--- Transaction Log ---\n")

                for idx, transaction in enumerate(data["transactions"], start=1):

                    if transaction["type"] == "income":
                        print(f"| {idx}.| Added ${transaction['amount']} to '{transaction['bucket']}' from '{transaction['purpose']}' with note: '{transaction.get('note')}' on {transaction['timestamp']}\n----------")
                    
                    elif transaction["type"] == "expense":
                        print(f"| {idx}.| Spent ${transaction['amount']} from '{transaction['bucket']}' on '{transaction['purpose']}' with note: '{transaction.get('note')}' on {transaction['timestamp']}\n----------")
                    
                    elif transaction["type"] == "log":
                        if "amount" not in transaction:
                            print(f"| {idx}.| Logged '{transaction['purpose']}' from bucket '{transaction['bucket']}': '{transaction.get('note')}' on {transaction['timestamp']}\n----------") 

                        else: print(f"| {idx}.| Logged '{transaction['purpose']}' from bucket '{transaction['bucket']}' worth ${transaction['amount']}: '{transaction.get('note')}' on {transaction['timestamp']}\n----------") 
                            
                    else: 
                        if "bucket" not in transaction:
                            print(f"| {idx}.| {transaction.get('purpose', '')} on {transaction['timestamp']}\n----------")
                        else: print(f"| {idx}.| Modified bucket '{transaction['bucket']}': {transaction.get('purpose', '')} on {transaction['timestamp']}\n----------")
        
            elif main_question == 3:
                # 3 would ask you if you want to "1. creates bucket 2. rename bucket 3. move money between buckets 4. delete bucket 5. back"
                    # if bucket has over 0 dollars warn user and tell them to spend it first before deleting it
                    # if option 3 is used move money and then print a special "moved money from x to y" transaction

                while True:
                    print("\n--- Bucket Management Menu ---\n")
                    print("| 1.| Create bucket\n| 2.| Rename bucket\n| 3.| Show bucket balances\n| 4.| Move money between buckets\n| 5.| Delete bucket\n| 6.| Back\n")
                    try:
                        manage_bucket = int(input("Select an option: "))

                        if manage_bucket == 1:
                            new_bucket = input("What do you want to call this new bucket: ").strip().lower().title()

                            if new_bucket in data["buckets"]:
                                print("\nBucket already exists!\n")
                                continue

                            else:
                                data["buckets"][new_bucket] = 0
                                # add tx log
                                data["transactions"].append({
                                    "type": "create_bucket",
                                    "bucket": new_bucket,
                                    "amount": 0,
                                    "purpose": f"Created bucket '{new_bucket}'",
                                    "timestamp": datetime.now().strftime("%Y-%m-%d")
                                })

                                # save data
                                with open("cracked_budget.json", "w") as data_file:
                                    json.dump(data, data_file, indent=4)
                                print("\nBucket added successfully.\n")
                            
                        elif manage_bucket == 2:

                            print("\n--- Bucket Renamer ---\n")   
                            for idx, (bucket_name, bucket_amount) in enumerate(data["buckets"].items(), start=1):
                                print(f"| {idx}.| {bucket_name}: ${format_money(bucket_amount)}")

                            change_bucket = input("\nWhat's the name of the bucket you want to change: ").strip().lower().title()

                            if change_bucket not in data["buckets"]:
                                print("\nInvalid input; Bucket doesn't exist.\n")
                                continue

                            new_bucket_name = input(f"What do you want to change {change_bucket} to: ").strip().lower().title()
                            
                            if new_bucket_name in data["buckets"]:
                                print("\nInvalid input; new bucket name already exists.\n")
                                continue
                            
                            data["buckets"][new_bucket_name] = data["buckets"][change_bucket]
                            del data["buckets"][change_bucket]

                            # add tx log
                            data["transactions"].append({
                                "type": "rename_bucket",
                                "bucket": new_bucket_name,
                                "amount": 0,
                                "purpose": f"Renamed bucket '{change_bucket}' to '{new_bucket_name}'",
                                "timestamp": datetime.now().strftime("%Y-%m-%d")
                            })
                            
                            # save data.
                            with open("cracked_budget.json", "w") as data_file:
                                json.dump(data, data_file, indent=4)
                            print("\nBucket renamed successfully.\n")
                                
                        elif manage_bucket == 3:

                            total = sum(data["buckets"].values())

                            print("\n--- Bucket Balances ---\n")
                            for name, amount in data["buckets"].items():
                                print(f" - {name}: ${format_money(amount)}")
                                
                            print(f" - Total: ${format_money(total)}")

                        elif manage_bucket == 4:



                            print("\n--- Balance Rebalancer ---\n")
                            for idx, (bucket_name, bucket_amount) in enumerate(data["buckets"].items(), start=1):
                                print(f"| {idx}.| {bucket_name}: ${format_money(bucket_amount)}")

                            try:
                                move_money_old = int(input("\nWhat is the number of the bucket you want to move money from: "))

                                if not (1 <= move_money_old <= len(bucket_names)):
                                    print("\nInvalid selection.\n")
                                    continue

                            except ValueError:
                                print("\nInvalid input; must be a number.\n")
                                continue

                            chosen_bucket_old = bucket_names[move_money_old - 1]

                            if chosen_bucket_old not in data["buckets"]:
                                print("Invalid input; must be an existing bucket.\n")
                                continue

                            else: 
                                try:
                                    move_money_amount = float(input("\nHow much do you want to move: $"))

                                    if move_money_amount > data["buckets"][chosen_bucket_old]:
                                        print("\nInvalid input; input greater than avaliable amount.\n")
                                        continue

                                    elif move_money_amount < 0:
                                        print("Invalid input; input must be positive.\n")
                                        continue

                                except ValueError:
                                    print("Invalid input; must be a positive integer.\n")
                                    continue

                                try:
                                    move_money_new = int(input("\nWhat is the number of the bucket you want to move money to: "))

                                    if not (1 <= move_money_new <= len(bucket_names)):
                                        print("\nInvalid selection.\n")
                                        continue

                                except ValueError:
                                    print("\nInvalid input; must be a number.\n")
                                    continue

                                chosen_bucket_new = bucket_names[move_money_new - 1]

                                data["buckets"][chosen_bucket_old] -= move_money_amount
                                data["buckets"][chosen_bucket_new] += move_money_amount

                                # add tx log
                                data["transactions"].append({
                                    "type": "move_money",
                                    "from": chosen_bucket_old,
                                    "to": chosen_bucket_new,
                                    "amount": format_money(move_money_amount),
                                    "purpose": f"Moved ${format_money(move_money_amount)} from '{chosen_bucket_old}' to '{chosen_bucket_new}'",
                                    "timestamp": datetime.now().strftime("%Y-%m-%d")
                                })

                                # update data.
                                with open("cracked_budget.json", "w") as data_file:
                                    json.dump(data, data_file, indent=4)
                                print("\nBucket value updated successfully.")
                                break
                        
                        elif manage_bucket == 5:

                            print("\n--- Bucket Execution Chamber ---\n")
                            for idx, (bucket_name, bucket_amount) in enumerate(data["buckets"].items(), start=1):
                                print(f"| {idx}.| {bucket_name}: ${format_money(bucket_amount)}")

                            try:
                                execution_chamber = int(input("\nWhat's the number of the bucket you want to delete: "))

                                if not (1 <= execution_chamber <= len(bucket_names)):
                                    print("\nInvalid selection.\n")
                                    continue

                            except ValueError:
                                print("\nInvalid input; must be a number.\n")
                                continue

                            chosen_execution_bucket = bucket_names[execution_chamber - 1]


                            if data["buckets"][chosen_execution_bucket] > 0:
                                areusure = input("There's still money in that bucket, are you sure you want to delete it? It's permanant! y/n: ").strip().lower()
                                if areusure != "y":
                                    continue                         

                                # add tx log
                                data["transactions"].append({
                                    "type": "delete_bucket",
                                    "bucket": chosen_execution_bucket,
                                    "purpose": f"Deleted bucket '{chosen_execution_bucket}'",
                                    "timestamp": datetime.now().strftime("%Y-%m-%d")
                                })

                                del data["buckets"][chosen_execution_bucket]
                            
                                # save data.
                                with open("cracked_budget.json", "w") as data_file:
                                    json.dump(data, data_file, indent=4)
                                    
                                print("\nBucket deleted successfully.\n")

                        elif manage_bucket == 6: break

                        else: print("\nInvalid input; must be between 1 and 5.\n")

                    except ValueError:
                        print("\nInvalid input; must be an integer.\n")
                        continue

            elif main_question == 4:
                # edit timestamps
                if not data["transactions"]:
                    print("\nNo transactions found.\n")
                    continue
                print("\n--- Transaction Fabricator ---\n")
                for idx, transaction in enumerate(data["transactions"], start=1):

                    if transaction["type"] == "income":
                        print(f"| {idx}.| Added ${transaction['amount']} to '{transaction['bucket']}' from '{transaction['purpose']}' with note: '{transaction.get('note')}' on {transaction['timestamp']}\n----------")
                    
                    elif transaction["type"] == "expense":
                        print(f"| {idx}.| Spent ${transaction['amount']} from '{transaction['bucket']}' on '{transaction['purpose']}' with note: '{transaction.get('note')}' on {transaction['timestamp']}\n----------")
                    
                    elif transaction["type"] == "log":
                        if "amount" not in transaction:
                            print(f"| {idx}.| Logged '{transaction['purpose']}' from bucket '{transaction['bucket']}': '{transaction.get('note')}' on {transaction['timestamp']}\n----------") 

                        else: print(f"| {idx}.| Logged '{transaction['purpose']}' from bucket '{transaction['bucket']}' worth ${transaction['amount']}: '{transaction.get('note')}' on {transaction['timestamp']}\n----------") 
                            
                    else: 
                        if "bucket" not in transaction:
                            print(f"| {idx}.| {transaction.get('purpose', '')} on {transaction['timestamp']}\n----------")
                        else: print(f"| {idx}.| Modified bucket '{transaction['bucket']}': {transaction.get('purpose', '')} on {transaction['timestamp']}\n----------")
                    
                try:
                    tx_selector = int(input("\nEnter the transaction number to edit its timestamp: "))

                    if not (1 <= tx_selector <= len(data["transactions"])):
                        print("\nInvalid selection.\n")
                        continue

                except ValueError:
                    print("\nInvalid input; must be a number.\n")
                    continue

                chosen_tx = data["transactions"][tx_selector - 1]

                # Ask for new timestamp
                new_timestamp = input("Enter new timestamp (yyyy-mm-dd): ").strip()
                try:
                    # Validate format
                    datetime.strptime(new_timestamp, "%Y-%m-%d")

                except ValueError:
                    print("\nInvalid format. Must be 'yyyy-mm-dd'.\n")
                    continue

                # Update timestamp
                chosen_tx["timestamp"] = new_timestamp

                # save data.
                with open("cracked_budget.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
                print("\nBucket renamed successfully.\n")
                    

            elif main_question == 5:
                help_what_exactly = int(input("\nWhat do you want help with?\n1. Adding a transaction/log\n2. Viewing all transactions\n3. Managing Buckets\n4. Updating transaction timestamps"))
                
                if help_what_exactly != 1 or 2 or 3 or 4 or 5 or 6:
                    print("\nInvalid input; must be an integer between 1 and 5.\n")
                    continue

                if help_what_exactly == 1:
                    print("The purpose of this option is to allow the user to log down logs or transactions")
                    print("with buckets, a written down purpose and timestamps to further specify it.")
                    print("Optional functionality includes notes and a warning when an amount spent is higher than what's in all buckets.")
                    continue

                elif help_what_exactly == 2:
                    print("The purpose of this option is to print all saved transactions.")
                    continue

                elif help_what_exactly == 3:
                    print("This option allows you to create, rename, show balance of, move money between, and delete buckets respectively.")
                    continue

                elif help_what_exactly == 4:
                    print("This option allows you to change the timestamp of a tranaction, either because it's not due yet or you already did it.")
                    continue

                elif help_what_exactly == 5:
                    print("The help option helps your dumbass")
                    continue

                elif help_what_exactly == 6:
                    print("This option quits the program.")
                    continue

            elif main_question == 6:
                # 5 would quit.
                sys.exit(0)

            else: 
                print("\nInvalid input; must be between 1 and 6.\n")
                continue

        except ValueError:
            print("\nInvalid input; must be an integer.\n")
            continue

def main():
    data = load_or_create()
    tx_logger(data)

if __name__ == "__main__":
    main()