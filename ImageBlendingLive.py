import cv2


n = int(input("Enter a number: "))
cap = cv2.VideoCapture(0)
image1 = cv2.imread('../draken.jpg')
image2 = cv2.imread('../micky.png')
image3 = cv2.imread('../baji.jpg')
image4 = cv2.imread('../haruki.png')
image5 = cv2.imread('../nahoya.jpg')
image6 = cv2.imread('../osonai.jpg')

if(n==1):
    while True:
        flag, frame =  cap.read()
        if not flag:
            print("Could not access webcam")
            break
        image1 = cv2.resize(image1, (frame.shape[1], frame.shape[0]))
        blended_frame = cv2.addWeighted(image1, 0.8, frame, 0.2, gamma=0.2)
        cv2.imshow("Blended", blended_frame)
        if cv2.waitKey(10) & 0xff == ord('q'):
            break
elif(n==2):
    while True:
        flag, frame =  cap.read()
        if not flag:
            print("Could not access webcam")
            break    
        image2 = cv2.resize(image2, (frame.shape[1], frame.shape[0]))
        blended_frame = cv2.addWeighted(image2, 0.8, frame, 0.2, gamma=0.2)
        cv2.imshow("Blended", blended_frame)
        if cv2.waitKey(10) & 0xff == ord('q'):
            break
elif(n==3):
    while True:
        flag, frame =  cap.read()
        if not flag:
            print("Could not access webcam")
            break 
        image3 = cv2.resize(image3, (frame.shape[1], frame.shape[0]))
        blended_frame = cv2.addWeighted(image3, 0.8, frame, 0.2, gamma=0.2)
        cv2.imshow("Blended", blended_frame)
        if cv2.waitKey(10) & 0xff == ord('q'):
            break
elif(n==4):
    while True:
        flag, frame =  cap.read()
        if not flag:
            print("Could not access webcam")
            break 
        image4 = cv2.resize(image4, (frame.shape[1], frame.shape[0]))
        blended_frame = cv2.addWeighted(image4, 0.8, frame, 0.2, gamma=0.2)
        cv2.imshow("Blended", blended_frame)
        if cv2.waitKey(10) & 0xff == ord('q'):
            break
elif(n==5):
    while True:
        flag, frame =  cap.read()
        if not flag:
            print("Could not access webcam")
            break
        image5 = cv2.resize(image5, (frame.shape[1], frame.shape[0]))
        blended_frame = cv2.addWeighted(image5, 0.8, frame, 0.2, gamma=0.2)
        cv2.imshow("Blended", blended_frame)
        if cv2.waitKey(10) & 0xff == ord('q'):
            break
elif(n==6):
    while True:
        flag, frame =  cap.read()
        if not flag:
            print("Could not access webcam")
            break
        image6 = cv2.resize(image6, (frame.shape[1], frame.shape[0]))
        blended_frame = cv2.addWeighted(image6, 0.8, frame, 0.2, gamma=0.2)
        cv2.imshow("Blended", blended_frame)
        if cv2.waitKey(10) & 0xff == ord('q'):
            break
else:
    print("Wrong Input")


cap.release()
cv2.destroyAllWindows()