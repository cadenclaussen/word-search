import random


boardSize = 30
board = []


words = [ "humanities", "humans", "ancestor", "cultures", "civilizations", "angelisland", "ellisisland", "stereotype", "nativeamerican", "ohlone", "artifact", "immigration", "goldrush", "migration", "generation", "chinese", "mexican", "bracero", "greatdepression", "segregation", "slavery", "civilrights", "phoenixes", "rainbowsharks", "greencard" ]
# words = [ "math", "addition", "subtraction", "multiplication", "division", "negative", "kenken", "riddles", "wordproblems", "mathcounts", "moens", "divisor", "setpuzzles", "equations", "decimals", "mixednumbers", "improperfraction", "powers", "squareroots", "factors", "multiples", "prime", "algebra", "distributive", "commutative", "associative", "exponents", "negatives", "fractions", "numerator", "denominator", "primefactors", "primefactorization", "lcm", "gcf", "patterns", "systematic", "operation", "numbers", "digits", "double", "triple", "single", "quadruple" ]
# words = [ "science", "chemist", "experiment", "mixture", "plant", "bird", "flight", "stemfair", "steamday", "data", "reaction", "molecule", "atom", "nuclear", "power", "mass", "light", "sound", "water", "waves", "tension", "refraction", "defraction", "solder", "arduino", "distance", "rate", "time" ]
# words = [ "sel", "helpful", "imessage", "trashcan", "community", "exclusion", "inclusion", "bestself", "feelings", "emotion", "emotionalthemometer", "listen", "heart", "calm", "tone", "selfreflection", "talkitout", "intention", "mindfullness", "listenwitheyes", "deescalate", "cooloff", "stepup", "stepdown", "empathy" ]
# words = [ "swi", "noun", "verb", "adverb", "adjective", "handwriting", "story", "base", "suffix", "compoundword", "prefix", "root", "greek", "latin", "middleenglish", "oldenglish", "final", "medial", "initial", "vowel", "script", "grapheme", "phoneme", "syllable" ]
# words = [ "exercise", "running", "pushharder", "healthy", "diet", "food", "jumprope", "sports", "football", "basketball", "soccer", "hockey", "climbing", "skiing", "swimming", "biking", "muscles", "bones", "body", "pingpong", "tennis", "persistence", "dodgeball", "thunderball", "ctf", "nutrition", "fiber", "lowsugar", "calories" ]
# words = [ "nueva", "community", "forts", "mansion", "teachers", "administration", "collaboration", "leadership", "campus", "gracious", "spirit", "kindness", "thankful", "caring", "innovate", "inclusion", "humor", "wisdom", "ilab", "ecenter", "sel", "swi", "quest", "stemfair", "steamday", "ilc", "garden", "trips", "auction", "klawn", "mavericks", "balletlawn", "library", "upperschool", "lowerschool", "differentiation", "cafe", "passionate", "citizenship", "stewardship", "asynchronous", "litclub", "bookgroups", "pathofthehero", "farmersmarket", "imessage", "stepupday", "celebrate" ]
# words = [ "scratch", "code", "integer", "string", "float", "if", "for", "while", "true", "false", "variable", "list", "listoflists", "array", "datastructure", "function", "parameters", "indentation", "python", "javascript", "arduino", "concatenate", "algorithm", "logic", "loops", "break", "continue", "pixel", "sprite", "input", "output" ]
# words = [ "kindergarten", "gingerbreadman", "investigation", "magnifyingglass", "flight", "detective", "klawn", "adddetail", "doyourbestwork", "choice", "mysteryreader", "circletime", "davinci", "monalisa", "postoffice", "postmaster", "sandbox", "garden", "joeyarea", "snacktime", "morningmeeting", "schedule", "readingtime", "clues", "curiosity", "resilience", "pioneer" ]


directions = [ "right", "left", "up", "down", "up right", "up left", "down right", "down left" ]


def main():
    initilizeBoard()
    insertWords()
    replaceDot()
    printBoard()


def initilizeBoard():
    for row in range(boardSize):
        board.append([])
        for _ in range(boardSize):
            board[row].append('.')


def printBoard():
    print()
    print()
    for row in range(boardSize):
        for column in range(boardSize):
            if (column == 0):
                print("    ", end="")
            if (board[row][column] == '.'):
                print(" ", end="  ")
            else:
                print(board[row][column], end="    ")
        print()
        print()
    print()
    printWords()
    print()


def printWords():
    count = 0
    for word in words:
        print("   ", word.ljust(20), end="")
        count = count + 1
        if count == 5:
            print();
            count = 0

def insertWords():
    for word in words:
        while True:
            row = random.randint(0, (boardSize - 1))
            column = random.randint(0, (boardSize - 1))
            direction = random.choice(directions)
            valid = isValid(word, row, column, direction)
            if valid == False:
                continue
            insertWord(word, row, column, direction)
            break


def isValid(word, row, column, direction):
    for ch in word:

        if row >= boardSize or row < 0:
            return False
        if column >= boardSize or column < 0:
            return False

        if board[row][column] != ".":
            if board[row][column] != ch:
                return False

        updateDirectionList = updateDirection(row, column, direction)
        row = updateDirectionList[0]
        column = updateDirectionList[1]

    return True


def insertWord(word, row, column, direction):
    for ch in word:
        board[row][column] = ch
        updateDirectionList = updateDirection(row, column, direction)
        row = updateDirectionList[0]
        column = updateDirectionList[1]


def replaceDot():
    letters = [ "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z" ]
    for row in range(boardSize):
        for column in range(boardSize):
            letterPut = random.choice(letters)
            if board[row][column] == ".":
                board[row][column] = letterPut


def updateDirection(row, column, direction):
    if direction == "right":
        column = column + 1
        return [row, column]
    elif direction == "left":
        column = column - 1
        return [row, column]
    elif direction == "up":
        row = row - 1
        return [row, column]
    elif direction ==  "down":
        row = row + 1
        return [row, column]
    elif direction == "up right":
        row = row - 1
        column = column + 1
        return [row, column]
    elif direction == "up left":
        row = row - 1
        column = column - 1
        return [row, column]
    elif direction == "down right":
        row = row + 1
        column = column + 1
        return [row, column]
    elif direction == "down left":
        row = row + 1
        column = column - 1
        return [row, column]


main()
