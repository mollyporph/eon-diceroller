import unittest
import diceroller

class TestDiceRoller(unittest.TestCase):

  def test_solveob_no_six_no_change(self):
      dices = [1,2,3]
      (newDices,obcount) = diceroller.solve_ob(6,dices)
      self.assertEqual(len(dices), len(newDices))

  def test_solveob_six_returns_more_dices(self):
      dices = [1,2,6]
      (newDices,obcount) = diceroller.solve_ob(6,dices)
      self.assertNotEqual(len(dices),len(newDices))
  def test_obthrow_does_not_return_dice_above_t(self):
      diceAmount = 1
      results = [val for sublist in [diceroller.roll_obthrow(diceAmount)[0] for _ in range(1,100)] for val in sublist]
      self.assertTrue(all(x <= 6 for x in results))
  def test_normalthrow_does_not_Return_dice_above_t(self):
      diceAmount = 1
      t = 10
      results = [val for sublist in [diceroller.roll_normalthrow(diceAmount,t)[0] for _ in range(1,100)] for val in sublist]
      self.assertTrue(all(x <= t for x in results))
if __name__ == '__main__':
    unittest.main()
