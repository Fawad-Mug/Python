def main():
    file = open('player_record.txt', 'r')
    number_of_players = int(file.readline())
    print(f'Number of players: {number_of_players}')
    player_number = 1
    while player_number < number_of_players:
        print(f'Player {player_number}:',end ='')
        number_of_matches = int(file.readline())
        matches = 1
        total_runs = 0
        while matches <= number_of_matches:
            runs = int(file.readline())
            print(runs, end=' ')
            total_runs = total_runs + runs
            if matches == 1:
                max_runs = runs
            elif runs > max_runs:
                max_runs = runs
            matches = matches + 1
        average = total_runs / number_of_matches
        if player_number == 1:
            overall_max_runs = max_runs
            best_average = average
            best_player_no = 1
        else:
            if best_average < average:
                best_average = average
                best_player_no = player_number
            if overall_max_runs < max_runs:
                overall_max_runs = max_runs
        player_number = player_number + 1
        print(f'Average: {average}\t Max: {max_runs}')
    print(f'Player {best_player_no} has best average')
    print(f'The highest runs are {overall_max_runs}')

main()


