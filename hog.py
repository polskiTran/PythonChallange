"""The Game of Hog."""


from dice import four_sided, six_sided, make_test_dice
import doctest
GOAL_SCORE = 100  # The goal of Hog is to score 100 points.
######################
# Phase 1: Simulator #
######################

# RQ1


def roll_dice(num_rolls, dice=six_sided):
    """
    >>> roll_dice(1,make_test_dice(4, 2, 1, 3))
    4
    >>> roll_dice(2,make_test_dice(4, 2, 1, 3))
    6
    >>> roll_dice(3,make_test_dice(4, 2, 1, 3))
    1
    >>> roll_dice(4,make_test_dice(4, 2, 1, 3))
    1
    """
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    # BEGIN Question 1
    "*** REPLACE THIS LINE ***"
    score = []
    for i in range(num_rolls):
        score.append(dice())
    if 1 not in score:
        return sum(score)
    else:
        return 1
    # END Question 1

# RQ2


def take_turn(num_rolls, opponent_score, dice=six_sided):
    """
    >>> take_turn(2, 0, make_test_dice(4, 6, 1))
    10
    >>> take_turn(3, 0, make_test_dice(4, 6, 1))
    1
    >>> take_turn(0, 35)
    6
    >>> take_turn(0, 71)
    8
    >>> take_turn(0, 7)
    8
    >>> take_turn(0, 0)
    1
    >>> take_turn(0, 9)
    10
    >>> take_turn(2, 0, make_test_dice(6))
    12
    >>> take_turn(0, 50)
    6
    """
    """Simulate a turn rolling NUM_ROLLS dice, which may be 0 (Free bacon).

    num_rolls:       The number of dice rolls that will be made.
    opponent_score:  The total score of the opponent.
    dice:            A function of no args that returns an integer outcome.
    """
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    assert opponent_score < 100, 'The game should be over.'
    # BEGIN Question 2
    "*** REPLACE THIS LINE ***"
    score = 0
    if num_rolls == 0:
        return 1 + max(opponent_score // 10, opponent_score % 10)
    else:
        score = roll_dice(num_rolls, dice)
        return score
    # END Question 2

# RQ3


def select_dice(score, opponent_score):
    """
    >>> select_dice(4, 24) == four_sided
    True
    >>> select_dice(16, 64) == four_sided
    False
    >>> select_dice(0, 0) == four_sided
    True
    >>> select_dice(50, 80) == four_sided
    False
    """
    """Select six-sided dice unless the sum of SCORE and OPPONENT_SCORE is a
    multiple of 7, in which case select four-sided dice (Hog wild).
    """
    # BEGIN Question 3
    "*** REPLACE THIS LINE ***"
    if ((score + opponent_score) % 7 == 0):
        return four_sided
    else:
        return six_sided
    # END Question 3

# RQ4


def is_swap(score0, score1):
    """
    >>> is_swap(19, 91)
    True
    >>> is_swap(20, 40)
    False
    >>> is_swap(41, 14)
    True
    >>> is_swap(23, 42)
    False
    >>> is_swap(55, 55)
    True
    >>> is_swap(114, 41) # We check the last two digits
    True
    """
    """Return True if ending a turn with SCORE0 and SCORE1 will result in a
    swap.

    Swaps occur when the last two digits of the first score are the reverse
    of the last two digits of the second score.
    """
    # BEGIN Question 4
    "*** REPLACE THIS LINE ***"
    score0List = []
    score1List = []
    score0Str = str(score0)
    score1Str = str(score1)
    # check for 1 digit and 2 digits case
    if len(score0Str) == 1:
        score0List = [0] + score0List
    elif len(score0Str) > 2:
        score0Str = score0Str[1::]
    if len(score1Str) == 1:
        score1List = [0] + score1List
    elif len(score1Str) > 2:
        score1Str = score1Str[1::]
    # convert to list
    score0Map = [digit for digit in score0Str]
    score0List = score0List + list(score0Map)
    score1Map = [digit for digit in score1Str]
    score1List = score1List + list(score1Map)
    # check for swap
    if (score0List[0] == score1List[1]) and (score0List[1] == score1List[0]):
        # temp = score0List
        # score0List = score1List
        # score1List = temp
        return True
    else:
        return False
    # END Question 4

# RQ5


def other(who):
    """Return the other player, for a player WHO numbered 0 or 1.

    >>> other(0)
    1
    >>> other(1)
    0
    """
    return 1 - who


# RQ6
def play(strategy0, strategy1, score0=0, score1=0, goal=GOAL_SCORE):
    """
    >>> four_sided = make_test_dice(1)
    >>> six_sided = make_test_dice(3)
    >>> always = always_roll
    >>> play(always(5), always(3), score0=91, score1=10)
    (106, 10)

    >>> play(always(5), always(5), goal=10)
    (1, 15)

    >>> play(always(5), always(3), score0=36, score1=15, goal=50)
    (15, 51)

    >>> # Swine swap applies to 3 digit scores
    >>> play(always(5), always(3), score0=98, score1=31)
    (31, 113)

    >>> # Goal edge case
    >>> play(always(4), always(3), score0=88, score1=20)
    (100, 20)
    """
    """Simulate a game and return the final scores of both players, with
    Player 0's score first, and Player 1's score second.

    A strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    strategy0:  The strategy function for Player 0, who plays first
    strategy1:  The strategy function for Player 1, who plays second
    score0   :  The starting score for Player 0
    score1   :  The starting score for Player 1
    """
    who = 0  # Which player is about to take a turn, 0 (first) or 1 (second)
    # BEGIN Question 5
    tempScore = 0
    numRoll0 = strategy0(score0, score1)
    numRoll1 = strategy1(score1, score0)
    "*** REPLACE THIS LINE ***"
    diceType = ""
    while True:
        if who == 0:
            diceType = select_dice(score0, score1)  # Hog Wild
            # Rolling dice, Free bacon
            score0 += take_turn(numRoll0, score1, dice=diceType)
            # Check if need to swap score (Swine swap)
            if (is_swap(score0, score1)):
                tempScore = score0
                score0 = score1
                score1 = tempScore
            who = other(who)
        else:
            diceType = select_dice(score1, score0)  # Hog Wild
            # Rolling dice, Free bacon
            score1 += take_turn(numRoll1, score0, dice=diceType)
            # Check if need to swap score (Swine swap)
            if (is_swap(score0, score1)):
                tempScore = score0
                score0 = score1
                score1 = tempScore
            who = other(who)
        if (score0 >= goal) or (score1 >= goal):
            break
    # END Question 5
    return score0, score1


def always_roll(n):
    """Return a strategy that always rolls N dice.

    A strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    >>> strategy = always_roll(5)
    >>> strategy(0, 0)
    5
    >>> strategy(99, 99)
    5
    """
    def strategy(score, opponent_score):
        return n
    return strategy

#######################
# Phase 2: Strategies #
#######################


# Experiments


def make_averaged(fn, num_samples=1000):
    """Return a function that returns the average_value of FN when called.

    To implement this function, you will have to use *args syntax, a new Python
    feature introduced in this project.  See the project description.

    >>> dice = make_test_dice(3, 1, 5, 6)
    >>> averaged_dice = make_averaged(dice, 1000)
    >>> averaged_dice()
    3.75
    >>> make_averaged(roll_dice, 1000)(2, dice)
    6.0

    In this last example, two different turn scenarios are averaged.
    - In the first, the player rolls a 3 then a 1, receiving a score of 1.
    - In the other, the player rolls a 5 and 6, scoring 11.
    Thus, the average value is 6.0.
    """
    # BEGIN Question 6
    "*** REPLACE THIS LINE ***"
    def average(*args):
        total = 0
        for i in range(num_samples):
            total += fn(*args)
        return total / num_samples
    return average
    # def average(*args):
    #     total = 0
    #     repeat = num_samples

    #     while repeat > 0:
    #         total = total + fn(*args)
    #         repeat -= 1

    #     avg = total / num_samples
    #     return avg

    # return average
    # END Question 6


def max_scoring_num_rolls(dice=six_sided, num_samples=1000):
    """Return the number of dice (1 to 10) that gives the highest average turn
    score by calling roll_dice with the provided DICE over NUM_SAMPLES times.
    Assume that dice always return positive outcomes.

    >>> dice = make_test_dice(3)
    >>> max_scoring_num_rolls(dice)
    10
    """
    # BEGIN Question 7
    "*** REPLACE THIS LINE ***"
    maxScore = 0
    maxScoreDiceNum = 0
    for numDice in range(1, 11):
        if maxScore < make_averaged(roll_dice, num_samples)(numDice, dice):
            maxScore = make_averaged(roll_dice, num_samples)(numDice, dice)
            maxScoreDiceNum = numDice
    return maxScoreDiceNum
    # END Question 7


def winner(strategy0, strategy1):
    """Return 0 if strategy0 wins against strategy1, and 1 otherwise."""
    score0, score1 = play(strategy0, strategy1)
    if score0 > score1:
        return 0
    else:
        return 1


def average_win_rate(strategy, baseline=always_roll(5)):
    """Return the average win rate (0 to 1) of STRATEGY against BASELINE."""
    win_rate_as_player_0 = 1 - make_averaged(winner)(strategy, baseline)
    win_rate_as_player_1 = make_averaged(winner)(baseline, strategy)
    return (win_rate_as_player_0 + win_rate_as_player_1) / 2  # Average results


def run_experiments():
    """Run a series of strategy experiments and report results."""
    if False:  # Change to False when done finding max_scoring_num_rolls
        six_sided_max = max_scoring_num_rolls(six_sided)
        print('Max scoring num rolls for six-sided dice:', six_sided_max)
        four_sided_max = max_scoring_num_rolls(four_sided)
        print('Max scoring num rolls for four-sided dice:', four_sided_max)

    if True:  # Change to True to test always_roll(8)
        print('always_roll(8) win rate:', average_win_rate(always_roll(8)))

    if True:  # Change to True to test bacon_strategy
        print('bacon_strategy win rate:', average_win_rate(bacon_strategy))

    if True:  # Change to True to test swap_strategy
        print('swap_strategy win rate:', average_win_rate(swap_strategy))

    if True:  # Change to True to test final_strategy
        print('final_strategy win rate:', average_win_rate(final_strategy))

    "*** You may add additional experiments as you wish ***"

# Strategies


def bacon_strategy(score, opponent_score, margin=8, num_rolls=5):
    """This strategy rolls 0 dice if that gives at least MARGIN points,
    and rolls NUM_ROLLS otherwise.
    """
    # BEGIN Question 8
    "*** REPLACE THIS LINE ***"
    if (1 + max(opponent_score // 10, opponent_score % 10)) >= margin:
        score += (1 + max(opponent_score // 10, opponent_score % 10))
        return 0
    else:
        return num_rolls
    # END Question 8


def swap_strategy(score, opponent_score, margin=8, num_rolls=5):
    """This strategy rolls 0 dice when it results in a beneficial swap and
    rolls NUM_ROLLS if rolling 0 dice results in a harmful swap. It also
    rolls 0 dice if that gives at least MARGIN points and rolls NUM_ROLLS
    otherwise.
    """
    # BEGIN Question 9
    "*** REPLACE THIS LINE ***"
    zeroRollSCore = score + \
        (1 + max(opponent_score // 10, opponent_score % 10))
    if is_swap(zeroRollSCore, opponent_score) and zeroRollSCore > opponent_score:
        return num_rolls
    elif is_swap(zeroRollSCore, opponent_score) and zeroRollSCore < opponent_score:
        return 0
    else:
        return bacon_strategy(score, opponent_score, margin, num_rolls)
    # END Question 9


def final_strategy(score, opponent_score, margin=8, num_rolls=5):
    """Write a brief description of your final strategy.

    *** YOUR DESCRIPTION HERE ***
    """
    # BEGIN Question 10
    "*** REPLACE THIS LINE ***"
    zeroRollSCore = score + \
        (1 + max(opponent_score // 10, opponent_score % 10))

    if select_dice(score, opponent_score) == "six_sided":
        if score >= 90:
            bacon_strategy(score, opponent_score, margin=5, num_rolls=2)
            num_rolls = num_rolls - 3
            # return num_rolls - 3
        elif score >= 80:
            num_rolls = num_rolls - 2
            # return num_rolls - 2
    else:
        if score >= 90:
            num_rolls = num_rolls - 4
            # return num_rolls - 4
        elif score >= 80:
            num_rolls = num_rolls - 3
            # return num_rolls - 3

    if is_swap(zeroRollSCore, opponent_score) and zeroRollSCore > opponent_score:
        if (select_dice(zeroRollSCore, opponent_score) == "four_sided") and ((opponent_score - zeroRollSCore)) < 5:
            return 0
        else:
            return num_rolls
    elif is_swap(zeroRollSCore, opponent_score) and zeroRollSCore < opponent_score:
        return 0
    else:
        return bacon_strategy(score, opponent_score, margin, num_rolls)

    # Test2
    # turn_score = take_turn(0, opponent_score) + score

    # if turn_score >= 100 and not is_swap(turn_score, opponent_score):
    #     return 0

    # if swap_strategy(score, opponent_score) == 0:
    #     return 0

    # if bacon_strategy(score, opponent_score) == 0:
    #     if is_swap(take_turn(0, opponent_score) + score, opponent_score):
    #         if opponent_score > take_turn(0, opponent_score) + score:
    #             return 0
    #         else:
    #             return 4
    #     else:
    #         return 0

    # if select_dice(score + take_turn(0, opponent_score), opponent_score) == four_sided:
    #     return 0

    # return 4
    # END Question 10


##########################
# Command Line Interface #
##########################

# Note: Functions in this section do not need to be changed.  They use features
#       of Python not yet covered in the course.


# @main
def run(*args):
    """Read in the command-line argument and calls corresponding functions.

    This function uses Python syntax/techniques not yet covered in this course.
    """
    import argparse
    parser = argparse.ArgumentParser(description="Play Hog")
    parser.add_argument('--final', action='store_true',
                        help='Display the final_strategy win rate against always_roll(5)')
    parser.add_argument('--run_experiments', '-r', action='store_true',
                        help='Runs strategy experiments')
    args = parser.parse_args()

    # if args.run_experiments:
    #     run_experiments()
    # elif args.final:
    #     from hog_eval import final_win_rate
    #     win_rate = final_win_rate()
    #     print('Your final_strategy win rate is')
    #     print('    ', win_rate)
    #     print('(or {}%)'.format(round(win_rate * 100, 2)))


if __name__ == "__main__":
    # uncomment 2 line below to test play
    four_sided = make_test_dice(1)  # For testing play
    six_sided = make_test_dice(3)  # For testing play

    # doctest
    doctest.testmod(verbose=True)

    # testing for extra credit
    run_experiments()
