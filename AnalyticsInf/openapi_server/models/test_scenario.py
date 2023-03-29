
import gdown
import os
import requests
import json

from openapi_server.AnLF.mnist_inference import *




#import AnalyticsInf.AnLF.mnist_inference
#from AnLF.mnist_inference import results


def analytic_result() :

    if os.path.isfile("/home/nwdaf/5GC_APIs_NWDAF/AnalyticsInf/openapi_server/AnLF/models/mnist_1.h5") :

        res_value = inference()
        print("Inference with saved ML model")
        return (str(res_value))
        
 
    else: 
        root_nwdaf_server = f"http://192.168.221.141:8081/nnwdaf-mlmodelprovision/v1/subscriptions/sbd"
        req_body = {
            "notifUri": "http://192.168.221.141:8081/nnwdaf-mlmodelprovision/v1/subscriptions/sbd",
            "mLEventSubscs": [
                {
                    "mLEvent": "ML_model_provision_request",       
                    "mLEventFilter": {
                        "not": {
                            "required": [
                                "anySlice",
                                "snssais"
                            ]
                        }
                    }
                }
            ]
        }
        headers = {'Content-type': 'application/json; charset=utf-8'}

        r = requests.put(root_nwdaf_server, headers = headers, data = json.dumps(req_body))
        res_body = json.loads(r.text)   

        MLmodel_url = res_body['m_l_file_addr'] # m_l_file_addr is in the response body)
        #event = res_body['event']
        #MLmodel_url = "https://drive.google.com/drive/folders/1zdpyXbnptSU4Yb0KdtJOrAUoXb3DN3EU?usp=sharing"
   
        gdown.download_folder(MLmodel_url, quiet=True, use_cookies=False, output="/home/nwdaf/5GC_APIs_NWDAF/AnalyticsInf/openapi_server/AnLF/models")

        

        res_value = inference()
        print("Inference with provisioned ML model")
        return (str(res_value))
        
