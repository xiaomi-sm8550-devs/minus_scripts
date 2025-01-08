from collections import Counter


def find_duplicates(file_path, output_path=None):
    """
    找到单个清单文件中重复的条目，并输出到命令行和文件（可选）。

    Args:
        file_path (str): 清单文件路径。
        output_path (str, optional): 保存重复条目的文件路径。默认为 None，不保存到文件。
    """
    # 读取文件内容
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # 统计每个条目的出现次数
    line_counts = Counter(lines)

    # 找到重复的条目
    duplicates = [line for line, count in line_counts.items() if count > 1]

    # 输出重复条目到命令行
    print("文件中重复的条目：")
    print("".join(duplicates), end="")  # 紧凑输出，不加空行
    print(f"\n（共 {len(duplicates)} 项）\n")

    # 如果指定了输出路径，保存到文件
    if output_path:
        with open(output_path, 'w', encoding='utf-8') as output_file:
            output_file.write("文件中重复的条目：\n")
            output_file.writelines(duplicates)
        print(f"重复条目已保存到文件：{output_path}")


# 使用示例
if __name__ == "__main__":
    file_path = "fuxi.txt"  # 替换为清单文件的路径
    output_path = "duplicates_in_file.txt"  # 可选，保存重复条目的文件路径

    find_duplicates(file_path, output_path)
