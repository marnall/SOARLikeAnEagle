def AddOrSubtractOffset(integer_in=None, integer_offset=None, **kwargs):
    """
    Given an integer input, this function will add a positive or negative offset to it. This can be useful when e.g. dealing with 0- and 1-indexed arrays
    
    Args:
        integer_in: The integer to which to add an offset.
        integer_offset: The number to add to the integer. Can be negative
    
    Returns a JSON-serializable object that implements the configured data paths:
        integer_output
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    
    outputs = {}
    
    # Write your custom code here...
    
    outputs['integer_output'] = int(integer_in) + int(integer_offset)
    
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
