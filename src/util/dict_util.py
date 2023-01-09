from copy import deepcopy


def deep_merge(s: dict, d: dict) -> dict:
    """
    a = { 'first' : { 'all_rows' : { 'pass' : 'dog', 'number' : '1' } } }
    b = { 'first' : { 'all_rows' : { 'fail' : 'cat', 'number' : '5' } } }
    deep_merge(b, a) == { 'first' : { 'all_rows' : { 'pass' : 'dog', 'fail' : 'cat', 'number' : '5' } } }

    深度递归合并字典, 因为 'dict.update()' 只合并第一层. 如果遇到值的类型是字典的时侯
    不会递归合并内部字典.
    :param s: 源数据 (被覆盖)
    :param d: 目标数据 (会覆盖s)
    :return: dict 合并后的字典
    """
    result = deepcopy(s)
    for dk, dv in d.items():
        av = result.get(dk)
        if isinstance(av, dict) and isinstance(dv, dict):
            result[dk] = deep_merge(av, dv)
        else:
            result[dk] = deepcopy(dv)
    return result


def dict_merge(s: dict, d: dict):
    """
    a = { 'first' : { 'all_rows' : { 'pass' : 'dog', 'number' : '1' } } }
    b = { 'first' : { 'all_rows' : { 'fail' : 'cat', 'number' : '5' } } }
    deep_merge(b, a) == { 'first' : { 'all_rows' : { 'pass' : 'dog', 'fail' : 'cat', 'number' : '5' } } }

    深度递归合并字典, 因为 'dict.update()' 只合并第一层. 如果遇到值的类型是字典的时侯
    不会递归合并内部字典.
    :param s: 源数据 (被覆盖)
    :param d: 目标数据 (会覆盖s)
    :return: None
    """
    for k, v in d.items():
        if k in s and isinstance(s[k], dict) and isinstance(d[k], dict):
            dict_merge(s[k], d[k])
        else:
            s[k] = d[k]