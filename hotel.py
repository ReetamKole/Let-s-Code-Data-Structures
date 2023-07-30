import requests
from bs4 import BeautifulSoup

def get_hotel_data(url):
    # Send an HTTP GET request to the URL
    response = requests.get(url)

    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the elements containing information about hotel rooms
    room_elements = soup.find_all('div', class_='room')

    # Create a list to store the scraped data
    hotel_data = []

    for room in room_elements:
        # Extract relevant details for each room
        room_name = room.find('h2', class_='room-name').text.strip()
        room_description = room.find('p', class_='room-description').text.strip()
        room_price = room.find('span', class_='room-price').text.strip()
        room_amenities = [amenity.text.strip() for amenity in room.find_all('li', class_='amenity')]

        # Create a dictionary to store the information of each room
        room_info = {
            'name': room_name,
            'description': room_description,
            'price': room_price,
            'amenities': room_amenities
        }

        hotel_data.append(room_info)

    return hotel_data

if __name__ == "__main__":
    # Replace 'your_hotel_url_here' with the URL of the hotel website you want to scrape
    hotel_url = 'your_hotel_url_here'
    scraped_data = get_hotel_data(hotel_url)

    # Display the scraped data
    for room in scraped_data:
        print("Room Name:", room['name'])
        print("Description:", room['description'])
        print("Price:", room['price'])
        print("Amenities:", ", ".join(room['amenities']))
        print("------------------------")
