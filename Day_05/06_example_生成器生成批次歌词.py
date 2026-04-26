"""
案例：基于传入的数值（每批次的歌词条数），创建 生成器，生成批次歌词

需求：基于文件中周杰伦的歌词，创建生成器，根据传入的每批次的歌词条数，生成歌词批次
"""
import math

def dataset_loader(batch_size):
    """
    自定义的歌词批量生成器
    :param batch_size: 每批次的歌词条数
    :return: 生成器，每个元素都是一批次的数据，例如：（8条，8条，8条...）
    """
    with open('./data/test.txt', 'r', encoding='utf-8') as src_f:
        # lines = [line.strip() for line in src_f.readlines()]
        lines = src_f.readlines()

        total_batch = math.ceil(len(lines) / batch_size)

        for idx in range(total_batch):
            yield lines[idx * batch_size : (idx + 1) * batch_size]

dl = dataset_loader(8)
print(next(dl))
print(next(dl))

for batch_data in dl:
    print(batch_data)
