# pi-mcp23017

This is a small library to interface the popular I²C MCP23017 portexpander with a Raspberry Pi and Python. A threaded
approach makes sure, that interrupt capability of the expander works properly.

### Dependencies

There are just these three python dependencies:

* `python>=3.6`
* `smbus`
* `RPi.GPIO`

### Installation

Just install the package with pip or your favorite package manager:  
`pip install pi-mcp23017`

### Usage

Connect the Port Expander to your Raspberry Pi and find out the address. If you haven't configured the address pins, it
should be under `0x20`. Also make sure to note the GPIO pin to which the interrupt pin is connected.

Pins are numbered from 0 to 15 and mapped as follows  
PORTA: 0 to 7 with PORTA_0 = Pin 0   
PORTB: 8 to 15 with PORTB_0 = Pin 8

The library merges the both interrupt pins of the MCP23017 for the sake of simplicity.

For a working example that uses most of the functions,
see the example below.  
For docs, see the docstrings in `mcp23017.py`. It is planned to add some kind
of proper documentation if needed.

```python
# This example registers one callback that toggles a pin
# on each press

from pi_mcp23017.mcp23017 import MCP23017, Banks, Directions, PullUp
from time import sleep

# example address and pin,
# change to your own data
ADDRESS = 0x20
PIN = 27


# define an interrupt callback
def callback(pin_number):
    print(f"got interrupt on pin {pin_number}!")
    state = port_expander.read_pin(8)
    port_expander.write_pin(8, not state)


# if you have multiple busses choose the right one!
port_expander = MCP23017(ADDRESS, int_pin=PIN, bus=0)

# set PORTA to Input and enable interrupts
port_expander.setup_port(Banks.A, Directions.INPUT, PullUp.ENABLED)
port_expander.attach_interrupt(0, callback)

# set PORTB_0 to Output and set it to LOW
port_expander.setup_pin(8, Directions.OUTPUT, PullUp.DISABLED)
port_expander.write_pin(8, False)

try:
    while True:
        sleep(.1)
except KeyboardInterrupt:
    print("Cleaning up automatically and exiting")
```
 
### Running tests
The testsuite is pretty small at the moment