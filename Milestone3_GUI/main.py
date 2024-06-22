from simulator_class import Simulator
from simulatorGUI_class import UVsim

if __name__ == "__main__":
    gui = UVsim(None)
    simulator = Simulator(gui.output_function)
    gui.simulator = simulator
    gui.start()
