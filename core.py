'''

"Can't Stop" Move Calculator v0.3
An abomination by Jeffrey Campbell

Uses the rule of 28 to determine whether the player should roll again or stop
'''
import re


class TurnCount:
    def __init__(self):
        self.count = 0
        self.marked = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}

    def update(self, pair1, pair2):
        valid = range(2, 13)
        self.count += self.count_roll(pair1)
        if pair2 in valid:
            self.count += self.count_roll(pair2)
        return

    def count_roll(self, n):
        gain = 0
        if self.marked[n] == 0:
            gain += 2 * self.value(n)
        else:
            gain += self.value(n)
        self.marked[n] += 1
        return gain

    @staticmethod
    def value(n):
        return abs(7 - n) + 1


def process_input():
    x = str(raw_input('Enter your roll(s)!\n'))
    raw = re.split('[\s]+', x)
    if len(raw) == 1:  # Only one number rolled
        roll_1 = int(x)
        roll_2 = 0
    else:  # No doubles rolled
        raw = re.split('[\s]+', x)
        roll_1 = int(raw[0])
        roll_2 = int(raw[1])

    return [roll_1, roll_2]


def check_valid(rolls):
    valid = range(2, 13)
    if rolls[0] in valid:
        return True
    else:
        return False


# ---------------------MAIN----------------
rule = 28  # Use the rule of 28
while True:
    x = TurnCount()
    while True:
        rolls = process_input()
        if check_valid(rolls):  # Check inputted rolls are valid numbers
            x.update(rolls[0], rolls[1])
            if x.count < rule:
                print 'DON\'T STOP! You have:', x.count
            else:
                print 'STOP! You have:',x.count,'Unless you have balls of steel...'
        else:  # User has signalled that they wiped out
            break
