from zillow import Soupy
from selen import Drive

soupy = Soupy()

price_list = soupy.find_prices()
address_list = soupy.find_addresses()
link_list = soupy.find_links()

# This will send the data to the terminal so that you can make sure it is working correctly
print(price_list)
print(address_list)
print(link_list)

drive = Drive()


for n in range(0, (len(price_list)-1)):
    drive.post_info(address=address_list[n], price=price_list[n], link=link_list[n])
