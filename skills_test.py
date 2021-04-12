################################################################
#   The following is a python test that tests your aptitude 
#   in the language as well as basic bioinformatics tasks. They 
#   are progressively more difficult. Good luck!
################################################################


# Problem 1: Length of Sequence: Difficulty 1/10
# provide an implementation to the below function that finds the length
# of a sequence.

def sequence_length( sequence ):
    pass

# Problem 2: Reverse Sequence. Difficulty 1/10
# provide an implementation to the below function that reverses an RNA
# sequence.

def reverse_sequence( sequence ):
    pass

# Problem 3: Valid sequence. Difficulty 2/10
# provide an implementation to the below function which returns True
# if the sequence only contains the nucleotides A, C, G and U. You 
# can asssume that all nucleotides will be valid and capitalized

def valid_seqeuence( sequence ):
    pass

# Problem 4: Complement. Difficulty 3/10
# provide an implementation to the below function which generates a 
# complement for a given inputted sequence. Below are the individual
# nucleotide changes that should occur
# A => U
# C => G 
# G => C
# U => A
# Example:
# complement( "GGGAAACCC" ) => "CCCUUUGGG"

def complement( sequence ):
    pass

# Problem 5: Longest repeat. Difficulty 3/10
# provide an implementation to the below function which returns the 
# length of the longest nucleotide repeat in an RNA sequence. 
# Example:
# longest_repeat("AGAAGGAAAGGGAAAAA") => 5

def longest_repeat( sequence ): 
    pass


# Problem 6: Sequence composition. Difficulty 4/10
# provide an implementation to the below function which takes a sequence
# as input and returns as dictionary with nucleotide frequencies. 
# Note this function takes a second boolean argument for whether or not
# the composition should be normalized.
# Example:
# sequence_composition("ACGU", False) => {'A': 1, 'C': 1, 'G': 1, 'U': 1}
# sequence_composition("ACGU", True) => {'A': 0.25, 'C': 0.25, 'G': 0.25, 'U': 0.25}

def sequence_composition( sequence, normed=False ):
    pass

# Problem 7: Valid dot bracket. Difficulty 5/10
# provide an implementation to the below function which takes a dot-bracket
# structure as input and returns whether or not it is a valid structure.
# For a dot bracket to be valid, the parantheses must always be balanced.
# Below are some examples of valid and invalid structures:
# valid_db("(((...)))") => True
# valid_db("(((...)((") => False
# valid_db("(((...)))(((...)))") => True
# valid_db("(((...))()(((...)))") => False

def valid_db( dot_bracket ):
    pass


# Problem 8: Lower energy. Difficulty 6/10
# provide an implementation to the below fucntion which takes two sequences
# and returns the sequence with the lower (i.e. more stable) predicted MFE. 
# Doing this will require the fold() function from the RNA module. It has
# the below API:

# RNA.fold( sequence ) => ( structure, mfe )

try:
    import RNA
except:
    pass

def lower_energy( seq1, seq2 ):
    pass


# Problem 9: Nucleotide enum. Difficulty 6/10
# provide an implementation for an enum class. This class should inherit
# from the Enum base class in the enum module. After compelting this, 
# provide an implementation for the sequence_to_enum() function which takes
# a seequence as input and returns a list of enum values. 

# Example:

# sequence_to_enum('ACGU') => [ Nucleotide.A, Nucleotide.C, Nucleotide.G, Nucelotide.U]

try:
    from enum import Enum
except:
    pass

class Nucleotide:
    pass


def seqeuence_to_enum( seqeuence ):
    pass

# Problem 10: Difficult helix identification. Difficulty 7/10
# provide an implementation to the the below function which takes a motif
# graph as input and returns a list of helices which have size less than 2. 
# Note that this implementation will require recursion and a helper 
# function. Some notable details about the motif.Motif API are:
# motif.is_hairpin() => True/False if is a helix
# motif.children() => returns a list of child motifs
# motif.buffer() => size of a helix

try:
    import motif
except:
    pass

def difficult_helices( m : motif.Motif ):
    pass

# Problem 11: Connectivity list. Difficulty 8/10
# Provide an implementation to the below function which takes a dot bracket
# structure as input and returns a list of connectivities. The list should 
# be arranged such that unpaired positions have a value of -1 and those with 
# a complement have the index of their complement. Below are some examples:
# connectivity_list("(((...)))") => [8,7,6,-1,-1,-1,2,1,0]
# connectivity_list("(((...)))((((......))))(...(...)...)") => [8, 7, 6, -1, -1, -1, 2, 1, 0, 22, 21, 20, 19, -1, -1, -1, -1, -1, -1, 12, 11, 10, 9, 35, -1, -1, -1, 31, -1, -1, -1, 27, -1, -1, -1, 23]

def connectivity_list( structure ):
    pass


