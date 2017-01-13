#Lock Screen Via Foot-switch
This repo is dead simple. I've used this code to solve the issue of locking my screen at work and me not really liking the process of having to press a sequence of keys to do so (security requirements require locked screens)  

User interaction  
=

Simple: 

1) User presses on usb-pedal  
2) Screen is locked  



USB Pedal
=

This code is set up to react to an FS1-P foot switch  
  
![img](https://images-na.ssl-images-amazon.com/images/I/41EIABYeteL._SX425_.jpg)

You can order an FS1-M on Amazon by following this [link](https://www.amazon.com/FS1-M-Single-Switch-Control-Keyboard/dp/B00G5ZRJDA) (The model numbers are different but the `FS` prefix is the only thing matters)  
  

Configuring the USB Pedal
=  

The code written here works on the basis that my keyboard only has `f1`-`f12`. I configure the switch to press `f14`. A python script listens and reacts to that key press.   

Configuration is fairly simple. Download the software [here](http://software.pcsensor.com/pc_en.html). 

>  I downloaded `FootSwitch V6.7.9.zip`. You can get away with selecting any item in the gallery that says footswitch and looks like a foot-switch. 

Refer to the following `.gif`  
  
![img](/docs/gifs/fs_animation.gif)  

  




Python Dependencies
=

- `Windows` - the foot-switch software runs on it  
- `pynput` - for listening to keys
- `ctypes` - for interacting with windows

Here's some bash to help you along:  

	pip install pynput
	pip install ctypes  

The code
=

So short I can display it in this `README.md` file



<pre><code class="python">
	import ctypes
	from pynput import keyboard
	
	def on_press(key):
	    if key == keyboard.Key.f14:
	        ctypes.windll.user32.LockWorkStation()
	
	def on_release(key):
		pass
	
	with keyboard.Listener(
	        on_press=on_press,
	        on_release=on_release) as listener:
	    listener.join()

</code></pre>


# Running it in windows

Running it in foreground:  

- Double click icon or execute using `python.exe`  

Running it in the background :  

- Save as `.pyw`  
- Run using `pythonw.exe`	

