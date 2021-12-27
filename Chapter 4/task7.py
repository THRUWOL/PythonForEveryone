def computegrade(score):
    if 1.0 > score >= 0.9:
        print('A')
    elif 0.9 > score >= 0.8:
        print('B')
    elif 0.8 > score >= 0.7:
        print('C')
    elif 0.7 > score >= 0.6:
        print('D')
    elif 0.6 > score:
        print('F')
    else:
        print('Bad score')


score = input('Enter score: ')

try:
    score = float(score)
except:
    score = 10

computegrade(score)
