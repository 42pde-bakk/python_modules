# Put this at the top of your kata00.py file
kata = (19, 42, 21)

if __name__ == '__main__':
    print(f'The {len(kata)} numbers are: {", ".join(str(k) for k in kata)}')
