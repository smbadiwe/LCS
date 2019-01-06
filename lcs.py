
def lcs3(str1, str2):
    """
    Find the length of the longest subsequence common to two strings. 
    Space: O(mn). Time: O(mn)
    :param str1: first string
    :param str1: second string
    :return: the length of the longest subsequence, as well as the common subsequence
    """
    m = len(str1) + 1
    n = len(str2) + 1
    lookup = [None] * m
    path = [None] * m
    for i in range(m):
        lookup[i] = [None] * n
        path[i] = [None] * n

    # path: -1 => from behind; 0 => from diag; 1 => from top; 
    # compute LCS of str1[0...i] and str2[0...j] substrings
    for i in range(m):
        lookup[i][0] = 0
        path[i][0] = 1  # above
    for j in range(n):
        lookup[0][j] = 0
        path[0][j] = -1  # behind
    for i in range(1, m):
        for j in range(1, n):
            path_val = -1  # behind
            maximum = lookup[i][j-1]
            if lookup[i-1][j] > lookup[i][j-1]:
                path_val = 1  # above
                maximum = lookup[i-1][j]

            if str1[i-1] == str2[j-1]:
                if (1+lookup[i-1][j-1]) > maximum:
                    path_val = 0  # diag
                    maximum = 1+lookup[i-1][j-1]
            
            lookup[i][j] = maximum
            path[i][j] = path_val

    path_trace = []
    i = m - 1
    j = n - 1
    print("str1: {}. str2: {}.".format(str1, str2))
    while True:
        # print("\ti: {}. j: {}. lookup[i][j]: {}. path[i][j]: {}".format(i, j, lookup[i][j], path[i][j]))
        if i == 0 or j == 0:
            break
        if path[i][j] == 0:  # from diag
            path_trace.append(str1[i-1])
            i -= 1
            j -= 1
        elif path[i][j] == 1:  # from above
            i -= 1
        elif path[i][j] == -1:  # from behind
            j -= 1
    path_trace.reverse() 
    return path_trace


def lcs2(str1, str2):
    """
    Find the length of the longest subsequence common to two strings. 
    Space: O(n). Time: O(mn)
    :param str1: first string
    :param str1: second string
    :return: the length of the longest subsequence
    """
    m = len(str1)
    n = len(str2)
    lookup = [None] * 2
    for i in range(2):
        lookup[i] = [0] * n

    for i in range(m):
        # move the bottom row up so we can set the bottom again
        for j in range(n):
            lookup[0][j] = lookup[1][j]
        # compute LCS of str1[0...i] and str2[0...j] substrings
        for j in range(n):
            maximum = max(lookup[0][j], (0 if j == 0 else lookup[1][j-1]))   # max(above, behind)
            if str1[i] == str2[j]:
                maximum = max(maximum, (1 if j == 0 else 1+lookup[0][j-1]))
            lookup[1][j] = maximum

    return lookup[1][n-1]


def lcs1(str1, str2):
    """
    Find the length of the longest subsequence common to two strings. 
    Space: O(mn). Time: O(mn)
    :param str1: first string
    :param str1: second string
    :return: the length of the longest subsequence
    """
    m = len(str1) + 1
    n = len(str2) + 1
    lookup = [None] * m
    for i in range(m):
        lookup[i] = [None] * n

    # compute LCS of str1[0...i] and str2[0...j] substrings
    for i in range(m):
        lookup[i][0] = 0
    for j in range(n):
        lookup[0][j] = 0
    for i in range(1, m):
        for j in range(1, n):
            maximum = max(lookup[i][j-1], lookup[i-1][j])
            if str1[i-1] == str2[j-1]:
                maximum = max(maximum, 1+lookup[i-1][j-1])
            lookup[i][j] = maximum

    return lookup[m-1][n-1]


def lcs_recursive_from_back(str1, str2):
    """
    Find the length of the longest subsequence common to two strings. 
    Space: O(.). Time: O(.)
    :param str1: first string
    :param str1: second string
    :return: the length of the longest subsequence
    """
    m = len(str1)
    n = len(str2)
    """
    Let the input sequences be X[0..m-1] and Y[0..n-1] of lengths m and n respectively. And let L(X[0..m-1], Y[0..n-1]) be the length of LCS of the two sequences X and Y. Following is the recursive definition of L(X[0..m-1], Y[0..n-1]).

    If last characters of both sequences match (or X[m-1] == Y[n-1]) then
    L(X[0..m-1], Y[0..n-1]) = 1 + L(X[0..m-2], Y[0..n-2])

    If last characters of both sequences do not match (or X[m-1] != Y[n-1]) then
    L(X[0..m-1], Y[0..n-1]) = MAX ( L(X[0..m-2], Y[0..n-1]), L(X[0..m-1], Y[0..n-2]) )
    """
    print("str1: {}.\tstr2: {}".format(str1, str2))
    if m == 0 or n == 0:
        return 0
    if str1[m - 1] == str2[n - 1]:
        return 1 + lcs_recursive_from_back(str1[:m-1], str2[:n-1])
    return max(lcs_recursive_from_back(str1[:m-1], str2[:n]), lcs_recursive_from_back(str1[:m], str2[:n-1]))


def lcs_recursive_from_front(str1, str2):
    """
    Find the length of the longest subsequence common to two strings. 
    Space: O(.). Time: O(.)
    :param str1: first string
    :param str1: second string
    :return: the length of the longest subsequence
    """
    m = len(str1)
    n = len(str2)

    def lcs_recursive_do(i, j):
        print("str1: {}.\tstr2: {}".format(str1[i:], str2[j:]))
        if i == m or j == n:
            return 0
        if str1[i] == str2[j]:
            return 1 + lcs_recursive_do(i+1, j+1)
        return max(lcs_recursive_do(i+1, j), lcs_recursive_do(i, j+1))
    
    return lcs_recursive_do(0, 0)


def lcs_test():
    # print(lcs_recursive_from_front("TGCATA", "ATCTGAT"))
    subsequence = lcs3("TGCATA", "ATCTGAT")
    print("".join(subsequence))
    print("Length: %d" % len(subsequence))
    print()
    subsequence = lcs3("ABCDGH", "AEDFHR")
    print("".join(subsequence))
    print("Length: %d" % len(subsequence))
    print()
    subsequence = lcs3("AGGTAB", "GXTXAYB")
    print("".join(subsequence))
    print("Length: %d" % len(subsequence))


lcs_test()