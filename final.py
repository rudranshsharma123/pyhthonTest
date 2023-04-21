list_1 = [
    {"id": "1", "name": "Shrey", "age": 25},
    {"id": "3", "age": 10, "name": "Hello"},
    {"id": "2", "name": "World", "age": 24},
]

list_2 = [
    {"id": "1", "marks": 100},
    {
        "id": "3",
        "marks": 90,
        "roll_no": 11,
        "extra_info": {
            "hello": "world",
        },
    },
    {"id": "1", "test": "passed"},
    {"id": "1", "hello": "world", "test": "failed"},
]


def merge_lists(list_1, list_2) -> list:
    '''
    Since the questions wasnt clear on duplicate values, I decided to keep that edge case in mind. The way it works is, it first tries to store all the values of list one in 
    a new list called merged_list, and then it loops over list 2 looking for the 'id' and if it find it, and it is also found in the merged list it updates the merged list with the values found
    in case it doesnt it creates a new dict element with the info found in the new list. 

    sample output from merge_list:
    [{'id': '1', 'name': 'Shrey', 'age': 25, 'marks': 100, 'test': 'failed', 'hello': 'world'}, {'id': '3', 'age': 10, 'name': 'Hello', 'marks': 90, 'roll_no': 11, 'extra_info': {'hello': 'world'}}, {'id': '2', 'name': 'World', 'age': 24}]

    as it is evident, the final value of test is failed since it comes later in the list2, however, if the intended effect were to be different the same could be ensured but the language, 
    wasnt clear so I kept the last occuring value. (Assumption behind it was that the lists of dict are coming either from a database, or from actions performed by the user and then the database is to be updated in any case my approach made more sense to me)
    '''
    
    merged_students = {}
    for student in list_1:
        merged_students[student["id"]] = student
    for student in list_2:
        id = student["id"]
        if id in merged_students:
            merged_students[id].update(student)
        else:
            merged_students[id] = student
    return list(merged_students.values())


list_3 = merge_lists(list_1, list_2)
print(list_3)
