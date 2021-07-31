import subprocess
from pathlib import Path
from src.infra import Logger
from src.infra import YamlHandler

# Defines
TEST_FILES = ['test_data_1.yaml']


class AnagramTester(object):

    def __init__(self):
        self.app_runner = None
        self._logger = Logger(module_name=self.__class__.__name__)

    @staticmethod
    def get_test_data_file(data_file_name):
        yaml_handler = YamlHandler(data_file_name)
        data = yaml_handler.get_data()
        return data['result']

    def check_output(self, actual_output, expected_output):
        for line_number in range(len(actual_output)):
            actual_list = actual_output[line_number]
            expected_list = expected_output[line_number]
            actual_set = set(actual_list)
            expected_set = set(expected_list)
            if actual_set.intersection(expected_set) != expected_set:
                self._logger.debug(f"Mismatch: expected_line={expected_list} actual_line={actual_list}")
                return False
        return True

    def test_app(self):
        for test_file in TEST_FILES:
            test_file = Path(__file__).parent / test_file
            runner = ApplicationRunner(test_file)
            runner.run()
            if not self.check_output(actual_output=runner.get_output(), expected_output=self.get_test_data_file(test_file)):
                self._logger.info(f"Data file {test_file} failed in test")
                return
        self._logger.info("All data files checked successfully")


class ApplicationRunner(object):

    def __init__(self, config_file):
        self.app = Path(__file__).parent.parent / 'app.py'
        self.config_file = Path(__file__).parent / config_file
        self.output = None

    def run(self):
        self.output = subprocess.run(['python', self.app, f'--config={self.config_file}'], stdout=subprocess.PIPE)

    def get_output(self):
        output_list = []
        output = self.output.stdout.decode('ascii')
        output = output.splitlines()
        for line in output:
            output_line = line.split(',')
            output_list.append([word.strip() for word in output_line])
        return output_list
