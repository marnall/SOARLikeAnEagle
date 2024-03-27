def Number_AddOrSubtractOffset(number_in=None, number_offset=None, **kwargs):
    """
    Given a numerical input, this function will add a positive or negative offset to it. This can be useful when e.g. dealing with 0- and 1-indexed arrays
    
    Args:
        number_in: The number to which to add an offset.
        number_offset: The number to add to the input. Can be negative
    
    Returns a JSON-serializable object that implements the configured data paths:
        number_out
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    
    outputs = {}
    
    # Write your custom code here...
    if number_in == None:
        return 1
    if number_offset == None:
        number_offset = 0
    
    outputs['number_out'] = number_in + number_offset
    
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
