import unittest
import os
import platform
from deepchem.utils import sequence_utils as seq_utils

IS_WINDOWS = platform.system() == 'Windows'


@unittest.skipIf(IS_WINDOWS,
                 "Skip test on Windows")  # hhsuite does not run on windows
class TestSeq(unittest.TestCase):
  """
  Tests sequence handling utilities.
  """

  def setUp(self):
    current_dir = os.path.dirname(os.path.realpath(__file__))
    self.dataset_file = os.path.join(current_dir, 'data/example.fasta')
    self.database_name = 'example_db'
    self.data_dir = os.path.join(current_dir, 'data')

  def test_hhsearch(self):
    seq_utils.hhsearch(
        self.dataset_file, database=self.database_name, data_dir=self.data_dir)
    with open('data/results.a3m', 'r') as f:
      resultsline = next(f)
    with open('data/example.hhr', 'r') as g:
      hhrline = next(g)

    assert hhrline[0:5] == 'Query'
    assert resultsline[0:5] == '>seq0'
    os.remove('data/results.a3m')
    os.remove('data/example.hhr')

  def test_hhblits(self):
    seq_utils.hhsearch(
        self.dataset_file, database=self.database_name, data_dir=self.data_dir)
    with open('data/results.a3m', 'r') as f:
      resultsline = next(f)
    with open('data/example.hhr', 'r') as g:
      hhrline = next(g)

    assert hhrline[0:5] == 'Query'
    assert resultsline[0:5] == '>seq0'
    os.remove('data/results.a3m')
    os.remove('data/example.hhr')
