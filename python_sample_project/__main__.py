from python_sample_project.data.load_numbers import load_numbers


def main():
    print('Welcome to the sample project!')
    nums = load_numbers()
    print(f'Numbers: {nums}')

if __name__ == '__main__':
    main()
