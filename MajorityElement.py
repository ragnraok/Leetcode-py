def majorityElement(self, num):
    num_map = {}
    for i in num:
        if i in num_map:
            num_map[i] += 1
        else:
            num_map[i] = 1

    for key in num_map:
        if num_map[key] > len(num) / 2:
            return key

    #NOTE: or we can pick the median in a sorted list
