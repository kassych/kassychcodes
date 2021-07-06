print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

secret_number = 777
a = int(input("Enter an Integer Number: "))
while a != secret_number:
    print(
    """
    +=============================+
    |  Ha ha! You're stuck in my  |
    |         loop !              |
    +=============================+
    
    """)
else:
    print(
        """
        +===========================+
        | Well done, muggle! you are|
        |      free now.            |
        +===========================+
        
    """)
    

