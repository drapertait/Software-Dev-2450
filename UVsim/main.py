from program_loader_class import ProgramLoader
from simulator_class import Simulator
from uvsim_gui import UVsim

if __name__ == "__main__":
    loader = ProgramLoader()
    gui = UVsim(None)
    simulator = Simulator(gui.output_function, loader)
    gui.simulator = simulator
    gui.start()
