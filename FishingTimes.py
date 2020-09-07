import requests
from pandas import read_html, isna


def fishing():
	fishing_times = read_html('https://www.fishingreminder.com/IE/charts/fishing_times/Dublin')[0]

	# Create dict for bite times
	# The tide site goes up to 18
	# Due to there being a colspan of 3
	# 6 (days) * 3 (entries for each day = 18
	# Therefore to make sure that the tides and
	# bite times match up on their respective
	# days we create a dict to be used later
	bite_reference = {}
	for i in range(6):
		day, mabt, mibt = fishing_times.values[i][0], fishing_times.values[i][2], fishing_times.values[i][2]
		bite_reference[i] = f"{day}\nMajor bite times: {mabt}\nMinor bite times: {mibt}\n"

	return bite_reference


def tides():
	# Annoying website, need to pretend to be a browser
	header = {
		"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
		"X-Requested-With": "XMLHttpRequest"
	}

	# tide_times = read_html('https://www.tide-forecast.com/locations/Dublin-Ireland/forecasts/latest/six_day')[0]
	tide_times = 'https://www.tideschart.com/Ireland/Leinster/Dublin-City/Dublin/Weekly/'

	r = requests.get(tide_times, headers=header)

	return read_html(r.text)[0]


def main():
	fish_dict = fishing()
	tide_table = tides()

	for i in range(6):
		entry = fish_dict[i]

		t1, t2, t3= tide_table.values[i][1], tide_table.values[i][2], tide_table.values[i][3]
		t4 = tide_table.values[i][4] if not isna(tide_table.values[i][4]) else ""

		_t1 = t1[:5]
		_t2 = t2[:5]
		_t3 = t3[:5]

		_t4 = t4[:5] if not t4 == "" else ""

		# underline date
		print(f"\033[4m{entry[:11]}\033[0m{entry[11:]}")
		print(f"\n\033[4mTides:\033[0m\n{_t1} {t1[8:]}\n{_t2} {t2[8:]}\n{_t3} {t3[8:]}\n{_t4} {t4[8:]}\n")


if __name__ == '__main__':
	main()
	# tides()

# 1                                        Change units
# 2                                                 NaN
# 3                                         Time of Day
# 4                        Wave Height Map See all maps
# 5                               High Tide  height (m)
# 6                                Low Tide  height (m)
# 7                                 Swell (m) direction
# 8                                     Wave Height (m)
# 9                                          Period (s)
# 10                                       Wind  (km/h)
# 11                                                NaN
# 12                                                NaN
# 13                                            Summary
# 14                                            Rain mm
# 15                                            High °C
# 16                                             Low °C
# 17                                           Chill °C
# 18                                            Sunrise
# 19                                             Sunset
