from components.Constants import * 

def draw_color_picker(surface, rect):
    for y in range(0, rect.height, 10):
        for x in range(0, rect.width, 10):
            hue = x / rect.width
            saturation = y / rect.height
            color = colorsys.hsv_to_rgb(hue, saturation, 1)
            pygame.draw.rect(surface, (int(color[0]*255), int(color[1]*255), int(color[2]*255)), (rect.x + x, rect.y + y, 10, 10))

def draw_brightness_slider(surface, rect, brightness):
    for y in range(0, rect.height, 10):
        color = colorsys.hsv_to_rgb(0, 0, 1 - y/rect.height)
        pygame.draw.rect(surface, (int(color[0]*255), int(color[1]*255), int(color[2]*255)), (rect.x, rect.y + y, rect.width, 10))

color_picker_surface = pygame.Surface((WINDOW_RECT.width, WINDOW_RECT.height), pygame.SRCALPHA)
color_picker_surface.fill((0, 0, 0, 0))
draw_color_picker(color_picker_surface, COLOR_PICKER_RECT)

selected_color = pygame.Color(255, 255, 255)
selected_hue_saturation = (0, 0)
selected_brightness = 1   

class Tab:
    def __init__(self):
        self.selected = 0
        self.name = TAB_NAMES[self.selected]
        self.clicked = False

        self.logo = pygame.image.load(os.path.join(sys._MEIPASS, "logo.png"))
        self.logo = pygame.transform.scale(self.logo, (300, 300))

        self.folder = False
        self.file = False
        self.manual = False
        self.color = False

        self.mode = MODE_SELECTED
        self.color_mode = False
        self.manual_mode = MANUAL_MODE
        self.SYNC = False

        self.selected_mode = ""
        self.load_process = False

    def draw(self, surface):
        BUTTON_WIDTH = 400
        BUTTON_HEIGHT = 50
        #draw tabs
        for i in range(len(TAB_NAMES)):
            tab = Rect(i * TAB_WIDTH, 0, TAB_WIDTH, TAB_HEIGHT)
            if self.selected == i:
                pygame.draw.rect(surface, BLACK, tab, border_radius=5)
                tab_text = FONT.render(TAB_NAMES[i], True, LIGHT_GREEN)
                tab_text_rect = tab_text.get_rect(center=tab.center)
                surface.blit(tab_text, tab_text_rect)
            else:
                pygame.draw.rect(surface, LIGHT_GREEN, tab, border_radius=5)
                tab_text = FONT.render(TAB_NAMES[i], True, BLACK)
                tab_text_rect = tab_text.get_rect(center=tab.center)
                surface.blit(tab_text, tab_text_rect)

            if self.mode == False:

                # wrapped_desc = textwrap.wrap(self.desc, width=65)  # Adjust the width as needed
                # for i, line in enumerate(wrapped_desc):
                #     desc_text = FONT.render(line, True, BLACK)
                #     desc_text_rect = desc_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4 + i * FONT.get_linesize()))
                #     surface.blit(desc_text, desc_text_rect)

                # Folder button and make it centered
                
                # Color picker button
                if self.name == "Start" and self.load_process == False:
                    #image logo in the middle of screen 
                    logo_rect = self.logo.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
                    surface.blit(self.logo, logo_rect)

                    #text that says "welcome to DolceLaze"
                    welcome_text = KINDA_BIG_FONT.render("Welcome to DolceLaze!", True, BLACK)
                    welcome_text_rect = welcome_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 150))
                    surface.blit(welcome_text, welcome_text_rect)

                    # Start button 
                    if self.SYNC == False:
                        if self.file == True:
                            file_button = Rect((SCREEN_WIDTH - BUTTON_WIDTH) // 2, SCREEN_HEIGHT // 2 + BUTTON_HEIGHT + BUTTON_PADDING + 120, BUTTON_WIDTH, BUTTON_HEIGHT)
                            pygame.draw.rect(surface, BLACK, file_button, border_radius=5)
                            pygame.draw.rect(surface, BLACK, file_button, 3, border_radius=5)  # Draw border
                            file_text = BIG_FONT.render('START SYNC', True, LIGHT_GREEN)
                            file_text_rect = file_text.get_rect(center=file_button.center)
                            surface.blit(file_text, file_text_rect)                    

                        else:
                            file_button = Rect((SCREEN_WIDTH - BUTTON_WIDTH) // 2, SCREEN_HEIGHT // 2 + BUTTON_HEIGHT + BUTTON_PADDING + 120, BUTTON_WIDTH, BUTTON_HEIGHT)
                            pygame.draw.rect(surface, LIGHT_GREEN, file_button, border_radius=5)
                            pygame.draw.rect(surface, BLACK, file_button, 3, border_radius=5)  # Draw border
                            file_text = BIG_FONT.render('START SYNC', True, BLACK)
                            file_text_rect = file_text.get_rect(center=file_button.center)
                            surface.blit(file_text, file_text_rect)
                    else: 
                        file_button = Rect((SCREEN_WIDTH - BUTTON_WIDTH) // 2, SCREEN_HEIGHT // 2 + BUTTON_HEIGHT + BUTTON_PADDING + 120, BUTTON_WIDTH, BUTTON_HEIGHT)
                        pygame.draw.rect(surface, DARK_BLUE, file_button, border_radius=5)
                        pygame.draw.rect(surface, BLUE, file_button, 3, border_radius=5)
                        file_text = BIG_FONT.render('SYNCED', True, LIGHT_GREEN)
                        file_text_rect = file_text.get_rect(center=file_button.center)
                        surface.blit(file_text, file_text_rect)
                    
                elif self.name == "File":
                    pass 
                    
                elif self.name == "Settings":
                    pass

                elif self.name == "Info":
                    #text that says "welcome to DolceLaze"
                    info_text = BIG_FONT.render("welcome to DolceLaze", True, BLACK)
                    info_text_rect = info_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
                    surface.blit(info_text, info_text_rect)

                    info_text = SMALL_FONT.render("This is a program for automating tasks. With built in AI, for eseay axcess to information you will be able to automate tasks with ease. This program is not to be used in any exams without the permission of the exam board. This tab is for information about how to use the program, and common practises to keep you safe. :)", True, BLACK)
                    info_text_rect = info_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4 + 100))
                    surface.blit(info_text, info_text_rect)

                    # How to use: 
                    info_text = FONT.render("How to use:", True, BLACK)
                    info_text_rect = info_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4 + 150))
                    surface.blit(info_text, info_text_rect)

                    #etc 

                elif self.name == "Credits": 
                    #text that says "Credits"
                    credits_text = VERY_BIG_FONT.render("Credits", True, BLACK)
                    credits_text_rect = credits_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4 - 30))
                    surface.blit(credits_text, credits_text_rect)

                    #logo 
                    logo_rect = self.logo.get_rect(center=(200, SCREEN_HEIGHT // 2 + 20))
                    surface.blit(self.logo, logo_rect)
                    
                    #know text that says: 
                    # Code by Adolf Nipple.
                    # Design by Stevie Wonder.
                    # Kernel driver by Patrick Star. 
                    # AI by Elon Musk.
                    # Yes, i know impressive. 
                    # Rights are reserved to the respective owners, not for commercial use.

                    credits_text = BIG_FONT.render("Code by Adolf Nipple.", True, BLACK)
                    credits_text_rect = credits_text.get_rect(center=(SCREEN_WIDTH // 2 + 200, SCREEN_HEIGHT // 4 + 120))
                    surface.blit(credits_text, credits_text_rect)

                    credits_text = BIG_FONT.render("Design by Stevie Wonder.", True, BLACK)
                    credits_text_rect = credits_text.get_rect(center=(SCREEN_WIDTH // 2 + 200, SCREEN_HEIGHT // 4 + 170))
                    surface.blit(credits_text, credits_text_rect)

                    credits_text = BIG_FONT.render("Kernel by Patrick Star.", True, BLACK)
                    credits_text_rect = credits_text.get_rect(center=(SCREEN_WIDTH // 2 + 200, SCREEN_HEIGHT // 4 + 220))
                    surface.blit(credits_text, credits_text_rect)

                    credits_text = BIG_FONT.render("AI by Elon Musk.", True, BLACK)
                    credits_text_rect = credits_text.get_rect(center=(SCREEN_WIDTH // 2 + 200, SCREEN_HEIGHT // 4 + 270))
                    surface.blit(credits_text, credits_text_rect)

                    credits_text = SMALL_FONT.render("Rights are reserved, not for commercial use.", True, BLACK)
                    credits_text_rect = credits_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4 + 420))
                    surface.blit(credits_text, credits_text_rect)

    def update(self, surface):
        BUTTON_WIDTH = 400
        BUTTON_HEIGHT = 50

        self.folder = False
        self.file = False
        self.manual = False
        self.color = False

        if pygame.mouse.get_pressed()[0]:
            mouse_pos = pygame.mouse.get_pos()
            for i in range(len(TAB_NAMES)):
                tab = Rect(i * TAB_WIDTH, 0, TAB_WIDTH, TAB_HEIGHT)
                if tab.collidepoint(mouse_pos):
                    self.selected = i
                    self.name = TAB_NAMES[i]
                    self.manual_mode = False
                    break

            self.clicked = True
            file_button = Rect((SCREEN_WIDTH - BUTTON_WIDTH) // 2, SCREEN_HEIGHT // 2 + BUTTON_HEIGHT + BUTTON_PADDING + 120, BUTTON_WIDTH, BUTTON_HEIGHT)
            color_picker_button = Rect((SCREEN_WIDTH - BUTTON_WIDTH) // 2, SCREEN_HEIGHT // 2 + 3 * (BUTTON_HEIGHT + BUTTON_PADDING), BUTTON_WIDTH, BUTTON_HEIGHT)

            if file_button.collidepoint(mouse_pos):
                self.file = True
            elif color_picker_button.collidepoint(mouse_pos):
                self.color = True


        elif pygame.mouse.get_pressed()[0] == False and self.clicked == True:
            mouse_pos = pygame.mouse.get_pos()
            pygame.time.wait(100)

            if self.name == "Start": 
                file_button = Rect((SCREEN_WIDTH - BUTTON_WIDTH) // 2, SCREEN_HEIGHT // 2 + BUTTON_HEIGHT + BUTTON_PADDING + 120, BUTTON_WIDTH, BUTTON_HEIGHT)
                color_picker_button = Rect((SCREEN_WIDTH - BUTTON_WIDTH) // 2, SCREEN_HEIGHT // 2 + 2 * (BUTTON_HEIGHT + BUTTON_PADDING), BUTTON_WIDTH, BUTTON_HEIGHT)

                if file_button.collidepoint(mouse_pos):
                    self.selected_mode = "File"

                    if self.SYNC == False:
                        surface.fill(BLACK)

                        # Press any key text
                        info_text = BIG_FONT.render("Press any key", True, LIGHT_GREEN)
                        info_text_rect = info_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
                        surface.blit(info_text, info_text_rect)

                        self.load_process = True 

                            
                if color_picker_button.collidepoint(mouse_pos):
                    self.color_mode = True
                    print("color mode")

            self.clicked = False
            self.foler = False
            self.file = False
            self.color = False

class Typer:
    def __init__(self):
        self.is_loading = False
        self.copy = False
        self.error = False
        self.error_message = ""

    def loading_bar(self, screen, bar_color, border_color, speed, max_bar_width, min_bar_width, bar_height, border_radius, bar_margin, file_selector, tab):
        start_ticks = pygame.time.get_ticks() #starter tick
        self.is_loading = True
        direction = speed
        position = 0
        max_position = 200 - min_bar_width - 2 * bar_margin
        last_width = max_bar_width
        screen_width, screen_height = screen.get_size()
        bar_x = (screen_width - 200) // 2
        bar_y = (screen_height - 50) // 2

        try: 
            pass
        except Exception as e:
            print(e)
            print("=================================================================ERROR=================================================================")
            self.error = True
            self.error_message = str(e)

            file_selector.is_successful = False
            self.is_loading = False

        while self.is_loading:
            file_selector.draw(screen)

            if file_selector.selected_files == set() or file_selector.selected_files == None:
                pygame.draw.rect(screen, BLACK, file_selector.submit_button, border_radius=5)
                pygame.draw.rect(screen, BLACK, file_selector.submit_button, 3, border_radius=5)
                submit_text = BIG_FONT.render('Submit', True, LIGHT_GREEN)
            else:
                pygame.draw.rect(screen, LIGHT_GREEN, file_selector.submit_button, border_radius=5)
                pygame.draw.rect(screen, BLACK, file_selector.submit_button, 3, border_radius=5)  # Draw border
                submit_text = BIG_FONT.render('Submit', True, BLACK)
            
            submit_text_rect = submit_text.get_rect(center=file_selector.submit_button.center)

            screen.blit(submit_text, submit_text_rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            tab.draw(screen)

            s = pygame.Surface((screen_width,screen_height))  # the size of your rect
            s.set_alpha(128)                # alpha level
            s.fill((0,0,0))           # this fills the entire surface
            screen.blit(s, (0,0))    # (0,0) are the top-left coordinates

            pygame.draw.rect(screen, border_color, pygame.Rect(bar_x, bar_y, 200, 50), 2, border_radius=border_radius) # draw loading bar border
            position += direction
            if position > max_position:
                direction = -speed
            elif position < 0:
                direction = speed
            width = max_bar_width - abs((position - max_position / 2) / (max_position / 2)) * (max_bar_width - min_bar_width) # width decreases as the bar moves away from the center
            position += (last_width - width) / 2 # compensate for the change in width
            last_width = width
            pygame.draw.rect(screen, bar_color, pygame.Rect(bar_x+position+bar_margin, bar_y+10, width, bar_height), border_radius=border_radius) # draw loading bar

            pygame.display.flip()
            pygame.time.wait(60)
        
        file_selector.update_file_cards()

class Textbox:
    def __init__(self, x, y, width, height, pre_text):
        self.rect = pygame.Rect(x, y, width, height)
        self.active = False
        self.text = pre_text
        self.cursor_visible = False
        self.cursor_counter = 0
        self.was_active = False
    def update(self, event, pre_text):
        if self.was_active:
            self.was_active = False
        if event.button and self.rect.collidepoint(event.pos):
            self.active = True
            self.cursor_visible = True
        elif event.button and not self.rect.collidepoint(event.pos):
            if self.active:
                self.was_active = True
            self.active = False
            self.cursor_visible = False
    
    def handel_key(self, event, pre_text):
        if self.active:
            if event.type == KEYDOWN:
                key_pressed = event.key
                if key_pressed == K_BACKSPACE:
                    self.text = self.text[:-1]
                elif key_pressed == K_RETURN:
                    self.active = False
                    self.cursor_visible = False
                    self.was_active = True
                elif len(str(self.text)) < 3 and event.unicode in '1234567890':
                    self.text += str(event.unicode)
        elif not self.active and not self.was_active: 
            return pre_text
        if self.was_active:
            self.was_active = False
            if self.text == '':
                self.text = '0'
            #if over 255, set to 255
            if int(self.text) > 255:
                self.text = '255'
            #if under 0, set to 0
            if int(self.text) < 0:
                self.text = '0'
            return self.text
        else: 
            return pre_text
       
    def draw(self, surface):
        if self.active:
            pygame.draw.rect(surface, GREEN, self.rect, border_radius=5)
            self.cursor_counter += 1
            if self.cursor_counter % 40 < 20:  
                pygame.draw.line(surface, BLACK, (self.rect.left + SMALL_FONT.size(self.text)[0] + PADDING, self.rect.bottom - 7), (self.rect.left + SMALL_FONT.size(self.text)[0] + 17, self.rect.bottom - 7), 2)
        else:
            pygame.draw.rect(surface, LIGHT_GREEN, self.rect, border_radius=5)
        pygame.draw.rect(surface, BLACK, self.rect, 2, border_radius=5)  # Draw border
        text = SMALL_FONT.render(self.text, True, BLACK)
        surface.blit(text, (self.rect.left + PADDING, self.rect.centery - text.get_height() // 2))


class TextBox: 
    def __init__(self):
        self.font = BIG_FONT

        self.name = ""   
        self.text = ""
        self.sudo_text = ""
        self.orgin_name = ""
        self.width = 200
        self.height = 32
        self.selected = False
        self.name_box_selected = False
        self.done = False 

        self.rect = pygame.Rect(100, 100, self.width, self.height)

        self.cursor_timer = 0
        self.cursor_visible = True
        self.cursor_speed = 500  # Cursor blinks every 500ms

        self.key_delay = 1
        self.time = 0
        self.accelaration = 0.4
        self.max_name_length = 40

        self.submit_rect = pygame.Rect(615, 50, 85, 30)
        self.name_box_rect = pygame.Rect(100, 50, 500, 30)

    def handle_event(self, event):

        if event.type == pygame.KEYDOWN:
            if self.selected:
                if event.key == pygame.K_BACKSPACE:
                    pass 
                elif event.key == pygame.K_RETURN:
                    self.sudo_text += '\n'
                    self.text += '\n'
                elif event.key == pygame.K_v and pygame.key.get_mods() & pygame.KMOD_CTRL:
                    self.sudo_text += pyperclip.paste()
                    self.text += pyperclip.paste()
                else:
                    self.sudo_text += event.unicode
                    self.text += event.unicode
                self.update_text()

            elif self.name_box_selected: 
                if event.key == pygame.K_BACKSPACE:
                    pass 
                elif event.key == pygame.K_v and pygame.key.get_mods() & pygame.KMOD_CTRL:
                    self.name += pyperclip.paste().replace("\n", "")
                    if len(self.name) > self.max_name_length:
                        self.name = self.name[:self.max_name_length]
                else:
                    if len(self.name) < self.max_name_length:
                        self.name += event.unicode
                self.update_text()
            
            
            # if click on text box
        
        if event.type == pygame.MOUSEBUTTONDOWN:

            if pygame.Rect(self.rect.x, self.rect.y - 2, SCREEN_WIDTH * 0.75, SCREEN_HEIGHT).collidepoint(event.pos):
                self.selected = True
            else:
                self.selected = False
            
            if pygame.Rect(self.submit_rect.x, self.submit_rect.y, self.submit_rect.width, self.submit_rect.height).collidepoint(event.pos):
                data = json.load(open("data.json", "r"))
                if self.name != "" and self.name not in data["Text_files"] and self.orgin_name == "":
                    #dump new data
                    with open("data.json", 'w') as outfile:
                        data["Text_files"][self.name] = self.text
                        self.done = True
                        outfile.write(json.dumps(data, indent=4))

                elif self.name in data["Text_files"] or self.orgin_name in data["Text_files"]: 
                    with open("data.json", 'w') as outfile:
                        #remove old data 
                        try: 
                            del data["Text_files"][self.orgin_name]
                        except:
                            pass
                        data["Text_files"][self.name] = self.text
                        self.done = True
                        outfile.write(json.dumps(data, indent=4))

            if pygame.Rect(self.name_box_rect.x, self.name_box_rect.y, self.name_box_rect.width, self.name_box_rect.height).collidepoint(event.pos):
                self.name_box_selected = True
            else:
                self.name_box_selected = False

    def update_text(self):
        if self.selected:
            self.sudo_text = self.text

            index = 0
            new_text = ""
            for char in self.text:
                index += 1 
                new_text += char
                if index == 49:
                    new_text += '\n'
                    index = 0
            
            self.sudo_text = new_text

    def update(self, dt):

        if self.selected or self.name_box_selected:
            self.cursor_timer += dt

            if self.cursor_timer >= self.cursor_speed:
                self.cursor_timer %= self.cursor_speed
                self.cursor_visible = not self.cursor_visible

    def draw(self, screen):

        # Submit button     
        if self.name != "" and self.text != "":  
            pygame.draw.rect(screen, BLACK, self.submit_rect, 2, border_radius=5)
            text_surface = self.font.render("Submit", True, BLACK)
            screen.blit(text_surface, (self.submit_rect.x+5, self.submit_rect.y+5))
        else:
            pygame.draw.rect(screen, BLACK, self.submit_rect, border_radius=5)
            text_surface = self.font.render("Submit", True, LIGHT_GREEN)
            screen.blit(text_surface, (self.submit_rect.x+5, self.submit_rect.y+5))

        # Name box
        pygame.draw.rect(screen, BLACK, self.name_box_rect, 2, border_radius=5)
        text_surface = self.font.render(self.name, True, BLACK)
        screen.blit(text_surface, (self.name_box_rect.x+5, self.name_box_rect.y+5))

        border = pygame.Rect(self.rect.x, self.rect.y - 2, SCREEN_WIDTH * 0.75, SCREEN_HEIGHT)
        pygame.draw.rect(screen, BLACK, border, 2, border_radius=5)

        text_surface = self.font.render(self.sudo_text, True, BLACK)
        screen.blit(text_surface, (self.rect.x+5, self.rect.y+5))

        if self.name_box_selected:
            if self.cursor_visible:
                pygame.draw.line(screen, BLACK, (self.name_box_rect.x + 5 + self.font.size(self.name)[0], self.name_box_rect.y + 5),
                                (self.name_box_rect.x + 5 + self.font.size(self.name)[0], self.name_box_rect.y + self.name_box_rect.height - 5), 3)
            else:
                pygame.draw.line(screen, LIGHT_GREEN, (self.name_box_rect.x + 5 + self.font.size(self.name)[0], self.name_box_rect.y + 5),
                                (self.name_box_rect.x + 5 + self.font.size(self.name)[0], self.name_box_rect.y + self.name_box_rect.height - 5), 3)

        if self.selected:

            if self.cursor_visible:
                # get number of indents 
                indents = 0
                for char in self.sudo_text:
                    if char == '\n':
                        indents += 1

                # get the width of the text at the current indent
                text_width = 10 + self.rect.x
                for char in self.sudo_text.split('\n')[-1]:
                    text_width += self.font.size(char)[0]
                
                pygame.draw.line(screen, BLACK, (text_width, self.rect.y + 5 + (indents * 20)),
                                (text_width, self.rect.y + self.height - 5 + (indents * 20)), 3)
            else: 
                # get number of indents 
                indents = 0
                for char in self.sudo_text:
                    if char == '\n':
                        indents += 1

                # get the width of the text at the current indent
                text_width = 10 + self.rect.x
                for char in self.sudo_text.split('\n')[-1]:
                    text_width += self.font.size(char)[0]

                pygame.draw.line(screen, GREEN, (text_width, self.rect.y + 5 + (indents * 20)),
                        (text_width, self.rect.y + self.height - 5 + (indents * 20)), 3)

class FileCard:
    def __init__(self, name, path, is_directory, rect, success):
        self.name = name
        self.path = path
        self.is_directory = is_directory
        self.rect = rect
        self.selected = False
        self.success = success

    def draw(self, surface, scroll):
        rect = self.rect.move(0, -scroll)
        pygame.draw.rect(surface, LIGHT_GREEN if not self.selected else GREEN, rect, border_radius=10)

        if self.selected:
            if self.success == None:
                pygame.draw.rect(surface, GREEN, rect, border_radius=10)
                pygame.draw.rect(surface, BLACK, rect, 3, border_radius=5)  # Draw border
            elif self.success == True:
                pygame.draw.rect(surface, DARK_BLUE, rect, border_radius=10)
                pygame.draw.rect(surface, BLUE, rect, 3, border_radius=5)
            else:
                pygame.draw.rect(surface, DARK_RED, rect, border_radius=10)            
                pygame.draw.rect(surface, RED, rect, 3, border_radius=5)
        else:
            pygame.draw.rect(surface, LIGHT_GREEN, rect, border_radius=10)
            
            
        # if file is a directory, draw a folder icon
        if self.is_directory:
            icon = FILE_ICONS.get(os.path.splitext(self.name)[1], os.path.join(sys._MEIPASS, "folder.png"))
        else: 
            icon = FILE_ICONS.get(os.path.splitext(self.name)[1], os.path.join(sys._MEIPASS, "files.png"))

        surface.blit(pygame.transform.scale(pygame.image.load(os.path.join(sys._MEIPASS, "logo.png")), (FILE_CARD_ICON_SIZE, FILE_CARD_ICON_SIZE)), rect.move((self.rect.width - FILE_CARD_ICON_SIZE) // 2, PADDING))

        # Truncate long file names
        display_name = self.name
        while FONT.size(display_name + '...')[0] > self.rect.width - 10:
            display_name = display_name[:-1]
        display_name += '...' if display_name != self.name else ''

        name_text = FONT.render(display_name, True, BLACK)
        name_text_rect = name_text.get_rect(midtop=(self.rect.centerx, rect.bottom - FILE_CARD_TEXT_HEIGHT))
        surface.blit(name_text, name_text_rect)

class FileSelector:
    def __init__(self, screen):
        self.current_path = os.getcwd()
        self.old_path = self.current_path
        self.entries = []
        self.cards = []
        self.scroll = 0
        self.back_button = Rect(70, 50, BUTTON_WIDTH, BUTTON_HEIGHT)
        self.search_box = Rect(120, 50, 610, BUTTON_HEIGHT)
        self.search_text = ''
        self.search_pretext = 'Search...'
        self.search_box_active = False
        self.scroll_bar = Rect(SCREEN_WIDTH - SCROLL_BAR_WIDTH, 0, SCROLL_BAR_WIDTH, 0)
        self.scroll_drag = False
        self.last_click_time = 0
        self.selected_files = set()
        self.is_successful = None
        self.load_cards = 16 # number of cards to load at a time
        self.update_file_cards()
        self.cursor_visible = True
        self.cursor_counter = 0
        self.submit_button = Rect(SCREEN_WIDTH - 170, SCREEN_HEIGHT - 50, 100, BUTTON_HEIGHT)
        self.submit_button_text = 'Submit'
        self.screen = screen
        self.back_button_clicked = False

    def get_drives(self):
        drives = win32api.GetLogicalDriveStrings()
        drives = drives.split('\000')[:-1]
        return drives

    def update_file_cards(self):
        self.cards.clear()
        #if have goen to a new directory, or if entries is not created yet
        if self.old_path != self.current_path or not self.entries:
            self.entries = []
            if self.current_path is not None:
                self.entries = [entry for entry in os.listdir(self.current_path) if entry.lower().startswith(self.search_text.lower())] # Filter entries by search text
            self.entries.sort(key=lambda x: (not os.path.isdir(os.path.join(self.current_path, x)), os.path.splitext(x)[1] != '.pdf', x)) # Sort by folders, then pdfs, then files

            self.old_path = self.current_path

        row = 0
        col = 0
        loaded_cards_index = []
        scroll = self.scroll
        # number of rows scrolled by 
        cards_scrolled = int((scroll/(FILE_CARD_HEIGHT + FILE_CARD_PADDING)))
        #the first cards 
        first_card = cards_scrolled * 4 + 1
        #add all the loaded cards to the list
        for i in range(self.load_cards):
            if i + first_card > len(self.entries):
                break
            loaded_cards_index.append(i + first_card)
        
        for i in loaded_cards_index:
            if i <= len(self.entries):
                # Get the file name
                name = self.entries[i-1]
                # Get the file path
                path = os.path.join(self.current_path, name)
                # Get the file rect, and add the space ontop
                rect = Rect((SCREEN_WIDTH - 4 * FILE_CARD_WIDTH - 3 * FILE_CARD_PADDING) // 2 + col * (FILE_CARD_WIDTH + FILE_CARD_PADDING),
                        self.search_box.bottom + PADDING + row * (FILE_CARD_HEIGHT + FILE_CARD_PADDING) + cards_scrolled * (FILE_CARD_HEIGHT + FILE_CARD_PADDING),
                        FILE_CARD_WIDTH,
                        FILE_CARD_HEIGHT)
                # Check if the file is a directory
                is_directory = os.path.isdir(path)
                # Add the card to the list
                card = FileCard(name, path, is_directory, rect, self.is_successful)
                if path in self.selected_files:
                    card.selected = True
                self.cards.append(card)
                # Increment
                col += 1
                if col == 4:
                    col = 0
                    row += 1

        # Update total height
        self.total_height = max(SCREEN_HEIGHT, self.search_box.bottom + PADDING + (len(self.entries)/4) * (FILE_CARD_HEIGHT + FILE_CARD_PADDING) + SCREEN_HEIGHT // 2)

        # Update scroll bar height
        scroll_bar_height = SCREEN_HEIGHT * SCREEN_HEIGHT // self.total_height
        if scroll_bar_height < 50:
            scroll_bar_height = 50
        self.scroll_bar.height = max(scroll_bar_height, 50)
        
        # Update scroll bar top
        scroll_bar_top = self.scroll * SCREEN_HEIGHT // self.total_height
        self.scroll_bar.top = min(max(scroll_bar_top, 0), SCREEN_HEIGHT - self.scroll_bar.height)

    def display_drives_selection(self):
        self.current_path = None  # Add this line
        self.cards.clear()
        drives = self.get_drives()  # Assuming get_drives is the function from the previous message
        row = 0
        col = 0
        for drive in drives:
            path = drive
            rect = Rect((SCREEN_WIDTH - 4 * FILE_CARD_WIDTH - 3 * FILE_CARD_PADDING) // 2 + col * (FILE_CARD_WIDTH + FILE_CARD_PADDING),
                        self.search_box.bottom + PADDING + row * (FILE_CARD_HEIGHT + FILE_CARD_PADDING + 10),
                        FILE_CARD_WIDTH,
                        FILE_CARD_HEIGHT)
            drive_card = FileCard(drive, path, True, rect, self.is_successful)  # Treat drives as directories
            if path in self.selected_files:
                drive_card.selected = True
            self.cards.append(drive_card)
            col += 1
            if col == 4:
                col = 0
                row += 1

        # Update total_height
        self.total_height = max(SCREEN_HEIGHT, self.search_box.bottom + PADDING + row * (FILE_CARD_HEIGHT + FILE_CARD_PADDING) + SCREEN_HEIGHT // 2)

        # Update scroll bar height
        scroll_bar_height = SCREEN_HEIGHT * SCREEN_HEIGHT // self.total_height
        self.scroll_bar.height = max(scroll_bar_height, 10)

        # Update scroll bar top
        scroll_bar_top = self.scroll * SCREEN_HEIGHT // self.total_height
        self.scroll_bar.top = min(max(scroll_bar_top, 0), SCREEN_HEIGHT - self.scroll_bar.height)


    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and self.search_box_active:
            if event.key == pygame.K_BACKSPACE:
                self.search_text = self.search_text[:-1]
            elif len(self.search_text) < SEARCH_BAR_MAX_LENGTH and event.unicode.isprintable():
                self.search_text += event.unicode
            self.scroll = 0
            if self.current_path is not None:
                self.update_file_cards()
            else:
                self.display_drives_selection()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.scroll_bar.collidepoint(event.pos):
                self.scroll_drag = True
            elif self.search_box.collidepoint(event.pos):
                self.search_box_active = True
                if self.search_text == self.search_pretext:
                    self.search_text = ''
            elif self.back_button.collidepoint(event.pos) and event.button == 1:
                self.back_button_clicked = True
            elif self.submit_button.collidepoint(event.pos) and event.button == 1:
                return self.selected_files
                #here is the code to copy the files

            else:
                self.search_box_active = False
                for card in self.cards:
                    if card.rect.move(0, -self.scroll).collidepoint(event.pos):
                        if card.is_directory and event.button == 1 and time.time() - self.last_click_time < DOUBLE_CLICK_TIME and card.path in self.selected_files:
                            self.is_successful = None
                            self.selected_files.clear()
                            self.current_path = card.path
                            self.scroll = 0
                            self.update_file_cards()
                        elif event.button == 1:
                            if card.selected and self.is_successful != None:
                                self.is_successful = None
                                if self.current_path is None:
                                    self.display_drives_selection()
                                else:
                                    self.update_file_cards()
                            elif card.selected and self.is_successful == None:
                                self.selected_files.remove(card.path)
                            else:
                                self.is_successful = None
                                self.selected_files.clear()
                                self.selected_files.add(card.path)
                                self.update_file_cards()
                            if self.current_path is None:
                                self.is_successful = None
                                self.selected_files.clear()
                                self.selected_files.add(card.path)
                                self.display_drives_selection()       
                            card.selected = not card.selected
                        break
                self.last_click_time = time.time()
        elif event.type == pygame.MOUSEBUTTONUP:
            if self.scroll_drag:
                self.scroll_drag = False
            if self.back_button_clicked and self.back_button.collidepoint(event.pos) and event.button == 1:
                pygame.time.wait(10)
                if self.current_path is None:
                    # We're currently at the drive selection level, so there's nothing to do
                    pass
                else:
                    parent_directory = os.path.dirname(self.current_path)
                    if parent_directory == self.current_path:  # We are at a root directory
                        self.scroll = 0
                        self.display_drives_selection()
                    else:
                        self.current_path = parent_directory
                        self.scroll = 0
                        self.update_file_cards()
                self.back_button_clicked = False
        elif event.type == pygame.MOUSEMOTION:
            if self.scroll_drag:
                self.scroll = min(max(self.scroll + event.rel[1] * self.total_height / SCREEN_HEIGHT, 0), self.total_height - SCREEN_HEIGHT)
                self.scroll_bar.top = min(max(self.scroll * SCREEN_HEIGHT // self.total_height, 0), SCREEN_HEIGHT - self.scroll_bar.height)
                if self.current_path is not None:
                    self.update_file_cards()
                else:
                    self.display_drives_selection()
        if event.type == pygame.MOUSEWHEEL:
            if not self.scroll_drag:
                self.scroll = min(max(self.scroll - event.y * SCROLL_SPEED, 0), self.total_height - SCREEN_HEIGHT) 
                self.scroll_bar.top = min(max(self.scroll * SCREEN_HEIGHT / self.total_height, 0), SCREEN_HEIGHT - self.scroll_bar.height)
                if self.current_path is not None:
                    self.update_file_cards()
                else:
                    self.display_drives_selection()

    def update_entries(self):
        # Here we're updating the entries, not the FileCard objects
        self.entries.clear()
        if self.current_path is not None:
            self.entries = [entry for entry in os.listdir(self.current_path) if entry.lower().startswith(self.search_text.lower())]
            self.entries.sort(key=lambda x: (not os.path.isdir(os.path.join(self.current_path, x)), os.path.splitext(x)[1] != '.pdf', x))
        self.current_range = (0, min(len(self.entries), NUM_VISIBLE_ENTRIES))


    def draw(self, surface):
        surface.fill(LIGHT_GREEN)
        for card in self.cards:
            card.draw(surface, self.scroll)
        pygame.draw.rect(surface, GREEN if self.search_box_active else LIGHT_GREEN, self.search_box, border_radius=5)
        pygame.draw.rect(surface, BLACK, self.search_box, 3, border_radius=5)  # Draw border
        if self.search_box_active:
            search_text = FONT.render(self.search_text, True, BLACK)
            surface.blit(search_text, (self.search_box.left + PADDING, self.search_box.centery - search_text.get_height() // 2))
            self.cursor_counter += 1
            if self.cursor_counter % 40 < 20:  # Change this to make the cursor blink faster
                pygame.draw.line(surface, BLACK, (self.search_box.left + FONT.size(self.search_text)[0] + PADDING, self.search_box.bottom - 7), (self.search_box.left + FONT.size(self.search_text)[0] + 20, self.search_box.bottom - 7), 2)
        else:
            search_pretext = FONT.render(self.search_pretext, True, BLACK)
            surface.blit(search_pretext, (self.search_box.left + PADDING, self.search_box.centery - search_pretext.get_height() // 2))
        
        if self.back_button_clicked:
            pygame.draw.rect(surface, BLACK, self.back_button, border_radius=5)
            pygame.draw.rect(surface, BLACK, self.back_button, 3, border_radius=5)  # Draw border
            back_text = BIG_FONT.render('<', True, LIGHT_GREEN)
            back_text_rect = back_text.get_rect(center=self.back_button.center)
        else:
            pygame.draw.rect(surface, LIGHT_GREEN, self.back_button, border_radius=5)
            pygame.draw.rect(surface, BLACK, self.back_button, 3, border_radius=5)  # Draw border
            back_text = BIG_FONT.render('<', True, BLACK)
            back_text_rect = back_text.get_rect(center=self.back_button.center)

        surface.blit(back_text, back_text_rect)
        # Draw scrollbar, but add 35 to the top.
        pygame.draw.rect(surface, BLACK if self.scroll_drag else GREEN, (self.scroll_bar.left, self.scroll_bar.top + 35, self.scroll_bar.width, self.scroll_bar.height - 35), border_radius=5)

class FileCardLoded:
    def __init__(self, name, path, is_directory, rect):
        self.name = name
        self.path = path
        self.is_directory = is_directory
        self.rect = rect
        self.selected = False

        self.delet_image = pygame.image.load(os.path.join(sys._MEIPASS, "delet.png"))
        self.delet_image = pygame.transform.scale(self.delet_image, (50, 50))
        self.edit_image = pygame.image.load(os.path.join(sys._MEIPASS, "edit.png"))
        self.edit_image = pygame.transform.scale(self.edit_image, (50, 50))

        self.icon =  pygame.image.load(os.path.join(sys._MEIPASS, "file.png"))
        self.delete_rect = pygame.Rect(rect.right - 60, rect.top + 10, 50, 50)
        self.edit_rect = pygame.Rect(rect.right - 60, rect.top + 70, 50, 50)

    def draw(self, surface, scroll):
        rect = self.rect.move(0, - scroll)
        if rect.collidepoint(pygame.mouse.get_pos()):
            self.selected = True
        else:
            self.selected = False

        pygame.draw.rect(surface, LIGHT_GREEN if not self.selected else GREEN, rect, border_radius=10)

        surface.blit(pygame.transform.scale(self.icon, (140, 140)), rect.move((self.rect.width - 140) // 2, PADDING))

        # Draw delete and edit icons
        if self.selected:
            surface.blit(self.delet_image, self.delete_rect.topleft)
            surface.blit(self.edit_image, self.edit_rect.topleft)

        # Truncate long file names
        display_name = str(self.name)
        while FONT.size(display_name + '...')[0] > self.rect.width - 10:
            display_name = display_name[:-1]
        display_name += '...' if display_name != self.name else ''

        name_text = FONT.render(display_name, True, BLACK)
        name_text_rect = name_text.get_rect(midtop=(self.rect.centerx, rect.bottom - FILE_CARD_TEXT_HEIGHT))
        surface.blit(name_text, name_text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.delete_rect.collidepoint(event.pos):
                return "delete"
            elif self.edit_rect.collidepoint(event.pos):
                return "edit"
        return None

class files: 
    def __init__(self):
        self.files = data["Text_files"]
        self.data_file_name = "data.json"
        self.load_data()

        self.cards = []
        self.selected_files = set()

        self.mode = "files"
        self.file_name = "test"
        self.edit_file_name = ""

        self.went_to_edit = False
        self.file_image = pygame.image.load(os.path.join(sys._MEIPASS, "file.png"))
        self.file_image = pygame.transform.scale(self.file_image, (150, 150))

        self.scroll = 0
        self.scroll_bar = Rect(SCREEN_WIDTH - SCROLL_BAR_WIDTH, 0, SCROLL_BAR_WIDTH, 0)
        self.scroll_drag = False

        self.file_selector = FileSelector(screen)
        self.text_box = TextBox()
    
    def load_data(self):
        # se if the data file exists
        if os.path.isfile(self.data_file_name):
            # load the data file
            with open(self.data_file_name) as json_file:
                data = json.load(json_file)
                self.files = data["Text_files"]
            
            if self.files == None:
                self.files = {"Text_files":{}}
        else:
            data = {
                "Text_files": {
                }
            }
            # create the data file
            with open(self.data_file_name, 'w') as outfile:
                json.dump(data, outfile)

    def add_file(self, file):
        self.file_name = file.split("\\")[-1]
        name = self.file_name.split(".")[0]
        
        try: 
            # get text from file
            with open(file, 'r') as f:
                self.files[name] = f.read()

            # save the data file
            with open(self.data_file_name, 'w') as outfile:
                data["Text_files"] = self.files
                json.dump(data, outfile)

        except Exception as e:
            print(e)

    def edit_file(self, file, new_file):
        self.files[self.files.index(file)] = new_file

    def update_cards(self):
            row = 0
            col = 0
            ofsetX = 100
            scroll = self.scroll

            BUTTON_PADDING = 30
            FILE_CARD_PADDING = 60

            for file in self.files:

                rect = Rect((SCREEN_WIDTH - 4 * FILE_CARD_WIDTH - 3 * FILE_CARD_PADDING) // 2 + col * (FILE_CARD_WIDTH + FILE_CARD_PADDING) + ofsetX,
                        PADDING + row * (FILE_CARD_HEIGHT + FILE_CARD_PADDING) + self.scroll * (FILE_CARD_HEIGHT + FILE_CARD_PADDING) + 40,
                        FILE_CARD_WIDTH + 20,
                        FILE_CARD_HEIGHT + 20)
                
                col += 1
                if col == 3:
                    col = 0
                    row += 1

                self.cards.append(FileCardLoded(file, None, False, rect))
            
            # Update total height
            self.total_height = max(SCREEN_HEIGHT, PADDING + (len(self.files)/3) * (FILE_CARD_HEIGHT + FILE_CARD_PADDING) + SCREEN_HEIGHT // 2)

            # Update scroll bar height
            scroll_bar_height = SCREEN_HEIGHT * SCREEN_HEIGHT // self.total_height
            self.scroll_bar.height = max(scroll_bar_height, 10)

            # Update scroll bar top
            scroll_bar_top = self.scroll * SCREEN_HEIGHT // self.total_height
            self.scroll_bar.top = min(max(scroll_bar_top, 0), SCREEN_HEIGHT - self.scroll_bar.height)

    def draw(self, surface):
        if self.mode == "files":

            # Draw cards 
            for card in self.cards:
                card.draw(surface, self.scroll)
        
            # Draw add file button
            pygame.draw.rect(surface, LIGHT_GREEN, pygame.Rect(800 - 120, 600 - 70, 100, 50), border_radius=10)
            pygame.draw.rect(surface, BLACK, pygame.Rect(800 - 120, 600 - 70, 100, 50), border_radius=10, width=3)
            add_file_text = BIG_FONT.render('+Add', True, BLACK)
            add_file_text_rect = add_file_text.get_rect(center=(800 - 70, 600 - 45))
            surface.blit(add_file_text, add_file_text_rect)

            pygame.draw.rect(surface, BLACK if self.scroll_drag else GREEN, (self.scroll_bar.left, self.scroll_bar.top + 35, self.scroll_bar.width, self.scroll_bar.height - 35), border_radius=5)

        elif self.mode == "select_mode": 
            # TEXT: Add text 
            add_text = VERY_BIG_FONT.render("Add text", True, BLACK)
            add_text_rect = add_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100))
            surface.blit(add_text, add_text_rect)

            # Back button in top left corner
            pygame.draw.rect(surface, LIGHT_GREEN, pygame.Rect(20, 60, 40, 40), border_radius=10)
            pygame.draw.rect(surface, BLACK, pygame.Rect(20, 60, 40, 40), border_radius=10, width=3)
            back_text = KINDA_BIG_FONT.render('<', True, BLACK)
            back_text_rect = back_text.get_rect(center=(40, 80))
            surface.blit(back_text, back_text_rect)

            # File selector button 
            pygame.draw.rect(surface, LIGHT_GREEN, pygame.Rect(SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2 - 25, 400, 50), border_radius=10)
            pygame.draw.rect(surface, BLACK, pygame.Rect(SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2 - 25, 400, 50), border_radius=10, width=3)
            file_selector_text = BIG_FONT.render('File', True, BLACK)
            file_selector_text_rect = file_selector_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            surface.blit(file_selector_text, file_selector_text_rect)

            # Manual button
            pygame.draw.rect(surface, LIGHT_GREEN, pygame.Rect(SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2 + 50, 400, 50), border_radius=10)
            pygame.draw.rect(surface, BLACK, pygame.Rect(SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2 + 50, 400, 50), border_radius=10, width=3)
            manual_text = BIG_FONT.render('Manual', True, BLACK)
            manual_text_rect = manual_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 75))
            surface.blit(manual_text, manual_text_rect)
            
        elif self.mode == "file_selector":
            self.file_selector.draw(screen)

            if self.file_selector.selected_files == set() or self.file_selector.selected_files == None:
                pygame.draw.rect(screen, BLACK, self.file_selector.submit_button, border_radius=5)
                pygame.draw.rect(screen, BLACK, self.file_selector.submit_button, 3, border_radius=5)
                submit_text = BIG_FONT.render('Submit', True, LIGHT_GREEN)
            else:
                if clicked:
                    pygame.draw.rect(screen, BLACK, self.file_selector.submit_button, border_radius=5)
                    pygame.draw.rect(screen, BLACK, self.file_selector.submit_button, 3, border_radius=5)
                    submit_text = BIG_FONT.render('Submit', True, LIGHT_GREEN)

                else:
                    pygame.draw.rect(screen, LIGHT_GREEN, self.file_selector.submit_button, border_radius=5)
                    pygame.draw.rect(screen, BLACK, self.file_selector.submit_button, 3, border_radius=5)  # Draw border
                    submit_text = BIG_FONT.render('Submit', True, BLACK)
            
            submit_text_rect = submit_text.get_rect(center=self.file_selector.submit_button.center)

            screen.blit(submit_text, submit_text_rect)

        elif self.mode == "manual" or self.mode == "edit":
            self.text_box.draw(screen)
          
    def update(self, event):

        if self.mode == "files":

            for card in self.cards:
                result = card.handle_event(event)
                if result == "delete":
                    del self.files[card.name]
                    self.cards.clear()
                    self.update_cards()

                    # save the data file
                    with open(self.data_file_name, 'w') as outfile:
                        data["Text_files"] = self.files
                        json.dump(data, outfile)
                    
                    break  # Exit the loop immediately after deleting a file

                elif result == "edit":
                    self.mode = "edit"
                    self.went_to_edit = True
                    self.edit_file_name = card.name

            # Scroll
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.scroll > 0:
                    if event.button == 4:
                        self.scroll -= SCROLL_SPEED
                if self.scroll < len(self.cards) * (FILE_CARD_HEIGHT + FILE_CARD_PADDING) - SCREEN_HEIGHT + PADDING:
                    if event.button == 5:
                        self.scroll += SCROLL_SPEED

            # Select files
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for card in self.cards:
                        # Adjust the card's rect for the scroll offset before checking for collision
                        adjusted_rect = card.rect.move(0, -self.scroll)
                        if adjusted_rect.collidepoint(event.pos):
                            # Deselect all other cards
                            for other_card in self.cards:
                                if other_card != card:
                                    other_card.selected = False
                            # Select this card
                            card.selected = not card.selected
                            break
                    
                    # Add file button
                    if pygame.Rect(800 - 120, 600 - 70, 100, 50).collidepoint(event.pos):
                        self.mode = "select_mode"
        elif self.mode == "select_mode":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    # Back button
                    if pygame.Rect(20, 60, 40, 40).collidepoint(event.pos):
                        self.mode = "files"
                    # File selector button
                    elif pygame.Rect(SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2 - 25, 400, 50).collidepoint(event.pos):
                        self.mode = "file_selector"
                    # Manual button
                    elif pygame.Rect(SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2 + 50, 400, 50).collidepoint(event.pos):
                        self.mode = "manual" 

        elif self.mode == "file_selector":
            text_file_path = str(self.file_selector.handle_event(event))

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.file_selector.submit_button.collidepoint(event.pos) == True and event.button == 1 and self.file_selector.selected_files != set() and self.file_selector.selected_files != None:
                    clicked = True

            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if self.file_selector.submit_button.collidepoint(event.pos) == True and event.button == 1 and self.file_selector.selected_files != set() and self.file_selector.selected_files != None and self.file_selector.current_path != None:
                    pygame.time.wait(100)
                    # typer.loading_bar(self.file_selector.screen, LIGHT_GREEN, LIGHT_GREEN, 5, 50, 10, 30, 5, 10, self.file_selector, tab)
                    clicked = False

            if text_file_path != None and self.file_name != "" or self.file_name != None or self.file_name not in self.files:
                # {'C:\\Mina_project\\r\\flipper\\intercept\\pixel.ttf'} to C:\Mina_project\r\flipper\intercept\pixel.ttf
                text_file_path = str(text_file_path)[2:-2]

                #if dosent end with .txt then break
                if text_file_path.split(".")[-1] != "txt":
                    return
                
                self.add_file(text_file_path)

                self.update_cards()

                self.mode = "files"

        elif self.mode == "manual":
            pass 

        elif self.mode == "edit":
            #use self.text_box 
            pass 

files = files()

files.update_cards() 

tab = Tab()
typer = Typer()

def update_UI():

    if tab.name == "File": 
        files.draw(screen)

        if files.mode == "manual":
            dt = clock.tick(60)
            files.text_box.update(dt)  
        
            if files.text_box.selected:

                if files.text_box.time < files.text_box.key_delay:
                    files.text_box.time += 1
                keys = pygame.key.get_pressed()

                if keys[pygame.K_BACKSPACE] and files.text_box.time >= files.text_box.key_delay:
                    if files.text_box.key_delay > 0.2:
                        files.text_box.key_delay -= files.text_box.accelaration
                    else: 
                        files.text_box.key_delay = 0            
                    files.text_box.sudo_text = files.text_box.sudo_text[:-1]
                    files.text_box.text = files.text_box.text[:-1]
                    files.text_box.update_text()

                    files.text_box.time = 0
                elif keys[pygame.K_BACKSPACE] == False:   
                    files.text_box.key_delay = 10
            
            elif files.text_box.name_box_selected:

                if files.text_box.time < files.text_box.key_delay:
                    files.text_box.time += 1
                keys = pygame.key.get_pressed()

                if keys[pygame.K_BACKSPACE] and files.text_box.time >= files.text_box.key_delay:
                    if files.text_box.key_delay > 0.2:
                        files.text_box.key_delay -= files.text_box.accelaration
                    else: 
                        files.text_box.key_delay = 0            
                    files.text_box.name = files.text_box.name[:-1]
                    files.text_box.time = 0
                elif keys[pygame.K_BACKSPACE] == False:   
                    files.text_box.key_delay = 10

        if files.mode == "edit":
            if files.went_to_edit == True:

                files.text_box.name = files.edit_file_name
                files.text_box.text = files.files[files.edit_file_name]
                files.text_box.update_text()
                files.went_to_edit = False
                files.text_box.orgin_name = files.edit_file_name


            dt = clock.tick(60)
            files.text_box.update(dt)  
        
            if files.text_box.selected:

                if files.text_box.time < files.text_box.key_delay:
                    files.text_box.time += 1
                keys = pygame.key.get_pressed()

                if keys[pygame.K_BACKSPACE] and files.text_box.time >= files.text_box.key_delay:
                    if files.text_box.key_delay > 0.2:
                        files.text_box.key_delay -= files.text_box.accelaration
                    else: 
                        files.text_box.key_delay = 0            
                    files.text_box.sudo_text = files.text_box.sudo_text[:-1]
                    files.text_box.text = files.text_box.text[:-1]
                    files.text_box.update_text()

                    files.text_box.time = 0
                elif keys[pygame.K_BACKSPACE] == False:   
                    files.text_box.key_delay = 10
            
            elif files.text_box.name_box_selected:

                if files.text_box.time < files.text_box.key_delay:
                    files.text_box.time += 1
                keys = pygame.key.get_pressed()

                if keys[pygame.K_BACKSPACE] and files.text_box.time >= files.text_box.key_delay:
                    if files.text_box.key_delay > 0.2:
                        files.text_box.key_delay -= files.text_box.accelaration
                    else: 
                        files.text_box.key_delay = 0            
                    files.text_box.name = files.text_box.name[:-1]
                    files.text_box.time = 0
                elif keys[pygame.K_BACKSPACE] == False:   
                    files.text_box.key_delay = 10

        if files.text_box.done: 
            files.mode = "files"
            files.text_box.done = False
            files.text_box.name = ""
            files.text_box.text = ""
            files.text_box.sudo_text = ""
            files.text_box.orgin_name = ""
            files.text_box.update_text()
            files.load_data()
            files.cards.clear()
            files.update_cards()

    if typer.copy == True:
        messagebox.showinfo("INFO", "File set")
        typer.copy = False
    
    if typer.error == True:
        messagebox.showerror("ERROR", typer.error_message)
        print(typer.error_message)
        typer.error = False

    tab.update(screen)
    tab.draw(screen)