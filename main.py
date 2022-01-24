import os
import json


def get_bmi_details(person_detail):
    person_weight_kg = person_detail['WeightKg']
    person_height_m = person_detail['HeightCm']/100
    bmi = round((person_weight_kg /
                 (person_height_m * person_height_m)),
                1)
    if bmi <= 18.4:
        bmi_category, health_risk = 'Underweight', 'Malnutrition risk'
    elif 18.5 <= bmi <= 24.9:
        bmi_category, health_risk = 'Normal weight', 'Low risk'
    elif 25 <= bmi <= 29.9:
        bmi_category, health_risk = 'Overweight', 'Enhanced risk'
    elif 30 <= bmi <= 34.9:
        bmi_category, health_risk = 'Moderately obese', 'Medium risk'
    elif 35 <= bmi <= 39.9:
        bmi_category, health_risk = 'Severely obese', 'High risk'
    else:
        bmi_category, health_risk = 'Very severely obese', 'Very high risk'

    out = person_detail.copy()
    out['BMI'] = bmi
    out['BMICategory'] = bmi_category
    out['HealthRisk'] = health_risk

    return out


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

    overweight_persons = list(filter(lambda x: x['BMICategory'] == 'Overweight', person_bmi_details))

    print(f'\noverweight_persons:')
    for opbd in overweight_persons:
        print(opbd)

    overweight_persons_count = len(overweight_persons)
    print(f'\noverweight_persons_count: {overweight_persons_count}')

