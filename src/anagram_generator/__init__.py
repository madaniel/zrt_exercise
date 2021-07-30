import sys
from pathlib import Path
project_path = Path(__file__).parent.parent.parent
sys.path.append(str(project_path))
from src.anagram_generator.anagram_generator_module import AnagramGenerator
