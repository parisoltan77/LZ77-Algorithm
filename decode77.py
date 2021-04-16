# Programmed by Soltanzadeh & Tabatabaee
# LZ77 Decoded Algorithm

#Decoding:
def decode77(FileIn, FileOut):
    f = open(FileIn,'r',encoding="utf-8") 
    lines = f.readlines()
    cursor=-1
    out=''
    for i in range(0,len(lines)): 
        line=lines[i]
        tmplist=line.split()
        if(len(tmplist)==0):
            continue
        offset=eval(tmplist[0])
        length=eval(tmplist[1])
        if(len(tmplist)==2): 
            #if the nest line is \n,the third element of the tuple is \n
            if(len(lines[i+1].split())==0):
                tail='\n'
            #else the third element of the tuple is ' '
            else:
                tail=' '
        else:
            tail=tmplist[2]
        if (offset == 0 and length == 0):
                out += tail
                cursor+=1
        else:
                # e.g.,(3, 5, d) <==> rarrarrad
                if(length + (cursor - offset+1) > len(out)):
                    l = len(out)
                    diff = (length + (cursor - offset+1)) - l
                    out += out[(cursor-offset+1):(l-1)]
                    out += out[l-1 : l + diff]
                    out += tail
                else:
                    out += (out[(cursor-offset+1):(cursor-offset+length+1)] + tail)
                cursor+=length+1      
            # the repetition of dictionary
    fout = open(FileOut, 'w', encoding = 'utf-8')    
    print (out,file=fout)
    f.close()

#main
def main():
    decode77('encoded77.txt' ,'decoded77.txt')
    
if __name__ == '__main__':
    main()