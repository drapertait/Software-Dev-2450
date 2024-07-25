class ProgramLoader:
    @staticmethod
    def load_program_from_file(file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()
        if len(lines) > 250:
            raise ValueError("Program exceeds the maximum allowed size of 250 commands.")
        return [int(line.strip()) for line in lines if line.strip()]
