class Patient:

    def __init__(
        self,
        age,
        gender,
        diabetes,
        hypertension,
        heart_disease,
        previous_admissions,
        stay,
        bmi
    ):
        self.age = age
        self.gender = gender
        self.diabetes = diabetes
        self.hypertension = hypertension
        self.heart_disease = heart_disease
        self.previous_admissions = previous_admissions
        self.stay = stay
        self.bmi = bmi

    def get_features(self):

        gender_value = 1 if self.gender == "Male" else 0

        return [[
            self.age,
            gender_value,
            self.diabetes,
            self.hypertension,
            self.heart_disease,
            self.previous_admissions,
            self.stay,
            self.bmi
        ]]