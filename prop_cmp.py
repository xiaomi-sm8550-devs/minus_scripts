def compare_build_props(file1_path, file2_path, output_path):
    """
    比较两个 build.prop 文件中的参数差异，并将结果保存到文件。

    Args:
        file1_path (str): 第一个 build.prop 文件路径。
        file2_path (str): 第二个 build.prop 文件路径。
        output_path (str): 差异结果保存的文件路径。
    """

    def parse_build_prop(file_path):
        """解析 build.prop 文件为字典"""
        props = {}
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line and not line.startswith("#"):  # 忽略注释和空行
                    key_value = line.split("=", 1)
                    if len(key_value) == 2:
                        key, value = key_value
                        props[key.strip()] = value.strip()
        return props

    # 解析两个文件
    props1 = parse_build_prop(file1_path)
    props2 = parse_build_prop(file2_path)

    # 比较差异
    only_in_file1 = {k: v for k, v in props1.items() if k not in props2}
    only_in_file2 = {k: v for k, v in props2.items() if k not in props1}
    different_values = {k: (props1[k], props2[k]) for k in props1 if k in props2 and props1[k] != props2[k]}

    # 写入差异到文件
    with open(output_path, 'w', encoding='utf-8') as output_file:
        output_file.write("仅在第一个文件中的参数：\n")
        for k, v in only_in_file1.items():
            output_file.write(f"{k}={v}\n")
        output_file.write("\n")

        output_file.write("仅在第二个文件中的参数：\n")
        for k, v in only_in_file2.items():
            output_file.write(f"{k}={v}\n")
        output_file.write("\n")

        output_file.write("键相同但值不同的参数：\n")
        for k, (v1, v2) in different_values.items():
            output_file.write(f"{k}：文件1值={v1}, 文件2值={v2}\n")

    print(f"参数差异已保存到：{output_path}")


# 使用示例
if __name__ == "__main__":
    file1_path = "build1.prop"  # 替换为第一个 build.prop 文件路径
    file2_path = "build2.prop"  # 替换为第二个 build.prop 文件路径
    output_path = "build_props_diff.txt"  # 差异结果保存的文件路径

    compare_build_props(file1_path, file2_path, output_path)
