
import json
import os
import os
import glob

# Extract dowloaded HTML files into a model file of each problem.
from bs4 import BeautifulSoup


class ProblemModel():
    def __init__(self, problem_number: int, problem_title: str):
        self.problem_number = problem_number
        self.problem_title = problem_title

    def __str__(self) -> str:
        return self.to_json()

    def to_dict(self) -> dict:
        return {
            "problem_number": self.problem_number,
            "problem_title": self.problem_title
        }
    
    def to_json(self) -> str:
        return json.dumps(self.to_dict())


def extract_model(abspath: str) -> ProblemModel:
    with open(abspath, "r") as f:
        try:
            soup = BeautifulSoup(f.read(), "html.parser")
            file = os.path.basename(abspath)
            problem_number = file.split("_")[1].replace(".html", "")
            problem_title = soup.find("h2").text
            str_enc = problem_title
            # str_enc = problem_title.decode(encoding='utf8') 

            return ProblemModel(int(problem_number), str_enc)
        except Exception as e:
            print(e)
            return None


def main():
    # list files in directory
    files = glob.glob("problem_*.html")
    for f in files:
        abspath = os.path.join(os.getcwd(), f)
        m = extract_model(abspath)
        if m is not None:
            print(m)
        else:
            print("Failed to extract model from {}".format(abspath))


if __name__ == "__main__":
    main()
