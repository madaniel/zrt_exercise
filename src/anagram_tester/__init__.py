import sys
from pathlib import Path
project_path = Path(__file__).parent.parent.parent
sys.path.append(str(project_path))
from src.anagram_tester.anagram_tester_module import AnagramTester
