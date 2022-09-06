# Put this at the top of your kata01.py file
kata = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
}

if __name__ == '__main__':
    for k, v in kata.items():
        print(f'{k} was created by {v}')
