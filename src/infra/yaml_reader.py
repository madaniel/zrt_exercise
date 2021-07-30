import yaml


class YamlReader(object):

    def __new__(cls, yaml_file, *args, **kwargs):
        return cls.get_config_file(yaml_file)

    @staticmethod
    def get_config_file(yaml_filename):
        try:
            with open(yaml_filename, 'r') as config_file:
                config_data = yaml.safe_load(config_file)
                return config_data

        except (FileNotFoundError, yaml.YAMLError) as exc:
            raise RuntimeError(f"Failed to parse {yaml_filename}! \nexception={exc}")
