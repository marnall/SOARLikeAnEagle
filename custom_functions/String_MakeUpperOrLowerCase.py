def String_MakeUpperOrLowerCase(string_in=None, string_operation=None, **kwargs):
    """
    Given an input string, this function will make the string uppercase, lowercase, or capitalized.
    
    Args:
        string_in: String of which to change the case.
        string_operation: The operation: (input: exaMple)
            upper -> EXAMPLE
            lower -> example
            capitalise -> Example
            swapcase -> EXAmPLE
    
    Returns a JSON-serializable object that implements the configured data paths:
        string_out: The final string in the desired case.
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    
    outputs = {}
    
    # Write your custom code here...
    
    if string_operation == "upper":
        outputs['string_out'] = string_in.upper()
    elif string_operation == "lower":
        outputs['string_out'] = string_in.lower()
    elif string_operation == "capitalise" or string_operation == "capitalize":
        outputs['string_out'] = string_in.capitalize()
    elif string_operation == "swapcase":
        outputs['string_out'] = string_in.swapcase()
    else:
        outputs['string_out'] = string_in
        
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
