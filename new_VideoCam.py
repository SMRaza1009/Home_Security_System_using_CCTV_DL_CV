import cv2
import numpy as np
import argparse
import time
	    filename = fd.askopenfilename()
            net = cv2.dnn.readNet('/home/syed/Desktop/Single-Multiple-Custom-Object-Detection-master/1. Project - Custom Object Detection/yolov3_best.weights', '/home/syed/Desktop/Single-Multiple-Custom-Object-Detection-master/1. Project - Custom Object Detection/yolov3.cfg')

            classes = []
            with open("/home/syed/Desktop/Single-Multiple-Custom-Object-Detection-master/1. Project - Custom Object Detection/classes.txt", "r") as f:
                classes = f.read().splitlines()
            #a = input("Enter Video number :")
            #a=int(a)
            #if a <= 0 or a is str:
                #print("invalid input")	
            #videoNum = "/home/syed/Desktop/Single-Multiple-Custom-Object-Detection-master/1. Project - Custom Object Detection/"+str(a)+".mp4"
            cap = cv2.VideoCapture(filename)
            font = cv2.FONT_HERSHEY_PLAIN
            colors = np.random.uniform(0, 255, size=(100, 3))

            while True:
                stime= time.time()
                _, img = cap.read()
                height, width, _ = img.shape
                
                

                blob = cv2.dnn.blobFromImage(img, 1/255, (416, 416), (0,0,0), swapRB=True, crop=False)
                net.setInput(blob)
                output_layers_names = net.getUnconnectedOutLayersNames()
                layerOutputs = net.forward(output_layers_names)

                boxes = []
                confidences = []
                class_ids = []

                for output in layerOutputs:
                    for detection in output:
                        scores = detection[5:]
                        class_id = np.argmax(scores)
                        confidence = scores[class_id]
                        if confidence > 0.2:
                            center_x = int(detection[0]*width)
                            center_y = int(detection[1]*height)
                            w = int(detection[2]*width)
                            h = int(detection[3]*height)

                            x = int(center_x - w/2)
                            y = int(center_y - h/2)

                            boxes.append([x, y, w, h])
                            confidences.append((float(confidence)))
                            class_ids.append(class_id)

                indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.2, 0.4)

                if len(indexes)>0:
                    for i in indexes.flatten():
                        x, y, w, h = boxes[i]
                        label = str(classes[class_ids[i]])
                        confidence = str(round(confidences[i],2))
                        color = colors[i]
                        cv2.rectangle(img, (x,y), (x+w, y+h), color, 2)
                        cv2.putText(img, label + " " + confidence, (x, y+20), font, 2, (255,255,255), 2)

                cv2.imshow('Image', img)
                key = cv2.waitKey(1)
                print('FPS {:1f}'.format(1/(time.time() -stime)))
                if key==27:
                    #break
                    cap.release()
                    cv2.destroyAllWindows()
            
