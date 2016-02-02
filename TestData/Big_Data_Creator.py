#Created By Nathan Burnham
import random

def main():
    files = 2
    for filenum in range(files):
        rows = random.randint(1, 10000);
        dimension = random.randint(1, 2);
        output = "{}\n{}\n".format(rows, dimension)
        objects = []
        for i in range(rows):
            weight = random.uniform(0, 10000)
            cost = 0
            if(dimension == 1):
                cost = random.uniform(0, 10000)
            objects.append((weight, cost))
            output += "{} {} {}\n".format(str(i), weight, cost)
        
            
        knapsize = random.uniform(0, rows);
        output += "{}\n".format((knapsize))
        f = open('{}.in'.format(filenum), 'w')
        f.write(output)
        f.close()
        output = ""

    
if __name__ == '__main__':
    main()