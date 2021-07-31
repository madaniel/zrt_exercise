import yaml


class YamlHandler(object):

    def __init__(self, yaml_file):
        self.yaml_file = yaml_file

    def get_data(self):
        try:
            with open(self.yaml_file, 'r') as config_file:
                config_data = yaml.safe_load(config_file)
                return config_data

        except (FileNotFoundError, yaml.YAMLError) as exc:
            raise RuntimeError(f"Failed to parse {self.yaml_file}! \nexception={exc}")

    def write_data(self, data):
        try:
            with open(self.yaml_file, 'w') as config_file:
                yaml.dump(data, config_file, default_flow_style=False)

        except (FileNotFoundError, yaml.YAMLError) as exc:
            raise RuntimeError(f"Failed to write to {self.yaml_file}! \nexception={exc}")
