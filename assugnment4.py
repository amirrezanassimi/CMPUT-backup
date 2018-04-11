## Ammirreza Nassimi 1513904
## Assignment 4

def main():
    while True:
        try: 
            capaicty = int(input("Choose your initial size of the pile. Should be more than 2: "))
            assert capaicty > 2
        except AssertionError as e:
            pass
        except ValueError as e:
            pass
        else: 
            break
    root = Minimax([capaicty], 0)
    root.build()
    root.printTree('', True) 
    
    
class Minimax:
    
    options = ['Max','Min']
    
    def __init__(self, nimState, minMaxLevel):
        self.state = nimState
        self.level = Minimax.options[minMaxLevel]
        self.children = []
  
    def single_split(self, val):
       
        split = []
        for i in range((val-1)//2):
            split.append([i+1,(val-1)-i])
        return split
    
    
    def split(self, state):
    
           
        splits = []
        for i in range(len(state)):
            alternative = list(state)
            if alternative[i] > 2 and alternative[i] not in alternative[i+1:]:
                newSplits = self.single_split(alternative.pop(i))
                for split in newSplits:
                    splits.append(sorted(alternative+split))
        return splits
    
    def addChild(self, splits):
        
        for state in splits:   
            self.children.append(Minimax(state, self.level == Minimax.options[0]))
     
    def build(self):
        
        self.addChild(self.split(self.state))
        for child in self.children:
            child.build()    
              
    def printTree(self, indentation, last):
           
        print(indentation, end='') 
        if last:
            print("\-", end='')
            indentation += "  "
        else:
            print("+ ", end = '')
            indentation += "| "
        if last:
            print(self.state, self.level)
        else:
            print(self.state)
        for child in self.children:
            child.printTree(indentation, child is self.children[-1])
            

if __name__ == "__main__":    
    main()
    
    
    
## I got help in few parts 