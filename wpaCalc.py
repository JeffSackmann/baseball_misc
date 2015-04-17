## Find win expectancy and volatility given inning, out, base, run situation.
 
## no. of runs that score with HR in diff. base situations
baseHr = {1: 1,
          2: 2,
          3: 2,
          4: 3,
          5: 2,
          6: 3,
          7: 3,
          8: 4
          }
    
tangoRunExp = {   '11': {   1: 0.6,
                              2: 0.243,
                              3: 0.097,
                              4: 0.037,
                              5: 0.014,
                              6: 0.006,
                              7: 0.002,
                              8: 0.001,
                              9: 0.0,
                              10: 0.0,
                              'b': 0.988,
                              'm': -0.296},
                    '12': {   1: 0.673,
                              2: 0.222,
                              3: 0.071,
                              4: 0.023,
                              5: 0.007,
                              6: 0.002,
                              7: 0.001,
                              8: 0.0,
                              9: 0.0,
                              10: 0.0,
                              'b': 1.014,
                              'm': -0.163},
                    '20': {   1: 0.424,
                              2: 0.299,
                              3: 0.15,
                              4: 0.072,
                              5: 0.032,
                              6: 0.013,
                              7: 0.005,
                              8: 0.002,
                              9: 0.001,
                              10: 0.0,
                              'b': 0.716,
                              'm': -0.278},
                    '21': {   1: 0.444,
                              2: 0.326,
                              3: 0.137,
                              4: 0.056,
                              5: 0.022,
                              6: 0.009,
                              7: 0.003,
                              8: 0.001,
                              9: 0.0,
                              10: 0.0,
                              'b': 0.863,
                              'm': -0.268},
                    '22': {   1: 0.453,
                              2: 0.374,
                              3: 0.116,
                              4: 0.039,
                              5: 0.012,
                              6: 0.005,
                              7: 0.001,
                              8: 0.0,
                              9: 0.0,
                              10: 0.0,
                              'b': 0.974,
                              'm': -0.194},
                    '30': {   1: 0.566,
                              2: 0.226,
                              3: 0.114,
                              4: 0.053,
                              5: 0.023,
                              6: 0.01,
                              7: 0.004,
                              8: 0.002,
                              9: 0.001,
                              10: 0.0,
                              'b': 0.559,
                              'm': -0.358},
                    '31': {   1: 0.594,
                              2: 0.234,
                              3: 0.104,
                              4: 0.042,
                              5: 0.017,
                              6: 0.006,
                              7: 0.003,
                              8: 0.001,
                              9: 0.0,
                              10: 0.0,
                              'b': 0.693,
                              'm': -0.191},
                    '32': {   1: 0.686,
                              2: 0.204,
                              3: 0.073,
                              4: 0.025,
                              5: 0.008,
                              6: 0.002,
                              7: 0.001,
                              8: 0.0,
                              9: 0.0,
                              10: 0.0,
                              'b': 0.832,
                              'm': -0.107},
                    '40': {   1: 0.362,
                              2: 0.256,
                              3: 0.194,
                              4: 0.104,
                              5: 0.048,
                              6: 0.02,
                              7: 0.009,
                              8: 0.004,
                              9: 0.002,
                              10: 0.001,
                              'b': 0.45,
                              'm': -0.167},
                    '41': {   1: 0.401,
                              2: 0.258,
                              3: 0.203,
                              4: 0.083,
                              5: 0.034,
                              6: 0.013,
                              7: 0.005,
                              8: 0.002,
                              9: 0.001,
                              10: 0.0,
                              'b': 0.669,
                              'm': -0.174},
                    '42': {   1: 0.494,
                              2: 0.237,
                              3: 0.181,
                              4: 0.06,
                              5: 0.018,
                              6: 0.007,
                              7: 0.002,
                              8: 0.001,
                              9: 0.0,
                              10: 0.0,
                              'b': 0.841,
                              'm': -0.144},
                    '50': {   1: 0.654,
                              2: 0.185,
                              3: 0.089,
                              4: 0.041,
                              5: 0.018,
                              6: 0.008,
                              7: 0.003,
                              8: 0.001,
                              9: 0.001,
                              10: 0.0,
                              'b': 0.355,
                              'm': -0.37},
                    '51': {   1: 0.737,
                              2: 0.152,
                              3: 0.067,
                              4: 0.027,
                              5: 0.011,
                              6: 0.004,
                              7: 0.001,
                              8: 0.001,
                              9: 0.0,
                              10: 0.0,
                              'b': 0.477,
                              'm': -0.27},
                    '52': {   1: 0.732,
                              2: 0.177,
                              3: 0.06,
                              4: 0.021,
                              5: 0.007,
                              6: 0.002,
                              7: 0.001,
                              8: 0.0,
                              9: 0.0,
                              10: 0.0,
                              'b': 0.763,
                              'm': -0.047},
                    '60': {   1: 0.514,
                              2: 0.194,
                              3: 0.15,
                              4: 0.075,
                              5: 0.035,
                              6: 0.017,
                              7: 0.006,
                              8: 0.003,
                              9: 0.001,
                              10: 0.001,
                              'b': 0.247,
                              'm': -0.216},
                    '61': {   1: 0.596,
                              2: 0.176,
                              3: 0.132,
                              4: 0.057,
                              5: 0.024,
                              6: 0.009,
                              7: 0.004,
                              8: 0.001,
                              9: 0.0,
                              10: 0.0,
                              'b': 0.406,
                              'm': -0.116},
                    '62': {   1: 0.559,
                              2: 0.206,
                              3: 0.158,
                              4: 0.052,
                              5: 0.017,
                              6: 0.005,
                              7: 0.002,
                              8: 0.001,
                              9: 0.0,
                              10: 0.0,
                              'b': 0.828,
                              'm': -0.199},
                    '70': {   1: 0.315,
                              2: 0.356,
                              3: 0.168,
                              4: 0.086,
                              5: 0.044,
                              6: 0.018,
                              7: 0.007,
                              8: 0.004,
                              9: 0.002,
                              10: 0.0,
                              'b': 0.261,
                              'm': -0.229},
                    '71': {   1: 0.413,
                              2: 0.328,
                              3: 0.138,
                              4: 0.073,
                              5: 0.029,
                              6: 0.011,
                              7: 0.005,
                              8: 0.002,
                              9: 0.001,
                              10: 0.0,
                              'b': 0.478,
                              'm': -0.311},
                    '72': {   1: 0.185,
                              2: 0.548,
                              3: 0.169,
                              4: 0.067,
                              5: 0.023,
                              6: 0.006,
                              7: 0.002,
                              8: 0.0,
                              9: 0.0,
                              10: 0.0,
                              'b': 0.785,
                              'm': -0.095},
                    '80': {   1: 0.311,
                              2: 0.247,
                              3: 0.17,
                              4: 0.144,
                              5: 0.071,
                              6: 0.031,
                              7: 0.013,
                              8: 0.008,
                              9: 0.003,
                              10: 0.002,
                              'b': 0.193,
                              'm': -0.127},
                    '81': {   1: 0.397,
                              2: 0.244,
                              3: 0.151,
                              4: 0.123,
                              5: 0.051,
                              6: 0.021,
                              7: 0.008,
                              8: 0.003,
                              9: 0.001,
                              10: 0.0,
                              'b': 0.402,
                              'm': -0.142},
                    '82': {   1: 0.273,
                              2: 0.355,
                              3: 0.17,
                              4: 0.138,
                              5: 0.041,
                              6: 0.015,
                              7: 0.005,
                              8: 0.001,
                              9: 0.0,
                              10: 0.0,
                              'b': 0.789,
                              'm': -0.209}
                    }

