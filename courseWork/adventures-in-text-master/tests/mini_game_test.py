from game import Game
import unittest

class TestMiniGame(unittest.TestCase):

    def test_play(self):
        "Tests basic play_game functions: moving locations, getting and dropping objects, interacting with objects, etc."
        game = Game()
        bedroom, closet = game.game['rooms'][0], game.game['rooms'][1]
        bed, lamp, dresser = bedroom.objects[0], bedroom.objects[1], bedroom.objects[2]
        chair = closet.objects[0]

        # go west
        game.play('west')
        self.assertEquals(game.game['location'].name, closet.name)
        # go north (impossible) should not change location
        game.play('north')
        self.assertEquals(game.game['location'], closet)
        # picking up chair should add it to inventory
        game.play('get chair')
        self.assertEquals(game.game['inv'], [chair])
        # and remove it from closet.objects
        self.assertEquals(closet.objects, [])
        # going east again should change location to the bedroom
        game.play('east')
        self.assertEquals(game.game['location'], bedroom)
        # dropping the chair should remove it from inventory
        game.play('drop chair')
        self.assertEquals(game.game['inv'], [])
        # and add it to bedroom.objects
        self.assertEquals(bedroom.objects, [bed, lamp, dresser, chair])
        # turning on lamp should not change lamp.is_lit to True (because it is type Unreachable)
        game.play('light lamp')
        self.assertFalse(lamp.is_lit)
        # climbing on the bed should not enable us to turn the lamp on
        game.play('climb bed')
        game.play('light lamp')
        self.assertFalse(lamp.is_lit)
        # climbing on the chair should set chair.has_user to True
        game.play('climb chair')
        self.assertTrue(chair.has_user)
        # now that we are standing on the chair, turning on the lamp should set lamp.is_lit to True
        game.play('light lamp')
        self.assertTrue(lamp.is_lit)

if __name__ == "__main__":
    unittest.main()