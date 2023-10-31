#EXERCITIU 1
def operations(a,b):
    intersection = set(a) & set(b)
    union = set(a) | set(b)
    dif_a = set(a) - set(b)
    dif_b = set(b) - set(a)
    list = [intersection, union, dif_a, dif_b]
    return list


#EXERCITIU 2
def ch_counter(s):
    dict = {}
    for character in s:
        dict[character] = dict.get(character,0) + 1
    return dict


#EXERCITIU 3
def compare_dict(d1,d2):
    if type(d1) != type(d2):
        return False

    if isinstance(d1,dict):
        if set(d1.keys()) != set(d2.keys()):
            return False

        for i in d1:
            if not compare_dict(d1[i],d2[i]):
                return False

        return True
    elif isinstance(d1, (tuple,set,list)):
        if len(d1) != len(d2):
            return False

        for i,j in zip(d1,d2):
            if not compare_dict(i,j):
                return False

        return True

    else:
        return d1 == d2


#EXERCITIU 4
def build_xml(tag, content, **elements):
    key_values = ' '.join([f'{i}="{j}"' for i,j in elements.items()])
    xml = f"<{tag} {key_values}>{content}</{tag}>"
    return xml


#EXERCITIU 5
def validate_dict(rule, dict):
    for key, prefix, middle, suffix in rule:
        if key not in dict:
            return False
        else:
            value_key = dict[key]

        if not value_key.startswith(prefix) or not value_key.endswith(suffix):
            return False

        if middle not in value_key[1:-1]:
            return False
    return True


#EXERCITIU 6
def unique_and_duplicate(list):
    unique = set()
    duplicate = set()

    for i in list:
        if i in unique:
            duplicate.add(i)
        else:
            unique.add(i)

    return len(unique), len(duplicate)


#EXERCITIU 7
def more_operarations(*s):
    dict = {}
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            first = set[i]
            second = set[j]

            union = f"{first} | {second}"
            dict[union] = first | second

            intersection = f"{first} & {second}"
            dict[intersection] = first & second

            diference1 = f"{first} - {second}"
            dict[diference1] = first - second

            diference2 = f"{second} - {first}"
            dict[diference2] =  second - first
    return dict


#EXERCITIU 10
def path(mapping):
    reached = set()
    current = mapping.get('start')
    list = []

    while current is not None and current not in reached:
        reached.add(current)
        list.append(current)
        current = mapping.get(current)
    return list


#EXERCITIU 11
def count_args(*args, **kwargs):
    count = 0
    for i in args:
        if i in kwargs.values():
            count = count + 1
    return count