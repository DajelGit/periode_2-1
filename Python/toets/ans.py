def hex_char(value):
    """Convert a numeric value to one of the possible hexadecimal values
    
    Remember, possible hexadecimal values are: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E and F.
    This is a base 16 type conversion and as such value cannot be higher than 16:
    
    0 => '0'
    ...
    16 => 'F'
    
    We handle two possible cases, first is the conversion of a value between 0 and 9 to 
    its textual representation ('0' ... '9'), the second case is converting numbers 10 to 16 
    into a textual representation from 'A' to 'F'. All is done by using the value's ASCII
    code number, e.g. the vale of ord('A') will be 65 and chr(65) will convert this back to 'A'.
    """
    if value <= 9 and value >= 0:
        # assert str(4) == chr(4 + ord('0')) == '4'
        return chr(value + ord('0'))
    else:
        return chr(value - 10 + ord('A'))

# given the above, what exactly happens when value > 9 ?   
for x in range(10, 16):
    v = x - 10 + ord('A') # ord('A') == 65
    print("Value: {} - 10, ASCII number: {}, ASCII value => {}".format(x, v, chr(v)))




"""
We weten nu dat de hex_var functie een getal kleiner of gelijk aan 16 kan omzetten naar een hexadecimale 
waarde. Maar hoe nu elke mogelijke decimale waarde om te zetten naar een hexadecimale representatie? 
Het probleem is dus hoe we elk mogelijk getal kunnen reduceren tot een veelvouden van 16.

Ter vergelijking: werken met het decimale stelsel is heel gewoon voor mensen en we kunnen gemakkelijk een 
getal als 279 opbreken in veelvouden van 10 (** is een machtsverheffing):

279 == 2 * (10**2) + 7 * (10**1) + 9 * (10**0)

Op basis van dit principe moeten we een getal opdelen in veelvouden van 16 (in plaats van 10). In de opgave 
wordt de hint gegeven de modulus % en integer division // te gebruiken, de uitwerking is ook tijdens het 
college CS besproken.
"""




def to_hex(decimal):
    """Convert a any decimal to its hexadecimal representation
    """
    # our final hexadecimal result value
    result = ''
    
    while decimal != 0:
        hex_value = decimal % 16
        result = hex_char(hex_value) + result
        decimal = decimal // 16

    return result

assert to_hex(79) == "{0:X}".format(79)
assert to_hex(279) == "{0:X}".format(279)

to_hex(279) # '117'

"""
De hexadecimale waarde 117 komt overeen met:

279 == 1 * (16**2) + 1 * (16**1) + 7 * (16**0)


"""





"""
Stream


Een uitwerking van oefenopgave 2

Een stream is een (on)eindig aantal signalen dat kan worden gelezen, denk bijvoorbeeld aan een 
bewegingssensor die elke keer dat een beweging wordt gedetecteerd een signaal stuurt. Maar denk ook aan 
de genoom opgave, daar was een signaal een opeenvolgend karakter in een (eindige) string.

Tijdens het werkcollege is het principe van een state machine geïnroduceerd: op een enkel moment kan iets 
zich maar in één bepaalde staat bevinden. Bijvoorbeeld, een lamp kan alleen maar aan of uit zijn en in de 
genoom opgave kon een gen in een genoom worden gevonden als het begon met ATF en eindigde met 
TAG, TAA of TGA.

In deze opgave gebeurt hetzelfde en gaan we werken met het volgende protocol:

de eerste 12 karakters is een mac adres
vervolgens 3 hexadecimale karakters die de lengte van de packet aangeven
verdere karakters tot en met de lengte is de inhoud van de packet

"""

with open('data/streams/packets.txt') as handle:
    packet_stream = handle.read()

packet_stream


"""
Wat zijn in dit geval de state(s) waar we mee moeten gaan werken? Weer hebben we te maken met een 
opeenvolging (iteration) en moeten eerst een mac adres weten om vervolgens een lengte te kunnen kennen, 
om vervolgens tot een bepaalde lengte te blijven lezen om de waarde van het packet te vinden 
(en waarna de cyclus weer opnieuw begint).

De states waar we in geïnteresseerd zijn om packets te kunnen lezen zijn dus:

een mac addres (wel of niet bekend)
een lengte van de packet (wel of niet bekend)
In de uitwerking wordt er van uitgegaan dat we met een continue stroom werken, m.a.w. dat we niet weten 
wat het volgende karakter is. Dit betekent dat we steeds naar achteren moeten kijken, dit in 
tegenstelling tot het de genoom opgave waar we vooruit konden kijken (het volgende karakter was immers 
al bekend omdat we de gehele sequentie al kenden).
"""


