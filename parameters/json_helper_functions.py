# User defined module that contains helpful functions for manipulating JSON files
import re

def pack(mylist):
    """
    This function takes a list and returns a string.
    """
    mystr=""
    for elem in mylist:
        elem_str = str(elem).replace(" ","__")
        mystr += "//"
        mystr += elem_str

    return(mystr)

def unpack(mystr):
    """
    This function takes a string and returns a list
    """
    mystr = mystr.replace("__"," ")
    mylist = mystr.split("//")

    if mylist[0] == "":
        mylist = mylist[1:]

    return(mylist)

def get_item(x,path):
    """
    This function returns the value of an item in a nested dictionary.
    The "filepath" of the item is specified by the variable path.
    """

    pathlist = unpack(path)

    if len(pathlist) > 1:
        k = pathlist.pop(0)
        item = get_item(x[k],pack(pathlist))
    else:
        k = pathlist.pop(0)
        item = x[k]

    return(item)

def update_item(x,path,value):
    """
    This function updates the value of an item in a nested dictionary.
    The "filepath" of the item is specified by the variable path,
    and the new value of the item is specified by the variable value.
    """
    pathlist = unpack(path)

    if len(pathlist) > 1:
        k = pathlist.pop(0)
        x[k] = update_item(x[k],pack(pathlist),value)
    else:
        k = pathlist.pop(0)
        x[k] = value

def is_leaf(x):
    """
    This function checks if a dictionary represents an element of an array
    (which I'm calling a leaf, since our structure is basically a tree)
    """

    # If not a dictionary, then it's a leaf
    if not isinstance(x,dict):
        still_leaf = True
    else:
        still_leaf = False

    return(still_leaf)

def is_vector(x):
    """
    This function checks if a dictionary represents a one-dimensional array
    """

    # Initially assume true
    still_vector=True

    # Must not be a leaf to start
    if is_leaf(x):
        still_vector=False

    # Check that all elements are leaves
    if still_vector:
        klist = list(x.keys())
        for k in klist:
            if not is_leaf(x[k]):
                still_vector=False
                break

    # Check that all elements are the same data type
    if still_vector:
        datatypes = [get_leaf_data_type(x[k]) for k in klist]
        if not all(d==datatypes[0] for d in datatypes):
            still_vector=False

    return(still_vector)


def is_table(x):
    """
    This function checks if a dictionary represents a two-dimensional array
    """

    # Initially assume that JSON represents a table
    still_table=True

    # Must not be a leaf to start
    if is_leaf(x):
        still_table = False
        #print("(1)")

    # Check if row contains columns
    if still_table:
        rownames=list(x.keys())
        for row in rownames:
            if not isinstance(x[row],dict):
                still_table=False
                #print("(2)")
                break

    # Check that all the column names match
    if still_table:
        colnames = list(x[rownames[0]].keys())
        for row in rownames:
            currentcol = list(x[row].keys())
            if currentcol != colnames:
                still_table=False
                #print("(3)")
                break

    # Check that all (row,column) entries are leaves
    if still_table:
        for row in rownames:
            for col in colnames:
                if not is_leaf(x[row][col]):
                    still_table=False
                    #print("(4)")
                    break
            if not still_table:
                break

    # Check that all elements are the same data type
    if still_table:
        datatypes = [get_leaf_data_type(x[row][col]) for row in rownames for col in colnames]
        if not all(d==datatypes[0] for d in datatypes):
            still_table=False

    return(still_table)

def get_vector_length(x):
    """
    This function gets the dimensions of a vector represented by a dictionary
    """
    klist = list(x.keys())
    length = len(klist)

    return(length)

def get_table_dimensions(x):
    """
    This function gets the dimensions of a table represented by a dictionary
    """

    klist = list(x.keys())
    k = klist[0]
    nrow = len(klist)
    ncol = len(list(x[k].keys()))

    return(nrow,ncol)

def get_type(x):

    """
    Determines what a dictionary represents
    """

    if is_leaf(x):
        mytype = 'leaf'

    elif is_vector(x):
        mytype = 'vector'

    elif is_table(x):
        mytype = 'table'

    else:
        mytype = 'node'

    return(mytype)

def get_leaf_data_type(x):

    """
    Determines the data type of a leaf
    """

    # The "leaves" of a nested JSON file can be any of the following types
    expr1 = type(x) == int
    expr2 = type(x) == float
    expr3 = type(x) == str
    expr4 = type(x) == bool
    expr5 = type(x) == list # lists can be a pain, especially if nested. Might just assume all lists are numeric and 1D
    expr6 = x == None

    if expr1 or expr2:
        dtype = 'number'
    elif expr3:
        dtype = 'string'
    elif expr4:
        dtype = 'boolean'
    elif expr5:
        dtype = 'list'
    else:
        dtype = 'null'

    return(dtype)

def get_vector_data_type(x):
    """
    Determines the data type of a vector
    (a condition for being a vector is that all elements are the same data type)
    """

    klist = list(x.keys())
    k = klist[0]
    dtype = get_leaf_data_type(x[k])
    return(dtype)

