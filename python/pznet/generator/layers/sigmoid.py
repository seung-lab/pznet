import copy
from .common import generate_param_string

def set_sigmoid_dim(params, bot_tensor):
    top_dim = copy.copy(bot_tensor.dim)
    params["top_dim"] = top_dim

    params["bn"]  = bot_tensor.dim[0]
    params["ifm"] = bot_tensor.dim[1]
    params["ofm"] = bot_tensor.dim[1]
    params["id"]  = bot_tensor.dim[2]
    params["ihw"] = bot_tensor.dim[3]

def parse_sigmoid(json_param, arch):
    params = {}
    params["arch"] = arch
    params["name"] = json_param["name"]
    params["top"]  = json_param["top"][0]
    params["bot"]  = json_param["bottom"][0]
    params["type"] = "sigmoid"

    return params

def allocate_sigmoid_lines(lparam):
    l = lparam
    allocation_params = lparam["top_dim"][0:4]

    param_str = generate_param_string(allocation_params)
    lines = []
    #allocate layer
    lines.append('layers["{}"] = new znn::phi::SigmoidLayer({});'.format(l["name"],
                                                                        param_str))
    return lines

