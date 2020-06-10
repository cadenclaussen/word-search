import random


puzzles = [
    [ "humanities", "sam", "samantha", "damon", "liane", "humans", "ancestor", "cultures", "civilizations", "angelisland", "ellisisland", "stereotype", "nativeamerican", "ohlone", "artifact", "immigration", "goldrush", "migration", "generation", "chinese", "mexican", "bracero", "greatdepression", "segregation", "slavery", "civilrights", "phoenixes", "rainbowsharks", "greencard" ],
    [ "math", "emily", "addition", "subtraction", "multiplication", "division", "negative", "kenken", "riddles", "wordproblems", "mathcounts", "moens", "divisor", "setpuzzles", "equations", "decimals", "mixednumbers", "improperfraction", "powers", "squareroots", "factors", "multiples", "prime", "algebra", "distributive", "commutative", "associative", "exponents", "negatives", "fractions", "numerator", "denominator", "primefactors", "primefactorization", "lcm", "gcf", "patterns", "systematic", "operation", "numbers", "digits", "double", "triple", "single", "quadruple" ],
    [ "science", "elena", "amy", "chemist", "experiment", "mixture", "plant", "bird", "flight", "stemfair", "steamday", "data", "reaction", "molecule", "atom", "nuclear", "power", "mass", "light", "sound", "water", "soundwaves", "tension", "refraction", "defraction", "solder", "arduino", "distance", "rate", "time" ],
    [ "sel", "lisa", "helpful", "imessage", "trashcan", "community", "exclusion", "inclusion", "bestself", "zentangle", "feelings", "emotion", "emotionalthemometer", "listen", "heart", "calm", "tone", "selfreflection", "talkitout", "intention", "mindfullness", "listenwitheyes", "deescalate", "cooloff", "stepup", "stepdown", "empathy" ],
    [ "swi", "rebecca", "noun", "verb", "adverb", "adjective", "handwriting", "story", "base", "suffix", "compoundword", "prefix", "root", "greek", "latin", "middleenglish", "oldenglish", "final", "medial", "initial", "vowel", "script", "grapheme", "phoneme", "syllable" ],
    [ "pe", "zubin", "exercise", "running", "pushharder", "healthy", "diet", "food", "jumprope", "sports", "football", "basketball", "soccer", "hockey", "climbing", "skiing", "swimming", "biking", "muscles", "bones", "body", "pingpong", "tennis", "persistence", "dodgeball", "thunderball", "ctf", "nutrition", "fiber", "lowsugar", "calories" ],
    [ "scratch", "lora", "code", "integer", "string", "float", "if", "for", "while", "true", "false", "variable", "list", "listoflists", "array", "datastructure", "function", "parameters", "indentation", "python", "javascript", "arduino", "concatenate", "algorithm", "logic", "loops", "break", "continue", "pixel", "sprite", "input", "output" ],
    [ "art", "reenie", "paint", "abstract", "modern", "clay", "sculpture", "tone", "statue", "colors", "carve", "brush", "design", "greetingcards", "drawing", "sketching", "pictures", "photos" ],
    [ "music", "gemma", "note", "rhythm", "beat", "song", "tone", "scale", "chorus", "instrument", "piano", "violin", "bass", "guitar", "chello", "trumpet", "melody", "harmony", "tune", "tenor", "pitch" ],
    [ "laraine", "kindergarten", "gingerbreadman", "investigation", "magnifyingglass", "flight", "detective", "klawn", "adddetail", "doyourbestwork", "choice", "mysteryreader", "circletime", "davinci", "monalisa", "postoffice", "postmaster", "sandbox", "garden", "joeyarea", "snacktime", "morningmeeting", "schedule", "readingtime", "clues", "curiosity", "resilience", "pioneer" ],
    [ "nueva", "diane", "megan", "community", "forts", "mansion", "teachers", "administration", "collaboration", "leadership", "campus", "gracious", "spirit", "kindness", "thankful", "caring", "innovate", "inclusion", "humor", "wisdom", "ilab", "ecenter", "sel", "swi", "quest", "stemfair", "steamday", "ilc", "garden", "trips", "auction", "klawn", "mavericks", "balletlawn", "library", "upperschool", "lowerschool", "differentiation", "cafe", "passionate", "citizenship", "stewardship", "asynchronous", "litclub", "bookgroups", "pathofthehero", "farmersmarket", "imessage", "stepupday", "celebrate" ],
]


boardSize = 30
board = []
directions = [ "right", "left", "up", "down", "up right", "up left", "down right", "down left" ]


def main():
    for words in puzzles:
        initializeBoard()
        insertWords(words)
        printHeader(words[0])
        replaceDot()
        printBoard()
        printWords(words)
        printFooter()


def printHeader(title):
    print()
    print()
    print()
    print("# ", title.upper())
    print()
    print("```")


def printFooter():
    print("```")


def initializeBoard():
    global board
    board = []
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
                print(".", end="  ")
            else:
                print(board[row][column], end="  ")
        print()
        print()


def printWords(words):
    print()
    count = 0
    for word in words:
        print("   ", word.ljust(20), end="")
        count = count + 1
        if count == 4:
            print();
            count = 0
    print()


def insertWords(words):
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
