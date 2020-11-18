def read_summary(filename):
    words = []
    chars_count = 0
    words_count = 0
    words_length=0
    ly_distribute = {}
    longest_words = {}
    longest_words_10=""

    with open(filename, encoding='utf-8') as file:

        for line in file.readlines():
            if line != "\n":
                word_lind = line.rstrip("—:.()").rstrip("\n").split()
                words.append(word_lind)
                for word in word_lind:
                    if word[-1]=="."or word[-1]==",":
                        word=word[:-1]
                    words_count += 1
                    words_length+= len(word)
                    if word[-2:]=="ly":
                        if word in ly_distribute.keys():
                            ly_distribute[word] += 1
                        else:
                            ly_distribute[word] = 1
                    if word in longest_words.keys():
                        pass
                    else:
                        longest_words[word] = len(word)
            char_line = line.rstrip("\n").split()
            for char in char_line:
                chars_count+=len(char)
        for w in sorted(longest_words.items(),key=lambda x:x[1],reverse=True)[:10]:
            if w !=sorted(longest_words.items(),key=lambda x:x[1],reverse=True)[-1]:
                longest_words_10+=w[0]+","
            else:
                longest_words_10+=w[0]
        return words,words_count,chars_count,ly_distribute,longest_words_10,words_length
        # print(line)


def count_sentence(sentence):
    # 大小写字母集合的生成
    alpha = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    ALPHA = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    A_S = alpha + ALPHA
    count = 0  # 句子数记录
    s_length=[]
    sentList = sentence.split('.')  # 使用'.'拆分句子
    for s in sentList:
        s_list=s.split(" ")
        for i in range(len(s)):
            if s[i] in A_S:
                count += 1
                tmp_length = 0
                for word in s_list:
                    if word != "":
                        tmp_length += 1
                s_length.append(tmp_length)
                break
    return count,s_length


if __name__ == '__main__':
    out_file = "summary.txt"
    in_file="article.txt"
    res=read_summary(in_file)
    total_s_len=0
    with open(in_file,encoding="utf-8") as file:
        contents = file.read().rstrip("—:()")
        sentence_count = count_sentence(contents)[0]
        sentences_length = count_sentence(contents)[1]
        for s_len in sentences_length:
            total_s_len += s_len
        average_sentences=total_s_len/sentence_count
    with open(out_file,"w",encoding="utf-8") as file_write:
        file_write.write("Total word count: " + str(res[1])+"\n")
        file_write.write("Total character count: " + str(res[2])+"\n")
        file_write.write("The average word length: " + str(int(res[-1] / res[1]))+"\n")
        file_write.write("The average sentence length: " + str(int(average_sentences))+"\n")
        file_write.write("A word distribution of all words ending in ""ly"": \n")
        for w, count in res[3].items():
            file_write.write(w + ":" + str(count)+"\n")
        file_write.write("A list of top 10 longest words: \n" + res[4])