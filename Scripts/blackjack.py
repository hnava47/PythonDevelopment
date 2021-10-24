import random, collections, sys, csv

class Hand:
    """Class that encapsulates a blackjack hand."""
    def __init__(self, cards=None):
        if cards is None:
            self.cards=list()
        else:
            self.cards=cards
            self.score()

    def __str__(self):
        return "{}".format(self.cards)

    def add_card(self):
        self.cards += [random.randint(1, 13)]
        self.score()

    def is_blackjack(self):
        scoreList = Hand(self.cards).score()
        return scoreList[0] == 21

    def is_bust(self):
        scoreList = Hand(self.cards).score()
        return scoreList[0] > 21

    def score(self):
        Score = collections.namedtuple("Score", "total soft_ace_count")
        total = 0
        soft_ace_count = 0
        for i in range(len(self.cards)):
            if self.cards[i] == 1 and (total+11) > 21:
                total += 1
            elif self.cards[i] == 1 and (total+11) <= 21:
                total += 11
                soft_ace_count += 1
            elif self.cards[i] > 10:
                total += 10
            else:
                total += self.cards[i]
        return Score(total, soft_ace_count)

class Strategy:
    def __init__(self, stand_on_value, stand_on_soft):
        self.stand_on_value = stand_on_value
        self.stand_on_soft = stand_on_soft

    def __repr__(self):
        return "Strategy({}, {})".format(self.stand_on_value, self.stand_on_soft)

    def __str__(self):
        if self.stand_on_soft is True:
            return "S{}".format(self.stand_on_value)
        elif self.stand_on_soft is False:
            return "H{}".format(self.stand_on_value)

    def stand(self, hand):
        Stand = collections.namedtuple("Stand", "stand total")
        total, soft_ace_count = Hand.score(hand)
        if self.stand_on_soft is True:
            if total >= self.stand_on_value:
                return Stand(True, total)[0]
            else:
                return Stand(False, total)[0]
        elif self.stand_on_soft is False:
            if total == self.stand_on_value:
                if soft_ace_count == 0:
                    return Stand(True, total)[0]
                else:
                    return Stand(False, total)[0]
            elif total < self.stand_on_value:
                return Stand(False, total)[0]
            else:
                return Stand(True, total)[0]

    def play(self):
        cardHand = Hand([random.randint(1, 13), random.randint(1, 13)])
        while self.stand(cardHand) is False:
            Hand.add_card(cardHand)
        if Hand.score(cardHand)[0] > 21:
            return 22
        else:
            return Hand.score(cardHand)[0]

def main(numSimulation):
    numSimulation = int(numSimulation)
    class Error(Exception):
        pass
    class SimulationError(Error):
        pass
    while True:
        try:
            if numSimulation < 1:
                raise SimulationError
            break
        except SimulationError:
            return "ERROR!: Number of simulation is not greater than 0"
    with open("HW_5_OUTPUT.csv", "w") as csvfile:
        filewriter = csv.writer(csvfile)
        headerList = ["P-Strategy"]
        for h in range(13, 21):
            headerList += ["D-H{}".format(h), "D-S{}".format(h)]
        filewriter.writerow(headerList)
        for m in range(13, 21):
            hardList = ["P-H{}".format(m)]
            softList = ["P-S{}".format(m)]
            for s in range(13, 21):
                playerStrat = Strategy(m, True)
                softWin = 0
                softOut = 0
                for f in range(numSimulation):
                    if len(softList)%2 == 0:
                        dealerStrat = Strategy(s, True)
                        playerSoft = playerStrat.play()
                        dealerSoft = dealerStrat.play()
                        if playerSoft < 22 and dealerSoft > 21:
                            softWin += 1
                        elif playerSoft < 22 and playerSoft > dealerSoft:
                            softWin += 1
                        elif playerSoft == dealerSoft:
                            softOut += 1
                    else:
                        dealerStrat = Strategy(s, False)
                        playerSoft = playerStrat.play()
                        dealerSoft = dealerStrat.play()
                        if playerSoft < 22 and dealerSoft > 21:
                            softWin += 1
                        elif playerSoft < 22 and playerSoft > dealerSoft:
                            softWin += 1
                        elif playerSoft == dealerSoft:
                            softOut += 1
                softList += [round((softWin/(numSimulation-softOut))*100,2)]

                softWin = 0
                softOut = 0
                for f in range(numSimulation):
                    if len(softList)%2 == 0:
                        dealerStrat = Strategy(s, True)
                        playerSoft = playerStrat.play()
                        dealerSoft = dealerStrat.play()
                        if playerSoft < 22 and dealerSoft > 21:
                            softWin += 1
                        elif playerSoft < 22 and playerSoft > dealerSoft:
                            softWin += 1
                        elif playerSoft == dealerSoft:
                            softOut += 1
                    else:
                        dealerStrat = Strategy(s, False)
                        playerSoft = playerStrat.play()
                        dealerSoft = dealerStrat.play()
                        if playerSoft < 22 and dealerSoft > 21:
                            softWin += 1
                        elif playerSoft < 22 and playerSoft > dealerSoft:
                            softWin += 1
                        elif playerSoft == dealerSoft:
                            softOut += 1
                softList += [round((softWin/(numSimulation-softOut))*100,2)]

            for h in range(13, 21):
                playerStrat = Strategy(m, False)
                hardWin = 0
                hardOut = 0
                for f in range(numSimulation):
                    if len(hardList)%2 == 0:
                        dealerStrat = Strategy(h, True)
                        playerHard = playerStrat.play()
                        dealerHard = dealerStrat.play()
                        if playerHard < 22 and dealerHard > 21:
                            hardWin += 1
                        elif playerHard < 22 and playerHard > dealerHard:
                            hardWin += 1
                        elif playerHard == dealerHard:
                            hardOut += 1
                    else:
                        dealerStrat = Strategy(h, False)
                        playerHard = playerStrat.play()
                        dealerHard = dealerStrat.play()
                        if playerHard < 22 and dealerHard > 21:
                            hardWin += 1
                        elif playerHard < 22 and playerHard > dealerHard:
                            hardWin += 1
                        elif playerHard == dealerHard:
                            hardOut += 1
                hardList += [round((hardWin/(numSimulation-hardOut))*100,2)]

                hardWin = 0
                hardOut = 0
                for f in range(numSimulation):
                    if len(hardList)%2 == 0:
                        dealerStrat = Strategy(h, True)
                        playerHard = playerStrat.play()
                        dealerHard = dealerStrat.play()
                        if playerHard < 22 and dealerHard > 21:
                            hardWin += 1
                        elif playerHard < 22 and playerHard > dealerHard:
                            hardWin += 1
                        elif playerHard == dealerHard:
                            hardOut += 1
                    else:
                        dealerStrat = Strategy(h, False)
                        playerHard = playerStrat.play()
                        dealerHard = dealerStrat.play()
                        if playerHard < 22 and dealerHard > 21:
                            hardWin += 1
                        elif playerHard < 22 and playerHard > dealerHard:
                            hardWin += 1
                        elif playerHard == dealerHard:
                            hardOut += 1
                hardList += [round((hardWin/(numSimulation-hardOut))*100,2)]

            filewriter.writerow(hardList)
            filewriter.writerow(softList)

if __name__ == "__main__":
    main(sys.argv[1])
