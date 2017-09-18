
## calculate the odds that at least one streak of a certain length (or greater)
## occurs in a season of a certain length, given a team's win probability

## Note: this is not *quite* correct -- it double counts a season in which there are
## multiple streaks of the desired length of longer. In that sense, it correctly
## answers a different question -- how many streaks of this length would we expect
## to see per season? -- and the error is also very close to irrelevant for long
## streaks, such as the Indians 22-game streak in a 162-game season.

## other solutions and discussion here:
## https://math.stackexchange.com/questions/383704/probability-of-streaks

win_prob = 0.65
streak = 22
season = 162

prob_sum = 0
for i in range(streak, season):
    ## loop through every possible streak length from desired up to
    ## one less than season length

    ## simple odds of n wins in n games:
    streak_odds = win_prob ** i

    ## odds of a sequence such as L W W W L [wins bracketed by a losses, to ensure
    ## it's the exact right length for a streak]
    l_streak_l_odds = streak_odds * (1 - win_prob) * (1 - win_prob)
    ## how many opportunities are there to start a sequence of, e.g. L W W W L ?
    l_streak_l_chances = season - i - 1
    ## overall probability of some L [streak] L sequence in the whole season
    l_streak_l_total = l_streak_l_odds * l_streak_l_chances

    ## also the possibility that a streak of this length either starts or ends the
    ## season, e.g. [streak] L or L [streak]
    start_or_end_odds = streak_odds * (1 - win_prob)
    start_or_end_chances = 2
    ## overall probability of one of these outcomes
    start_or_end_total = start_or_end_odds * start_or_end_chances

    ## toal probability of L [streak] L or streak and beginning or end of season
    this_streak_total = l_streak_l_total + start_or_end_total

    ## add probability of *this* streak length to total probability of all streaks
    prob_sum += this_streak_total

## also possibility for entire-season streak
season_streak = win_prob ** season
prob_sum += season_streak

print 'streak-in-season probability:', prob_sum
print '... or once every', 1 / prob_sum, 'seasons'
