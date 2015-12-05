import unittest
from multiset import *


class TestContained(unittest.TestCase):

    def test_element_contained(self):
        Multi1 = MultiSet()
        Multi1.insert('a')
        result = 'a' in Multi1
        expected = True
        self.assertEqual(result, expected)

    def test_string_contained(self):
        Multi = MultiSet()
        Multi.insert('warblegarble')
        result = 'warblegarble' in Multi
        self.assertTrue(result)

    def test_multiple_contained(self):
        multi = MultiSet()
        multi.insert(1)
        multi.insert(2414)
        multi.insert(24)
        multi.insert(315)
        result = 2414 in multi
        self.assertTrue(result)

    def test_multiple_string(self):
        multi = MultiSet()
        multi.insert('ga')
        multi.insert('i hope a2 is easier')
        multi.insert('and shorter')
        multi.insert('since we dont have many weeks left')
        result = 'and shorter' in multi
        self.assertTrue(result)

    def test_element_false(self):
        multi = MultiSet()
        multi.insert(1)
        multi.insert(21433442)
        result = 54553535 in multi
        self.assertFalse(result)


class TestElementCount(unittest.TestCase):

    def test_single_element_count(self):
        Multi1 = MultiSet()
        Multi1.insert('a')
        result = Multi1.count('a')
        expected = 1
        self.assertEqual(result, expected)

    def test_multiple_element_count(self):
        multi = MultiSet()
        multi.insert(1)
        multi.insert(2)
        multi.insert(4343)
        multi.insert(1)
        multi.insert(4343)
        multi.insert(1)
        result = multi.count(4343)
        expected = 2
        self.assertEqual(result, expected)

    def test_multiple_string_element_count(self):
        multi = MultiSet()
        multi.insert('321321')
        multi.insert('agdaf')
        multi.insert('mindless string')
        multi.insert('agdef')
        multi.insert('agdaf')
        multi.insert('Y AM I DOIN DIS')
        multi.insert('agdaf')
        result = multi.count('agdaf')
        expected = 3
        self.assertEqual(result, expected)

    def test_empty_count(self):
        multi = MultiSet()
        result = multi.count('hehlol')
        expected = 0
        self.assertEqual(result, expected)

    def test_bool_count(self):
        x = MultiSet()
        y = MultiSet()
        x.insert(True)
        result = x.count(1)
        expected = 1
        self.assertEqual(result, expected)


class TestElementInsert(unittest.TestCase):

    def test_element_insert(self):
        Multi1 = MultiSet()
        Multi1.insert('b')
        result = 'b' in Multi1
        self.assertTrue(result)

    def test_multiple_element_insert(self):
        multi = MultiSet()
        multi.insert(1)
        multi.insert(2)
        multi.insert(3)
        result = (1 in multi)*(2 in multi)*(3 in multi)
        expected = 1
        self.assertEqual(result, expected)

    def test_multiple_false_elements(self):
        multi = MultiSet()
        multi.insert('fad')
        multi.insert('hi')
        multi.insert('uwotm8')
        result = 'wot' in multi
        expected = False


class TestElementClear(unittest.TestCase):

    def test_element_clear(self):
        Multi1 = MultiSet()
        Multi1.insert('a')
        Multi1.insert('b')
        Multi1.clear()
        result = Multi1
        expected = MultiSet()
        self.assertEqual(result, expected)

    def test_empty_set(self):
        multi = MultiSet()
        multi.clear()
        result = multi
        expected = MultiSet()
        self.assertEqual(result, expected)

    def test_false_clear(self):
        multi = MultiSet()
        multi.insert(1)
        multi.insert(234)
        multi1 = MultiSet()
        multi1.insert(1)
        multi.clear()
        result = multi == multi1
        self.assertFalse(result)


