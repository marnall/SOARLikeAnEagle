def RegexExtract(input_strings=None, regex=None, **kwargs):
    """
    Args:
        input_strings: The input string(s) from which to extract the desired values.
        regex: The regex pattern to use to extract the desired value(s) from the input_string.
    
    Returns a JSON-serializable object that implements the configured data paths:
        match_list: A list containing all of the regex-extracted values.
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    import re
        
    outputs = []
    match_list = []
    
    # Since SOAR auto escapes string inputs, the backslashes need to be un-escaped \\ -> \
    regex = regex.replace('\\\\','\\')
    
    if input_strings and regex:
        matches = []
        for string in input_strings:
            mat = re.findall(regex, string)
            matches.append(mat)
        for group in matches:
            match_list.append(group)
        
    if match_list:
        for matc in match_list:
            outputs.append({"match_list": matc})
    else:
        outputs.append({"match_list": None})
    phantom.debug("RegexExtract extracted: {}".format(outputs))
    
    # Return a JSON-serializable object
    assert isinstance(outputs, list)  # Will raise an exception if the :outputs: object is not a list
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
