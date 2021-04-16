# Programmed by Soltanzadeh & Tabatabaee
# LZ77 Encoded Algorithm
    
#Encoding:
def encode77(search_buf , lookahead_buf , FileIn , FileOut):
    with open(FileIn, 'r', encoding = 'utf-8') as FileIn:
        paper = FileIn.read()
    fout = open(FileOut, 'w', encoding = 'utf-8')
    pointer = 0
    length = len(paper)
    search_buf_window = '' # search buffer window
    
    while 1:
        # check if the pointer is near the end of the paper 
        if pointer + len(search_buf_window) + lookahead_buf < length:
            lookahead_buf_window = paper[pointer + len(search_buf_window) : pointer + len(search_buf_window) + lookahead_buf]
        else:
            lookahead_buf_window = paper[pointer + len(search_buf_window) : ]  # look-ahead buffer window 

        matchLength = 0
        prefix = lookahead_buf_window[0 : matchLength + 1]
        p = search_buf_window.find(prefix)
        pos = len(search_buf_window)
        while (p != -1 and matchLength+1 < len(lookahead_buf_window)):
            matchLength += 1
            prefix = lookahead_buf_window[0 : matchLength + 1]
            pos = p
            p = search_buf_window.find(prefix)
		# e.g., adabrar|rarrad <==> (3, 5, d) 
        if (matchLength and pos+matchLength == len(search_buf_window)):
            lpp = 0
            while (matchLength < len(lookahead_buf_window)-1 and lookahead_buf_window[lpp] == lookahead_buf_window[matchLength]):
                lpp += 1
                matchLength += 1
        print(len(search_buf_window) - pos, matchLength, lookahead_buf_window[matchLength], file = fout)
        
        search_buf_window = search_buf_window + lookahead_buf_window[0 : matchLength + 1]     
        cut = len(search_buf_window) - search_buf
        if cut > 0:
            search_buf_window = search_buf_window[cut:]
            pointer += cut
            if pointer + search_buf >= length:
                break       
    fout.close()

#main
def main():
    # length of search buffer and look-ahead buffer
    search_buf = int(input("Search buffer : "))
    lookahead_buf = int(input("Look-ahead buffer : "))

    encode77(search_buf, lookahead_buf ,'input.txt', 'encoded77.txt')
    

if __name__ == '__main__':
    main()