class TestLength(unittest.TestCase):

    def test_length(self):
        Multi = MultiSet()
        Multi.insert('a')
        Multi.insert('a')
        Multi.insert('b')
        result = len(Multi)
        expected = 3
        self.assertEqual(result, expected)

    def test_empty_set(self):
        multi = MultiSet()
        result = len(multi)
        expected = 0
        self.assertEqual(result, expected)

    def test_long_set(self):
        multi = MultiSet()
        multi.insert(1)
        multi.insert(254)
        multi.insert(345)
        multi.insert(2)
        multi.insert(32504984)
        multi.remove(254)
        result = len(multi)
        expected = 4
        self.assertEqual(result, expected)


class TestRepr(unittest.TestCase):

    def test_repr(self):
        Multi = MultiSet()
        Multi.insert('a')
        Multi.insert('b')
        result = repr(Multi)
        expected = 'MultiSet([\'a\', \'b\'])'
        self.assertEqual(result, expected)

    def test_integer_repr(self):
        multi = MultiSet()
        multi.insert(5)
        multi.insert(435)
        multi.insert(9)
        multi.insert(24)
        result = repr(multi)
        expected = 'MultiSet([5, 9, 24, 435])'
        self.assertEqual(result, expected)

    def test_empty_set(self):
        multi = MultiSet()
        result = repr(multi)
        expected = 'MultiSet([])'
        self.assertEqual(result, expected)


class TestEquals(unittest.TestCase):

    def test_equals(self):
        Multi = MultiSet()
        Multi1 = MultiSet()
        Multi.insert('1234')
        Multi.insert('4321')
        Multi1.insert('4321')
        Multi1.insert('1234')
        result = Multi == Multi1
        self.assertTrue(result)

    def test_empty_set(self):
        multi = MultiSet()
        multi1 = MultiSet()
        result = multi == multi1
        self.assertTrue(result)

    def test_different_length_equals(self):
        multi = MultiSet()
        multi.insert('x')
        multi.insert('x')
        multi1 = MultiSet()
        multi1.insert('x')
        result = multi == multi1
        self.assertFalse(result)

    def test_multiple_occurrences_equals(self):
        multi = MultiSet()
        multi.insert('a')
        multi.insert('a')
        multi.insert('y')
        multi.insert('y')
        multi1 = MultiSet()
        multi1.insert('a')
        multi1.insert('a')
        multi1.insert('y')
        multi1.insert('y')
        result = multi == multi1
        self.assertTrue(result)


class TestSubset(unittest.TestCase):

    def test_subset(self):
        multi = MultiSet()
        multi1 = MultiSet()
        multi1.insert('a')
        multi.insert('b')
        multi1.insert('b')
        multi.insert('a')
        multi1.insert('c')
        result = (multi <= multi1)
        self.assertTrue(result)

    def test_empty_set(self):
        multi = MultiSet()
        multi1 = MultiSet()
        result = multi <= multi1
        self.assertTrue(result)

    def test_string_set(self):
        multi = MultiSet()
        multi1 = MultiSet()
        multi.insert('hi')
        multi.insert('bye')
        multi.insert('no')
        multi1.insert('hi')
        multi1.insert('bye')
        multi1.insert('no')
        multi1.insert('hajime no ippo is the best anime')
        result = multi <= multi1
        self.assertTrue(result)

    def test_equal_set(self):
        multi = MultiSet()
        multi1 = MultiSet()
        multi.insert(1)
        multi1.insert(5)
        multi1.insert(6)
        multi.insert(6)
        multi1.insert(1)
        multi.insert(5)
        result = multi <= multi1
        self.assertTrue(result)

    def test_not_subset(self):
        multi = MultiSet()
        multi1 = MultiSet()
        multi.insert(1)
        multi.insert(4101341304)
        multi.insert(24325)
        multi1.insert(5455)
        multi1.insert(1)
        multi1.insert(4101341304)
        result = multi <= multi1
        self.assertFalse(result)

    def test_switched_subset(self):
        multi = MultiSet()
        multi1 = MultiSet()
        multi.insert(1)
        multi.insert(2)
        multi.insert(3)
        multi1.insert(1)
        multi1.insert(2)
        result = multi <= multi1
        self.assertFalse(result)

    def test_multiple_occurrences_subset(self):
        multi = MultiSet()
        multi.insert(1)
        multi.insert(2)
        multi.insert(2)
        multi.insert(3)
        multi.insert(3)
        multi.insert(3)
        multi1 = MultiSet()
        multi1.insert(1)
        multi1.insert(1)
        multi1.insert(2)
        multi1.insert(2)
        multi1.insert(3)
        multi1.insert(3)
        multi1.insert(3)
        multi1.insert(3)
        result = multi <= multi1
        self.assertTrue(result)

    def test_single_occurrence_subset(self):
        multi = MultiSet()
        multi.insert(1)
        multi.insert(10)
        multi.insert(10)
        multi.insert(30)
        multi.insert(30)
        multi.insert(30)
        multi1 = MultiSet()
        multi1.insert(1)
        multi1.insert(10)
        multi1.insert(10)
        multi1.insert(10)
        multi1.insert(30)
        multi1.insert(30)
        multi1.insert(30)
        result = multi <= multi1
        self.assertTrue(result)

    def test_single_occurrences_false_subset(self):
        multi = MultiSet()
        multi.insert('a')
        multi.insert('b')
        multi.insert('b')
        multi.insert('c')
        multi1 = MultiSet()
        multi1.insert('a')
        multi1.insert('b')
        multi1.insert('c')
        multi1.insert('c')
        multi1.insert('a')
        result = multi <= multi1
        self.assertFalse(result)


