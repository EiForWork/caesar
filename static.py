import matplotlib.pylab as plt

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# The methodd to do frequency analysis: we just count the occurrences
# of the given character
def frquency_analysis(text):
    text = text.upper()

    # we use a dictionary to store the letter-fre
    letter_frequencies = {}

    for letter in LETTERS:
        letter_frequencies[letter] = 0


    #let's consider the text we want to analyse
    for letter in text:
        if letter in LETTERS:
            letter_frequencies[letter] += 1

    return letter_frequencies

def plot_distribution(frequencies):
    plt.bar(frequencies.keys(),frequencies.values())
    plt.show()

if __name__ == '__main__':
    plain_text = "AAAAAAAAAAAAAAAAAAA BB CCCC M"
    freq = frquency_analysis(plain_text)
    plot_distribution(freq)