import pandas as pd
import joblib
import os

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


class ModelTrainer:

    def __init__(self, dataset_path):

        self.dataset_path = dataset_path

        self.model = RandomForestClassifier(
            n_estimators=100,
            random_state=42
        )

    def load_data(self):

        self.df = pd.read_csv(
            self.dataset_path
        )

    def preprocess_data(self):

        self.df["Gender"] = self.df["Gender"].map({
            "Male": 1,
            "Female": 0
        })

    def train(self):

        X = self.df.drop(
            "Readmitted",
            axis=1
        )

        y = self.df["Readmitted"]

        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=0.2,
            random_state=42,
            stratify=y
        )

        self.model.fit(
            X_train,
            y_train
        )

        predictions = self.model.predict(
            X_test
        )

        accuracy = accuracy_score(
            y_test,
            predictions
        )

        print(
            "Model Accuracy:",
            round(accuracy * 100, 2),
            "%"
        )

        os.makedirs(
            "model",
            exist_ok=True
        )

        joblib.dump(
            self.model,
            "model/model.pkl"
        )

        print(
            "Model saved successfully!"
        )


if __name__ == "__main__":

    trainer = ModelTrainer(
        "dataset/patient_readmission.csv"
    )

    trainer.load_data()

    trainer.preprocess_data()

    trainer.train()