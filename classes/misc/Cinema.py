import numpy as np
import pandas as pd

CINEMA_DIR = "../datasets/"

class CinemaDataset():
    people: np.ndarray
    movie: np.ndarray
    stars: np.ndarray

    def __init__(self, size:str):
        self.people = pd.read_csv(f"{CINEMA_DIR}{size.lower()}/people.csv").to_numpy()
        self.movie = pd.read_csv(f"{CINEMA_DIR}{size.lower()}/movies.csv").to_numpy()
        self.stars = pd.read_csv(f"{CINEMA_DIR}{size.lower()}/stars.csv").to_numpy()

    # Gets Movie Record by ID
    def get_movie(self, id:int) -> np.ndarray:
        mask = np.isin(element=self.movie[:,0], test_elements=id)
        return self.movie[mask].flatten()
    
        # Gets Actor Record by ID
    def get_actor(self, id:int) -> np.ndarray:
        mask = np.isin(element=self.people[:,0], test_elements=id)
        return self.people[mask].flatten()
        