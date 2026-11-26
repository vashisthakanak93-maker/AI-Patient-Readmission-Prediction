import joblib


class Predictor:

    def __init__(self):

        self.model = joblib.load(
            "model/model.pkl"
        )

    def predict(self, patient):

        features = patient.get_features()

        prediction = self.model.predict(features)[0]

        probability = self.model.predict_proba(features)[0][1]

        if prediction == 1:
            result = "High Risk"
        else:
            result = "Low Risk"

        return result, probability