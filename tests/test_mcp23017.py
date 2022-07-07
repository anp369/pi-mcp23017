from pi_mcp23017 import mcp23017
import unittest


class TestMCP23017(unittest.TestCase):
    def test_byte_to_list(self):
        b1 = 0b11111111
        b2 = 0b00000000
        b3 = 0b10101010

        self.assertListEqual(mcp23017.MCP23017.byte_to_list(b1),
                             [1, 1, 1, 1, 1, 1, 1, 1])

        self.assertListEqual(mcp23017.MCP23017.byte_to_list(b2),
                             [0, 0, 0, 0, 0, 0, 0, 0])

        self.assertListEqual(mcp23017.MCP23017.byte_to_list(b3),
                             [0, 1, 0, 1, 0, 1, 0, 1])

    def test_get_bank_of_pin(self):
        self.assertEqual(mcp23017.MCP23017.get_bank_of_pin(0), mcp23017.Banks.A)
        self.assertEqual(mcp23017.MCP23017.get_bank_of_pin(7), mcp23017.Banks.A)
        self.assertEqual(mcp23017.MCP23017.get_bank_of_pin(8), mcp23017.Banks.B)
        self.assertEqual(mcp23017.MCP23017.get_bank_of_pin(15), mcp23017.Banks.B)
        with self.assertRaises(ValueError):
            mcp23017.MCP23017.get_bank_of_pin(16)

    def test_pin_to_register(self):
        self.assertEqual(mcp23017.MCP23017.pin_to_register(0), (mcp23017.Registers.GPIOA, 0b00000001))
        self.assertEqual(mcp23017.MCP23017.pin_to_register(1), (mcp23017.Registers.GPIOA, 0b00000010))
        self.assertEqual(mcp23017.MCP23017.pin_to_register(7), (mcp23017.Registers.GPIOA, 0b10000000))
        self.assertEqual(mcp23017.MCP23017.pin_to_register(8), (mcp23017.Registers.GPIOB, 0b00000001))
        self.assertEqual(mcp23017.MCP23017.pin_to_register(15), (mcp23017.Registers.GPIOB, 0b10000000))

        with self.assertRaises(ValueError):
            mcp23017.MCP23017.pin_to_register(16)


if __name__ == '__main__':
    unittest.main()
