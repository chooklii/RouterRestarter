# RouterRestarter
Restart a Vodafone Router each day from your Raspberry Pi at 3:00 in the morning.

## Settup

Bevor starting create a config.py File. A Template is given.

```
const PASSWORD = XY
```

## Run

To run the script in the background simpy add

```
nohup python restart.py &
```

to sth. like the .bashrc to start the Scheduler.
