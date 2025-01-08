import json
import os

class JsonVerification():

    def jsonScores():
        resultados = {}

        if os.path.exists('resultadosASD.json'):
            with open('resultadosASD.json', 'r') as f:
                try:
                    resultados = json.load(f)
                except:
                    pass

    def jsonSave(scores):
        with open('resultadosASD.json', 'w') as f:
            json.dump(scores, f)

    def jsonDict(name, points, turn, win):

        data = []

        dict = {
            "Nome":name,
            "Win:":win,
            "Points:":points,
            "Turns:":turn
        }

        if os.path.exists('resultadosASD.json'):
            with open('resultadosASD.json', 'r') as f:
                try:
                    data = json.load(f)
                except:
                    pass

        data.append(dict)

        return data
    
    def jsonHighScore():

        data = []
        score = 0

        if os.path.exists('resultadosASD.json'):
            with open('resultadosASD.json', 'r') as f:
                try:
                    data = json.load(f)
                except:
                    pass
        
        if data:
            for x in data:
                unit = x
                points = unit.get("Points:")
                if points > score:
                    score = points
        
        return score

