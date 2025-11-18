def longest_common_substring(s1, s2):
    n, m = len(s1), len(s2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    max_len = 0
    end_idx = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_len:
                    max_len = dp[i][j]
                    end_idx = i
            else:
                dp[i][j] = 0

    start = end_idx - max_len
    substring = s1[start:end_idx]
    return substring, max_len


a = input("Pierwszy napis: ")
b = input("Drugi napis: ")
sub, length = longest_common_substring(a, b)
print(f"Najdłuższy spójny podciąg: '{sub}' (długość: {length})")