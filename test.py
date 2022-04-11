import unittest
import dictionary as dictionary
import wordle_ui as u_i
import wordle as wordle
import letterFrequency as l_Freq
from unittest.mock import patch

class wordle_test(unittest.TestCase):
    def test_compare_word_true(self) -> None:
        """To test compare word function"""
        w = wordle.Wordle()
        self.assertTrue(w.compareWord("hello","hello"))
    
    def test_compare_word_false(self) -> None:
        """To test compare word function"""
        w = wordle.Wordle()
        self.assertFalse(w.compareWord("hello","books"))

    def test_exit_game_true(self) -> None:
        """To check if the game exits successfully"""
        ui = u_i.UI()
        self.assertTrue(ui.exit_game(""))

    def test_exit_game_false(self) -> None:
        """To check if the game exits successfully"""
        ui = u_i.UI()
        self.assertFalse(ui.exit_game("hello"))

    def test_check_char_true(self) -> None:
        """To check if the user input consists of characters only"""
        ui = u_i.UI()
        self.assertTrue(ui.check_char("@wert"))

    def test_check_char_false(self) -> None:
        """To check if the user input consists of characters only"""
        ui = u_i.UI()
        self.assertFalse(ui.check_char("hello"))

    def test_check_dic_true(self) -> None:
        """To check if the word is present in the dictionary"""
        ui = u_i.UI()
        self.assertTrue(ui.check_dic("aaaaa"))

    # def test_check_dic_false(self) -> None:
    #     """To check if the word is present in the dictionary"""
    #     ui = u_i.UI()
    #     self.assertFalse(ui.check_dic("hello"))

    def test_check_len_true(self) -> None:
        """To check if the length of the word is 5"""
        ui = u_i.UI()
        self.assertTrue(ui.check_len("aaaa"))
        

    def test_check_len_false(self) -> None:
        """To check if the length of the word is 5"""
        ui = u_i.UI()
        self.assertFalse(ui.check_len("hello"))

    def test_check_likelihood_true(self) -> None:
        """To check if the likelihood is less than 1"""
        lFreq = l_Freq.Letter_Frequency()
        self.assertTrue(lFreq.check_likelihood_range(0.5))

    def test_check_likelihood_false(self) -> None:
        """To check if the likelihood is greater than 1"""
        lFreq = l_Freq.Letter_Frequency()
        self.assertFalse(lFreq.check_likelihood_range(1.5))

    
if __name__ == "__main__":
    unittest.main()