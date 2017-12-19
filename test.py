import unittest

from task import handle_numbers, handle_string, handle_list_of_tuples


class HandleNumberTestCase(unittest.TestCase):

    def test_positive_range(self):
        self.assertEqual(handle_numbers(1, 10, 2), 5)
        self.assertEqual(handle_numbers(15, 29, 6), 2)
        self.assertEqual(handle_numbers(12, 21, 11), 0)

    def test_negative_range(self):
        self.assertEqual(handle_numbers(-12, 0, 2), 7)
        self.assertEqual(handle_numbers(-31, -16, -5), 3)
        self.assertEqual(handle_numbers(-5,-4, -3), 0)

    def test_divisible_by_zero(self):
        self.assertEqual(handle_numbers(1, 10, 0), 0)


class HandleStringTestCase(unittest.TestCase):

    def test_letter_and_number(self):
        t1 = handle_string("Hello world! 123!")
        self.assertEqual(t1['letters'], 10)
        self.assertEqual(t1['numbers'], 3)

        t2 = handle_string("Som1 phr3e 21 ! l10")
        self.assertEqual(t2['letters'], 8)
        self.assertEqual(t2['numbers'], 6)

    def test_only_letter(self):
        t1 = handle_string("Hello world !!!")
        self.assertEqual(t1['letters'], 10)
        self.assertEqual(t1['numbers'], 0)

    def test_only_number(self):
        t1 = handle_string("93983 291_43 9")
        self.assertEqual(t1['letters'], 0)
        self.assertEqual(t1['numbers'], 11)


class HandleListOfTuplesTestCase(unittest.TestCase):

    def test_sort(self):
        list1 = [
            ("Tom", "19", "167", "54"),
            ("Jony", "24", "180", "69"),
            ("Json", "21", "185", "75"),
            ("John", "27", "190", "87"),
            ("Jony", "24", "191", "98"),
        ]
        result1 = [
            ("John", "27", "190", "87"),
            ("Jony", "24", "191", "98"),
            ("Jony", "24", "180", "69"),
            ("Json", "21", "185", "75"),
            ("Tom", "19", "167", "54"),
        ]
        self.assertListEqual(handle_list_of_tuples(list1), result1)

        list2 = [
            ("Tom", "19", "167", "54"),
            ("Jony", "25", "180", "69"),
            ("Json", "21", "185", "75"),
            ("Jony", "27", "190", "87"),
            ("Jony", "24", "191", "98"),
        ]
        result2 = [
            ("Jony", "27", "190", "87"),
            ("Jony", "25", "180", "69"),
            ("Jony", "24", "191", "98"),
            ("Json", "21", "185", "75"),
            ("Tom", "19", "167", "54"),
        ]
        self.assertListEqual(handle_list_of_tuples(list2), result2)


if __name__ == '__main__':
    unittest.main()