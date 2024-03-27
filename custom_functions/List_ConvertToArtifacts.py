def List_ConvertToArtifacts(custom_list_name=None, container_id=None, headers=None, artifact_name=None, **kwargs):
    """
    For every entry in a custom list, make an artifact in a container containing the columns as cef fields.
    
    Args:
        custom_list_name: The name of the custom list to make artifacts.
        container_id: The container in which to put the new artifacts.
        headers: Supply a list of values here to override the headers. If set to False, then it will use generic col+N headers. E.g. [col1, col2, col3, ...]
        artifact_name: If desired, the new artifacts can have a custom artifact name. Defaults to "Artifact from <custom_list_name>"
    
    Returns a JSON-serializable object that implements the configured data paths:
        
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    
    outputs = {}
    
    # Write your custom code here...
    funcname = "List_ConvertToArtifacts"
    phantom.debug("--- STARTING {} ---".format(funcname))
    
    
    if custom_list_name == None:
        phantom.debug("ERROR: Need custom_list_name!")
        
        # error
        return 1
    if artifact_name == None:
        
        #warning
        artifact_name = "Artifact from "+custom_list_name
    if container_id == None:
        phantom.debug("ERROR: Need container_id!")
        # error
        return 1
    
    custom_list_request = ""
    try:
        custom_list_request = phantom.requests.get(phantom.build_phantom_rest_url('decided_list',custom_list_name),verify=False)
    except Exception as e:
        phantom.debug("ERROR: {}".format(e))
        #error
        return 1
    
    custom_list = custom_list_request.json().get('content',[])
    
    # Iterate through every list item.
    nonzero = None
    try:
        for row in custom_list:
            for col in row:
                if col != '' and col != None:
                    nonzero = col
                    raise StopIteration
    except StopIteration:
        # list is not empty
        phantom.debug("stopiteration")    
        
    if nonzero == None:
        # error list is empty
        return 1
        
    maxwidth = len(custom_list[0])
    
    header_offset = 0
    
    if headers == None:
        headers=custom_list[0]
        header_offset = 1
    elif headers == False:
        headers = []
        for r in range(0,maxwidth):
            headers.append("col"+str(r))
    elif type(headers) == str:
        headers = headers.split(",")
        if len(headers) < maxwidth:
            i = len(headers)
            for r in range(i+1,maxwidth+1):
                headers.append("col"+str(r))
    
    data = {}
    for y in range(1,len(custom_list)):
        data = {
            "container_id":container_id,
            "name":artifact_name,
            "cef":{"rownumber":y+header_offset}
        }
        for x in range(0,maxwidth):
            if custom_list[y][x] == "None":
                custom_list[y][x] = None
            data['cef'][headers[x]] = custom_list[y][x]
            
        purl = phantom.build_phantom_rest_url('artifact')
        i = json.dumps(data)
        p = phantom.requests.post(purl,i,verify=False)
        
    phantom.debug("--- FINISHED {} ---".format(funcname))
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
