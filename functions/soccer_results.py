def soccer_scores(first_team_scores, second_team_scores ):
    """ A function that takes two integer arguments that represents a
        soccer result and prints the winner from the score  """
    if first_team_scores > second_team_scores:
        print(f"Final score is {first_team_scores}:{second_team_scores} \nTeam one won the match")
    elif first_team_scores == second_team_scores:
        print(f"Final score is {first_team_scores}:{second_team_scores} \nMatch ended in a draw")
    else:
        print(f"Final score is {second_team_scores}:{first_team_scores} \nTeam two won the match")

soccer_scores(3,2)