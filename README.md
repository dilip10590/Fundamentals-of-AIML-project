Topic: Investment Portfolio Management 
Course: Fundamentals of AIML 
Name: Dilip S

Project Overview:

This Python code is a impressive tool for managing and tracking financial investments across three primary categories: Stocks, Mutual Funds, and Bonds,even if you multiple demat account you can view all investments in one place. The system utilizes a MySQL backend for persistent data storage.The core objective of this project is to demonstrate the integration of Python with relational databases to perform (Create, Read, Update, Delete) operations and basic financial data analysis.


Investment Categories:

Stocks: Track individual stock names, quantities, and buying prices. The system automatically calculates average buying prices when updating existing stock quantities.
Mutual Funds: Record lumpsum investments and their intended maturity duration.
Bonds: Manage bond portfolios including face value, quantity, coupon rates, and maturity dates. 


Portfolio Management:

Data Insertion: Add multiple investment records at once for any category.
Live Tracking: Display detailed tables of current investments using pandas and tabulate for a clean, professional look.
Smart Updates: Update stock quantities with automated cost-averaging logic.
Granular Deletion: Remove specific records by name or clear entire tables.
Financial Analytics:
          Total Investment Value: A dedicated function to aggregate and display the total value held in Stocks, Mutual Funds, and Bonds separately, concluding with a Grand Total across the entire portfolio.


Technical StackLanguage: 

PythonDatabase: MySQL 
Key Libraries: 
          mysql.connector: Facilitates the connection between Python and the SQL database.
          pandas: Used for structured data handling and DataFrame creation.
          tabulate: Enhances the visual presentation of data tables in the console.

          
Prerequisites & Installation:

Before running the program, ensure you have a MySQL server running and the required Python modules installed.
MySQL ConfigurationThe script is configured to connect with the following default credentials(Host: localhostUser: rootPassword: root)
Note: You can update these credentials in the mysql.connector.connect() function within the code to match your local setup.


Install Dependencies:
Run the following command in your terminal/command prompt to install the necessary libraries:
pip install mysql.connector pandas tabulate


Error Handling:

The system includes robust error handling to manage:Missing dependencies (prompts the user to install them).Database connection failures.Invalid user inputs or menu choices.
