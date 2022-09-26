# USB_Dual_handle_controller_JR_EAST_Train_Simulator
USB Dual handle controller "support" for JR EAST Train Simulator.  
  
This was only tested with a flashed Densha de Go! Plug & Play.  
To flash yours, check out: https://github.com/GMMan/dengo-plug-and-play-controller  

If you happen to have an original DGOC-44U, let me know if this script also works for you.  
  
Required Python packages:  
pyautogui  
pygame  

Download the .py file and run via: python.exe .\USB_Dual_handle_controller_JR_EAST_Train_Simulator.py  
Alternatively you can now also download a executable release that was created with py2exe.  

Make sure that the power lever is in the OFF position.                              
Start the game and use the EB notch to sync the controller once you are in the train.  
Do NOT use both levers at the same time when driving a single lever train.  
  
## Make sure to disable Steam Input for the game, otherwise the controller will behave incorrectly.  

Both levers and all buttons except the D-pad ones are working.  
There is currently an issue with the horns.  
  
Button mappings:
 

| Controller  | Game |
| :-------------: | :-------------: |
| A  | Switch cabin view  |
| B  | Back (Menu)  |
| C  | Confirm (Menu)  |
| D  | Deadman switch reset  |
| Select  | Left  |
| Start  | Right  |  
  
Since I could not get the D-pad working, I opted for Select/Start as a replacement.  
