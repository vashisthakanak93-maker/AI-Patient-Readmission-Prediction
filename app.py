from flask import Flask, render_template, request

from patient import Patient
from predictor import Predictor
from database import Database


app = Flask(__name__)

predictor = Predictor()


# ---------------- HOME ----------------
@app.route("/")
def home():
    return render_template("index.html")


# ---------------- HISTORY ----------------
@app.route("/history")
def history():

    db = Database()

    patients = db.get_patients()

    db.close()

    return render_template(
        "history.html",
        patients=patients
    )

@app.route("/search", methods=["GET", "POST"])
def search_patient():

    patient = None
    message = ""

    if request.method == "POST":

        patient_id = request.form.get("patient_id")

        db = Database()
        patient = db.get_patient_by_id(patient_id)
        db.close()

        if patient is None:
            message = "Patient not found!"

    return render_template(
        "search.html",
        patient=patient,
        message=message
    )


# ---------------- PREDICTION ----------------
@app.route("/predict", methods=["POST"])
def predict():

    try:

        age = int(request.form["age"])

        gender = request.form["gender"]

        diabetes = int(
            request.form["diabetes"]
        )

        hypertension = int(
            request.form["hypertension"]
        )

        heart_disease = int(
            request.form["heart_disease"]
        )

        previous_admissions = int(
            request.form["previous_admissions"]
        )

        stay = int(
            request.form["stay"]
        )

        bmi = float(
            request.form["bmi"]
        )


        # Create Patient object
        patient = Patient(

            age=age,

            gender=gender,

            diabetes=diabetes,

            hypertension=hypertension,

            heart_disease=heart_disease,

            previous_admissions=previous_admissions,

            stay=stay,

            bmi=bmi
        )


        # AI prediction
        result, probability = predictor.predict(
            patient
        )


        # Save patient to MySQL
        database = Database()

        database.save_patient(
            patient,
            result,
            probability
        )

        database.close()


        # Show result page
        return render_template(
            "result.html",

            result=result,

            probability=round(
                probability * 100,
                2
            )
        )


    except Exception as e:

        return f"""
        <h2>Error occurred:</h2>

        <p>{e}</p>

        <br>

        <a href="/">Go Back</a>
        """


# ---------------- START APPLICATION ----------------
if __name__ == "__main__":

    app.run(
        debug=True
    )