class TestSubtraction(unittest.TestCase):

    def test_subtraction(self):
        multi = MultiSet()
        multi1 = MultiSet()
        multi1.insert('a')
        multi.insert('b')
        multi1.insert('b')
        multi.insert('a')
        multi1.insert('c')
        result = multi1 - multi
        multi2 = MultiSet()
        multi2.insert('c')
        expected = multi2
        self.assertEqual(result, expected)

    def test_empty_set(self):
        multi = MultiSet()
        multi1 = MultiSet()
        result = multi - multi1
        expected = MultiSet()
        self.assertEqual(result, expected)

    def test_same_set(self):
        x = MultiSet()
        y = MultiSet()
        x.insert('warble')
        y.insert('warble')
        x.insert('garble')
        y.insert('garble')
        x.insert('1234567890')
        y.insert('1234567890')
        result = x - y
        expected = MultiSet()
        self.assertEqual(result, expected)

    def test_smaller_subtract_bigger_set(self):
        x = MultiSet()
        y = MultiSet()
        x.insert(12)
        x.insert(15)
        x.insert(15)
        x.insert(50)
        x.insert(25)
        x.insert(25)
        x.insert(25)
        y.insert(13)
        y.insert(12)
        y.insert(25)
        y.insert(25)
        y.insert(25)
        y.insert(25)
        y.insert(25)
        y.insert(100)
        result = x - y
        z = MultiSet()
        z.insert(15)
        z.insert(15)
        z.insert(50)
        expected = z
        self.assertEqual(result, expected)


