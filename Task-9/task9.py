#!/usr/bin/python3
print("Content-Type: text/html")
print()

import subprocess as sp
import cgi
field = cgi.FieldStorage()
inputString = field.getvalue("x")


inputString = inputString.lower()
inputstrList = inputString.split(" ")
#kubectl run pod1 --image httpd
#launch pod with name=pod1 using image=httpd with port=80
if (("launch" in inputString or "run" in inputString) and ("pod" in inputString)):
    option = ""
    for s in inputstrList:
        if("name=" in s):
            podName = s[5:]
        elif("image=" in s):
            imageName = s[6:]
            option ="{0}--image={1} ".format(option,imageName)
        elif("podname=" in s):
            podName = s[8:]
        elif("port=" in s):
            port = s[5:]
            option ="{0}--port={1} ".format(option,port)
    print(sp.getoutput("kubectl run {0} {1}--labels={2} --generator=run-pod/v1".format(podName,option,"app=web,env=dev")))     
#run deployment using image=httpd with name=dep and port=80 with replica=3      
elif(("launch" in inputString or "run" in inputString) and ("deployment" in inputString)):
    option = ""
    for s in inputstrList:
        if("name=" in s):
            deploymentName = s[5:]
        elif("image=" in s):
            imageName = s[6:]
            option ="{0}--image={1} ".format(option,imageName)
        elif("podname=" in s):
            podName = s[8:]
        elif("port=" in s):
            port = s[5:]
            option ="{0}--port={1} ".format(option,port)
    print(sp.getoutput("kubectl create deployment {0} {1}".format(deploymentName,option)) )   
#scale the pods with replicas=1

elif("scale" in inputString and ("replicas" in inputString or "replica" in inputString)):
    for s in inputstrList:
        if ("replicas=" in s):
            replicas = s[9:]
        elif("name=" in s):
            name = s[5:]
    print(sp.getoutput("kubectl scale deployment.apps/{0} --replicas={1}".format(name,replicas))  )   
#delete pod name=pod1
#delete deployment name=dep
#delete all
elif("delete" in inputString):
    if ("pod" in inputString):
        resource = "pod"
        for s in inputstrList:
            if("name=" in s):
                name = s[5:]
        print(sp.getoutput("kubectl delete {0} {1}".format(resource,name)) )
    elif("deployment" in inputString):
        resource ="deployment"
        for s in inputstrList:
            if ("name=" in s):
                name = s[5:]
        print(sp.getoutput("kubectl delete {0} {1}".format(resource,name)) )
    elif(("pod" not in inputString) and ("deployment" not in inputString) and ("all" in inputString)):
        name = "all"
        print(sp.getoutput("kubectl delete all --all") )
#get all pods
elif(("get" in inputString) and ("all" in inputString) or ("pods" in inputString)):
    print(sp.getoutput("kubectl get all"))