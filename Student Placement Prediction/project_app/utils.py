from copyreg import pickle
from re import A
import numpy as np
import json
import pickle


class CollegePlacement():
    def __init__(self, Age, Intership, CGPA, HistoryOfBacklogs, Stream):
        self.Age=Age
        self.Intership = Intership
        self.CGPA = CGPA
        self.HistoryOfBacklogs = HistoryOfBacklogs
        self.Stream = Stream

    def load_file(self):
        with open("project_app/CollegePlace.pkl", "rb") as f:
            self.model = pickle.load(f)

        with open("project_app/JsonFile.json", "r") as f:
            self.file_json = json.load(f)

        
    def get_predict(self):
        self.load_file()
        z = np.zeros(len(self.file_json["columns1"]))
        z[0] =  self.Age
        z[1] =  self.Intership
        z[2] =  self.CGPA
        z[3] =  self.HistoryOfBacklogs

        stream_index = self.file_json["columns1"].index(self.Stream)
        z[stream_index] = 1

        final = self.model.predict([z])
        return final



# if __name__ == "__main__":
    
# obj =   CollegePlacement(22,1,8,0,"Computer Science")
# obj.get_predict()
    
