from semantic_coherence import semantic_coherence
import glob
from pprint import pprint  # pretty-printer
from delusion_index.delusion_index import index_input
from delusion_index.conceptnet5parser import get_concepts_from_files
from delusion_index.delusion_queries import add_delusions, remove_delusions
from corpusdict import compute_basics, compute_basics_text

default_delusion_categories = [
'time',
'self',
'surveillance',
'unfair',
'mind_control',
'alien',
]

def delusion_index_file(file_name, concept_dict):
    basics = compute_basics(file_name)
    smart_ave_dict = index_input(basics, concept_dict)
    print(file_name)
    pprint(smart_ave_dict)

def delusion_index_string(text, concept_dict):
    basics = compute_basics_text(text, 'all')
    smart_ave_dict = index_input(basics, concept_dict)
    pprint(smart_ave_dict)

remove_delusions()
add_delusions(default_delusion_categories)
concept_dict = get_concepts_from_files()

for file_name in glob.glob('patient_dir/*.txt'):
    print(file_name)
    sims_pat = semantic_coherence.index_file(file_name)
    delusion_index_file(file_name, concept_dict)

for file_name in glob.glob('control_dir/*.txt'):
    sims_ctl = semantic_coherence.index_file(file_name)
    delusion_index_file(file_name, concept_dict)
