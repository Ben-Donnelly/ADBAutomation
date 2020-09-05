from pandas import read_html


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

	tide_times = read_html('https://www.tide-forecast.com/locations/Dublin-Ireland/forecasts/latest/six_day')[0]

	return tide_times


def main():
	fish_dict = fishing()
	tide_table = tides()

	# 3 entries are returned for each day
	# init a list to store days that
	# have already been used
	days_l = []

	x = ""
	# Count needed here
	# to stop duplicates
	count = 0
	for i in range(1, 19):
		day = tide_table[i][2]

		if day not in days_l:
			days_l.append(day)

			entry = fish_dict[count]
			try:
				# underline date
				x += f"\n\033[4m{entry[:11]}\033[0m{entry[11:]}"
				count += 1
			except KeyError:
				break
		# High tide and low tide
		x += f"{tide_table[i][5]}m\n{tide_table[i][6]}m\n"

	# tide td on website may not have
	# an entry for either low or high tide (i.e. nan entry)
	# so regex them out
	x = x.replace('nanm', '')

	print(x)


if __name__ == '__main__':
	main()


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
