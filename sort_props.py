def sort_build_prop_by_blocks(file_path, output_path):
    """
    对 build.prop 文件中的每个块（以 '#' 开头作为标题）单独排序，并将结果保存到文件。

    Args:
        file_path (str): build.prop 文件路径。
        output_path (str): 排序后结果保存的文件路径。
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    sorted_blocks = []  # 用于存储排序后的块
    current_block = []  # 当前块内容
    block_title = None  # 当前块标题

    for line in lines:
        stripped_line = line.strip()
        if stripped_line.startswith("#"):  # 如果是注释标题
            if block_title is not None:  # 保存上一个块
                sorted_blocks.append((block_title, sorted(current_block)))
            block_title = stripped_line  # 更新当前块标题
            current_block = []  # 清空当前块内容
        elif stripped_line:  # 非空行
            current_block.append(stripped_line)  # 添加到当前块

    # 保存最后一个块
    if block_title is not None:
        sorted_blocks.append((block_title, sorted(current_block)))

    # 写入输出文件
    with open(output_path, 'w', encoding='utf-8') as output_file:
        for title, sorted_content in sorted_blocks:
            output_file.write(title + "\n")  # 写入标题
            output_file.writelines(f"{entry}\n" for entry in sorted_content)  # 写入排序后的内容
            output_file.write("\n")  # 每个块之间添加空行

    print(f"排序后的 build.prop 已保存到：{output_path}")

# 使用示例
if __name__ == "__main__":
    input_file = "build1.prop"  # 替换为输入的 build.prop 文件路径
    output_file = "sorted_build.prop"  # 指定排序后保存的文件路径

    sort_build_prop_by_blocks(input_file, output_file)
