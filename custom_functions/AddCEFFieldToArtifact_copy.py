def AddCEFFieldToArtifact_copy(artifact_id=None, cef_field_name=None, cef_field_value=None, **kwargs):
    """
    Adds a CEF field and value to an artifact.
    
    Args:
        artifact_id: The artifact to which to apply the CEF field and value.
        cef_field_name: The name of the CEF field to add.
        cef_field_value: The value to store in the CEF field.
    
    Returns a JSON-serializable object that implements the configured data paths:
        
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    
    outputs = {}
    
    # Write your custom code here...

    # Get the artifact
    url = phantom.build_phantom_rest_url('artifact')
    params = [('_filter_id',artifact_id),('page_size',0)]
    r = phantom.requests.get(url,params=params,verify=False)
    data=""
    # Try loading the data from the artifact. Will fail if the artifact did not load.
    try:   
        response = json.loads(r.text)
        data=response['data']
    except Exception as e:
        phantom.debug(f"ERROR: {e}")
        
    # Set the CEF value
    data[0]['cef'][cef_field_name] = cef_field_value
    
    # Put the artifact back
    try:
        purl = phantom.build_phantom_rest_url('artifact',data[0]['id'])
        i = json.dumps(data[0])
        p = phantom.requests.post(purl,i,verify=False)
        response = json.loads(p.text)
    except Exception as e:
        phantom.debug(f"ERROR: {e}")
           
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
