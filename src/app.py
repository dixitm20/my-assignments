import os
import json

from utils.bmi_helpers import get_bmi_details, overweight_persons_filter

if __name__ == '__main__':
    present_working_dir = os.path.dirname(__file__)
    input_filename = os.path.join(present_working_dir, 'resources/input.json')

    f = open(input_filename, "r")

    input_person_details = json.loads(f.read())

    print(f'input_person_details:')
    for pd in input_person_details:
        print(pd)

    person_bmi_details = list(map(get_bmi_details, input_person_details))
    print(f'\nperson_bmi_details:')
    for pbd in person_bmi_details:
        print(pbd)

    overweight_persons = list(filter(overweight_persons_filter, person_bmi_details))

    print(f'\noverweight_persons:')
    for opbd in overweight_persons:
        print(opbd)

    overweight_persons_count = len(overweight_persons)
    print(f'\noverweight_persons_count: {overweight_persons_count}')
