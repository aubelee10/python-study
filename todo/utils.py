import pickle

def load_tasks(file_path):
    try:
        with open(file_path, "rb") as f:
            return pickle.load(f)
    except:
        print("Error loading tasks")
        return []

def save_tasks(file_path, tasks):
    try:
        with open(file_path, "wb") as f:
            pickle.dump(tasks, f)
    except:
        print("Error saving tasks")
