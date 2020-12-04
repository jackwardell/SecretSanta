from secret_santa import Participant, Hat


def test():
    participants = [
        Participant("jack", excluded=["emma"]),
        Participant("emma", excluded=["jack"]),
        Participant("alex"),
        Participant("zoe", excluded=["paddy"]),
        Participant("paddy", excluded=["zoe"]),
        Participant("fin"),
        Participant("giulia", excluded=["ludo"]),
        Participant("ludo", excluded=["giulia"]),
    ]

    hat = Hat(participants)

    hat.choices()
    for i, j in hat.choices().items():
        print(i, "=", j)
    print(hat.choices())

    results = hat.distribute()

    for result in results:
        assert result.giver != result.receiver
        assert result.giver.name not in result.receiver.excluded
        assert result.receiver.name not in result.giver.excluded
    print(results)


test()
