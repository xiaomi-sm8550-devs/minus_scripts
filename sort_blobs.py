def sort_blobs_by_blocks(file_path, output_path):
    """
    将清单文件的每个块（以 '#' 开头作为标题）单独排序，并将结果保存到文件。

    Args:
        file_path (str): 清单文件路径。
        output_path (str): 排序后结果保存的文件路径。
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    sorted_blocks = []  # 用于存储排序后的块
    current_block = []  # 当前块内容
    block_title = None  # 当前块标题

    for line in lines:
        if line.startswith("#"):  # 如果是标题
            if block_title is not None:  # 保存上一个块
                sorted_blocks.append((block_title, sorted(current_block)))
            block_title = line.strip()  # 更新当前块标题
            current_block = []  # 清空当前块内容
        else:
            current_block.append(line.strip())  # 添加到当前块

    # 保存最后一个块
    if block_title is not None:
        sorted_blocks.append((block_title, sorted(current_block)))

    # 写入输出文件
    with open(output_path, 'w', encoding='utf-8') as output_file:
        for title, sorted_content in sorted_blocks:
            output_file.write(title + "\n")  # 写入标题
            output_file.writelines(f"{blob}\n" for blob in sorted_content)  # 写入排序后的内容
            output_file.write("\n")  # 每个块之间加一个空行

    print(f"排序后的清单已保存到：{output_path}")


# 使用示例
if __name__ == "__main__":
    input_file = "fuxi.txt"  # 替换为清单文件路径
    output_file = "sorted_blobs.txt"  # 指定排序后保存的文件路径

    sort_blobs_by_blocks(input_file, output_file)
