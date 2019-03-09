import sys
import boto3
import pyttsx3

imgWidth = 3024
imgHeight = 4032

if __name__ == "__main__":

    imageFile=sys.argv[1]
    client=boto3.client('rekognition')
   
    with open(imageFile, 'rb') as image:
        response = client.detect_labels(Image={'Bytes': image.read()})
    
    result = ''
    confidence = round(response['Labels'][1]['Confidence'],2)

    print('Detected labels in ' + imageFile)    
    for label in response['Labels']:
        if (('Bed' in label['Name']) or ('Bedroom' in label['Name'])):
            result = 'Bedroom'
            
        elif (('Kitchen' in label['Name']) or ('Kitchen Island' in label['Name'])):
            result = 'Kitchen'
        elif (('Bathroom' in label['Name']) or ('Bathtub' in label['Name'])):
            result = 'Bathroom'
        elif (('Dining Room' in label['Name']) or ('Table' in label['Name'])):
            result = 'Dining Room'
        #else :
            #result = 'Room'
        #confidence = round(label['Confidence'],2)
        print (label)
    print (result + ' : ' + str(confidence))
    
            
    engine = pyttsx3.init()
    engine.say("I am " + str(confidence)+ "percent confident that This is a " + result)
    #+ " Its height is " + str(height) + "pixels, and"
    #+ " Its width is " + str(width) + "pixels")
    engine.runAndWait()
            
#box = label['Instances'][0]['BoundingBox']
#width = imgWidth * box['Width']
#height = imgHeight * box['Height']
#print("Width : ") 
#print(width) 
#print("  Height : ")
#print(height)

    print('Done...')