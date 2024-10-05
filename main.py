from auth import Auth
from geo import Geo

def main():
    auth = Auth('regno.csv')
    login_success = auth.login()
    
    if login_success:
        geo = Geo()
        geo.run()
    else:
        print("Exiting application.")

if __name__ == "__main__":
    main()
