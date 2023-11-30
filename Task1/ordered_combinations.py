#combination order program

def combo_maker(lis):

    if lis[-1]==variables[-1]:
        return

    rem_elements=variables.copy()
    temp=[]
    largest_val=rem_elements.index(lis[-1])
    rem_elements=rem_elements[largest_val+1:]

    for i in rem_elements:
        temp=lis.copy()
        temp.append(i)
        combinations.append(temp)
        combo_maker(temp)
        

def sorter(lis):
    sorted_combos={}
    for combo in lis:
        if len(combo) not in sorted_combos:
            sorted_combos[len(combo)]=list()
            sorted_combos[len(combo)].append(combo)
        
        else:
            sorted_combos[len(combo)].append(combo)

    combinations.clear()
    for i in sorted_combos:
        for j in sorted_combos[i]:
            combinations.append(j)


def finder():
    inp=input('enter combination to find: ')
    tofind=inp.split()
    tofind.sort()

    for i in range(0,len(combinations)):

        combo=combinations[i]
        check=False

        if len(combo)==len(tofind):

            for j in range(0,len(combo)):
                if combo[j]!=tofind[j]:
                    check=False
                    break
            else:
                check=True
        
        if check==True:
            print('Found at position:',i+1)
            break

    else:
        print("could not find the given combination")



inp = input("enter list: ")
variables=inp.split()
combinations=[]

for i in variables:
    combinations.append(list(i))
    combo_maker(list(i))

sorter(combinations)

for combo in combinations:
    for j in combo:
        print(j,end=' ')
    print()

finder()
while True:
    inp=input("would you like to continue? y/n: ")
    if inp=='y' or inp=='Y':
        finder()
    elif inp=='n' or inp=='N':
        break
    else:
        print("invalid input")
        continue
