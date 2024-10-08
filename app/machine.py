from sklearn.ensemble import RandomForestClassifier
import joblib
import time


class Machine:

    def __init__(self, df):
        target = [int(x.split()[1]) for x in df['Rarity']]
        features = df.drop(columns=['Rarity'])
        mod = RandomForestClassifier(random_state=42)
        mod.fit(features, target)
        self.model = mod
        sec = time.time()
        self.timestamp = time.ctime(sec)
        self.name = 'Random Forrest Classifier'

    def __call__(self, feature_basis):
        prediction = self.model.predict(feature_basis)[0]
        confidence = self.model.predict_proba(feature_basis)[0].max()
        return prediction, confidence

    def save(self, filepath):
        joblib.dump(self, filepath)

    @staticmethod
    def open(filepath):
        return joblib.load(filepath)

    def info(self):
        return f'Base Model: {self.name}, Timestamp: {self.timestamp}'
