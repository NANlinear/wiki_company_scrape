import wptools
from treelib import Node, Tree

tree = Tree()
tree.create_node("Top", 'top')

par_srch_list = ['currentowner','parent','owner', 'manufacturer']
sub_srch_list = ['brands']

# Stores whether their is a parent term match and which it is.
cur_srch = []

# Checks to see if there is a key from the search terms.
def rel_check(page, srch_list):
    global cur_srch
        
    for i in srch_list:
        if i in page.data['infobox']:
            cur_srch = [True, i]
            return cur_srch
        
    return [False, 'None']

def main():
    # Input a new company.
    search = str(input("Enter a company: ") or "Jaguar Cars")
    
    page = wptools.page(search)
    page.get_parse()
    tree.create_node(search, search, parent='top')

    
    while rel_check(page, par_srch_list)[0]:
        owner = page.data['infobox'][cur_srch[1]]   
        
        # page.data['infobox']['owner'] returns: 
        # {{nowrap|[[Jaguar Land Rover]] (since 2013)}} as a str?
        # Finds all text between start and end [[   ]] to fix this.
        if '[[' and ']]' in owner:
            start = '[['
            end = ']]'
            temp_search = owner.split(start)[1].split(end)[0]    
        print('new search: ', search)
        
        # Tata Sons owner comes back as 'Tata Sons'. This is to deal with those loops.
        # else update search term.
        if search == temp_search:
            print('Reached the end of the chain')
            break
        else:
            # Changes previous company and adds new relationship.
            tree.create_node(temp_search, temp_search, parent='top')
            tree.move_node(search, temp_search)
            
            # Updates current search term to the new company.
            search = temp_search
        
        # Creates the new 'wptools.page' from the new search term.
        page = wptools.page(search)
        page.get_parse()
    
    print('\n\n')
    tree.show()
    print('\n')
    print('!!!Finished!!!')

if __name__ == "__main__":
    main()
