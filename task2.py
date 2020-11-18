def read_file(filename):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    ALPHA = alpha.upper()
    A_S = alpha + ALPHA
    letter_dict = {}
    sorted_letter_dict={}
    with open(filename, encoding="utf-8") as file:
        for line in file.readlines():
            line_list = line.rstrip("\n").rstrip("—:()").split()
            for word in line_list:
                for letter in word:
                    if letter in A_S:
                        if letter in letter_dict.keys():
                            letter_dict[letter] += 1
                        else:
                            letter_dict[letter] = 1
    for letter in sorted(letter_dict):
        sorted_letter_dict[letter]=letter_dict[letter]
    return sorted_letter_dict

if __name__ == '__main__':
    read_filename="book.txt"
    upper_flag=[]
    lower_flag=[]
    with open("summary.txt","w") as out_file:
        for l,fre in read_file(read_filename).items():
            out_file.write(l+":"+str(fre)+"\n")
            if l.isupper():
                upper_flag.append(l)
            else:
                lower_flag.append(l)
        if len(upper_flag)==26 or len(lower_flag)==26:
            out_file.write("It has all letters.")
        else:
            out_file.write("It doesn't have all letters.")