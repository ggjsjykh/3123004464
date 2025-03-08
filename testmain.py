from main import read_file, compute_minhash, jaccard_similarity, longest_common_subsequence, calculate_similarity, write_result
import os
import pytest


# 测试 read_file 函数
def test_read_file():
    # 创建一个临时文件
    with open("test.txt", "w", encoding="utf-8") as f:
        f.write("这是一个测试文件。")

    # 测试读取文件内容
    assert read_file("test.txt") == "这是一个测试文件。"


def test_read_file_file_not_found():
    # 测试文件不存在的情况
    with pytest.raises(SystemExit):
        read_file("non_existent_file.txt")


def test_read_file_unicode_decode_error():
    # 创建一个非 UTF-8 编码的文件
    with open("test_gbk_file.txt", "w", encoding="gbk") as f:
        f.write("这是一个测试文件。")

    # 测试读取非 UTF-8 编码的文件
    with pytest.raises(SystemExit):
        read_file("test_gbk_file.txt")

    # 删除测试文件
    os.remove("test_gbk_file.txt")


# 测试 compute_minhash 函数
def test_compute_minhash():
    text = "这是一个测试文本。"
    minhash = compute_minhash(text)
    assert minhash is not None


def test_compute_minhash_empty_text():
    # 测试空文本
    minhash = compute_minhash("")
    assert minhash is not None


# 测试 jaccard_similarity 函数
def test_jaccard_similarity():
    orig_text = "这是一个测试文本。"
    plag_text = "这是一个测试文本。"
    similarity = jaccard_similarity(orig_text, plag_text)
    assert similarity == 1.0


def test_jaccard_similarity_different_texts():
    orig_text = "这是一个测试文本。"
    plag_text = "这是一个不同的测试文本。"
    similarity = jaccard_similarity(orig_text, plag_text)
    assert similarity < 1.0


def test_jaccard_similarity_empty_texts():
    orig_text = ""
    plag_text = ""
    similarity = jaccard_similarity(orig_text, plag_text)
    assert similarity == 0.0


# 测试 longest_common_subsequence 函数
def test_longest_common_subsequence():
    a = "abcde"
    b = "abzde"
    lcs_length = longest_common_subsequence(a, b)
    assert lcs_length == 4


def test_longest_common_subsequence_empty_strings():
    a = ""
    b = ""
    lcs_length = longest_common_subsequence(a, b)
    assert lcs_length == 0


def test_longest_common_subsequence_one_empty_string():
    a = "abcde"
    b = ""
    lcs_length = longest_common_subsequence(a, b)
    assert lcs_length == 0


# 测试 calculate_similarity 函数
def test_calculate_similarity():
    orig_text = "这是一个测试文本。"
    plag_text = "这是一个测试文本。"
    similarity = calculate_similarity(orig_text, plag_text, jaccard_threshold=0.1)
    assert similarity == 100.0


def test_calculate_similarity_below_threshold():
    orig_text = "这是一个测试文本。"
    plag_text = "这是一个完全不同的文本。"
    similarity = calculate_similarity(orig_text, plag_text, jaccard_threshold=0.1)
    assert similarity == 0.0


def test_calculate_similarity_empty_text():
    orig_text = ""
    plag_text = ""
    similarity = calculate_similarity(orig_text, plag_text, jaccard_threshold=0.1)
    assert similarity == 0.0


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

    # 删除测试文件
    os.remove("test_output.txt")


def test_write_result_file_not_writable():
    # 测试写入不可写的文件
    with pytest.raises(SystemExit):
        write_result("non_writable_file.txt", 100.0)


# 清理临时文件
def teardown_module():
    files_to_remove = ["test.txt", "test_gbk_file.txt", "test_output.txt", "non_writable_file.txt"]
    for file in files_to_remove:
        if os.path.exists(file):
            os.remove(file)


