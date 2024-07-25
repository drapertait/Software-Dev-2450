class ProgramLoader:
    @staticmethod
    def load_program_from_file(file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()
        return [int(line.strip()) for line in lines if line.strip()]
