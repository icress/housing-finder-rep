from bs4 import BeautifulSoup
import requests

# This url will be the one scraped for addresses, prices, and links
URL = "https://www.zillow.com/san-francisco-ca/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22San%20Francisco%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56207553271484%2C%22east%22%3A-122.30458346728516%2C%22south%22%3A37.672915110006386%2C%22north%22%3A37.8775272266833%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A597887%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"

# The headers are necessary to allow BeautifulSoup to not be rejected as a bot
HEADERS = {
    "User-Agent": "Defined",
    "Accept-Language": "en-US,en;q=0.9"
}


class Soupy:

    def __init__(self):

        self.response = requests.get(url=URL, headers=HEADERS)
        self.contents = self.response.text
        self.soup = BeautifulSoup(self.contents, "html.parser")

    def find_prices(self):

        prices = self.soup.find_all(class_="StyledPropertyCardDataArea-c11n-8-70-0__sc-yipmu-0 jSVWjf")

        price_list = []
        for price in prices:
            price_text = price.getText()
            price_num = price_text.split()[0]
            price_list.append(price_num)

        return price_list

    def find_addresses(self):

        addresses_raw = self.soup.find_all(class_="StyledPropertyCardDataArea-c11n-8-70-0__sc-yipmu-0 dYZVUW property-card-link")

        address_list = []
        for address in addresses_raw:
            address_list.append(address.text)

        return address_list

    def find_links(self):

        links_raw = self.soup.find_all(name="a", class_="property-card-link")

        link_list = []
        n = 0
        # This part adds the zillow.com to hyperlinks that don't have it to make them work
        for link in links_raw:
            n += 1
            if n % 2 == 0:
                link_part = link["href"]
                link_split = str(link_part).split("/")
                if link_split[0] != "https:":
                    new_link = f"https://www.zillow.com{link_part}"
                else:
                    new_link = link_part
                link_list.append(new_link)

        return link_list
