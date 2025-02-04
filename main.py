# Koncsik Michael

import score
# import lyrics 

filenames = ["Barbara_Streisand", "Bohemian_Rhapsody", "Lemon_Tree", "One", "Respect", "Stairway_to_Heaven"]

def main():
    for name in filenames:
        file_path = f"lyrics_folder/{name}"
        with open(file_path, "r") as file:
            content = file.read()
            print(f"The score for {name} is: {round(score.score(content), 2)}.")

if __name__ == "__main__":
    main()