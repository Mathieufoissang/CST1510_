"""Project population growth for each of the next five years."""

population = 312_032_486
seconds_per_year = 365 * 24 * 60 * 60

births_per_year = seconds_per_year // 7
deaths_per_year = seconds_per_year // 13
immigrants_per_year = seconds_per_year // 45
net_change_per_year = births_per_year - deaths_per_year + immigrants_per_year

for year in range(1, 6):
    population += net_change_per_year
    print(f"Year {year}: {population:,}")
