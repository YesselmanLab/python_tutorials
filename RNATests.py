import unittest


class RNA:
    def __init__(self, sequence, secondarystructure):
        self.sequence = sequence
        self.secondarystructure = secondarystructure

    def contains(self, substring):
        if substring in self.secondarystructure:
            return "{} is in secondarystructure".format(substring)

    def find_content(self):
        """Method that takes an input_sequence string and returns a dictionary of normalized bp content"""
        total_nts = len(self.sequence)
        bp_content = {}
        for nt in self.sequence:
            if nt not in bp_content:
                bp_content[nt] = 1.
            else:
                bp_content[nt] += 1.
        for bp in bp_content.keys():
            bp_content[bp] /= float(total_nts)
        return bp_content

    def legal(self):
        count_open_paran = 0
        count_close_paran = 0
        for val in self.secondarystructure:
            if val == "(":
                char_in_s = 1
                count_open_paran += 1
            elif val == ")":
                char_in_s = 1
                count_close_paran += 1
            elif val == ".":
                char_in_s = 1
            else:
                char_in_s = 0
                break
        for val in self.sequence:
            if val == "A":
                char_in_s1 = 1
            elif val == "C":
                char_in_s1 = 1
            elif val == "G":
                char_in_s1 = 1
            elif val == "U":
                char_in_s1 = 1
            else:
                char_in_s = 0
                break
        if char_in_s == 1 and char_in_s1 == 1 and count_open_paran == count_close_paran and len(self.sequence) == len(
                self.secondarystructure):
            return True
        else:
            return False

    def longest_A_substring(self):
        count_A = 0
        count_A1 = 0
        for val in self.sequence:
            if val == "A":
                count_A += 1
                if count_A > count_A1:
                    count_A1 = count_A
            else:
                count_A = 0
        return count_A1

    def __str__(self):
        count_dot = 0
        count = []
        for val in self.secondarystructure:
            if val == ".":
                count_dot += 1
            else:
                count_dot = 0
            count.append(count_dot)
        if 3 in count:
            return "{} contains a triplet-loop".format(self.sequence)
        else:
            return "{} does not contain a triplet-loop".format(self.sequence)

    def __eq__(self, other):
        if self.sequence == other.sequence and self.secondarystructure == other.secondarystructure:
            return "The two RNA strands are equivalent."
        else:
            return "The two RNA strands are not equivalent."


class RNAUnittests(unittest.TestCase):
    """Unit tests for the RNA Class from lesson8.py"""

    def test_contains_method(self):
        """Testing that the .contains() method can identify if a substring is in the secondary structure"""
        sequence = "A"*12
        ss = "((((....))))"
        testrna = RNA(sequence,ss)

        self.assertTrue(testrna.contains("(....)"))
        self.assertFalse(testrna.contains("((.("))

    def test_find_content(self):
        """Testing that the .find_content() returns a dictionary with the appropriate bp frequencies"""
        target1 = {
            "A" : 0.25,
            "C" : 0.25,
            "G" : 0.25,
            "U" : 0.25
        }
        testrna = RNA("ACGU", "....")

        self.assertDictEqual(target1, testrna.find_content())

        target2 = {
            "A" : 1.,
            "C" : 0.,
            "G" : 0.,
            "U" : 0.
        }

        testrna = RNA("AAAA","....")
        self.assertDictEqual(target2, testrna.find_content())

    def test_legal(self):
        """Method to test if the .legal() method can determine if the sequence, structure pair is legal"""
        # should fail
        length_mismatch = RNA("AA",".")
        self.assertFalse(length_mismatch.legal())
        paren_mismatch = RNA("AAA", "(()")
        self.assertFalse(paren_mismatch.legal())
        bad_bp = RNA("AD", "..")
        self.assertFalse(bad_bp.legal())
        # should work
        small = RNA("AAA","...")
        self.assertTrue(small.legal())
        medium = RNA("AAACCCAAAGGG","...(((...)))")
        self.assertTrue(medium.legal())
        large = RNA("A"*1000, "()"*500)
        self.assertTrue(large.legal())

    def test_longest_A_substring(self):
        """Testing that the .longest_A_substring() method functions properly"""
        no_As = RNA("GGGG","....")
        self.assertEqual(no_As.longest_A_substring(),0)
        long_A = RNA("G" + "A"*20 + "C","."*22)
        self.assertEqual(long_A.longest_A_substring(),20)

    def test_eq(self):
        """Testing the overloaded __eq__() method for the RNA class"""
        rna1 = RNA("A",".")
        rna2 = RNA("A",".")
        rna3 = RNA("G",'.')
        self.assertTrue(rna1 == rna2)
        self.assertFalse(rna2 == rna3)

if __name__ == "__main__":
    unittest.main()