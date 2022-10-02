from SampleSystems import FeedbackLoop, Repeater, SimpleRelay, TwoMessages

if __name__ == "__main__":
    # print("testing relay")
    # relay = SimpleRelay("test")
    # relay.execute("Execute")

    # twomessages = TwoMessages("test")
    # twomessages.execute("Execute")
    # twomessages.execute("Start")
    # twomessages.print_summary()

    # print("testing feedback")
    # feedback = FeedbackLoop("test")
    # feedback.print_mouths()
    # feedback.execute()
    # feedback.print_containers()

    repeater = Repeater("test")
    repeater.print_summary()
    repeater.execute(10, debug=False)