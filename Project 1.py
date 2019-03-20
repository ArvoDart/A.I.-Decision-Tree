from sklearn import tree
import pandas as pd


user_tree = tree.DecisionTreeClassifier()
temp = []

tree_names = []
not_fit = True 
num_attributes = []

def printMenu():
    print("|---------------------------|")
    print("|   1. Learn a tree         |")
    print("|   2. Save Previous Tree   |")
    print("|   3. Test New Case        |")
    print("|   4. Load Tree            |")
    print("|   5. Quit                 |")
    print("|---------------------------|")

def getMenuChoice():
    choice = input("Enter your choice: ")
    return choice

def loadData():
    file_name = input("Enter the file name for the csv data: ")
    file_training = pd.read_csv(file_name)
    return file_training

def fitTree(training):
    attribute_names = list(training)
    class_name = attribute_names[len(attribute_names)-1]
    x_train = training.drop(class_name, axis =1)
    y_train = training[class_name]
    c = tree.DecisionTreeClassifier()
    c.fit(x_train,y_train)
    return c
def pressToCont():
    input("Press enter to continue")

def numAttributes(training):
    shape = str(training.shape)
    shape = shape.replace(")","")
    shape = shape.split(",")
    num_attributes = int(shape[1]) - 1
    return num_attributes

def findTreeAnswer(answer):
    somewhere = answer[0]
    flag = False
    for x in range(len(somewhere)):
        if somewhere[x] >0:
            here = x
            flag = True
            break
    if(flag):
        return x+1
    else:
        return -69
head_list = []
item_4_flag = False
while True:
    flag = False
    
    if item_4_flag:
        user_choice = '3'
    else:
        printMenu()
        user_choice = getMenuChoice()

    if user_choice == '5':
        print("Goodbye!")
        break
    elif user_choice == '1':
        training_data = loadData()
        head_names = training_data.columns
        user_tree = fitTree(training_data)
        user_tree_name = input("Enter the name for this tree: ")
        print("Tree has been learned")
        num_attributes.append(numAttributes(training_data))
        not_fit = False

    elif user_choice == '3':
        if(item_4_flag):
            item_4_flag = False
            head_names = head_list[len(head_list)-1]
        if not_fit:
            print("Tree is empty")
        else :
            menu3_user = int(input("Enter 1 to traverse tree or 2 to go back to menu"))
            if menu3_user == 1:
                thresh = user_tree.tree_.threshold
                feat = user_tree.tree_.feature
                vals = user_tree.tree_.value
                left_child = user_tree.tree_.children_left
                right_child = user_tree.tree_.children_right
                
                i = len(head_names)-1
                user_class = int(input("enter index value (i.e. 1, 2, 3, etc) for the class target ("+head_names[i]+") outcomes to ask the tree: "))
                print("This function will sometimes ask you to input the previous threshold again")
                found = False
                node = 0
                while ~found:
                    user_feat = float(input("Enter again the value for "+head_names[feat[node]]+": "))
                    if float(user_feat) <= float(thresh[node]):
                        node = left_child[node]
                        if float(thresh[node]) < 0:
                            tree_answer = vals[node]
                            found = True
                            break       
                    else:
                        node = right_child[node]
                        if float(thresh[node]) < 0:
                            tree_answer = vals[node]
                            found = True
                            break
                            
                p = findTreeAnswer(tree_answer)
                if(p>=0):
                    if p == user_class:
                        print("the outcomes match")
                    else:
                        print("outcomes don't match")
                else:
                    print("error")
            else:
                print("back to menu")
    elif user_choice == '2':
        if not_fit:
            print("No tree to save")
        else:
            print("Save "+user_tree_name+"?")
            tree_names.append([user_tree,user_tree_name,num_attributes[len(num_attributes)-1],head_names])
    else:
        print("These are the saved trees")
        for j in tree_names:
            print(j[1],end = ", ")
        print('\n')
        which_tree = int(input("Enter the corresponding index for the tree you wish to load (i.e. 1, 2, 3, etc): "))
        if which_tree > len(tree_names) or which_tree<=0:
            print("Not a valid index")
        else:
            which_tree = which_tree-1
            user_tree = tree_names[which_tree][0]
            user_tree_name = tree_names[which_tree][1]
            num_attributes.append(tree_names[which_tree][2])
            head_list.append(tree_names[which_tree],[3])
            print("Tree has been loaded")
            item_4_flag = True
    pressToCont()
        
        









 
