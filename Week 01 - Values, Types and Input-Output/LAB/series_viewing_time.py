"""Calculate total viewing time for the five-season series."""

season_1_episodes = 10
other_episodes = 4 * 10

season_1_seconds = season_1_episodes * (45 * 60 + 35)
other_seasons_seconds = other_episodes * (35 * 60 + 15)
total_seconds = season_1_seconds + other_seasons_seconds

hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60

print(f"Total time: {hours}h {minutes}m {seconds}s")

# With the durations in the task, the total is 31h 5m 50s; the supplied
# example output (39h 30m 0s) does not match those durations.
