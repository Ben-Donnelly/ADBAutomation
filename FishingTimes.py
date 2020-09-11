import requests
from pandas import read_html, isna
from bs4 import BeautifulSoup
import re


def fishing():
	fishing_times = read_html('https://www.fishingreminder.com/IE/charts/fishing_times/Dublin')[0]
	data = requests.get('https://www.fishingreminder.com/IE/charts/fishing_times/Dublin')
	soup = BeautifulSoup(data.text, 'html.parser')

	# x = soup.find_all('tr', {"class": re.compile("^forecastrow weekday rating_\d$")})
	x = soup.find_all('tr')
	l = []
	for i in range(1, len(x)):
		l.append(x[i].attrs['class'][2][-1:])
	# raise SystemExit
	#
	# result = x.search( )
	# matchedText = result.groups()[0]

	# Create dict for bite times
	bite_ref = {}
	for i in range(7):
		day, mabt, mibt = fishing_times.values[i][0], fishing_times.values[i][2], fishing_times.values[i][3]
		bite_ref[i] = f"{day} ({l[i]}/4)\nMajor bite times: {mabt}\nMinor bite times: {mibt}\n"

	return bite_ref


def tides():
	# Annoying website, need to pretend to be a browser
	header = {
		"User-Agent":
			"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
		"X-Requested-With":
			"XMLHttpRequest"
	}

	tide_times = 'https://www.tideschart.com/Ireland/Leinster/Dublin-City/Dublin/Weekly/'

	tide_table = read_html(requests.get(tide_times, headers=header).text)[0]

	tide_ref = {}
	for i in range(7):
		t1, t2, t3 = tide_table.values[i][1], tide_table.values[i][2], tide_table.values[i][3]

		# Deals with NaN value if a day only has 3 tides
		t4 = tide_table.values[i][4] if not isna(tide_table.values[i][4]) else ""

		# index doesnt care if a line is blank, just outputs blank, also underline "Tides"
		tide_ref[i] = f"\033[4mTides:\033[0m\n{t1[:5]} {t1[8:]}\n{t2[:5]} {t2[8:]}\n{t3[:5]} {t3[8:]}\n{t4[:5]} {t4[8:]}"

	return tide_ref


def main():
	fish_dict = fishing()
	tide_dict = tides()

	for i in range(7):
		f_entry = fish_dict[i]
		t_entry = tide_dict[i]

		# underline
		print(f"\033[4m{f_entry[:11]}\033[0m{f_entry[11:]}\n{t_entry}\n\n")


if __name__ == '__main__':
	main()
