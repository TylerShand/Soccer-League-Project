import csv

# Sort a csv file of player info evenly into three teams
# Team names passed in after file
def sort_players(file, team1_name, team2_name, team3_name):

    # Create three teams list with the team name at index 0
    team1 = [team1_name]
    team2 = [team2_name]
    team3 = [team3_name]

    # Convert csv_file to dict separate dicts
    with open(file, newline='') as csv_file:
        player_reader = csv.DictReader(csv_file, delimiter=',')
        # Store Dicts in a list
        players = list(player_reader)
        # Variable to hold a list of players with soccer experience
        skilled_players = []
        for player in players:
            if player['Soccer Experience'] == 'YES':
                skilled_players.append(player)
                players.remove(player)
        # Variable to hold the maximum number of UNSKILLED players allowed on each team
        max_players = (len(players) / 3)
        # Variable to hold the maximum number of UNSKILLED players + SKILLED players allowed on each team
        max_skilled_players = (len(skilled_players) / 3) + max_players

        # Sort UNSKILLED players into teams
        for player in players:
            if len(team1) <= max_players:
                team1.append(player)
            elif len(team2) <= max_players:
                team2.append(player)
            else:
                team3.append(player)

        # Sort SKILLED players into teams
        for player in skilled_players:
            if len(team1) <= max_skilled_players:
                team1.append(player)
            elif len(team2) <= max_skilled_players:
                team2.append(player)
            else:
                team3.append(player)

    return team1, team2, team3

# Write three teams with their respective players to the specified file
# Teams are sliced to start at index 1 to prevent the team name from being mistaken for a player
def write_teams(file, team1, team2, team3):
    with open(file, 'w') as file:
        file.write(team1[0] + '\n')
        for player in team1[1:]:
            file.write("{}, {}, {} \n".format(player['Name'], player['Soccer Experience'], player['Guardian Name(s)']))

        file.write(team2[0] + '\n')
        for player in team2[1:]:
            file.write("{}, {}, {} \n".format(player['Name'], player['Soccer Experience'], player['Guardian Name(s)']))

        file.write(team3[0] + '\n')
        for player in team3[1:]:
            file.write("{}, {}, {} \n".format(player['Name'], player['Soccer Experience'], player['Guardian Name(s)']))

# Write letters individually to players on the specified teams
# Teams are sliced to start at index 1 to prevent a letter being sent to the team name
def write_player_letters(team1, team2, team3):
    for player in team1[1:]:
        filename = 'player_letters/' + player['Name'] + '.txt'
        with open(filename, 'w') as letter:
            letter.write('Dear {},\n'.format(player['Guardian Name(s)']))
            letter.write('We are happy to that {} has joined our soccer league! The first game will be on the 10th of February.\n'.format(player['Name']))
            letter.write('{} will be playing on the {} team; be sure to bring all the required equipment: shin-guards, cleats, \n'.format(player['Name'], team1[0]))
            letter.write('etc. We hope to see you all there!\n')
            letter.write('Sincerely,\nVirginia Soccer League')
    for player in team2[1:]:
        filename = 'player_letters/' + player['Name'] + '.txt'
        with open(filename, 'w') as letter:
            letter.write('Dear {},\n'.format(player['Guardian Name(s)']))
            letter.write(
                'We are happy to that {} has joined our soccer league! The first game will be on the 10th of February.\n'.format(
                    player['Name']))
            letter.write(
                '{} will be playing on the {} team; be sure to bring all the required equipment: shin-guards, cleats, \n'.format(
                    player['Name'], team2[0]))
            letter.write('etc. We hope to see you all there!\n')
            letter.write('Sincerely,\nVirginia Soccer League')
    for player in team3[1:]:
        filename = 'player_letters/' + player['Name'] + '.txt'
        with open(filename, 'w') as letter:
            letter.write('Dear {},\n'.format(player['Guardian Name(s)']))
            letter.write(
                'We are happy to that {} has joined our soccer league! The first game will be on the 10th of February.\n'.format(
                    player['Name']))
            letter.write(
                '{} will be playing on the {} team; be sure to bring all the required equipment: shin-guards, cleats, \n'.format(
                    player['Name'], team3[0]))
            letter.write('etc. We hope to see you all there!\n')
            letter.write('Sincerely,\nVirginia Soccer League')

def main():
    teams = 'Sharks', 'Dragons', 'Raptors'
    # Holds the tuple return value from sort_players
    teams = sort_players('soccer_players.csv', *teams)

    # Writes teams and players to teams.txt
    write_teams('teams.txt', *teams)

    # Write letters to players on the Sharks, Dragons, and the Raptors teams
    write_player_letters(*teams)

# Check if running directly
if __name__ == '__main__':
    main()



