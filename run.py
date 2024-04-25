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

# Get the sales sheet from the spreadsheet
sales = SHEET.worksheet('sales')

# Get the values from the sales worksheet
data = sales.get_all_values()

print(data)
