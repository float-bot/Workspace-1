#written by jGlue
from typing import Text
import pygame
from pygame.draw import ellipse
import pygame_gui
import random
import time

from pygame_gui.elements import ui_drop_down_menu

pygame.init()
pygame.display.set_caption('GM Lore Keeper v.0')
screen_size=(1000,500)
window_surface=pygame.display.set_mode(screen_size)
background=pygame.Surface(screen_size)
background.fill(pygame.Color('#505000'))
manager=pygame_gui.UIManager(screen_size) #manager needs to know the size of the window
clock=pygame.time.Clock()

'''start buttons'''
button_active_battle=pygame_gui.elements.ui_button.UIButton(relative_rect=pygame.Rect((30,20),(150,50)),
                                                                text='Active Battle',
                                                                manager=manager,
                                                                tool_tip_text='open the active battle'
                                                                )
button_gm_note=pygame_gui.elements.ui_button.UIButton(relative_rect =pygame.Rect((30,90),(150,50)),
                                                        text='GM Notes',
                                                        manager=manager,
                                                        )
button_pc_detail=pygame_gui.elements.ui_button.UIButton(relative_rect=pygame.Rect((30,160),(150,50)),
                                                            text='PC Details',
                                                            manager=manager
                                                            )
button_updates=pygame_gui.elements.ui_button.UIButton(relative_rect=pygame.Rect((30,230),(150,50)),
                                                            text='Upcoming',
                                                            manager=manager
                                                            )                     
'''start windows'''
def window_active_battle():
    pygame_gui.elements.ui_window.UIWindow(rect=pygame.Rect((500,0),(500,250)),
                                                manager=manager,
                                                window_display_title='Active Battle',
                                                element_id='active_battle',
                                                )
    pygame_gui.elements.ui_drop_down_menu.UIDropDownMenu(relative_rect=pygame.Rect((100,50),(100,50)),
                                                            options_list=['test2','test3'],
                                                            starting_option='test1',
                                                            manager=manager)
def window_gm_note():
    pygame_gui.elements.ui_window.UIWindow(rect=pygame.Rect((500,0),(500,250)),
                                                manager=manager,
                                                window_display_title='GM Notes',
                                                element_id='gm_note',
                                                )
def window_pc_detail():
    pygame_gui.elements.ui_window.UIWindow(rect=pygame.Rect((500,0),(500,250)),
                                                manager=manager,
                                                window_display_title='PC Details',
                                                element_id='pc_detail',
                                                )
'''start messages'''
def message_updates():
    pygame_gui.windows.UIMessageWindow(rect=pygame.Rect((100,0),(500,250)),
                                        html_message='Focus on just the active battle window. Give an option for the active battle to have PC,s and NPC,s added with their intitative ',
                                        manager=manager,
                                        window_title='updates',
                                        )

running = True

while running:
    time_delta = clock.tick(60)/1000.0 #this locks in the frame rate...not really necessary but its good to control it.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.USEREVENT: # this will print hello world to the console when hello_button is clicked.
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == button_active_battle:
                    print('active battle displayed')
                    window_active_battle()
                if event.ui_element == button_gm_note:
                    print('GM notes displayed')
                    window_gm_note()
                if event.ui_element == button_pc_detail:
                    print('PC Details displayed')
                    window_pc_detail()
                if event.ui_element == button_updates:
                    print('Updates displayed')
                    message_updates()
        manager.process_events(event)
    manager.update(time_delta)
    window_surface.blit(background, (0,0))
    manager.draw_ui(window_surface)
    pygame.display.update()
