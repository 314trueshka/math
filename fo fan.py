import random

all_count = 10000
count = 100
stop = count//2



def random_strategy(zek, boxes):
    new_korobki = boxes.copy()
    counter = 1
    while counter != stop:
        box = new_korobki.pop(random.randint(0, len(new_korobki)-1))
        if zek == box:
            return True
        counter += 1
    return False

def beautiful_strategy(zek, boxes):
    new_korobki = boxes.copy()
    counter = 1
    opened_boxes = []
    last_box = None
    while counter != stop:
        if last_box is None:
            box = new_korobki[zek]
        else:
            box = new_korobki[last_box]
        if zek == box:
            return True
        counter += 1
        if box in opened_boxes:
            random_int = None
            while random_int is not None and random_int not in opened_boxes:
                random_int = random.randint(0, count-1)
            last_box = random_int
        else:
            opened_boxes.append(box)
            last_box = box

    return False

count_random_lucky = 0
count_random_unlucky = 0
boxes = [i for i in range(count)]
zeki = [i for i in range(count)]

for _ in range(all_count):

    random.shuffle(boxes)
    random.shuffle(zeki)
    luck = []
    for zek in zeki:
        result_try = random_strategy(zek, boxes)
        luck.append(result_try)

    if all(luck):
        count_random_lucky += 1
    else:
        count_random_unlucky += 1
print(f'Всего попыток: {all_count}')
print(f'везучих групп зеков - {count_random_lucky}, невезучих - {count_random_unlucky}')

count_beuty_lucky = 0
count_beuty_unlucky = 0

for _ in range(all_count):

    random.shuffle(boxes)
    random.shuffle(zeki)
    luck = []
    for zek in zeki:
        result_try = beautiful_strategy(zek, boxes)
        luck.append(result_try)

    if all(luck):
        count_beuty_lucky += 1
    else:
        count_beuty_unlucky += 1

print(f'везучих групп зеков - {count_beuty_lucky}, невезучих - {count_beuty_unlucky}')