import requests

def fetch_covid_data():
    url = "https://api.covidtracking.com/v1/states/daily.csv "
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        return data
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def main():
    covid_data = fetch_covid_data()
    if covid_data:
        # Process the fetched data here
        print(covid_data)
        print("Data fetched successfully!")
    else:
        print("Failed to fetch data.")

if __name__ == "__main__":
    main()