def getRunsInn(rpinn):
    runsinn = {0:   1/((rpinn*.761)+1),
               1:   (rpinn*(0.761**2))/(((rpinn*.761)+1)**2)
               }
 
    for i in range(2, 11):
        v = (rpinn*(0.761**2)*(((rpinn*.761) - 0.761 + 1)**(i-1)))/(((rpinn*.761)+1)**(i+1))
        runsinn[i] = v
    return runsinn
 
 
def getRunExp(rpinn, runsinn):
    runExp = {'10': runsinn
              }
    for i in range(0, 3):
        for j in range(1, 9):
            k = str(j) + str(i)
            if k == '10':   continue
            runExp[k] = {0: ((tangoRunExp[k]['m']*rpinn) + tangoRunExp[k]['b'])
                         }
            for r in range(1, 11):
                runExp[k][r] = ((1 - runExp[k][0])*tangoRunExp[k][r])
    return runExp
 
def getInnWinexp(runExp):
    ## Chance of home team winning with zero
    ## outs at the beg. of each inning
 
    innWinexp = {'101': {0: 0.5
                      }
              }
 
    for i in range(-25, 0):
        innWinexp['101'][i] = 0
    for i in range(1, 26):
        innWinexp['101'][i] = 1
 
    for i in range(9, 0, -1):
        for j in range(2, 0, -1):
            if j == 2:  next = str(i+1) + '1'
            else:   next = str(i) + '2'
            this = str(i) + str(j)
            innWinexp[this] = {}
            if j == 2:
                for k in range(-25, 26):
                    p = 0
                    if i == 9 and k > 0:
                        innWinexp[this][k] = 1
                        continue
                    else:   pass
                    for m in range(0, 11):
                        if k+m > 25:    iw = 1
                        else:   iw = innWinexp[next][k+m]
                        p += runExp['10'][m]*iw
                    innWinexp[this][k] = p
            else:
                for k in range(-25, 26):
                    p = 0
                    for m in range(0, 11):
                        if k-m < -25:   iw = 0
                        else:   iw = innWinexp[next][k-m]
                        p += runExp['10'][m]*iw
                    innWinexp[this][k] = p
    return innWinexp
 
 
