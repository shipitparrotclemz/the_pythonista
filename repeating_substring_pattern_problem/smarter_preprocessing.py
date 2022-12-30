def smarter_preprocess_lpp_table(s: str) -> list[int]:
    """
    Calculates the lpp table of `s` using a slightly smarter approach;

    Using the lpp of the previous substring, we can infer exactly where the prefix and suffix candidate are in `s`

    It's not visible in the code, but given

    the prefix candidate and suffix candidate has the same length M

    N is the length of the string

    N = len(s)

    For a given substring ss from index 0 to N

    M is the length of the prefix candidate / suffix candidate for ss

    M = lpp_table[N-1] + 1

    prefix candidate is from index 0 to s[:M]
    suffix candidate is from index N - M to M: s[N-M:]

    Time Complexity: O(N**2)
    - With the optimization of using the lpp table, we avoid a brute force search for where the prefix and suffix are
    - This allows the calculation of the lpp for a given substring to be done in O(N) time
    - However, since we have N-1 substrings, the total time complexity is O(N**2)

    Space Complexity: O(N)
    - memory used for lpp table scales linearly with length of s; N
    """
    n: int = len(s)
    # lpp of previous substring is used to infer the first few characters of the prefix / suffix candidate as equal
    lpp_table: list[int] = [0] * n

    # O(N) iteration, each iteration takes O(N) time
    for end_index in range(1, n):
        # calculate the lpp of the substring from index 0 to end_index, inclusive

        # if the previous substring from index 0 to 1 has a lpp of 1
        # the current substring from index 0 to 2 starts with a possible lpp of 2
        lpp_candidate_length: int = lpp_table[end_index - 1] + 1

        # iterate the candidate prefix and suffix to check if they are equal
        # use prefix_start and suffix_start to iterate the prefix and suffix candidate
        prefix_start: int = 0
        suffix_start: int = end_index - lpp_candidate_length + 1
        suffix_end: int = end_index

        # O(N) iteration. N is the length of the candidate prefix / suffix
        while suffix_start < suffix_end + 1:
            if s[prefix_start] == s[suffix_start]:
                prefix_start += 1
                suffix_start += 1
            else:
                if prefix_start == 0:
                    # move to the next possible lpp candidate
                    break
                else:
                    # we are still calculating the lpp for this substring
                    # the next possible lpp candidate for this current substring has length lpp_table[prefix_start - 1] + 1
                    # move to the next possible lpp candidate
                    lpp_candidate_length = lpp_table[prefix_start - 1] + 1
                    prefix_start = 0
                    suffix_start = end_index - lpp_candidate_length + 1

        if suffix_start == suffix_end + 1:
            # the prefix and suffix candidate are equal! set lpp_table to previous substring lpp + 1
            lpp_table[end_index] = lpp_candidate_length
            # else, leave lpp of current substring to 0

    return lpp_table


if __name__ == "__main__":
    assert smarter_preprocess_lpp_table("abacababac") == [0, 0, 1, 0, 1, 2, 3, 2, 3, 4]
    assert smarter_preprocess_lpp_table("abacababacab") == [0, 0, 1, 0, 1, 2, 3, 2, 3, 4, 5, 6]
    assert smarter_preprocess_lpp_table("abc") == [0, 0, 0]
    assert smarter_preprocess_lpp_table("ababc") == [0, 0, 1, 2, 0]
    assert smarter_preprocess_lpp_table("abcabc") == [0, 0, 0, 1, 2, 3]
    assert smarter_preprocess_lpp_table("abcab") == [0, 0, 0, 1, 2]
    assert smarter_preprocess_lpp_table("abcabcabc") == [0, 0, 0, 1, 2, 3, 4, 5, 6]
    assert smarter_preprocess_lpp_table("abcabcabcabc") == [0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert smarter_preprocess_lpp_table("abcabcabcabcabc") == [0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    assert smarter_preprocess_lpp_table("abcabcabcabcabcabc") == [0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    assert smarter_preprocess_lpp_table("abcabcabcabcabcabcabc") == [0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
