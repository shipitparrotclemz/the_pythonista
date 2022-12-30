def kmp_preprocess_lpp_table(s: str) -> list[int]:
    """
    Calculates the lpp table of `s` using the KMP algorithm

    It's not visible in the code, but given

    the prefix candidate and suffix candidate has the same length M

    N is the length of the string

    N = len(s)

    prefix_index points at the last character of a prefix candidate substring
    suffix_index points at the last character of a suffix candidate substring

    M is the length of the prefix candidate / suffix candidate
    M = prefix_index + 1

    prefix candidate is from index 0 to prefix_index: s[:prefix_index + 1]
    suffix candidate is from index suffix_index - M + 1 to suffix_index: s[suffix_index-M+1):]

    Time Complexity: O(N)
    - With the optimization of using the lpp table, we only need to iterate through the string once
    Space Complexity: O(N)
    - memory used for lpp table scales linearly with length of s; N
    """
    n: int = len(s)
    # lpp of previous substring is used to infer the first few characters of the prefix / suffix candidate as equal
    lpp_table: list[int] = [0] * n

    prefix_index: int = 0
    suffix_index: int = 1

    while suffix_index < n:
        if s[prefix_index] == s[suffix_index]:
            """
            prefix and suffix candidate are equal!
            set the lpp of the current substring from index 0 to suffix_index to the length of the prefix candidate / suffix_candidate
            """
            lpp_length: int = prefix_index + 1
            lpp_table[suffix_index] = lpp_length

            """
            Now, we are ready to move on to calculate the lpp of the next substring
            
            Optimization: we are using the lpp of the previous substring,
            to infer the first few characters of the current prefix and suffix candidate as equal, and skip visiting them.
            """
            # expand the substring to the right by one
            suffix_index += 1
            prefix_index = lpp_table[suffix_index - 1]
        else:
            # if prefix_index == 0, the current substring has no longest proper prefix.
            if prefix_index == 0:
                # Leave the lpp of the current substring as 0
                """
                Now, we are ready to move on to calculate the lpp of the next substring

                Optimization: we are using the lpp of the previous substring,
                to infer the first few characters of the current prefix and suffix candidate as equal, and skip visiting them.
                """
                # expand the substring to the right by one
                suffix_index += 1
                prefix_index = lpp_table[suffix_index - 1]
            else:
                # we are still calculating the lpp for this substring
                # the next possible lpp candidate for this current substring has length lpp_table[prefix_start - 1] + 1
                # move to the next possible lpp candidate
                prefix_index = lpp_table[prefix_index - 1]
    return lpp_table


if __name__ == "__main__":
    assert kmp_preprocess_lpp_table("abacababac") == [0, 0, 1, 0, 1, 2, 3, 2, 3, 4]
    assert kmp_preprocess_lpp_table("abacababacab") == [0, 0, 1, 0, 1, 2, 3, 2, 3, 4, 5, 6]
    assert kmp_preprocess_lpp_table("abc") == [0, 0, 0]
    assert kmp_preprocess_lpp_table("ababc") == [0, 0, 1, 2, 0]
    assert kmp_preprocess_lpp_table("abcabc") == [0, 0, 0, 1, 2, 3]
    assert kmp_preprocess_lpp_table("abcab") == [0, 0, 0, 1, 2]
    assert kmp_preprocess_lpp_table("abcabcabc") == [0, 0, 0, 1, 2, 3, 4, 5, 6]
    assert kmp_preprocess_lpp_table("abcabcabcabc") == [0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert kmp_preprocess_lpp_table("abcabcabcabcabc") == [0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    assert kmp_preprocess_lpp_table("abcabcabcabcabcabc") == [0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    assert kmp_preprocess_lpp_table("abcabcabcabcabcabcabc") == [0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]