packet_list = []  # list for collecting extracted packets

# possible states we need to check:
# mac address, empty string or not empty if set
mac = ''

# the packet length, 0 or > 0 if set
# note: keeping it simple, we assume there are no 0 length packets
length = 0

length_as_hex = None

# collect characters as we go (look behind!), should get reset on any state change
chars = ''

for char in packet_stream:
    chars += char
    if not mac: # reference equality check, in this case (string) also evaluates as: mac == ''
        if len(chars) == 12:
            mac = chars # set mac
            chars = ''  # state change, reset chars
        continue        # check actual mac state in next iteration, continue
    
    # at this point the mac address is known
        
    if length == 0: # value equaltity check, in this case (int) also evaluates as: length is 0
        if len(chars) == 3:
            length = int(chars, 16) # set the packet length (a base 16 string to int conversion)
            length_as_hex = chars # set the hexadecimal length value, we need it later
            chars = '' # state change, reset chars 
        continue  # check actual length state in next iteration, continue
    
    # at this point the packet length is known
        
    if len(chars) == length:
        packet_list.append( (mac, length_as_hex, chars) ) # packet length reached
        
        length = 0  # full state reset
        mac = chars = ''

packet_list












"""
Employees


Een uitwerking van opgave 3

In deze oplossing zie je een aantal handige methoden om de klassen compact en efficiënt (pythonic?) uit te werken:

het gebruik van de property class method decorator om een salaris te berekenen
__repr__ (en __str__) is natuurlijk éénmaal gedefiniëerd, met behulp van:
f-string formatting (sinds python 3.6)
*args voor het verzamelen van positionele argumenten
bonus in de Manager class als een keyword argument met een default waarde
Tijdens het werkcollege is kort type hinting genoemd als een recente ontwikkeling om objecten te kunnen annoteren, je kan een toepassing van deze notatie in de uitwerking zien.

N.B: in de opgave wordt gevraagd __repr__ te implementeren om een object te kunnen printen. Het is meer gangbaar hier __str__ voor te gebruiken omdat __repr__ voornamelijk bedoeld is voor de object representatie (zie einde uitwerking opgave).
"""


from typing import Union

class Employee:
    """A company employee class
    """
    def __init__(self, name: str, role: str, department: str, salary: Union[int, float]):
        self.name = name
        self.role = role
        self.department = department
        self.salary = int(salary) # can't be bothered with cents
    
    @property
    def calculated(self) -> int:
        """Return a calculated salary
        """
        # nothing to compute, just return salary
        return self.salary
    
    def __str__(self) -> str:
        # f-string, since python 3.6
        return f"{self.name}, {self.role} at {self.department}, €{self.calculated/1000:.1f}k"

    def __repr__(self) -> str:
        # hex(id(self)) will return the hexadecimal memory address of this object
        return f"<{self.__class__.__name__}: {self.name} at {hex(id(self))}>"




class Manager(Employee):
    """A company manager class
    """
    def __init__(self, *args, bonus: Union[int, float]=0):
        super().__init__(*args)
        self.bonus = bonus
    
    @property
    def calculated(self) -> int:
        """Return a calculated salary
        
        Adds bonus as a percentage of the employee salary.
        """
        # bonus can be a float or int which matters for the 
        # calculation, but cast final result to int
        return int(self.salary + self.salary * self.bonus / 100)




employees = [
    Employee('Julia', 'Accountmanager', 'Products', 18000.99),
    Manager('Jane', 'VP Sales', 'Sales', 45000, bonus=5),
    Employee('John', 'Aftersales specialist', 'Sales', 21000),
    Manager('Bob', 'Head of R&D', 'Products', 35000.75, bonus=8.0),
    Manager('Mary', 'VP Human Resources (bonus next year!)', 'HRM', 30000)
]

for employee in employees:
    print('=>', employee)



"""
=> Julia, Accountmanager at Products, €18.0k
=> Jane, VP Sales at Sales, €47.2k
=> John, Aftersales specialist at Sales, €21.0k
=> Bob, Head of R&D at Products, €37.8k
=> Mary, VP Human Resources (bonus next year!) at HRM, €30.0k
Om het verschil tussen __str__ en __repr__ duidelijk te maken, zie wat er gebeurt als we het employees list object opvragen:
"""


employees[:2]  # [<Employee: Julia at 0x7f4b742fe128>, <Manager: Jane at 0x7f4b742fef28>]