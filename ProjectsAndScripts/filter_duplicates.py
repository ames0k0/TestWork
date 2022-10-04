# Есть не сортированный список операций:
operations = [
    {"id": 1, "timestamp": 2, "amount": 1},
    {"id": 2, "timestamp": 4, "amount": 8},
    {"id": 1, "timestamp": 3, "amount": 2}
]

# В этом списке операции дублируются по id
# если так случилось, то правильной операцией считается та,
# у которой timestamp более поздний

# Задача: модифицировать функцию filter, так чтобы она
# возвращала только правильные операции
# как только все тесты пройдут - задача решена

def filter(operations: list) -> list:
    # id -> operation
    without_duplicates = {}
    # DRY
    filter_by = 'timestamp'

    for operation in operations:
        operation_id = operation.get('id')
        operation_duplicate = without_duplicates.get(operation_id)

        if (operation_duplicate is None):
            without_duplicates[operation_id] = operation
            continue

        if (operation_duplicate.get(filter_by) < operation.get(filter_by)):
            without_duplicates[operation_id] = operation

    # NOTE: Не сохраняется порядок!
    # Можно использовать OrderedDict() из модуля *collections для сохранение порядка операции
    return list(without_duplicates.values())



# Do not touch this
test_data = [
    {"in": [], "out": []},
    {"in": [{"id":1, "timestamp": 2}], "out": [{"id":1, "timestamp": 2}]},
    {"in": [{"id":1, "timestamp": 2}, {"id":1, "timestamp": 3}], "out": [{"id":1, "timestamp": 3}]},
    {"in": [{"id":1, "timestamp": 5}, {"id":1, "timestamp": 4}], "out": [{"id":1, "timestamp": 5}]}
]

def test():
  for i, t in enumerate(test_data):
    try:
      assert filter(t["in"]) == t["out"]
      print(f"Test#{i} [ok]")
    except Exception as e:
      print(f"Test#{i} [error]")

test()


# Решение: https://www.online-python.com/evL4wgp2am


# Задание: https://www.online-python.com/Jc7K8R1OZf
