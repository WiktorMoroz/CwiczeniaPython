ranks = (
    'Private',
    'Corporal',
    'Sergeant',
    'Lieutenant',
    'Captain',
    'Major',
    'Colonel',
)


num_ranks = len(ranks)
major_index = ranks.index('Major')
colonel_present = 'Colonel' in ranks
print(num_ranks)
print(major_index)
print(colonel_present)
print("test")