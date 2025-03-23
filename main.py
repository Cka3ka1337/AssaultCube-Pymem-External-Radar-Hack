import os
import math

# math.atan2()

import win32api
import win32con
import pygame
os.system('cls')


from memory import GetLocalPlayer, GetEntityList, GetName, GetPos, GetHealth, GetCam
    

def main():
    pygame.init()
    
    sc = pygame.display.set_mode((300, 300), pygame.RESIZABLE)
    pygame.display.set_caption('External Radar Hack')
    clock = pygame.time.Clock()

    pygame.display.update()
    font = pygame.font.SysFont('Arial', 12, False, False)

    stop = False
    while not win32api.GetAsyncKeyState(win32con.VK_PAUSE) and not stop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stop = True

        sc.fill((20, 20, 20))
        pygame.draw.line(
            surface=sc,
            color=(230, 230, 230),
            start_pos=(
                0,
                sc.get_height() / 2
            ),
            end_pos=(
                sc.get_width(),
                sc.get_height() / 2
            )
        )
        
        pygame.draw.line(
            surface=sc,
            color=(230, 230, 230),
            start_pos=(
                sc.get_width() / 2,
                sc.get_height()
            ),
            end_pos=(
                sc.get_width() / 2,
                0
            )
        )
        
        pygame.draw.circle(
            surface=sc,
            color=(20, 230, 20),
            center=(
                sc.get_width() / 2,
                sc.get_height() / 2
            ),
            radius=5
        )

        
        EntityListPointers = GetEntityList()
        LocalPlayer = GetLocalPlayer()
        local_x, _, local_z = GetPos(LocalPlayer)
        local_yaw, local_pitch = GetCam(LocalPlayer)
        local_yaw = (local_yaw - 360) * -1
        
        for entity_ptr in EntityListPointers:
            entity_x, _, entity_z = GetPos(entity_ptr)
            x, z = entity_x - local_x, entity_z - local_z
            angle_radians = math.atan2(z, x)
            angle_degrees = math.degrees(angle_radians) * -1
            
            angle_degrees -= 90
            if angle_degrees < 0:
                angle_degrees += 360
            
            angle_degrees -= local_yaw
            if angle_degrees < -180:
                angle_degrees = angle_degrees % 180
            
            distance = math.sqrt(x ** 2 + z ** 2) * 2.5
            
            x_on_screen, y_on_screen = math.cos(math.radians(angle_degrees)), math.sin(math.radians(angle_degrees)) * -1
            x_on_screen, y_on_screen = y_on_screen * distance, x_on_screen * distance
            
            pygame.draw.circle(
                surface=sc,
                color=(230, 20, 20),
                center=(
                    sc.get_width() / 2 + x_on_screen,
                    sc.get_height() / 2 - y_on_screen
                ),
                radius=5
            )
            pygame.draw.aaline(
                surface=sc,
                color=(150, 150, 150),
                start_pos=(
                    sc.get_width() / 2 + x_on_screen,
                    sc.get_height() / 2 - y_on_screen
                ),
                end_pos=(
                    sc.get_width() / 2,
                    sc.get_height() / 2
                )
            )

            text = font.render(f'{GetName(entity_ptr)}: {GetHealth(entity_ptr)}', True, (230, 230, 230))
            sc.blit(
                source=text,
                dest=(
                    sc.get_width() / 2 + x_on_screen - text.get_width() / 2,
                    sc.get_height() / 2 - y_on_screen - text.get_height() - 5
                )
            )
            # print(distance, x_on_screen, y_on_screen)
            # print(angle_degrees, math.cos(angle_degrees), math.sin(angle_degrees))
            
            # print([f'{x:.3f}' for x in[entity_x - local_x, entity_z - local_z]])
        

        pygame.display.update()
        clock.tick(128)
    
    pygame.quit()


if __name__ == '__main__':
    main()