class TestMutatedSubtraction(unittest.TestCase):

    def test_mutated_subtraction(self):
        multi = MultiSet()
        multi1 = MultiSet()
        multi1.insert('a')
        multi.insert('b')
        multi1.insert('b')
        multi.insert('a')
        multi1.insert('c')
        multi1 -= multi
        multi3 = MultiSet()
        multi3.insert('c')
        result = multi1
        expected = multi3
        self.assertEqual(result, expected)

    def test_integer_mutated_subtraction(self):
        x = MultiSet()
        y = MultiSet()
        x.insert(1)
        x.insert(1)
        x.insert(2)
        x.insert(2)
        y.insert(2)
        y.insert(2)
        z = MultiSet()
        z.insert(1)
        z.insert(1)
        x -= y
        result = x
        expected = z
        self.assertEqual(result, expected)

    def test_disjoint_set(self):
        x = MultiSet()
        y = MultiSet()
        x.insert('a')
        x.insert('b')
        x.insert('t')
        x.insert('c')
        x.insert('c')
        y.insert('d')
        y.insert('d')
        y.insert('z')
        y.insert('DYEL?')
        x -= y
        result = x
        z = MultiSet()
        z.insert('c')
        z.insert('c')
        z.insert('t')
        z.insert('b')
        z.insert('a')
        expected = z
        self.assertEqual(result, expected)

    def test_equal_set(self):
        multi = MultiSet()
        multi1 = MultiSet()
        multi.insert(1)
        multi1.insert(5)
        multi1.insert(6)
        multi.insert(6)
        multi1.insert(1)
        multi.insert(5)
        multi -= multi1
        result = multi
        expected = MultiSet()
        self.assertEqual(result, expected)


class TestAddition(unittest.TestCase):

    def test_addition(self):
        multi = MultiSet()
        multi1 = MultiSet()
        multi1.insert('a')
        multi.insert('b')
        multi1.insert('b')
        multi.insert('a')
        multi1.insert('c')
        result = multi1 + multi
        multi2 = MultiSet()
        multi2.insert('c')
        multi2.insert('a')
        multi2.insert('a')
        multi2.insert('b')
        multi2.insert('b')
        expected = multi2
        self.assertEqual(result, expected)

    def test_empt_set(self):
        x = MultiSet()
        y = MultiSet()
        result = x + y
        expected = MultiSet()
        self.assertEqual(result, expected)

    def test_multiple_occurrences(self):
        x = MultiSet()
        y = MultiSet()
        x.insert(5)
        x.insert(5)
        x.insert(10)
        x.insert(10)
        x.insert(10)
        x.insert(17.5)
        x.insert(17.5)
        x.insert(0.5)
        y.insert(17.5)
        y.insert(10)
        y.insert(3.14159)
        y.insert(0.5)
        y.insert(0.5)
        result = x + y
        z = MultiSet()
        z.insert(5)
        z.insert(5)
        z.insert(10)
        z.insert(10)
        z.insert(10)
        z.insert(17.5)
        z.insert(17.5)
        z.insert(0.5)
        z.insert(17.5)
        z.insert(10)
        z.insert(3.14159)
        z.insert(0.5)
        z.insert(0.5)
        expected = z
        self.assertEqual(result, expected)


class TestMutatedAddition(unittest.TestCase):

    def test_mutated_addition(self):
        multi = MultiSet()
        multi1 = MultiSet()
        multi1.insert('a')
        multi.insert('b')
        multi1.insert('b')
        multi.insert('a')
        multi1.insert('c')
        multi1 += multi
        multi3 = MultiSet()
        multi3.insert('c')
        multi3.insert('a')
        multi3.insert('a')
        multi3.insert('b')
        multi3.insert('b')
        result = multi1
        expected = multi3
        self.assertEqual(result, expected)

    def test_empty_set(self):
        x = MultiSet()
        y = MultiSet()
        x += y
        result = x
        expected = MultiSet()
        self.assertEqual(result, expected)

    def test_disjoint_set(self):
        x = MultiSet()
        y = MultiSet()
        x.insert('a')
        x.insert('b')
        x.insert('t')
        x.insert('c')
        x.insert('c')
        y.insert('d')
        y.insert('d')
        y.insert('z')
        y.insert('DYEL?')
        x += y
        result = x
        z = MultiSet()
        z.insert('c')
        z.insert('c')
        z.insert('t')
        z.insert('b')
        z.insert('a')
        z.insert('d')
        z.insert('d')
        z.insert('z')
        z.insert('DYEL?')
        expected = z
        self.assertEqual(result, expected)

    def test_equal_set(self):
        multi = MultiSet()
        multi1 = MultiSet()
        multi.insert(1)
        multi1.insert(5)
        multi1.insert(6)
        multi.insert(6)
        multi1.insert(1)
        multi.insert(5)
        multi += multi1
        result = multi
        z = MultiSet()
        z.insert(1)
        z.insert(1)
        z.insert(6)
        z.insert(6)
        z.insert(5)
        z.insert(5)
        expected = z
        self.assertEqual(result, expected)


