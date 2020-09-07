import requests
from pandas import read_html, isna


def fishing():
	fishing_times = read_html('https://www.fishingreminder.com/IE/charts/fishing_times/Dublin')[0]

	# Create dict for bite times
	bite_reference = {}
	for i in range(7):
		day, mabt, mibt = fishing_times.values[i][0], fishing_times.values[i][2], fishing_times.values[i][3]
		bite_reference[i] = f"{day}\nMajor bite times: {mabt}\nMinor bite times: {mibt}\n"

	return bite_reference


def tides():
	# Annoying website, need to pretend to be a browser
	header = {
		"User-Agent":
			"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
		"X-Requested-With":
			"XMLHttpRequest"
	}

	# tide_times = read_html('https://www.tide-forecast.com/locations/Dublin-Ireland/forecasts/latest/six_day')[0]
	tide_times = 'https://www.tideschart.com/Ireland/Leinster/Dublin-City/Dublin/Weekly/'

	r = requests.get(tide_times, headers=header)

	return read_html(r.text)[0]


def main():
	fish_dict = fishing()
	tide_table = tides()

	for i in range(7):
		entry = fish_dict[i]

		t1, t2, t3 = tide_table.values[i][1], tide_table.values[i][2], tide_table.values[i][3]

		# Deals with NaN value if a day only has 3 tides
		t4 = tide_table.values[i][4] if not isna(tide_table.values[i][4]) else ""

		# underline date
		print(f"\033[4m{entry[:11]}\033[0m{entry[11:]}")

		# index doesnt care if a line is blank, just outputs blank
		print(f"\033[4mTides:\033[0m\n{t1[:5]} {t1[8:]}\n{t2[:5]} {t2[8:]}\n{t3[:5]} {t3[8:]}\n{t4[:5]} {t4[8:]}\n\n")


if __name__ == '__main__':
	main()
