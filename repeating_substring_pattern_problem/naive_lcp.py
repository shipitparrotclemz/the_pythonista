def naive_longest_proper_prefix_table(s: str) -> list[int]:
    """
    Returns the longest proper prefix for all substrings in s

    Time Complexity: O(N**3)
    - Takes O(N**2) time for each substring in s
    - We have N-1 substrings to process in `s`

    Space Complexity: O(N)
    - memory in lpp_table scales linearly with the length of s
    """
    lpp_table: list[int] = [0] * len(s)

    for end_index in range(len(s)):
        lpp_table[end_index] = len(naive_longest_proper_prefix(s, end_index))

    return lpp_table


def naive_longest_proper_prefix(s: str, end_index: int) -> str:
    """
    Calculates the longest common prefix for substring in `s`, from index 0 to end_index
    Given s = "abc", start_index = 0, end_index = 0
    We will calculate the longest proper prefix for "a"

    Time Complexity: O(N^2)
    - Worst case happens when all characters in `s` are equal, except the last character
    - e.g "aaac"
    - This causes the suffix_index to never reach the end for N iterations

    Space Complexity: O(N)
    - Memory used is the longest proper prefix, which is a substring of s
    - In the worst case, the longest proper prefix is of 1 character less than the length of s
    e.g longer proper prefix of "aaaa" is "aaa"
    """
    start_suffix_index: int = 1
    prefix_index: int = 0
    suffix_index: int = start_suffix_index

    while suffix_index < end_index + 1:
        if s[prefix_index] == s[suffix_index]:
            """
            prefix and suffix candidate are equal!
            """
            prefix_index += 1
            suffix_index += 1
        else:
            prefix_index = 0
            start_suffix_index += 1
            suffix_index = start_suffix_index
    return s[:prefix_index]


if __name__ == "__main__":
    # Test naive longest proper prefix
    assert naive_longest_proper_prefix("abacababacab", 11) == "abacab"
    assert naive_longest_proper_prefix("abc", 2) == ""
    assert naive_longest_proper_prefix("ababc", 4) == ""
    assert naive_longest_proper_prefix("abcabc", 5) == "abc"
    assert naive_longest_proper_prefix("abcab", 4) == "ab"
    assert naive_longest_proper_prefix("abcabcabc", 8) == "abcabc"
    assert naive_longest_proper_prefix("abcabcabcabc", 11) == "abcabcabc"
    assert naive_longest_proper_prefix("abcabcabcabcabc", 14) == "abcabcabcabc"
    assert naive_longest_proper_prefix("abcabcabcabcabcabc", 17) == "abcabcabcabcabc"
    assert naive_longest_proper_prefix("abcabcabcabcabcabcabc", 20) == "abcabcabcabcabcabc"

    assert naive_longest_proper_prefix_table("abacababacab") == [0, 0, 1, 0, 1, 2, 3, 2, 3, 4, 5, 6]
    assert naive_longest_proper_prefix_table("abc") == [0, 0, 0]
    assert naive_longest_proper_prefix_table("ababc") == [0, 0, 1, 2, 0]
    assert naive_longest_proper_prefix_table("abcabc") == [0, 0, 0, 1, 2, 3]
    assert naive_longest_proper_prefix_table("abcab") == [0, 0, 0, 1, 2]
    assert naive_longest_proper_prefix_table("abcabcabc") == [0, 0, 0, 1, 2, 3, 4, 5, 6]
    assert naive_longest_proper_prefix_table("abcabcabcabc") == [0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert naive_longest_proper_prefix_table("abcabcabcabcabc") == [0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    assert naive_longest_proper_prefix_table("abcabcabcabcabcabc") == [0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    assert naive_longest_proper_prefix_table("abcabcabcabcabcabcabc") == [0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