def get_table_data_type(x):
    """
    Determines the data type of a table
    (a condition for being a table is that all elements are the same data type)
    """

    klist = list(x.keys())
    k = klist[0]
    dtype = get_vector_data_type(x[k])
    return(dtype)

def get_all_paths(x,mystr):
    """
    Extracts the filepath of all subdictionaries from a nested dictionary.
    """

    mylist = []
    klist= list(x.keys())

    for k in klist:
        mylist = mylist + [mystr + k]
        if get_type(x[k])=='node':
            mylist = mylist + get_all_paths(x[k],mystr+k+"//")

    # Remove spaces
    mylist = [elem.replace(" ","__") for elem in mylist]

    return(mylist)

def get_all_leaves(x,mystr):

    """
    Extracts the filepath of all tree leaves.
    """

    mylist = []
    klist = list(x.keys())

    for k in klist:
        if get_type(x[k])=='leaf':
            mylist = mylist + [mystr + k]
        else:
            mylist = mylist + get_all_leaves(x[k],mystr+k+"//")

    # Remove spaces
    mylist = [elem.replace(" ","__") for elem in mylist]

    return(mylist)

def get_generic_path(path):
    """
    Determine the "generic" json path that interchangeable components will share.
    """

    # Start out same as path
    generic_path = path

    # Remove intervention numbers, tn_group numbers, and test numbers
    to_remove = [r'[0-9]+']  # Can expand this to a list if we think of more things to remove (ages?)

    for s in to_remove:
        generic_path = re.sub(s,'',generic_path)

    return(generic_path)

def get_html_template(component_type,data_type):

    template_dict = {'leaf':{'number':'tree_leaf_view.html',
                         'string':'tree_leaf_view.html',
                         'boolean':'tree_leaf_view.html',
                         'list':'tree_leaf_view.html',
                         'null':'tree_leaf_view.html'},
                 'vector':{'number':'tree_vector_view.html',
                           'string':'tree_vector_view.html',
                           'boolean':'tree_vector_view.html',
                           'list':'tree_vector_view.html',
                           'null':'tree_vector_view.html'},
                'table':{'number':'tree_table_view.html',
                         'string':'tree_table_view.html',
                         'boolean':'tree_table_view.html',
                         'list':'tree_table_view.html',
                         'null':'tree_table_view.html'}}

    html_template = template_dict[component_type][data_type]

    return(html_template)

def get_metadata(x,path):

    component_type = get_type(x)

    # Defaults
    data_type = None
    length = None
    nrow = None
    ncol = None

    # Get information on data type if not a node
    if component_type == 'leaf':
        data_type = get_leaf_data_type(x)
    elif component_type == 'vector':
        data_type = get_vector_data_type(x)
        length = get_vector_length(x)
    elif component_type == 'table':
        data_type = get_table_data_type(x)
        nrow,ncol = get_table_dimensions(x)

    # Determine html template that should be used to render element
    if component_type == 'node':
        html_template = 'tree_node_view.html'
    else:
        html_template = get_html_template(component_type,data_type)

    mylabel = path.split("//")[-1]
    mylabel = mylabel.replace("__"," ")

    generic_path = get_generic_path(path)

    metadata = {"json_path":path,
                "generic_path":generic_path,
                "html_id":None,  # For now, leave html_id blank - we'll generate this after the ledger has been built
                "html_template":html_template,
                "label":mylabel,
                "component_type":component_type,
                "data_type":data_type,
                "length":length,
                "nrow":nrow,
                "ncol":ncol,
                "tracked":False,
                "param_pk":None,
                "similar_components": None} # For now, leave this blank

    return(metadata)

def build_metadata_ledger(x):
    """
    This function collects the metadata needed to render model input files.
    This metadata is similar to (but distinct from) the metadata associated with tracked model parameters.
    Here the focus is on information needed to create a user interface to interact with an input file.
    """
    # Create empty dictionary
    ledger = {}

    # Get paths for nodes, leaves, vectors, and tables contained in JSON
    all_paths = get_all_paths(x,'')

    # Get metadata and add to dictionary
    for i in range(len(all_paths)):
        itempath = all_paths[i]
        item = get_item(x,itempath)
        ledger[itempath] = get_metadata(item,itempath)
        ledger[itempath]['html_id'] = 'element_' + str(i)

    return(ledger)

def build_field_ledger(x):
    """
    This function collects the metadata associated with input file form fields (leaves of tree).
    """
    # Create empty dictionary
    field_ledger = {}

    # Get paths for fields contained in JSON
    all_fields = get_all_leaves(x,'')

    # Add metadata to dictionary
    for i in range(len(all_fields)):
        fieldpath = all_fields[i]
        fieldvalue = get_item(x,fieldpath)
        field_ledger[fieldpath] = {'data_type': get_leaf_data_type(fieldvalue),
                                   'initial': fieldvalue}
    return(field_ledger)
