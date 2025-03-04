def get_book_text (input):
    with open(input) as f:
        output = f.read()
    return output

def num_words (input):
    output = len(input.split())
    return output

def characters (input):
    data = list(input.lower())
    output = {}
    for x in data:
        if x in output:
            output[x] += 1
        else:
            output.update({x: 1})
    return output

def sort_dict (input):
    data = []
    for x in input:
        if x.isalpha() == False:
            continue
        else:
            data.append({x: input[x]})
    data.sort(reverse=True, key=lambda item: list(item.values())[0])
    output = str(data).replace(",","\n").replace("{", "").replace("}", "").replace("[", " ").replace("]", "").replace("'", "")
    return output