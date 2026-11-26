import mysql.connector


class Database:

    def __init__(self):

        self.connection = None
        self.cursor = None

        try:
            self.connection = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="kanak@123",
                database="hospital"
            )

            self.cursor = self.connection.cursor()

            print("MySQL Connected Successfully!")

        except mysql.connector.Error as error:

            print("MySQL Connection Failed!")
            print("Error:", error)

    def save_patient(self, patient, prediction, probability):

        if self.connection is None or not self.connection.is_connected():
            print("MySQL is not connected!")
            return

        query = """
        INSERT INTO patients
        (
            age,
            gender,
            diabetes,
            hypertension,
            heart_disease,
            previous_admissions,
            length_of_stay,
            bmi,
            prediction,
            probability
        )
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """

        values = (
            patient.age,
            patient.gender,
            patient.diabetes,
            patient.hypertension,
            patient.heart_disease,
            patient.previous_admissions,
            patient.stay,
            patient.bmi,
            prediction,
            probability
        )
        self.cursor.execute(query,values)
        self.connection.commit()

   
    def get_patients(self):

      query = """
            SELECT *
            FROM patients
            ORDER BY id DESC
       """

      self.cursor.execute(query)

      return self.cursor.fetchall()
     
    def get_patient_by_id(self,patient_id):
        query="SELECT * FROM patients WHERE id=%s"
        self.cursor.execute(query, (patient_id,))
        return self.cursor.fetchone()

    def close(self):

        if self.cursor is not None:
            self.cursor.close()

        if self.connection is not None and self.connection.is_connected():
            self.connection.close()

        print("MySQL connection closed!")


if __name__ == "__main__":

    print("Testing MySQL connection...")

    db = Database()
    db.close()