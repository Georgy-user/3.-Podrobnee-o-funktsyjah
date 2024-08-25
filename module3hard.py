def calculate_structure_sum(entering_stuct):
    res_summing = 0
    for unit in entering_stuct:
        if isinstance(unit, str):
            res_summing = res_summing + len(unit)
        elif isinstance(unit, list) or isinstance(unit, tuple):
            res_summing = res_summing + calculate_structure_sum(unit)
        elif isinstance(unit, dict):
            list_elem_dict = list(unit.keys()) + list(unit.values())
            res_summing = res_summing + calculate_structure_sum(list_elem_dict)
        elif isinstance(unit, set):
            res_summing = res_summing + calculate_structure_sum(list(unit))
        else:
            res_summing = res_summing + unit
    return res_summing


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
