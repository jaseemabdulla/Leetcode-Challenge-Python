# Number of Flowers in Full Bloom

# You are given a 0-indexed 2D integer array flowers, where flowers[i] = [starti, endi] means the ith flower will be in full bloom from starti to endi (inclusive). You are also given a 0-indexed integer array people of size n, where people[i] is the time that the ith person will arrive to see the flowers.

# Return an integer array answer of size n, where answer[i] is the number of flowers that are in full bloom when the ith person arrives.

class Solution(object):
    def fullBloomFlowers(self, flowers, people):
        from collections import defaultdict

        # Create a defaultdict to track bloom intervals
        blooming_intervals = defaultdict(int)

        # Iterate through the flower intervals and update bloom_interval
        for start, end in flowers:
            blooming_intervals[start] += 1
            blooming_intervals[end + 1] -= 1

        # Initialize dictionaries and variables
        blooming_status, bloom_count = {}, 0
        remaining_persons = sorted(people, reverse=True)  # Sort persons in reverse order

        # Iterate through sorted bloom times
        for time in sorted(blooming_intervals.keys()):
            bloom_change = blooming_intervals[time]  # Get bloom change at this time

            # Process persons whose bloom time has arrived
            while remaining_persons and time > remaining_persons[-1]:
                blooming_status[remaining_persons.pop()] = bloom_count

            # If there are no remaining persons, exit the loop
            if not remaining_persons:
                break

            bloom_count += bloom_change  # Update bloom count

        # Create a list of bloom statuses for each person
        return [blooming_status[p] if p in blooming_status else 0 for p in people]