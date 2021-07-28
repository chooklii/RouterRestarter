# RouterRestarter
Restart a Vodafone Router from your Raspberry Pi each day  at 3:00 in the morning.

## Settup

Bevor starting create a config.py File. A Template is given.

```
const PASSWORD = XY
```

## Installation

You may have to install some packages. If so just run

Make sure you run the script with python 3, not python 2. If Python 2 is your default install the packages like this ```pip3 install selenium```

```
pip install selenium
pip install webdriver-manager
pip install schedule
```

## Run

To run the script in the background simpy add

```
nohup python restart.py &
```

to sth. like the .bashrc to start the Scheduler.
