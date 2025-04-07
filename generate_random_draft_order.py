"""
QPFL Offensive Line Draft 2024
"""

import random

teams = [
    "Griffin",
    "Ryan",
    "Kaminska",
    "Reardon",
    "Stephen",
    "Spencer/Tim",
    "Joe/Joe",
    "Anagh",
    "Bill",
    "Arnav",
]

order = random.sample(teams, len(teams))

for team in order:
    print(team)