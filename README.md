# Virtual Mouse Controller
```
• We can control mouse movements virtually in front of camera by fingers
# python
```
# Steps
```
• Find hand Landmarks
• Get the tip of the index and middle fingers
• Check which fingers are up
• Only Index Finger : Moving Mode
• Convert finger Coordinates with screen resolution by Interpolation method
• Smoothen Values for accurate movement of mouse
• Both Index and middle fingers are up : Clicking Mode
• Both Index and middle fingers are up : Clicking Mode
• Find distance between fingers
• Click mouse if distance short
• Drawing & Displaying Anotations
```
## Used Interpolation concept 
```
numpy.interp(x, xp, fp, left=None, right=None, period=None)
```
## Mouse Movement 
![GIF-210711_105932-min](https://user-images.githubusercontent.com/55943851/125184637-1c437f00-e23d-11eb-9604-1dd611195434.gif)

## Double Click
![GIF-210710_222929-min](https://user-images.githubusercontent.com/55943851/125184520-2913a300-e23c-11eb-911a-45b2f0688fda.gif)
