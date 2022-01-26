
def get_bmi_details(person_detail):
    person_weight_kg = person_detail['WeightKg']
    person_height_m = person_detail['HeightCm'] / 100
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


def overweight_persons_filter(person_bmi_detail):
    return person_bmi_detail['BMICategory'] == 'Overweight'
