PNAME = 'ac_client.exe'
WINNAME = 'AssaultCube'


LocalPlayer = 0x17E0A8
EntityList = 0x191FCC



class Offsets:
    CountPlayers = 0x18AC0C
    Fov = 0x18A7CC
    
    Health = 0xEC
    Name = 0x204
    
    X = 0x28
    Y = 0x30
    Z = 0x2C
    
    CrouchY = 0x50
    
    CamX = 0x34
    CamY = 0x38
    
    AmmoPistol = 0x12C
    AmmoRiffle = 0x140
    AmmoDoublePistol = 0x148