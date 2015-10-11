def isAnagram(s, t):
    if s is None or t is None:
        return False
    if len(s) != len(t):
        return False
    s_dict = {}
    t_dict = {}
    for ss in s:
        if ss in s_dict:
            s_dict[ss] += 1
        else:
            s_dict[ss] = 1
    for tt in t:
        if tt in t_dict:
            t_dict[tt] += 1
        else:
            t_dict[tt] = 1
    return s_dict == t_dict

