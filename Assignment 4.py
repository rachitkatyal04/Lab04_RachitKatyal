class Match:
    def __init__(self, location, team1, team2, timing):
        self.location = location
        self.team1 = team1
        self.team2 = team2
        self.timing = timing

class FlightTable:
    def __init__(self):
        self.matches = []

    def addmatch(self, match):
        self.matches.append(match)

    def searchbyteam(self, team_name):
        result = []
        for match in self.matches:
            if team_name in [match.team1, match.team2]:
                result.append(match)
        return result

    def searchbylocation(self, location):
        result = []
        for match in self.matches:
            if match.location == location:
                result.append(match)
        return result

    def searchbytiming(self, timing):
        result = []
        for match in self.matches:
            if match.timing == timing:
                result.append(match)
        return result

    def print_matches(self, matches):
        if not matches:
            print("No matches found.")
        else:
            print("Match Location\tTeam 01\tTeam 02\tTiming")
            for match in matches:
                print(f"{match.location}\t{match.team1}\t{match.team2}\t{match.timing}")

flight_table = FlightTable()
flight_table.addmatch(Match("Mumbai", "India", "Sri Lanka", "DAY"))
flight_table.addmatch(Match("Delhi", "England", "Australia", "DAY-NIGHT"))
flight_table.addmatch(Match("Chennai", "India", "South Africa", "DAY"))
flight_table.addmatch(Match("Indore", "England", "Sri Lanka", "DAY-NIGHT"))
flight_table.addmatch(Match("Mohali", "Australia", "South Africa", "DAY-NIGHT"))
flight_table.addmatch(Match("Delhi", "India", "Australia", "DAY"))

print("Select a search parameter:")
print("1. List of all the matches of a Team")
print("2. List of Matches on a Location")
print("3. List of Matches based on timing")
choice = input("Enter your choice (1-3): ")

if choice == "1":
    team_name = input("Enter the team name: ")
    matches = flight_table.searchbyteam(team_name)
    flight_table.print_matches(matches)
elif choice == "2":
    location = input("Enter the location: ")
    matches = flight_table.searchbylocation(location)
    flight_table.print_matches(matches)
elif choice == "3":
    timing = input("Enter the timing: ")
    matches = flight_table.searchbytiming(timing)
    flight_table.print_matches(matches)
else:
    print("Invalid choice.")