#!/usr/bin/python3
def best_score(my_dict):
    if my_dict is None or my_dict == {}:
        return None
    biggest = max(my_dict.values())
    for key, value in my_dict.items():
        if value is biggest:
            return key


a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
best_key = best_score(a_dictionary)
print("Best score: {}".format(best_key))

best_key = best_score(None)
print("Best score: {}".format(best_key))