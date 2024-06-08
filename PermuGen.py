import itertools

def generate_word_variants(words):
    variants = []
    for word in words:
        variants.append(word)
        if word[0].islower():
            variants.append(word.capitalize())
    return variants

def generate_passwords(words, numbers, specials):
    # Generate all variants of words
    word_variants = list(itertools.product(*[[word, word.capitalize()] for word in words]))
    
    passwords = set()
    for variant in word_variants:
        base = ''.join(variant) + numbers
        
        # Generate all possible combinations with special characters interspersed
        for positions in itertools.combinations(range(len(base) + 1), len(specials)):
            for chars in itertools.permutations(specials):
                new_password = list(base)
                for pos, char in zip(sorted(positions), chars):
                    new_password.insert(pos, char)
                passwords.add(''.join(new_password))
    
    return list(passwords)

def save_to_file(passwords, output_file):
    with open(output_file, 'w') as file:
        for password in passwords:
            file.write(password + '\n')

def main():
    print("Welcome to Custom Password Dictionary Generator!")
    print("This script helps you generate custom password dictionaries for brute force attacks.")
    print("You can specify the characters, numbers, and special characters to include in the passwords.")
    print()

    words = input("Enter words to include (separated by spaces, e.g., yyy zzz): ").split()
    numbers = input("Enter numbers to include (e.g., 1234): ")
    specials = input("Enter special characters to include (e.g., !@#$%): ")
    output_file = input("Enter output file name: ")

    # Generate passwords
    passwords = generate_passwords(words, numbers, specials)

    # Save passwords to file
    save_to_file(passwords, output_file)
    print("Passwords generated successfully and saved to", output_file)

if __name__ == "__main__":
    main()
