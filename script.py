import os

def analyze_differences(file1_path, file2_path, output_dir=None):
    # 读取文件内容
    with open(file1_path, 'r', encoding='utf-8') as f1, open(file2_path, 'r', encoding='utf-8') as f2:
        content1 = set(f1.readlines())
        content2 = set(f2.readlines())

    # 计算差异
    only_in_file1 = sorted(content1 - content2)
    only_in_file2 = sorted(content2 - content1)
    common_entries = sorted(content1 & content2)

    # 在命令窗口中输出
    print("仅在第一个文件中的条目：")
    print("".join(only_in_file1), end="")  # 输出每行不加额外换行
    print(f"\n（共 {len(only_in_file1)} 项）\n")

    print("仅在第二个文件中的条目：")
    print("".join(only_in_file2), end="")  # 输出每行不加额外换行
    print(f"\n（共 {len(only_in_file2)} 项）\n")

    print("两个文件共有的条目：")
    print("".join(common_entries), end="")  # 输出每行不加额外换行
    print(f"\n（共 {len(common_entries)} 项）\n")

    # 如果指定了输出目录，将结果保存到文件
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)

        output_file1 = os.path.join(output_dir, 'only_in_file1.txt')
        output_file2 = os.path.join(output_dir, 'only_in_file2.txt')
        output_common = os.path.join(output_dir, 'common_entries.txt')

        with open(output_file1, 'w', encoding='utf-8') as f:
            f.write("仅在第一个文件中的条目：\n")
            f.writelines(only_in_file1)

        with open(output_file2, 'w', encoding='utf-8') as f:
            f.write("仅在第二个文件中的条目：\n")
            f.writelines(only_in_file2)

        with open(output_common, 'w', encoding='utf-8') as f:
            f.write("两个文件共有的条目：\n")
            f.writelines(common_entries)

        print("结果已保存到文件：")
        print(f"仅在第一个文件中的条目：{output_file1}")
        print(f"仅在第二个文件中的条目：{output_file2}")
        print(f"两个文件共有的条目：{output_common}")

if __name__ == "__main__":
    file1_path = "fuxi.txt"  # 替换为第一个清单的路径
    file2_path = "socrates.txt"  # 替换为第二个清单的路径
    output_dir = ".\\"  # 如果不需要保存到文件，将其设置为 None，否则指定一个输出目录

    analyze_differences(file1_path, file2_path, output_dir)
