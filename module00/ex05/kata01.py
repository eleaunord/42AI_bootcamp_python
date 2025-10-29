kata = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
}


# print(kata.keys())
# print(kata.values())

for key, value in kata.items():
	print(f"{key} was created by {value}")