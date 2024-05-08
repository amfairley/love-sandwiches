# Import gspread library
import gspread
# Import the credentials class from the service_account function of the google-auth library
from google.oauth2.service_account import Credentials
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

# # Get the sales sheet from the spreadsheet
# sales = SHEET.worksheet('sales')

# # Get the values from the sales worksheet
# data = sales.get_all_values()

# print(data)

def get_sales_data():
    '''
    Get sales figures input from user
    '''
    print("Please enter sales data from the last market.")
    print("Data should be six numbers, separated by commas.")
    print("For example: 10,20,30,40,50,60\n")

    data_str = input("Please enter your data here: ")
    print(f'The data provided is {data_str}')

    sales_data = data_str.split(",")

def validate_data(values):
    '''
    Validates the sales figures input
    '''
    try:
        [int(values) for value in values]
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values required, you provided {len(values)} values"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.")



    
sales_data = get_sales_data()

