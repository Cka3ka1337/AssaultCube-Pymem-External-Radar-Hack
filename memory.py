import pymem

from pymem.ptypes import RemotePointer

from offsets import *


def GetPointer(base, offsets) -> int:
    #base = base   !!!!!!!!
    for offset in offsets:
        base = RemotePointer(mem.process_handle, base + offset).value
        
    return base


def GetLocalPlayer():
    return GetPointer(mem.base_address, [LocalPlayer])


def GetName(ptr) -> str:
    try:
        return ''.join(x for x in mem.read_bytes(ptr + Offsets.Name, 15).decode('utf-8') if x not in '#*' and x != '\x00')
    except:
        pass
    
    
def GetPos(ptr) -> tuple:
    try:
        return (
            mem.read_float(ptr + Offsets.X),
            mem.read_float(ptr + Offsets.Y),
            mem.read_float(ptr + Offsets.Z)
        )
    except:
        pass


def GetCam(ptr) -> tuple:
    try:
        return (
            # abs(mem.read_float(ptr + Offsets.CamX) - 360),
            mem.read_float(ptr + Offsets.CamX),
            mem.read_float(ptr + Offsets.CamY)
        )
    except:
        pass

    
def GetHealth(ptr) -> int:
    try:
        return mem.read_int(ptr + Offsets.Health)
    except:
        pass


def GetEntityList() -> list:
    EntityList_out = []
    
    player_list_ptr = GetPointer(mem.base_address, offsets=[EntityList])
    count_players = mem.read_int(mem.base_address + Offsets.CountPlayers) - 1

    for index in range(count_players):
        player = RemotePointer(mem.process_handle, player_list_ptr + (0x4 * index)).value
        EntityList_out.append(player)
    
    return EntityList_out

mem = pymem.Pymem(process_name=PNAME)