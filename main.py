import argparse
from datasketch import MinHash
import jieba


def parse_arguments():
    """
    解析命令行参数，获取文件路径。
    """
    parser = argparse.ArgumentParser(description="Jaccard similarity and LCS")
    parser.add_argument("orig_file", type=str, help="Path to the original paper file")
    parser.add_argument("plag_file", type=str, help="Path to the plagiarized paper file")
    parser.add_argument("output_file", type=str, help="Path to the output file")
    return parser.parse_args()


def read_file(file_path):
    """
    读取文件内容。
    """
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


def compute_minhash(text, num_perm=128):
    """
    计算文本的MinHash签名。
    """
    m = MinHash(num_perm=num_perm)
    # 使用 jieba 进行中文分词
    for word in jieba.cut(text):
        m.update(word.encode('utf-8'))
    return m


def jaccard_similarity(orig_text, plag_text, num_perm=128):
    """
    计算两个文本的Jaccard相似度。
    """
    orig_minhash = compute_minhash(orig_text, num_perm)
    plag_minhash = compute_minhash(plag_text, num_perm)

    return orig_minhash.jaccard(plag_minhash)


def longest_common_subsequence(a, b):
    """
    计算两个字符串的最长公共子序列（LCS）。
    """
    m, n = len(a), len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


def calculate_similarity(orig_text, plag_text, jaccard_threshold=0.5):
    """
    计算两个文本的相似度。
    """
    # Step 1: Use Jaccard similarity to quickly filter
    jaccard_sim = jaccard_similarity(orig_text, plag_text)
    print(jaccard_sim)
    if jaccard_sim < jaccard_threshold:
        return 0.0

    # Step 2: Use LCS for precise calculation
    lcs_length = longest_common_subsequence(orig_text, plag_text)
    plag_length = len(plag_text)
    if plag_length == 0:
        return 0.0
    return lcs_length / plag_length * 100


def write_result(output_file, similarity):
    """
    将结果写入到指定的输出文件。
    """
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("{:.2f}\n".format(similarity))


def main():
    args = parse_arguments()
    # 读取文件内容
    orig_text = read_file(args.orig_file)
    plag_text = read_file(args.plag_file)
    # 计算相似度
    similarity = calculate_similarity(orig_text, plag_text)

    # 写入结果
    write_result(args.output_file, similarity)


if __name__ == "__main__":
    main()
