def String_Strip(string_in=None, string_chars_to_strip=None, string_strip_function=None, **kwargs):
    """
    Given an input string, this function can be used to apply the strip, rstrip, or lstrip functions on it, thereby removing undesired whitespace and/or other characters.
    E.g.
    "     this   is   a   string    " -strip-> "this   is   a   string" 
    "     this   is   a   string    " -rstrip-> "     this   is   a   string" 
    "aaaaahelloaaaa" -> strip(a) -> "hello"
    
    Args:
        string_in: The string on which to apply the strip operation.
        string_chars_to_strip: If additional characters are desired to be stripped from the input string, this function can be used.
        string_strip_function: If desired, a specific strip function can be specified:
            lstrip -> strip only from the left
            rstrip -> strip only from the right
            (defaults to regular strip)
    
    Returns a JSON-serializable object that implements the configured data paths:
        string_out: The string after applying the strip function.
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    
    outputs = {}
    
    # Write your custom code here...
    
    if string_in == None:
        return 1
    if string_chars_to_strip == None:
        string_chars_to_strip = ''
        
        
        
    if string_strip_function == "rstrip":
        outputs['string_out'] = string_in.rstrip(string_chars_to_strip)
    elif string_strip_function == "lstrip":
        outputs['string_out'] = string_in.lstrip(string_chars_to_strip)
    else:
        outputs['string_out'] = string_in.strip(string_chars_to_strip)
        
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
