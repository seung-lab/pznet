from conv    import set_conv_dim
from deconv  import set_deconv_dim
from pool    import set_pool_dim
from bnorm   import set_bnorm_dim
from elu     import set_elu_dim 
from sigmoid import set_sigmoid_dim 
from scale   import set_scale_dim 
from slc     import set_slc_dim 
from eltwise import set_eltwise_dim 

def set_layer_dim(lparams, bot_tensor):
   lt = lparams["type"]
   if lt == "input":
      return 
   elif lt == "conv":
      set_conv_dim(lparams, bot_tensor)
   elif lt == "deconv":
      set_deconv_dim(lparams, bot_tensor)
   elif lt == "pool":
      set_pool_dim(lparams, bot_tensor)
   elif lt == "bnorm":
      set_bnorm_dim(lparams, bot_tensor)
   elif lt == "elu":
      set_elu_dim(lparams, bot_tensor)
   elif lt == "sigmoid":
      set_sigmoid_dim(lparams, bot_tensor)
   elif lt == "scale":
      set_scale_dim(lparams, bot_tensor)
   elif lt == "slc":
      set_slc_dim(lparams, bot_tensor)
   elif lt == "eltwise":
      set_scale_dim(lparams, bot_tensor)
   else:
      lparams["top_dim"] = bot_tensor.dim
   '''elif lt == "ELU":
   elif lt == "Sigmoid":
   elif lt == "BatchNorm":
   elif lt == "Scale":
   elif lt == "Eltwise":
      #TODO: do I need to reset dimensions here?
   else:
      raise Exception("Unsupported Layer: {}".format(lt))'''
