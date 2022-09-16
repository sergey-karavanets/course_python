with open('nums.txt', encoding='utf-8') as file:
    nums = list(file)
    content = []
    for i in range(len(nums)):
        for j in range(len(nums[i])):
            if nums[i][j] in '0123456789':
                content.append(nums[i][j])
            else:
                content.append(' ')
    total = sum(map(lambda x: int(x.strip()), ''.join(content).split()))
    print(total)