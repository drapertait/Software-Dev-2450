from simulator_class import Simulator
from uvsim_gui import UVsim  # Updated import statement

if __name__ == "__main__":
    gui = UVsim(None)
    simulator = Simulator(gui.output_function)
    gui.simulator = simulator
    gui.start()
