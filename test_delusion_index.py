from pprint import pprint  # pretty-printer
from delusion_index.delusion_index import index_input
from delusion_index.conceptnet5parser import get_concepts_from_files
from delusion_index.delusion_queries import add_delusions, remove_delusions
from corpusdict import compute_basics

default_delusion_categories = [
'time',
'self',
'surveillance',
'unfair',
'mind_control',
'alien',
]

def index_file(file_name, concept_dict):
    basics = compute_basics(file_name)
    smart_ave_dict = index_input(basics, concept_dict)
    pprint(smart_ave_dict)

remove_delusions()
add_delusions(default_delusion_categories)
concept_dict = get_concepts_from_files()
index_file('timecube_raw.txt', concept_dict)
index_file('control_raw.txt', concept_dict)


