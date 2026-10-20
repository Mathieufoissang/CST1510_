"""Project savings over three years using arithmetic and augmented assignment."""

weeks_per_year = 52
years = 3
weekly_saving = 10
year_1_weekly_bonus = 20
sister_withdrawal = 0.50

total_weeks = weeks_per_year * years
savings = weekly_saving * total_weeks
savings += year_1_weekly_bonus * weeks_per_year
savings -= (total_weeks // 2) * sister_withdrawal

print(f"Final savings after {years} years: £{savings:.2f}")

# Following the stated amounts gives £2,561.00; the supplied example output
# (£4,689.50) does not match the stated assumptions.
