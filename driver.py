from MagicMouth import MagicMouth
from SampleSystems import SimpleRelay, TwoMessages


if __name__ == "__main__":
    # relay = SimpleRelay("test")
    # relay.execute("Execute")

    twomessages = TwoMessages("test")
    twomessages.execute("Start")
    twomessages.print_containers()
    twomessages.print_summary()