class TestAnd(unittest.TestCase):

    def test_and(self):
        multi = MultiSet()
        multi1 = MultiSet()
        multi.insert('a')
        multi.insert('b')
        multi.insert('b')
        multi1.insert('c')
        multi1.insert('b')
        multi.insert('a')
        result = multi & multi1
        multi2 = MultiSet()
        multi2.insert('b')
        expected = multi2
        self.assertEqual(result, expected)

    def test_empty_Set(self):
        x = MultiSet()
        y = MultiSet()
        result = x & y
        expected = MultiSet()
        self.assertEqual(result, expected)

    def test_disjoint_set(self):
        x = MultiSet()
        y = MultiSet()
        x.insert('1')
        x.insert('so many test cases...')
        y.insert('61')
        y.insert('its getting kinda annoying thinking of values')
        result = x & y
        expected = MultiSet()
        self.assertEqual(result, expected)

    def test_multiple_occurrences_set(self):
        x = MultiSet()
        y = MultiSet()
        x.insert(1)
        x.insert(5)
        x.insert(5)
        x.insert(7)
        x.insert(7)
        y.insert(10)
        y.insert(5)
        y.insert(7)
        y.insert(5)
        y.insert(7)
        result = x & y
        z = MultiSet()
        z.insert(5)
        z.insert(5)
        z.insert(7)
        z.insert(7)
        expected = z
        self.assertEqual(result, expected)


class TestMutatedAnd(unittest.TestCase):

    def test_mutate_and_simple(self):
        multi = MultiSet()
        multi1 = MultiSet()
        multi.insert('a')
        multi.insert('b')
        multi.insert('b')
        multi1.insert('c')
        multi1.insert('b')
        multi.insert('a')
        multi &= multi1
        result = multi
        multi2 = MultiSet()
        multi2.insert('b')
        expected = multi2
        self.assertEqual(result, expected)

    def test_empty_set(self):
        x = MultiSet()
        y = MultiSet()
        x &= y
        result = x
        expected = MultiSet()
        self.assertEqual(result, expected)

    def test_disjoint_set(self):
        x = MultiSet()
        y = MultiSet()
        x.insert('1')
        x.insert('so many test cases...')
        y.insert('61')
        y.insert('its getting kinda annoying thinking of values')
        x &= y
        result = x
        expected = MultiSet()
        self.assertEqual(result, expected)


class TestIsDisjoint(unittest.TestCase):

    def test_disjoint(self):
        multi = MultiSet()
        multi1 = MultiSet()
        result = multi.isdisjoint(multi1)
        self.assertTrue(result)

    def test_subset_set(self):
        x = MultiSet()
        y = MultiSet()
        x.insert(1)
        y.insert(3)
        x.insert(5)
        y.insert(1)
        result = x.isdisjoint(y)
        self.assertFalse(result)

    def test_multiple_occurrence_set(self):
        x = MultiSet()
        y = MultiSet()
        x.insert('a')
        x.insert('a')
        x.insert('b')
        x.insert('b')
        x.insert('b')
        x.insert('c')
        y.insert('a')
        y.insert('b')
        y.insert('c')
        result = x.isdisjoint(y)
        self.assertFalse(result)

    def test_true_disjoint(self):
        x = MultiSet()
        y = MultiSet()
        x.insert(1)
        y.insert(2)
        x.insert(100)
        y.insert(101)
        x.insert(500024)
        y.insert(999)
        result = x.isdisjoint(y)
        self.assertTrue(result)

    def test_true_set(self):
        x = MultiSet()
        y = MultiSet()
        x.insert(True)
        y.insert(1)
        result = x.isdisjoint(y)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main(exit=False)
