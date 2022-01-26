from utils.bmi_helpers import get_bmi_details, overweight_persons_filter


def test_get_bmi_details():
    input_person_detail = {'Gender': 'Male', 'HeightCm': 171, 'WeightKg': 96}
    expected = {'Gender': 'Male',
                'HeightCm': 171,
                'WeightKg': 96,
                'BMI': 32.8,
                'BMICategory': 'Moderately obese',
                'HealthRisk': 'Medium risk'}
    actual = get_bmi_details(input_person_detail)
    assert expected == actual


def test_overweight_persons_filter():
    input_person_bmi_detail = {'Gender': 'Female',
                               'HeightCm': 167,
                               'WeightKg': 82,
                               'BMI': 29.4,
                               'BMICategory': 'Overweight',
                               'HealthRisk': 'Enhanced risk'}
    expected = True
    actual = overweight_persons_filter(input_person_bmi_detail)
    assert expected == actual