def getWinexp(innWinexp, runExp, inn, half, base, outs, rdiff):    
    if inn > 9: inn = 9
    innkey = str(inn) + str(half)
    if outs > 2:    outs = 2
    sitkey = str(base) + str(outs)
    if half == 2:  next = str(inn+1) + '1'
    else:   next = str(inn) + '2'
    if sitkey == '10':  ## beginning of half inning
        if rdiff > 25:  rdiff = 25
        elif rdiff < -25:   rdiff = -25
        else:   pass
        Winexp = innWinexp[innkey][rdiff]
    elif half == 1:
        Winexp = 0
        for i in range(10, -1, -1):
            if rdiff-i < -25:   iw = 0
            elif rdiff-i > 25:  iw = 1
            else:   iw = innWinexp[next][rdiff-i]
            Winexp += runExp[sitkey][i]*iw
    else:
        Winexp = 0
        for i in range(0, 11):
            if rdiff-i < -25:   iw = 0
            elif rdiff+i > 25:   iw = 1
            else:   iw = innWinexp[next][rdiff+i]
            Winexp += runExp[sitkey][i]*iw
    return Winexp
 
def getVol(innWinexp, runExp, inn, half, base, outs, rdiff):
    ## changes if strikeout:
    if outs == 2:
        outsK = 0
        baseK = 1
        if half == 1:
            halfK = 2
            innK = inn
        else:
            halfK = 1
            innK = inn + 1
    else:
        outsK = outs + 1
        baseK, halfK, innK = base, half, inn
    WinexpK = getWinexp(innWinexp, runExp, innK, halfK, baseK, outsK, rdiff)
    ## changes if homerun
    if half == 1:
        rdiff -= baseHr[base]
    else:
        rdiff += baseHr[base]
    base = 1
    WinexpHr = getWinexp(innWinexp, runExp, inn, half, base, outs, rdiff)
    return (abs(WinexpHr - WinexpK))/0.133
 
def rpgToInnWinexp(rpg):
    rpinn = float(rpg)/9 ## r/inn
    runsinn = getRunsInn(rpinn)
    runExp = getRunExp(rpinn, runsinn)
    innWinexp = getInnWinexp(runExp)
    return innWinexp, runExp
 
####sample usage
##inn = 2
##half = 1 ## 1 = top, 2 = bottom
##base = 1 ## base situation: 1 through 8
##outs = 2
##rdiff = 2 ## run differential from home team perspective
##
##rpg = 4.5 ## runs per team-game
##innWinexp, runExp = rpgToInnWinexp(rpg)
##
##winexp = getWinexp(innWinexp, runExp, inn, half, base, outs, rdiff)
##
##vol = getVol(innWinexp, runExp, inn, half, base, outs, rdiff)
##
##print winexp, lev
