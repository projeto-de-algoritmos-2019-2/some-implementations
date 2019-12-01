gas_station = [
	(0, 15),
	(12, 15),
	(14, 15),
	(20, 15),
	(25, 15),
	(30, 15),
	(40, 15),
	(45, 15),
]

gas_station.sort(reverse=True) # n*log(n)

at, max_range = 0, 0
stopped_at = []

destination = 60

while max_range < destination and gas_station:

	furthest_gas_station = None

	while gas_station and gas_station[-1][0] <= max_range:
		furthest_gas_station = gas_station.pop()

	if furthest_gas_station == None:
		print("Impossible")

	else:
		stopped_at.append(furthest_gas_station)

		at = furthest_gas_station[0]
		max_range = at + furthest_gas_station[1]


if(max_range >= destination):
	print(stopped_at)