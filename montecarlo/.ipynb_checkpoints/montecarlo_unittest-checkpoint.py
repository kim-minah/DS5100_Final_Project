import unittest
from montecarlo import Die, Game, Analyzer
import pandas as pd
import numpy as np

class MonteCarloTestSuite(unittest.TestCase):
    
    def test_1_die_changeweight(self):
        die = Die(np.array([1,2,3,4,5,6]))
        die.change_weight(1,5)
        expected_weights = list([5.,1.,1.,1.,1.,1.])
        changed_weights = die.show().weights.values
        self.assertListEqual(expected_weights,list(changed_weights))
    
    def test_2_die_changeweight_false(self):
        die = Die(np.array([1,2,3,4,5,6]))
        with self.assertRaises(ValueError):
            die.change_weight(1,"hi")
            
    def test_3_die_roll(self):
        die = Die(np.array([1,2,3,4,5,6]))
        num_rolls = 5
        roll_count = len(die.roll(num_rolls)) 
        expected_roll_count = 5
        self.assertEqual(roll_count,expected_roll_count)
        
    def test_4_die_show(self):
        die = Die(np.array([1,2,3,4,5,6]))
        output = die.show()
        num_faces = 6
        self.assertEqual(len(output),num_faces)        
        
    def test_5_game_play(self):
        die1 = Die(np.array([1,2,3,4,5,6]))
        die2 = Die(np.array([1,2,3,4,5,6]))
        game = Game([die1,die2])
        num_plays = 5
        game.play(num_plays)
        self.assertEqual(len(game._private_plays),num_plays)        
        
    def test_6_game_show_narrow(self):
        die1 = Die(np.array([1,2,3,4,5,6]))
        die2 = Die(np.array([1,2,3,4,5,6]))
        die_list = list([die1,die2])
        game = Game([die1,die2])
        num_plays = 5
        game.play(num_plays)
        pd = game.show('narrow')
        expected_length = num_plays * len(die_list)
        self.assertEqual(len(pd), expected_length)        
        
    def test_7_game_show_wide(self):
        die1 = Die(np.array([1,2,3,4,5,6]))
        die2 = Die(np.array([1,2,3,4,5,6]))
        die_list = list([die1,die2])
        game = Game([die1, die2])
        num_plays = 5
        game.play(num_plays)
        expected_dim = tuple([num_plays,len(die_list)])
        self.assertTupleEqual(game.show().shape, expected_dim)            
   
    def test_8_analyzer_jackpot(self):
        die1 = Die(np.array([1,2,3]))
        die2 = Die(np.array([1,2,3]))
        die_list = list([die1,die2])
        game = Game([die1, die2])
        game.play(1000)
        analyzer = Analyzer(game)
        self.assertGreater(analyzer.jackpot(),0)
    
    def test_9_analyzer_combo(self):
        die1 = Die(np.array([1,1,1]))
        die2 = Die(np.array([2,2,2]))
        die_list = list([die1,die2])
        game = Game([die1, die2])
        num_plays = 5
        game.play(num_plays)
        analyzer = Analyzer(game) 
        self.assertEqual(analyzer.combo().Counts.values[0],num_plays)
    
    def test_10_analyzer_facecountsperroll(self):
        die1 = Die(np.array([1,2,3,4,5,6]))
        die2 = Die(np.array([2,2,3,4,5,6]))
        die_list = list([die1,die2])
        game = Game([die1, die2])
        num_plays = 5
        game.play(num_plays)
        analyzer = Analyzer(game)      
        sums = analyzer.face_counts_per_roll().sum(axis=1).values 
        expected_sums = np.repeat(len(die_list),num_plays)
        self.assertListEqual(list(sums), list(expected_sums))
        
        
if __name__ == '__main__':
    unittest.main(verbosity=3)       