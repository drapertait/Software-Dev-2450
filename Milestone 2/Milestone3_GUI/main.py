from simulator_class import Simulator
from simulatorGUI_class import SimulatorGUI

if __name__ == "__main__":
    gui = SimulatorGUI(None)
    simulator = Simulator(gui.output_function)
    gui.simulator = simulator
    gui.start()
