kata = (0, 4, 132.42222, 10000, 12345.67)

print(f"module_{kata[0]:02d}, ex_{kata[1]:02d} : {kata[2]:.2f}, {kata[3]:.2e}, {kata[4]:.2e}")

"""
| Format | Meaning                                | Example    |
| ------ | -------------------------------------- | ---------- |
| `:02d` | integer, 2 digits, zero-padded         | `04`       |
| `:.2f` | float, 2 decimals                      | `132.42`   |
| `:.2e` | float, scientific notation, 2 decimals | `1.23e+04` |

so

| Expression      | Meaning                                      | Example Result |
| --------------- | -------------------------------------------- | -------------- |
| `{kata[0]:02d}` | Integer, 2 digits, pad with 0 if needed      | `00`           |
| `{kata[1]:02d}` | Same for the second integer                  | `04`           |
| `{kata[2]:.2f}` | Float with 2 decimal places                  | `132.42`       |
| `{kata[3]:.2e}` | Float in scientific notation with 2 decimals | `1.00e+04`     |
| `{kata[4]:.2e}` | Same style                                   | `1.23e+04`     |


"""