import argparse


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


def main():
    args = parse_arguments()
    # 读取文件内容
    orig_text = read_file(args.orig_file)
    plag_text = read_file(args.plag_file)
