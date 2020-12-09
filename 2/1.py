List = [1, 2, 3, 4, 5, 6, 7, 8, 8, 8, 9, 9]
if (List):
    # sort使相同的元素相邻，便于删除
    List.sort()
    last = List[-1]
    # 为防止删除扰乱元素位置，由后向前遍历
    for i in range(len(List) - 2, -1, -1):
        if (List[i + 1] == List[i]):
            del List[i]
print(List)
