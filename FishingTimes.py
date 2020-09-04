from pandas import read_html, set_option
set_option('display.max_columns', None)

def fishing():
	# data = get('https://www.fishingreminder.com/IE/charts/fishing_times/Dublin')

	table = read_html('https://www.fishingreminder.com/IE/charts/fishing_times/Dublin')[0]

	# print(table.T)
	# print()
	# print()
	# print(table.columns)
	# print()
	# print()
	for i in range(6):
		x = table.values[i]
		print(f"{x[0]}\nMajor: {x[2]}\nMinor: {x[3]}\n")

	# rating_col = {
	# 	1 : Fore.RED,
	# 	2 : Fore.LIGHTYELLOW_EX,
	# 	3 : Fore.GREEN,
	# 	4 : Fore.GREEN
	# }
	#
	# soup = BeautifulSoup(data.text, 'html.parser')
	# tree = html.fromstring(data.content)
	#
	#
	# rating = tree.xpath('//*[@id="static"]/div[1]/div[2]/div[1]/p[1]/b[1]/text()')[0]
	# # Change 'out of' to /
	#
	# sun_rise = tree.xpath('//*[@id="static"]/div[1]/div[2]/div[1]/p[1]/b[3]/text()')[0]
	# sun_set = tree.xpath('//*[@id="static"]/div[1]/div[2]/div[1]/p[1]/b[4]/text()')[0]
	#
	# first_major = tree.xpath('//*[@id="static"]/div[1]/div[2]/div[1]/p[3]/b[2]/text()')[0]
	# second_major = tree.xpath('//*[@id="static"]/div[1]/div[2]/div[1]/p[3]/b[4]/text()')[0]
	#
	# first_minor = tree.xpath('//*[@id="static"]/div[1]/div[2]/div[1]/p[4]/b[2]/text()')[0]
	# second_minor = tree.xpath('//*[@id="static"]/div[1]/div[2]/div[1]/p[4]/b[4]/text()')[0]
	# print(f"Today's rating: {rating_col[int(rating[0])]}{rating[0]}/{rating[9]}")
	# print(f"{Fore.RESET}Sun Rise: {sun_rise}\nSun Set: {sun_set}")
	#
	# print(f"Best times begin at {Fore.GREEN + first_major + Fore.RESET} and {Fore.GREEN + second_major + Fore.RESET} and will last for about 2 hours")
	# print(f"Then {Fore.RED + first_minor + Fore.RESET} and {Fore.RED + second_minor + Fore.RESET} for 1-2 hours (potentially less activity){Fore.RESET}\n\n")

	# print(tree.xpath('//*[@id="forecast_table"]/div/div/div[2]/div/table/tbody/text()'))

# def tides():
# 	data = get('https://www.tide-forecast.com/locations/Dublin-Ireland/forecasts/latest/six_day')
# 	tree = html.fromstring(data.content)
#
# 	soup = BeautifulSoup(data.text, 'html.parser')
#
# 	for idx, tr in enumerate(soup.find_all('tr', {'class' : 'tin sma'})):
# 		y = " ".join(tr.text.split()).strip()
# 		# y = y.replace(" ", "\n")
#
# 		t = y[20:].split()
#
# 		# print(y[20:].split()[::2])
# 		# print(y[20:].split()[::3])
#
# 		height = {0 : 'High Tide:', 1 : 'Low Tides'}
# 		days = {0 : 'Mon:', 1 : 'Tue', 2 : 'Wed', 3 : 'Thur', 4 : 'Fri', 5 : 'Sat', 6 : 'Sun'}
#
# 		# problem with 3 tides check if can pull columns ftom tables instead
# 		count = 0
# 		print(f'''   {height[idx]}''')
# 		for i, (x, y) in enumerate(zip(t[::2], t[1::2])):
# 			if i % 2 == 0:
# 				print(days[count])
# 				count += 1
# 				# count += 1
# 			print('\n'.join(['%s %s : %sm' % (i, x, y)]))
# 		# print('\n'.join(['%s %s : %sm'%(i, x, y) for i, (x, y) in enumerate(zip(t[::2], t[1::2]))]))
# 		print()


	# table = tree.xpath('//*[@id="forecasts"]')[0]


	# table = xml.xpath("//table[@class='datadisplaytable']")[0]

	# xml = html.fromstring(h)
	# gets the table
	# table = xml.xpath("//table[@class='datadisplaytable']")[0]

	# iterate over all the rows
	# for row in table.xpath(".//tr"):
	# 	# get the text from all the td's from each row
	# 	print([row.text])

	# rows = []
	# for tr in soup.select('tr'):
	# 	rows.append([td.get_text(strip=True) for td in tr.select('tr, td')])
	#
	# rows = [*zip(*rows)]  # transpose values
	#
	# for row in rows:
	# 	print(''.join(r'{: <5}'.format(d) for d in row))

def tides():
	Fishing_times = read_html('https://www.fishingreminder.com/IE/charts/fishing_times/Dublin')[0]

	d = {}
	for i in range(6):
		x = Fishing_times.values[i]
		d[i] = f"{x[0]}\nMajor bite times: {x[2]}\nMinor bite times: {x[3]}\n"
		# print(f"{x[0]}\nMajor: {x[2]}\nMinor: {x[3]}\n")
	# print(d)

	table = read_html(
		'https://www.tide-forecast.com/locations/Dublin-Ireland/forecasts/latest/six_day')[0]

	days_l = []

	x = ""
	count = 0
	for i in range(1, 19):
		if table[i][2] not in days_l:
			days_l.append(table[i][2])

			if count == 0:
				x += f"\033[4m{d[count][:11]}\033[0m{d[count][11:]}\n"
				count += 1
			else:
				try:
					x += f"\n\033[4m{d[count][:11]}\033[0m{d[count][11:]}"
					count += 1
				except KeyError:
					break



		x += (f"{table[i][5]}m\n{table[i][6]}m\n")
	x = x.replace('nan', '')
	x = x.replace('\nm\n', '\n\n')
	# x = re.sub("(\w\s)","\1\n", x)

	print(x)

	f = 10


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

if __name__ == '__main__':
	tides()
