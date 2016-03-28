# brmngr
A /sys/class/backlight/ cli frontend

A pretty horrible attempt at a python script as well. If you're good at this stuff, please tell me what I'm doing horribly wrong.

###### Commands (as of 0.0.1)

```
brmng v0.0.1 help message:
-b <backlight> Sets the backlight. This arg must be set before manipulating or reading a backlight.
-l             Lists available backlights.
-s <value>     Sets the backlight brightness to the given value.
-m             Returns the maximum brightness of the backlight.
-g             Returns the current brightness of the backlight.
-h             Prints this message.
```
## License

MIT
