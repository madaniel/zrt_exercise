import argparse
from anagram_generator import AnagramGenerator


parser = argparse.ArgumentParser(description='Anagram Generator')
parser.add_argument('--config', dest='config_file', help='YAML file name for configuration', required=False)
args = parser.parse_args()

if __name__ == '__main__':
    # User input is taken from config.yaml
    anagram_generator = AnagramGenerator(config_file=args.config_file)
    print(anagram_generator.get_result(), end='')
