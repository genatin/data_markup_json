import load from json
import cv2

with open('annotation.json', 'r') as f:
    d = json.load(f)

def tevian (d):

    for filename, value in d.items():
        image = cv2.imread(filename)
        for face in value['objects']:
            start_point = (face['x'], face['y'])
            end_point = (face['x'] + face['w'], face['y'] + face['h'])
            color = (255, 0, 0)
            thickness = 2
            str=""

            if face["isOccluded"] == 1:
                str+="Occluded "
            if face["isTruncated"] == 1:
                str+="Truncated "
            if face["isDepiction"] == 1:
                str+="Depiction "
            if face["isInside"] == 1:
                str+="Inside "
            if face["isGroupOf"] == 1:
                str+="GroupOf "
            if str=="":
                str+="good"

            image = cv2.rectangle(image, start_point, end_point, color, thickness)
            font_size=0.5
            if face['y'] <= 15:
                cv2.putText(image, str, (face['x']+5, face['y']+20), cv2.FONT_HERSHEY_SIMPLEX, font_size, (36,255,12), thickness)
            else:
                cv2.putText(image, str, (face['x'], face['y']-10), cv2.FONT_HERSHEY_SIMPLEX, font_size, (36,255,12), thickness)

        path_result = "images_result/" + filename.split("/")[-1]
        cv2.imwrite(path_result, image)

tevian (d)