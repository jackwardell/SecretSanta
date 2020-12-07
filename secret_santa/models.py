import random

import attr
from functools import wraps


@attr.s(frozen=True)
class Participant:
    """model for a secret santa participant"""

    name = attr.ib()
    excluded = attr.ib(factory=list, repr=False, hash=False)

    def __str__(self):
        return self.name


@attr.s
class Result:
    """model for a pair of giver and receiver"""

    giver = attr.ib()
    receiver = attr.ib()


def retry(num_times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            iterations = 0
            while iterations <= num_times:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    iterations += 1

        return wrapper

    return decorator


@attr.s
class Hat:
    """model for a hat full of participants"""

    participants = attr.ib()

    @participants.validator
    def check_participants(self, attribute, value):
        if len(self.participants) != len(set([participant.name for participant in value])):
            raise ValueError(f"{attribute} names MUST be unique!")
        for v in value:
            if not [p for p in value if p.name != v.name and p.name not in v.excluded]:
                raise ValueError(f"{v.name} has NO choices!")

    def choices(self):
        choices = {}
        for participant in self.participants:
            choices[participant] = [
                p
                for p in self.participants
                if p.name != participant.name and p.name not in participant.excluded
            ]
        return choices

    @retry(100)
    def distribute(self):
        givers = self.participants.copy()
        random.shuffle(givers)

        received = []
        results = []

        for giver in givers:
            choices = [p for p in self.choices()[giver] if p.name not in received]
            receiver = random.choice(choices)
            received.append(receiver.name)

            result = Result(giver, receiver)
            results.append(result)

        for result in results:
            assert result.giver != result.receiver
            assert result.giver.name not in result.receiver.excluded
            assert result.receiver.name not in result.giver.excluded

        return results



