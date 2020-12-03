import random

import attr


@attr.s
class Participant:
    """model for a secret santa participant"""

    name = attr.ib()
    excluded = attr.ib(factory=list)
    # email_address = attr.ib()


@attr.s
class Result:
    """model for a pair of giver and receiver"""

    giver = attr.ib()
    receiver = attr.ib()


@attr.s
class Hat:
    """model for a hat full of participants"""

    participants = attr.ib()

    def distribute(self):
        givers = self.participants.copy()
        # receivers = self.participants.copy()

        random.shuffle(givers)
        # random.shuffle(receivers)

        results = []
        received = []

        for giver in givers:
            choices = [
                receiver
                for receiver in self.participants
                if receiver != giver
                and receiver not in received
                # and receiver not in giver.excluded
            ]
            receiver = random.choice(choices)
            received.append(receiver)
            result = Result(giver, receiver)
            results.append(result)

        return results


def test():
    participants = [
        Participant("jack"),
        Participant("james"),
        Participant("jane"),
        Participant("jill"),
        Participant("jeremy"),
    ]

    hat = Hat(participants)

    results = hat.distribute()
    print(results)


test()
