def count_worlds(filename):
    try :
        with open (filename, "r") as file:
            lines = file.read()
            line_count = len(lines)
            word_count = sum(len(line.split()) for line in lines)
            
            print(f"number of the lines : {line_count}")
            print(f"number of the lines : {word_count}")
            
    except FileNotFoundError:
        print(f"file not found {filename}")
        
        
count_worlds("sample1.txt")
            