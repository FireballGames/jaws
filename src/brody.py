import os
import pygame

from globals import BLOCK, RES_ROOT
from resource.jaws import JawsResources


LEFT = 0
RIGHT = 1


class Brody(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.width = 2 * BLOCK
        self.height = 2 * BLOCK

        self.direction = LEFT

        self.speed = 4

        # if self.image is None:
        #     self.image = pygame.image.load(os.path.join(RES_ROOT, "brody.png"))
        self.base_image = pygame.image.load(os.path.join(RES_ROOT, "brody.png"))
        self.image = self.base_image

        self.rect = pygame.Rect((15 * BLOCK, BLOCK, self.width, self.height))
        self.movement = (0, 0)

    def update(self, field=None, *args):
        old_rect = self.rect
        self.rect = field.move_in(self.movement, self)
        if pygame.sprite.spritecollideany(self, field):
            self.rect = old_rect

    def move(self, x, y, field):
        if x > 0:
            self.image = pygame.transform.flip(self.base_image, True, False)
            self.direction = RIGHT
        elif x < 0:
            self.image = self.base_image
            self.direction = LEFT

        self.movement = (x * self.speed, y * self.speed)
        self.update(field)


class Controls:
    def __init__(self, controls):
        self.controls = controls
        self.l = 0
        self.r = 0
        self.u = 0
        self.d = 0
        self.fire = False

    def event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == self.controls["L"]:
                self.l = 1
            elif event.key == self.controls["R"]:
                self.r = 1
            elif event.key == self.controls["U"]:
                self.u = 1
            elif event.key == self.controls["D"]:
                self.d = 1
            elif event.key == self.controls["Fire"]:
                self.fire = True
        elif event.type == pygame.KEYUP:
            if event.key == self.controls["L"]:
                self.l = 0
            elif event.key == self.controls["R"]:
                self.r = 0
            elif event.key == self.controls["U"]:
                self.u = 0
            elif event.key == self.controls["D"]:
                self.d = 0
            elif event.key == self.controls["Fire"]:
                pass


class Thought:
    def __init__(self):
        self.current_thought = None

        self.queue = []
        self.to = 0
        self.thought_len = 0

    def reset(self):
        self.queue = []
        self.to = 0
        self.thought_len = 0

    def set_thought(self, thought, to):
        self.current_thought = thought

        self.queue = []  # [i for i in range(len(Resources.thoughtsurfs[thought]))]
        self.thought_len = to
        self.to = to

    def kill(self):
        self.current_thought = 'arrggh'

        self.queue = [0]
        self.thought_len = 45
        self.to = 30



class Submarine:
    def __init__(self, camera, tiled_layers):
        self.camera = camera
        self.tiled_layers = tiled_layers

        self.thought = Thought()
        self.controls = Controls(JawsResources.controls)
        self.heading = RIGHT

        self.gaittype = 'float'
        self.gait = 0
        self.gait_to = 5
        # self.bubblegait_to = 0

    def reset(self, pos):
        # self.control = KeyControl(Resources.controlmap)
        self.controls = Controls(JawsResources.controls)

        self.heading = RIGHT
        self.gaittype = 'float'
        self.gait = 0
        self.gait_to = 5
        self.bubblegait_to = 0

        # self.harpoon = Harpoons(self)

        self.health = 10
        self.alive = True
        self.death_to = 60

        self.thought.reset()

        # Add submarine to space
        # mass = 10
        # # vs_body = [(-24,-16),(-24,0),(-8,16),(8,16),(24,0),(24,-16)]
        # vs_body = [(-18, -16), (-18, 0), (-8, 16), (8, 16), (18, 0), (18, -16)]
        # moment = pymunk.moment_for_poly(mass, vs_body)
        # self.body = pymunk.Body(mass, moment)
        # self.shape = pymunk.Poly(self.body, vs_body)
        # self.shape.friction = 0.5
        # self.shape.collision_type = 3
        # self.body.position = pos
        # self.body.angle = 0
        # self.space.add(self.body, self.shape)

        self.hudflash_to = 0

    def set_thought(self, thought, to):
        self.thought.set_thought(thought, to)

    def kill(self):
        self.alive = False

        # self.space.remove(self.body, self.shape)
        # x = self.body.position[0]
        # y = self.body.position[1]
        # vx = self.body.velocity[0]
        # vy = self.body.velocity[1]
        # mass = 5
        # vs_body1 = [(-12, -16), (-12, 0), (12, 16), (12, -16)]
        # vs_body2 = [(12, -16), (12, 0), (-12, 16), (-12, -16)]

        # moment = pymunk.moment_for_poly(mass, vs_body1)
        # self.body = pymunk.Body(mass, moment)
        # self.shape = pymunk.Poly(self.body, vs_body1)
        # self.shape.friction = 0.5
        # self.shape.collision_type = 0
        # self.body.position = (x - 12, y)
        # self.body.velocity = (vx, vy)
        # self.body.angle = 0
        # self.body.apply_impulse((-100.0, 0.0))
        # self.space.add(self.body, self.shape)

        # moment = pymunk.moment_for_poly(mass, vs_body2)
        # self.body2 = pymunk.Body(mass, moment)
        # self.shape2 = pymunk.Poly(self.body2, vs_body2)
        # self.shape2.friction = 0.5
        # self.shape2.collision_type = 0
        # self.body2.position = (x + 12, y)
        # self.body2.velocity = (vx, vy)
        # self.body2.angle = 0
        # self.body2.apply_impulse((100.0, 0.0))
        # self.space.add(self.body2, self.shape2)

        # for i in range(10):
        #     self.h_tiledlayers.bubbles.AddBubble([x - 32 + random.randint(0, 64), -y - 32 + random.randint(0, 64)])

        # if self.harpoon.state == 2:
        #     self.harpoon.release()

        self.gait = 0

        self.thought.kill()

        # Resources.soundfx['subbreak'].play()

    def update(self):

        if self.alive == True:

            # set animation stuff
            vx = self.controls.r - self.controls.l
            vy = self.controls.u - self.controls.d
            if abs(vx) > 0 or abs(vy) > 0:
                # if self.harpoon.state == 2 or self.harpoon.fire_to > 0:
                #     self.gaittype = "move_harp"
                # else:
                #     self.gaittype = "move"
                self.gaittype = "move"
                # if self.bubblegait_to == 0:
                #     self.bubblegait_to = 5
                #     if self.heading == RIGHT:
                #         self.h_tiledlayers.bubbles.AddBubble([self.body.position[0] - 30, -self.body.position[1]],
                #                                              global_to=100)
                #     else:
                #         self.h_tiledlayers.bubbles.AddBubble([self.body.position[0] + 16, -self.body.position[1]],
                #                                              global_to=100)
                # else:
                #     self.bubblegait_to -= 1
            else:
                pass
                # if self.harpoon.state == 2 or self.harpoon.fire_to > 0:
                #     self.gaittype = "float_harp"
                # else:
                #     self.gaittype = "float"
                self.gaittype = "float"

            # Set heading and gait info
            if vx > 0:
                self.heading = RIGHT
            elif vx < 0:
                self.heading = LEFT

            # Player animation
            if (self.gaittype == 'move' or self.gaittype == 'move_harp') and self.gait_to == 0:
                self.gait_to = 3
                self.gait = self.gait + 1
                if self.gait > 3:
                    self.gait = 0
            elif self.gaittype == 'float' or self.gaittype == 'float_harp':
                self.gait = 0
                self.gait_to = 0
            self.gait_to = max(0, self.gait_to - 1)

            # Apply impulses to player based on control inputs
            # if self.h_tiledlayers.exiting == False:
            #     control_gain_x = 200
            #     control_gain_y = 200
            #     if self.control.l == 1:
            #         self.body.apply_impulse((-control_gain_x, 0.0))
            #     elif self.control.r == 1:
            #         self.body.apply_impulse((control_gain_x, 0.0))
            #     if self.control.u == 1:
            #         self.body.apply_impulse((0.0, control_gain_y))
            #     elif self.control.d == 1:
            #         self.body.apply_impulse((0.0, -control_gain_y))
            # else:
            #     self.gaittype = 'float'
            #     self.gait = 0
            #     self.gait_to = 0

            # Apply buoyancy and drag
            # gain_x = 1.0
            # gain_y = 1.0
            # drag = (-gain_x * self.body.velocity[0], -gain_y * self.body.velocity[1])
            # self.body.apply_impulse(drag)
            # self.body.apply_impulse((0.0, 150.0))  # buoyancy

            # gain_ang1 = 100.0
            # gain_ang2 = 500.0
            # righting = gain_ang1 * self.body.angular_velocity + gain_ang2 * self.body.angle
            # self.body.apply_impulse((0.0, righting), r=(-10, 0))
            # self.body.apply_impulse((0.0, -righting), r=(10, 0))

            # tsize = self.h_tiledlayers.tilesize
            # self.init_tile = self.h_tiledlayers.map_size[0] * (-int(self.body.position[1]) / tsize) + (
            #             int(self.body.position[0]) / tsize)

            if self.health <= 0:
                self.Kill()

        else:  # dead

            # Apply buoyancy and drag
            # gain_x = 0.3
            # gain_y = 0.3
            # drag = (-gain_x * self.body.velocity[0], -gain_y * self.body.velocity[1])
            # self.body.apply_impulse(drag)
            # self.body.apply_impulse((0.0, 50.0))  # buoyancy
            # drag2 = (-gain_x * self.body2.velocity[0], -gain_y * self.body2.velocity[1])
            # self.body2.apply_impulse(drag2)
            # self.body2.apply_impulse((0.0, 50.0))  # buoyancy

            if self.death_to > 0:
                self.death_to -= 1

        # Update harpoon
        # self.harpoon.Update()

        if self.thought.to > 0:
            self.thought.to -= 1
        else:
            if len(self.thought.queue) > 0:
                self.thought.queue.pop()
                self.thought.to = self.thought.thought_len

        if self.hudflash_to > 0:
            self.hudflash_to -= 1

    def post_update(self):
        pass
        # Check if need to inform tilemap object layer of updates
        # tsize = self.h_tiledlayers.tilesize
        # final_tile = self.h_tiledlayers.map_size[0] * (-int(self.body.position[1]) / tsize) + (
        #             int(self.body.position[0]) / tsize)
        # if not self.init_tile == final_tile:
        #     self.h_tiledlayers.UpdateObj(self.init_tile, final_tile, 0)

    def draw(self, screen):
        if self.alive == True:
            pass
            # ang_ind = int(round((180 * self.body.angle / pi + 180) / 10.0)) % 35
            # sprite_data = resources.sub_spritedata[self.heading][resources.sub_spriteseq[self.gaittype][self.gait]][
            #     ang_ind]
            # x = int(self.body.position[0])
            # y = int(-self.body.position[1])
            # (imw, imh) = (sprite_data.get_width(), sprite_data.get_height())
            # screen.blit(sprite_data, (x - (imw / 2) - self.h_camera.x + self.h_camera.w_view / 2,
            #                           y - (imh / 2) - self.h_camera.y + self.h_camera.h_view / 2))
        else:
            pass
            # ang_ind1 = int(round((180 * self.body.angle / pi + 180) / 10.0)) % 35
            # sprite_data1 = resources.sub_spritedata[self.heading][resources.sub_spriteseq["dead"][0]][ang_ind1]
            # x1 = int(self.body.position[0])
            # y1 = int(-self.body.position[1])
            # (imw1, imh1) = (sprite_data1.get_width(), sprite_data1.get_height())
            # screen.blit(sprite_data1, (x1 - (imw1 / 2) - self.h_camera.x + self.h_camera.w_view / 2,
            #                            y1 - (imh1 / 2) - self.h_camera.y + self.h_camera.h_view / 2))
            # ang_ind2 = int(round((180 * self.body2.angle / pi + 180) / 10.0)) % 35
            # sprite_data2 = resources.sub_spritedata[self.heading][resources.sub_spriteseq["dead"][1]][ang_ind2]
            # x2 = int(self.body2.position[0])
            # y2 = int(-self.body2.position[1])
            # (imw2, imh2) = (sprite_data2.get_width(), sprite_data2.get_height())
            # screen.blit(sprite_data2, (x2 - (imw2 / 2) - self.h_camera.x + self.h_camera.w_view / 2,
            #                            y2 - (imh2 / 2) - self.h_camera.y + self.h_camera.h_view / 2))

    def render_hud(self, screen):
        pass
        # if (self.hudflash_to / 2) % 2 == 0:
        #     border_c = (225, 201, 151)
        #     inner_c = (186, 143, 54)
        # else:
        #     border_c = (255, 0, 0)
        #     inner_c = (186, 143, 54)
        # # border_c = (200,200,0)
        # # inner_c = (128,128,0)
        # screen.blit(resources.hudtext_spritedata, (518, 8))
        # pygame.draw.rect(screen, border_c, ((524, 24), (103, 8)), 2)
        # barlen = 10 * self.health
        # if barlen > 0:
        #     pygame.draw.rect(screen, inner_c, ((526, 26), (barlen, 5)), 0)

    def render_thought(self, screen):
        pass
        # if len(self.thought_queue) > 0:
        #     td1 = self.thought_to - self.thoughtlen + 15
        #     if td1 > 0:
        #         alpha = int(255 * (1.0 - float(td1) / 15.0))
        #     elif self.thought_to <= 15:
        #         alpha = int(255 * (self.thought_to / 15.0))
        #     else:
        #         alpha = 255
        #     surf_thought = resources.thoughtsurfs[self.current_thought][self.thought_queue[-1]]
        #     surf_thought_bg = resources.thoughtsurfs_bg[self.current_thought][self.thought_queue[-1]]
        #     (imw, imh) = (surf_thought_bg.get_width(), surf_thought_bg.get_height())
        #     x = int(self.body.position[0])
        #     y = int(-self.body.position[1]) - 16 - imh
        #     surf_thought_bg.set_alpha(alpha / 2)
        #     screen.blit(surf_thought_bg, (x - (imw / 2) - self.h_camera.x + self.h_camera.w_view / 2,
        #                                   y - (imh / 2) - self.h_camera.y + self.h_camera.h_view / 2))
        #     (imw2, imh2) = (surf_thought.get_width(), surf_thought.get_height())
        #     surf_thought.set_alpha(alpha)
        #     screen.blit(surf_thought, (x - (imw2 / 2) - self.h_camera.x + self.h_camera.w_view / 2,
        #                                y - (imh2 / 2) - self.h_camera.y + self.h_camera.h_view / 2))
