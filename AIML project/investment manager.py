try:
    import mysql.connector
    import pandas as pd
    from tabulate import tabulate
    # Connect to MySQL
    con = mysql.connector.connect(host='localhost', user='root', password='root')
    cursor = con.cursor()
    cursor.execute('CREATE DATABASE IF NOT EXISTS INVESTMENTS')
    cursor.execute('USE INVESTMENTS')
    cursor.execute('CREATE TABLE IF NOT EXISTS STOCKS (Name VARCHAR(30),Quantity INT,BuyPrice FLOAT)')
    cursor.execute('CREATE TABLE IF NOT EXISTS MUTUAL_FUNDS (FundName VARCHAR(50),amount FLOAT,MaturityDate FLOAT)')
    cursor.execute('''CREATE TABLE IF NOT EXISTS BONDS
(BondName VARCHAR(50),Quantity INT,FaceValue FLOAT,CouponRate FLOAT,MaturityDate DATE)''')

    def stocks():
        def Insert_stocks():
            n = int(input('Enter the number of stocks: '))
            for i in range(n):
                name = input("Enter the name of stock: ")
                Name = name.upper()
                qty = int(input('Enter quantity of stock: '))
                buy_price = float(input('Enter your buying price: '))
                cursor.execute('INSERT INTO STOCKS (Name, Quantity, BuyPrice) VALUES (%s, %s, %s)', (Name, qty, buy_price))
                con.commit()
            print('Stocks are inserted sucessfully!!!')

        def track_investments():
            cursor.execute('SELECT * FROM STOCKS')
            rows = cursor.fetchall()
            results = []
            total_invested = 0
            for Name, qty, buy_price in rows:
                invested = qty * buy_price
                total_invested += invested
                results.append({'Name': Name, 'Quantity': qty, 'Buy Price': buy_price, 'Invested': invested})
            df = pd.DataFrame(results)
            print(tabulate(df, headers="keys", tablefmt="psql"))
            print('Total Invested:', total_invested)

        def update_stock_quantity():
            n = int(input('enter the number of stocks you want update:'))
            for i in range(n):
                name = input('Enter the stock symbol to update: ')
                Name = name.upper()
                qty = int(input('Enter quantity you bought again: '))
                new_price = float(input('Enter buying price: '))
                cursor.execute('SELECT BuyPrice FROM STOCKS WHERE Name = %s', (Name,))
                r = cursor.fetchone()
                cursor.execute('SELECT Quantity FROM STOCKS WHERE Name=%s', (Name,))
                r2 = cursor.fetchone()
                if r:
                    old_price = r[0]
                    old_qty = r2[0]
                    new_qty = qty + old_qty
                    avg_price = (old_price * old_qty + qty * new_price) / new_qty
                    cursor.execute('UPDATE STOCKS SET Quantity = %s, BuyPrice = %s WHERE Name = %s', (new_qty, avg_price, Name))
                    con.commit()
                    print('The stocks has been updated sucessfully!!!')
                else:
                    print('Stock not found.')

        def Delete_all_stocks():
            cursor.execute('DELETE FROM STOCKS')
            con.commit()
            print('All stock records are deleted.')

        def Delete_stock_by_symbol():
            name = input('Enter the stock symbol to delete: ')
            Name = name.upper()
            cursor.execute('DELETE FROM STOCKS WHERE Name = %s', (Name,))
            con.commit()
            print('Stock has been deleted.')
        try:
            while True:
                print('menu\n1-insert data\n2-display data\n3-update stocks quantity\n4-delete a stock\n5-delete all stocks\n6-exit')
                ch = int(input('enter the choice:'))
                if ch == 1:
                    Insert_stocks()
                elif ch == 2:
                    track_investments()
                elif ch == 3:
                    update_stock_quantity()
                elif ch == 4:
                    Delete_stock_by_symbol()
                elif ch == 5:
                    Delete_all_stocks()
                elif ch == 6:
                    break
                else:
                    print('The choice entered is wrong')
        except Exception as e:
            print("Unexpected error in menu:", e)

    def mf():
        def Insert_mutual_funds():
            print('Note (only for lumpsum mutual funds)!!!')
            n = int(input('Enter the number of mutual funds: '))
            for i in range(n):
                Fund_name = input('Enter mutual fund name: ')
                fund_name = Fund_name.upper()
                amount = float(input('Enter the lumpsum amount:'))
                MaturityDate = float(input('Enter the no of years you invested for:'))
                cursor.execute('''INSERT INTO MUTUAL_FUNDS (FundName, amount, MaturityDate)
VALUES (%s, %s, %s)''', (fund_name, amount, MaturityDate))
                con.commit()
            print('Mutual funds inserted successfully!!!.')

        def Fetch_mutual_funds_data():
            cursor.execute('SELECT * FROM MUTUAL_FUNDS')
            rows = cursor.fetchall()
            portfolio = pd.DataFrame(rows, columns=['FundName', 'amount', 'MaturityDate'])
            print(tabulate(portfolio, headers="keys", tablefmt="psql"))
            t_v = 0
            for fund_name, amount, MaturityDate in rows:
                t_v += amount
            print('Total invested amount:', t_v)

        def Delete_mutual_fund_by_name():
            fund_name = input('Enter the mutual fund name to delete: ')
            cursor.execute('DELETE FROM MUTUAL_FUNDS WHERE FundName = %s', (fund_name,))
            con.commit()
            print('Mutual fund has been deleted.')

        def Delete_all_mutual_funds():
            cursor.execute('DELETE FROM MUTUAL_FUNDS')
            con.commit()
            print('All mutual funds have been deleted.')
        try:
            while True:
                print('Menu\n1-Insert mutual funds\n2-Display mutual funds\n3-Delete a mutual fund by name\n4-Delete all mutual funds\n5-Exit')
                choice = int(input('Enter your choice: '))
                if choice == 1:
                    Insert_mutual_funds()
                elif choice == 2:
                    Fetch_mutual_funds_data()
                elif choice == 3:
                    Delete_mutual_fund_by_name()
                elif choice == 4:
                    Delete_all_mutual_funds()
                elif choice == 5:
                    break
                else:
                    print('Invalid choice, try again.')
        except Exception as e:
            print(" Unexpected error in menu:", e)

    def bonds():
        def Insert_bonds():
            n = int(input('Enter the number of bonds: '))
            for i in range(n):
                Bond_name = input('Enter bond name: ')
                bond_name = Bond_name.upper()
                qty = int(input('Enter the quantity: '))
                face_value = float(input('Enter face value per bond: '))
                coupon_rate = float(input('Enter coupon rate (%): '))
                maturity_date = input('Enter maturity date (YYYY-MM-DD): ')
                cursor.execute('''INSERT INTO BONDS (BondName, Quantity, FaceValue, CouponRate, MaturityDate)
                               VALUES (%s, %s, %s, %s, %s)''', (bond_name, qty, face_value, coupon_rate, maturity_date))
                con.commit()
                print('Bond inserted successfully!!!.')

        def Fetch_bonds_data():
            cursor.execute('SELECT * FROM BONDS')
            r = cursor.fetchall()
            portfolio = pd.DataFrame(r, columns=['BondName', 'Quantity', 'FaceValue', 'CouponRate', 'MaturityDate'])
            print(tabulate(portfolio, headers="keys", tablefmt="psql"))
            t = 0
            for BondName, Quantity, FaceValue, CouponRate, MaturityDate in r:
                t += Quantity * FaceValue
            print('Total value:', t)

        def Delete_bond_by_name():
            Bond_name = input('Enter the bond name to delete: ')
            bond_name = Bond_name.upper()
            cursor.execute('DELETE FROM BONDS WHERE BondName = %s', (bond_name,))
            con.commit()
            print('Bond has been deleted.')

        def Delete_all_bonds():
            cursor.execute('DELETE FROM BONDS')
            con.commit()
            print('All bonds have been deleted.')
        try:
            while True:
                print('Bond Menu\n1 - Insert bonds\n2 - Display bonds\n3 - Delete a bond by name\n4 - Delete all bonds\n5 - Exit')
                choice = int(input('Enter your choice: '))
                if choice == 1:
                    Insert_bonds()
                elif choice == 2:
                    Fetch_bonds_data()
                elif choice == 3:
                    Delete_bond_by_name()
                elif choice == 4:
                    Delete_all_bonds()
                elif choice == 5:
                    break
                else:
                    print('Invalid choice, try again.')
        except Exception as e:
            print("Unexpected error in menu:", e)
    def total():
        # Stocks
        cursor.execute('SELECT * FROM STOCKS')
        rows = cursor.fetchall()
        results = []
        total_invested = 0
        for Name, qty, buy_price in rows:
            invested = qty * buy_price
            total_invested += invested
            results.append({'Name': Name, 'Quantity': qty, 'Buy Price': buy_price, 'Invested': invested})
        df = pd.DataFrame(results)
        print(tabulate(df, headers="keys", tablefmt="psql"))
        print('Total Invested in Stocks:', total_invested)

        # Mutual Funds
        cursor.execute('SELECT * FROM MUTUAL_FUNDS')
        rows = cursor.fetchall()
        portfolio = pd.DataFrame(rows, columns=['FundName', 'amount', 'MaturityDate'])
        print(tabulate(portfolio, headers="keys", tablefmt="psql"))
        t_v = 0
        for fund_name, amount, MaturityDate in rows:
            t_v += amount
        print('Total Invested in Mutual Funds:', t_v)

        # Bonds
        cursor.execute('SELECT * FROM BONDS')
        r = cursor.fetchall()
        portfolio = pd.DataFrame(r, columns=['BondName', 'Quantity', 'FaceValue', 'CouponRate', 'MaturityDate'])
        print(tabulate(portfolio, headers="keys", tablefmt="psql"))
        t = 0
        for BondName, Quantity, FaceValue, CouponRate, MaturityDate in r:
            t += Quantity * FaceValue
        print('Total Value of Bonds:', t)

        # Grand Total
        Total = t_v + t + total_invested
        print('Grand Total Invested Amount:', Total)

    def delete():
        ch=input('are you sure you want to delete all the records(yes/no):')
        if ch.lower()=='yes':
            cursor.execute('DELETE FROM BONDS')
            con.commit()
            cursor.execute('DELETE FROM MUTUAL_FUNDS')
            con.commit()
            cursor.execute('DELETE FROM STOCKS')
            con.commit()
            print('All records are deleted.')
        else:
            print('Aborted')
    try:
        while True:
            print('menu\n1-stocks\n2-mutual funds\n3-bonds\n4-total investment value\n5-delete all records\n6-exit')
            ch=int(input('enter the choice:'))
            if ch==1:
                stocks()
            elif ch==2:
                mf()
            elif ch==3:
                bonds()
            elif ch==4:
                total()
            elif ch==5:
                delete()
            elif ch==6:
                break
            else:
                print(' Invalid choice, try again.')
    except ValueError:
        print("Please enter a valid number.")
    except Exception as e:
        print("Unexpected error in menu:", e)

    cursor.close()
    con.close()
except ModuleNotFoundError:
    print('''Note before you run this program you need mysql.connector, pandas, tabulate modules so
if you don't have the modules installed, install the modules using the prompt
(pip install mysql.connector pandas tabulate)''')
except mysql.connector.Error as e:
    print(" Database connection error:", e)
except Exception as e:
    print(" Unexpected program error:", e)
finally:
    print('program sucessfully completed running without any error!!!')

