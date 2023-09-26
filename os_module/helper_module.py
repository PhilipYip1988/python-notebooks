
def identifier_group(obj, kind='all', second=object, show_unique_identifiers=False, show_only_intersection_identifiers=False):
    
    """ Group identifiers from an obj into categories defined by the parameter kind. kind can have the possible values: 
    'all', 'datamodel_method, 'datamodel_attribute', 'error_class', 'class', 'method', 'constant', or 'attribute'.

    second class is an optional second class for comparison, normally a parent class. 
    
    show_unique_identifiers can be used to show only identifiers that are unique to the first class.

    show_only_intersection_identifiers can be used to show identifiers in the first class that also occur in the second class.
    These are inherited from the second class when the second class is a parent class.

    Returns:
        list: list of strings corresponding to identifiers in the grouping
    """

    identifiers = dir(obj)
    second_identifiers = dir(second)
    
    if ((show_unique_identifiers == False) and (show_only_intersection_identifiers == False)):
        identifiers_to_examine = identifiers
    else:
        unique_identifiers = set(identifiers) - set(second_identifiers)
        inherited_identifiers = set(identifiers) & set(second_identifiers) 
        if (show_only_intersection_identifiers == False):
            identifiers_to_examine = [identifier for identifier in identifiers if identifier in unique_identifiers]
        else:
            identifiers_to_examine = [identifier for identifier in identifiers if identifier in inherited_identifiers]

    all_grouping = []
    datamodel_method_grouping = []
    datamodel_attribute_grouping = []
    error_class_grouping = []
    class_grouping = []
    method_grouping = []
    constant_grouping = []
    attribute_grouping = []

    for identifier in identifiers_to_examine:
        is_method = callable(getattr(obj, identifier))
        is_class = type(getattr(obj, identifier)) == type
        is_upper = identifier[0].isupper()
        is_datamodel = identifier[0:2] == '__'

        all_grouping.append(identifier)
        if (is_method and is_datamodel):
            datamodel_method_grouping.append(identifier)
        if (not is_method and is_datamodel):
            datamodel_attribute_grouping.append(identifier)
        if (is_upper and is_class and not is_datamodel):
            error_class_grouping.append(identifier)
        if (not is_upper and is_class and not is_datamodel):
            class_grouping.append(identifier)
        if (is_method and not is_upper and not is_class and not is_datamodel):
            method_grouping.append(identifier)
        if (not is_method and is_upper and not is_datamodel):
            constant_grouping.append(identifier)
        if (not is_method and not is_upper and not is_datamodel):
            attribute_grouping.append(identifier)

    if (kind == 'all'):    
        print(all_grouping)
    elif (kind == 'datamodel_method'):   
        print(datamodel_method_grouping)
    elif (kind == 'datamodel_attribute'):   
        print(datamodel_attribute_grouping)
    elif (kind == 'error_class'):   
        print(error_class_grouping)
    elif (kind == 'class'):   
        print(class_grouping)
    elif (kind == 'method'):   
        print(method_grouping)    
    elif (kind == 'constant'):   
        print(constant_grouping) 
    elif (kind == 'attribute'):   
        print(attribute_grouping) 
    else:
        raise(ValueError, "Invalid value for kind. Possible values are 'all', 'datamodel_method, 'datamodel_attribute', 'error_class', 'class', 'method', 'constant', or 'attribute'")
    

def print_identifier_group(obj, kind='all', second=object, show_unique_identifiers=False, show_only_intersection_identifiers=False):
    
    """ Group identifiers from an obj into categories defined by the parameter kind and print. kind can have the possible values: 
    'all', 'datamodel_method, 'datamodel_attribute', 'error_class', 'class', 'method', 'constant', or 'attribute'.

    second class is an optional second class for comparison, normally a parent class. 
    
    show_unique_identifiers can be used to show only identifiers that are unique to the first class.

    show_only_intersection_identifiers can be used to show identifiers in the first class that also occur in the second class.
    These are inherited from the second class when the second class is a parent class.

    Returns:
        None
    """

    identifiers = dir(obj)
    second_identifiers = dir(second)
    
    if ((show_unique_identifiers == False) and (show_only_intersection_identifiers == False)):
        identifiers_to_examine = identifiers
    else:
        unique_identifiers = set(identifiers) - set(second_identifiers)
        inherited_identifiers = set(identifiers) & set(second_identifiers) 
        if (show_only_intersection_identifiers == False):
            identifiers_to_examine = [identifier for identifier in identifiers if identifier in unique_identifiers]
        else:
            identifiers_to_examine = [identifier for identifier in identifiers if identifier in inherited_identifiers]

    all_grouping = []
    datamodel_method_grouping = []
    datamodel_attribute_grouping = []
    error_class_grouping = []
    class_grouping = []
    method_grouping = []
    constant_grouping = []
    attribute_grouping = []

    for identifier in identifiers_to_examine:
        is_method = callable(getattr(obj, identifier))
        is_class = type(getattr(obj, identifier)) == type
        is_upper = identifier[0].isupper()
        is_datamodel = identifier[0:2] == '__'

        all_grouping.append(identifier)
        if (is_method and is_datamodel):
            datamodel_method_grouping.append(identifier)
        if (not is_method and is_datamodel):
            datamodel_attribute_grouping.append(identifier)
        if (is_upper and is_class and not is_datamodel):
            error_class_grouping.append(identifier)
        if (not is_upper and is_class and not is_datamodel):
            class_grouping.append(identifier)
        if (is_method and not is_upper and not is_class and not is_datamodel):
            method_grouping.append(identifier)
        if (not is_method and is_upper and not is_datamodel):
            constant_grouping.append(identifier)
        if (not is_method and not is_upper and not is_datamodel):
            attribute_grouping.append(identifier)

    if (kind == 'all'):    
        print(all_grouping)
    elif (kind == 'datamodel_method'):   
        print(datamodel_method_grouping)
    elif (kind == 'datamodel_attribute'):   
        print(datamodel_attribute_grouping)
    elif (kind == 'error_class'):   
        print(error_class_grouping)
    elif (kind == 'class'):   
        print(class_grouping)
    elif (kind == 'method'):   
        print(method_grouping)    
    elif (kind == 'constant'):   
        print(constant_grouping)
    elif (kind == 'attribute'):   
        print(attribute_grouping)
    else:
        raise(ValueError, "Invalid value for kind. Possible values are 'all', 'datamodel_method, 'datamodel_attribute', 'error_class', 'class', 'method', 'constant', or 'attribute'")