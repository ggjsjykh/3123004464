import pytest
from main import read_file, compute_minhash, jaccard_similarity, longest_common_subsequence, calculate_similarity, \
    write_result


# 测试 read_file 函数
def test_read_file():
    # 创建一个临时文件
    with open("test.txt", "w", encoding="utf-8") as f:
        f.write("这是一个测试文件。")

    # 测试读取文件内容
    assert read_file("test.txt") == "这是一个测试文件。"


# 测试 compute_minhash 函数
def test_compute_minhash():
    text = "这是一个测试文本。"
    minhash = compute_minhash(text)
    assert minhash is not None


# 测试 jaccard_similarity 函数
def test_jaccard_similarity():
    orig_text = "这是一个测试文本。"
    plag_text = "这是一个测试文本。"
    similarity = jaccard_similarity(orig_text, plag_text)
    assert similarity == 1.0


# 测试 longest_common_subsequence 函数
def test_longest_common_subsequence():
    a = "abcde"
    b = "abzde"
    lcs_length = longest_common_subsequence(a, b)
    assert lcs_length == 4


# 测试 calculate_similarity 函数
def test_calculate_similarity():
    orig_text = "这是一个测试文本。"
    plag_text = "这是一个测试文本。"
    similarity = calculate_similarity(orig_text, plag_text, jaccard_threshold=0.1)
    assert similarity == 100.0


# 测试 write_result 函数
def test_write_result():
    # 创建一个临时文件
    with open("test_output.txt", "w", encoding="utf-8") as f:
        f.write("")

    # 测试写入结果
    write_result("test_output.txt", 100.0)
    with open("test_output.txt", "r", encoding="utf-8") as f:
        result = f.read()
    assert result == "100.00\n"


# 清理临时文件
def teardown_module():
    import os
    os.remove("test.txt")
    os.remove("test_output.txt")