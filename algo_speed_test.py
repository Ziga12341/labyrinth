from main import Labyrinth
from tqdm import tqdm

for i in tqdm(range(100)):
    labyrinth = Labyrinth()
    labyrinth.marking_crossroads_as_dead()
    labyrinth.all_branches_from_valid_crossroads()
    labyrinth.get_coordinates_for_all_way()
    labyrinth.from_coordinates_to_directions()
    labyrinth.write_final_result_in_file()