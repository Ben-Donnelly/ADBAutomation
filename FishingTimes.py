from bs4 import BeautifulSoup
from requests import get
from lxml import html
from colorama import Fore


data = get('https://www.fishingreminder.com/IE/charts/fishing_times/Dublin')

rating_col = {
	1 : Fore.RED,
	2 : Fore.LIGHTYELLOW_EX,
	3 : Fore.GREEN,
	4 : Fore.GREEN
}

soup = BeautifulSoup(data.text, 'html.parser')
tree = html.fromstring(data.content)

rating = tree.xpath('//*[@id="static"]/div[1]/div[2]/div[1]/p[1]/b[1]/text()')[0]
# Change 'out of' to /

sun_rise = tree.xpath('//*[@id="static"]/div[1]/div[2]/div[1]/p[1]/b[3]/text()')[0]
sun_set = tree.xpath('//*[@id="static"]/div[1]/div[2]/div[1]/p[1]/b[4]/text()')[0]

first_major = tree.xpath('//*[@id="static"]/div[1]/div[2]/div[1]/p[3]/b[2]/text()')[0]
second_major = tree.xpath('//*[@id="static"]/div[1]/div[2]/div[1]/p[3]/b[4]/text()')[0]

first_minor = tree.xpath('//*[@id="static"]/div[1]/div[2]/div[1]/p[4]/b[2]/text()')[0]
second_minor = tree.xpath('//*[@id="static"]/div[1]/div[2]/div[1]/p[4]/b[4]/text()')[0]
print(f"Today's rating: {rating_col[int(rating[0])]}{rating[0]}/{rating[9]}")
print(f"{Fore.RESET}Sun Rise: {sun_rise}\nSun Set: {sun_set}")

print(f"{Fore.GREEN}Best times begin at {first_major} and {second_major} and will last for about 2 hours")
print(f"{Fore.RED}Then {first_minor} and {second_minor} for 1-2 hours (potentially less activity)")

