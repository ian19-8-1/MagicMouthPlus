from LogicGates import Binary
from SampleSystems import AndGateTest, FeedbackLoop, OrGateTest, Repeater, SimpleRelay, TwoMessages, XorGateTest
from MagicMouthSystem import MagicMouthSystem

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

    # repeater = Repeater("test")
    # repeater.print_summary()
    # repeater.execute(10, debug=False)

    # andtest = AndGateTest("test")
    # andtest.execute("Execute", "Start", "s1", "s2", False)

    # ortest = OrGateTest("test")
    # ortest.execute("Execute", "Start", "s1", "s2")

    xortest = XorGateTest("test")
    xortest.execute("Execute", "Start", "s1", "s2")